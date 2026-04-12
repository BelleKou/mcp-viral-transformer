from mcp.server.fastmcp import FastMCP
import httpx
from bs4 import BeautifulSoup
import os
import re
from pydantic import Field

# Initialize FastMCP Server
mcp = FastMCP("ViralTransformer")

# --- 1. Resources: ---
@mcp.resource("mcp://docs/viral-logic")
def get_viral_logic() -> str:
    """Returns the 2026 version of viral content logic."""
    return """
    # MODERN VIRAL CONTENT SOP (2026 Edition)
    1. THE HOOK: Challenge a common belief or highlight a "hidden cost" in the first sentence.
    2. DATA BOMB: Include at least one specific number, technical fact, or industry comparison.
    3. NO CLICHÉS: Strictly avoid "Shocking," "Unbelievable," or "Must-read." Use intelligent intensity.
    4. FORMAT: Use comparison tables or structured bullet points for high-density information.
    5. UNIQUE ANGLE: Provide a logical inference that connects the news to a broader trend.
    6. CTA: Ask a polarizing or scenario-based question to trigger high-quality debate.
    """

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
        {"role": "user", "content": f"""
You are a high-end Content Strategist for top-tier tech media. 

GOAL: Transform the content from this link into a viral masterpiece: {url}

LOGIC STEPS:
1. **Analyze**: Identify the 3 most controversial or innovative points in the `scrape_article` output.
2. **Consult**: Match these points with the high-density rules in `mcp://docs/viral-logic`.
3. **Drafting**: Create two distinct versions:
   - **Version A (Professional/Insightful)**: Focus on industry impact, logic, and "why it matters." (Tone: Jike/LinkedIn/Medium)
   - **Version B (High-Energy/Visual)**: Focus on the "wow" factor, urgency, and direct impact. (Tone: Red/X/Social Media)
4. **Finalize**: Combine the best insights and ADD a 'Unique Angle' (a logical inference about the future) that wasn't in the original text.

CRITICAL INSTRUCTION:
- DO NOT use generic marketing clichés like "Unbelievable" or "Game-changer."
- Use semantic, lowercase_with_underscores filenames based on the core topic.
- Once finished, use `save_draft` to store the output.

Execute now.
"""}
    ]

if __name__ == "__main__":
    mcp.run()