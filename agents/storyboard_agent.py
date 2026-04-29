from .base import BaseAgent

class StoryboardAgent(BaseAgent):
    def __init__(self):
        super().__init__("StoryboardArtist", "负责将脚本场景转化为视觉提示词")

    def run(self, script_scenes):
        print(f"[{self.name}] 正在生成 9 宫格分镜视觉描述词...")
        storyboard = []
        for scene in script_scenes:
            prompt = f"3D animation style, cinematic lighting, {scene['content']}, high detail, 8k"
            storyboard.append({"scene_id": scene['id'], "prompt": prompt})
        return storyboard