from mcp.server.fastmcp import FastMCP
import httpx
from bs4 import BeautifulSoup
import os
import re
from pydantic import Field
from sops import VIRAL_LOGIC_2026, REMAKE_PROMPT_TEMPLATE

# Initialize FastMCP Server
mcp = FastMCP("ViralTransformer")

# --- 1. Resources: ---
@mcp.resource("mcp://docs/viral-logic")
def get_viral_logic() -> str:
    """Returns the 2026 version of viral content logic."""
    return VIRAL_LOGIC_2026

# --- 2. Tools ---
@mcp.tool()
async def scrape_article(url: str) -> str:
    """Scrapes clean content from a URL, focusing on the main article body."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url, follow_redirects=True, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding # 自动识别编码，防止中文变乱码
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for s in soup(["script", "style", "nav", "footer", "header", "aside"]):
                s.extract()

            title = soup.title.string.strip() if soup.title else "Untitled Source"
            
            main_body = soup.find('article') or soup.find('main') or soup.find('div', class_=re.compile(r'content|article|post', re.I)) or soup

            paragraphs = [p.get_text().strip() for p in main_body.find_all('p') if len(p.get_text()) > 30]
            content = "\n\n".join(paragraphs[:15]) # 抓取深度提升至 15 段
            
            return f"SOURCE_TITLE: {title}\n\nBODY_CONTENT:\n{content[:5000]}"
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"

@mcp.tool()
def save_draft(filename: str, content: str) -> str:
    """Saves content with a safe filename to the /drafts folder."""
    try:
        os.makedirs("./drafts", exist_ok=True)
        safe_name = re.sub(r'[^\w\s-]', '', filename).strip().lower()
        safe_name = re.sub(r'[-\s]+', '_', safe_name)
        if not safe_name.endswith('.md'):
            safe_name += '.md'
            
        path = os.path.join("./drafts", safe_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved to: {os.path.abspath(path)}"
    except Exception as e:
        return f"Failed to save file: {str(e)}"

# --- 3. Prompts ---
@mcp.prompt(name="remake")
def remake_viral_content(url: str = Field(description="The source URL to transform")):
    """The elite workflow to transform links into high-density viral content."""
    return [
        {
            "role": "user", 
            "content": REMAKE_PROMPT_TEMPLATE.replace("{url}", url) 
        }
    ]

if __name__ == "__main__":
    mcp.run()