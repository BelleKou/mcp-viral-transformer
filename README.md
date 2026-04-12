🚀 ViralTransformer MCP Server
ViralTransformer is a workflow automation server built on the Model Context Protocol (MCP). It enables AI assistants (like Claude) to scrape web content and transform it into high-engagement social media posts using structured marketing logic.

ViralTransformer 是一个基于 MCP 协议构建的自动化工作流服务器。它赋予 AI 助手（如 Claude）抓取网页内容的能力，并遵循内置的营销逻辑将其转化为高参与度的社交媒体文案。

✨ Key Features | 核心功能
🌐 Smart Scraping (Tool): Automatically extracts core titles and text content from URLs using asynchronous fetching.

智能抓取：使用异步请求自动从 URL 中提取核心标题与正文。

🧠 Viral Logic SOP (Resource): Injects a predefined "Viral Content SOP" (Hooks, Scannability, Emotion, CTA) into the AI's context.

营销逻辑注入：将预设的爆款文案 SOP（钩子、可读性、情绪价值、行动号召）注入 AI 上下文。

💾 Auto-Drafting (Tool): Standardizes and saves generated content to a local ./drafts directory for immediate use.

自动存档：将生成内容标准化并自动保存至本地 ./drafts 目录。

🤖 Orchestrated Workflow (Prompt): A pre-configured pipeline (remake) that guides the AI through scraping, analyzing, and saving in one sequence.

编排工作流：预设 remake 指令，引导 AI 按序完成抓取、分析与保存。

🛠️ Tech Stack | 技术栈
FastMCP: High-performance Python framework for MCP server implementation.

Httpx: Async HTTP client for efficient web requests.

BeautifulSoup4: Robust HTML parsing and content extraction.

Pydantic: Type safety and data validation for tool inputs.

🚀 Quick Start | 快速开始
📦 Prerequisites | 前置条件
Python 3.10+

uv (Recommended for high-performance dependency management)

📥 Installation | 安装
Bash
git clone https://github.com/your-username/mcp-viral-transformer.git
cd mcp-viral-transformer
pip install -r requirements.txt
▶️ Development & Testing | 开发与测试
Use the MCP Inspector to verify the server locally:

Bash
uv run --with mcp mcp dev server.py
🤖 Claude Desktop Integration | 集成到 Claude
To use this with Claude Desktop, add the following to your claude_desktop_config.json:

JSON
{
  "mcpServers": {
    "viral-transformer": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp",
        "mcp", "run",
        "D:/mcp-viral-transformer/server.py"
      ]
    }
  }
}
(Note: Replace the path with your actual local path as shown in your environment)

📝 Example Output | 成果展示
The system follows a Native Consistency principle: scraping English yields English, scraping Chinese yields Chinese, while the Unique Angle remains bilingual for global insight.

Case 1: Silicon Valley Power Play (English Native)
Source: Anthropic’s $30B Compute Deal with Google & Broadcom

File: anthropic_30b.md

Insight: "In 2026, competitive advantage isn't code—it's custom silicon and power grid access. / 2026年，竞争优势不再是代码，而是定制芯片和电网准入权。"

Case 2: Industrial Moonshots (Chinese Native)
Source: 36Kr - 吉利沃飞长空 IPO (李书福的低空帝国)

File: sky_economy.md

Insight: "Low-altitude economy isn't about flying; it's about the sovereignty of time. / 低空经济的核心不在于飞行，而在于对时间主权的掌控。"

📂 Directory Structure | 目录结构
Plaintext
.
├── server.py           # Core MCP logic
├── requirements.txt    # Project dependencies
├── .gitignore          # Environment & cache filters
├── drafts/             # Generated markdown posts
└── README.md           # Documentation
🖥️ System Validation | 系统验证
The server implementation has been fully validated using the **MCP Inspector**. The trace below confirms successful protocol handshakes, tool registration, and STDIO transport.

<details>
<summary>👉 Click to view technical logs (Environment Verified)</summary>

Bash
# Log verified on 2026-04-12
Starting MCP inspector...
⚙️ Proxy server listening on localhost:6277
🚀 MCP Inspector is up and running at http://localhost:6274/

New STDIO connection request
Query parameters: {"command":"uv","args":"run --with mcp mcp run server.py"}
# Success: Created client & server transport for sessionId d7faa613
</details>

⚖️ License
MIT License. Open for modification and only personal use.