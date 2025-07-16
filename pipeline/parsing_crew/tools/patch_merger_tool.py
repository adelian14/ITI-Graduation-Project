from crewai.tools import BaseTool

class PatchMergerTool(BaseTool):
    name: str = "patch_merger_tool"
    description: str = "Splits a long list of image paths into smaller patches and merges partial text results."

    def _run(self, image_paths: list[str], patch_size: int = 5) -> list[list[str]]:
        return [image_paths[i:i + patch_size] for i in range(0, len(image_paths), patch_size)]
