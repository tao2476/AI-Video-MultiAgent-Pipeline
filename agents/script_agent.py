from .base import BaseAgent

class ScriptAgent(BaseAgent):
    def __init__(self):
        super().__init__("ScriptWriter", "负责创作具有情感共鸣的短视频脚本")

    def run(self, theme):
        print(f"[{self.name}] 正在根据主题 '{theme}' 创作脚本...")
        # 模拟生成逻辑，实际应调用 LLM API
        script = {
            "title": f"关于 {theme} 的感人故事",
            "scenes": [
                {"id": 1, "content": "开场：清晨的阳光洒进老屋，墙上的合照显得格外温馨。", "voice_text": "家，是永远的避风港。"},
                {"id": 2, "content": "近景：一双布满老茧的手正在整理行囊，动作缓慢而坚定。", "voice_text": "那些没说出口的话，都藏在了细节里。"},
                {"id": 3, "content": "特写：眼神中流露出的不舍与期待。", "voice_text": "爱，从来不需要华丽的词藻。"}
            ]
        }
        return script