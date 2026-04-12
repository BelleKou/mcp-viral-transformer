# 2026 viral-content
VIRAL_LOGIC_2026 = """
# MODERN VIRAL CONTENT SOP (2026 Edition)
1. THE HOOK: Challenge a common belief or highlight a "hidden cost" in the first sentence.
2. DATA BOMB: Include at least one specific number, technical fact, or industry comparison.
3. NO CLICHÉS: Strictly avoid "Shocking," "Unbelievable," or "Must-read." Use intelligent intensity.
4. FORMAT: Use comparison tables or structured bullet points for high-density information.
5. UNIQUE ANGLE: Provide a logical inference that connects the news to a broader trend.
6. CTA: Ask a polarizing or scenario-based question to trigger high-quality debate.
"""

# Remake workflow-template
REMAKE_PROMPT_TEMPLATE = """
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
"""