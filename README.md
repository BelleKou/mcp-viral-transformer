# 🚀 ViralTransformer MCP Server 
[**⭐ 点我直达右上角点亮星星 | Star this Project**](https://github.com/BelleKou/mcp-viral-transformer)
> **Turn raw URLs into viral hits. Because manually writing posts is so 2025.** <br> **将枯燥的链接化为爆款。毕竟，手动写文案已经是 2025 年的老古董了。**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BelleKou/mcp-viral-transformer/blob/main/LICENSE)
![Star Counter](https://img.shields.io/github/stars/BelleKou/mcp-viral-transformer?style=social)
![MCP Powered](https://img.shields.io/badge/MCP-Compatible-blue)

**ViralTransformer** is a high-performance MCP server that turns Claude into a 24/7 social media growth hacker. It doesn't just scrape; it thinks, analyzes, and drafts.

**ViralTransformer** 是一款高性能 MCP 服务器。它不仅仅是抓取网页，更是将 Claude 变成了一个 24/7 全天候在线的自媒体增长黑客。

---

## ✨ Features | 核心功能

* **🌐 Smart Extraction**: Scrapes the meat, leaves the bones (async fetching).
* **🧠 Viral SOP**: Injects professional copywriting logic (Hooks, CTA, Scannability).
* **💾 Local Drafts**: Auto-saves every genius idea to `./drafts` immediately.
* **智能抓取**：只取干货，异步高效；**营销逻辑**：内置爆款 SOP；**自动存档**：灵感自动落库。

---

## 🎮 How to Play | 怎么玩？

1. **The "Remake" Command**: Give Claude a URL and say "remake this".
2. **Dual-Version Output**: Get a "Deep Insight" version for LinkedIn/WeChat and a "High-Energy" version for X/Xiaohongshu.
3. **一键洗稿**：丢给 Claude 一个链接，执行 `remake`，直接收获商业深度稿与情绪爆款稿。

---

## 🎭 Star Achievement | 星星对赌协议

If this tool saves you 10 minutes of brain cells, hit that ⭐.
如果这个工具帮你省下了死掉的脑细胞，请赏一颗 ⭐。

| Stars | Achievement |
| :--- | :--- |
| **⭐50** | **The Roast Master** — AI rewrites news with extreme sarcasm <br> **毒舌教主**：开启“键盘侠”模式，让 AI 用最阴阳怪气的口吻重写新闻。 | 
| **⭐188** | **Cyberpunk 2077** — Tech-noir storytelling <br>**赛博大饼**：把平凡的科技更新，改写成充满霓虹灯、义体、反乌托邦色彩的科幻文案。 | 
| **⭐300** | **The Abstract Master** — Post-modern "Madness" style <br> **抽象大师**：解锁“互联网抽象话”。废话文学、发疯文学，怎么好玩怎么来。 | 
| **⭐520** | **"Blind Date" Profile** — News as a high-end date bio <br> **高端相亲模式**：把枯燥财报改写成“年入百万、海归精英、热爱滑雪”的凡尔赛相亲文案。 | 
| **⭐888** | **"The Secret Agent"** — Auto-monitor competitors <br> **赛博间谍**：发布自动监控对手动态并生成“回击文案”的保姆级自动化教程。 | 

---

## 🛠️ Tech Stack | 技术栈

- **FastMCP**: High-performance Python framework for MCP.
- **Httpx**: Async HTTP client.
- **BeautifulSoup4**: Robust HTML parsing.
- **Pydantic**: Type safety and data validation.

---

## 🚀 Quick Start | 快速开始

### 📦 Prerequisites | 前置条件

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Recommended for dependency management)

### 📥 Installation | 安装

```bash
git clone https://github.com/BelleKou/mcp-viral-transformer.git
cd mcp-viral-transformer
pip install -r requirements.txt
```

### 🤖 Claude Desktop Integration | 集成到 Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "viral-transformer": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp",
        "mcp", "run",
        "/your/path/to/mcp-viral-transformer/server.py"
      ]
    }
  }
}
```

> ⚠️ Replace the path with your actual local path.

---

## 📝 Example Output | 成果展示

### Case 1: Silicon Valley Power Play (English Native)

**Source**: Anthropic's $30B Compute Deal
**Generated File**: 📄 `drafts/anthropic_30b.md`

<details>
<summary>👉 Click to expand viral content preview</summary>

---

**⚡️ THE $30B COMPUTE HEGEMONY: ANTHROPIC X GOOGLE X BROADCOM**

**🏛️ Version A: Professional Insight**

**Title**: The Death of Asset-Light AI: Anthropic's Vertical Integration Bet

The recent $30B partnership between Anthropic, Google, and Broadcom marks a tectonic shift. We are moving away from "Algorithm Supremacy" toward "Compute Sovereignty."

- **The Hardware Pivot**: Co-designing ASICs with Broadcom to bypass the NVIDIA bottleneck.
- **Infrastructure Moat**: Scaling laws now require a direct relationship with the power grid.

**🚀 Version B: High-Energy Viral**

**Title**: $30 BILLION. That's the price of admission for the AGI race. 💸

While everyone is arguing over prompts, Anthropic just bought the building. And the chips. And the power lines.

**🔮 UNIQUE ANGLE**

AI is shifting from software to a "Digital Utility." In 2026, the leading AI company looks less like Microsoft and more like a combination of TSMC and energy conglomerates.

---

</details>

### Case 2: Industrial Moonshots (Chinese Native)

**Source**: 36Kr - 吉利沃飞长空 IPO
**Generated File**: 📄 `drafts/sky_economy.md`

<details>
<summary>👉 点击展开预览爆款文案内容</summary>

---

**🚁 11个IPO！"汽车狂人"的最后拼图：低空经济不是梦，是生意。**

**🏛️ Version A: 深度商业观察**

**标题**：从"二维道路"到"三维空间"：沃飞长空的资本纵横术

沃飞长空启动IPO辅导，标志着"低空经济"已从概念进入资本收割期。这不仅是造飞行汽车，更是对城市空间主权的重构。

**🚀 Version B: 情绪爆款文案**

**标题**：别再地面卷了！以后出门打"飞的"，只要10分钟？💸

当年被嘲笑的"疯话"，现在全成了真！天空正式变成"车道"，低空出行的时代来了。卖的不是飞机，是"绕过拥堵的特权"。

**🔮 UNIQUE ANGLE**

时间主权的阶级化：2026年，阶级分层将体现在"垂直准入权"上。沃飞长空抢占的300米高度，是未来50年城市秩序的终极解释权。

---

</details>

---

## 📂 Directory Structure | 目录结构

```plaintext
.
├── server.py           # Core MCP logic
├── LICENSE             # MIT License
├── requirements.txt    # Project dependencies
├── drafts/             # Generated markdown posts (Output)
└── README.md           # Documentation
```

---

## ⚖️ License

Licensed under the [MIT License](./LICENSE). Open for modification and personal use.
