from crewai.tools import BaseTool

class MarkdownNormalizerTool(BaseTool):
    name: str = "markdown_normalizer_tool"
    description: str = "Cleans and structures extracted raw text into readable Markdown format."

    def _run(self, raw_text: str) -> str:
        lines = raw_text.split("\n")
        cleaned = []

        for line in lines:
            if line.strip().endswith(":"):
                cleaned.append(f"### {line.strip()}")
            elif line.strip().startswith("-") or line.strip().startswith("*"):
                cleaned.append(line.strip())
            elif line.strip():
                cleaned.append(f"{line.strip()}")
        return "\n\n".join(cleaned)
