from .base import BaseAgent

class VoiceAgent(BaseAgent):
    def __init__(self):
        super().__init__("VoiceDirector", "负责匹配角色性格并合成语音")
        # 预设的性格音频库映射
        self.voice_map = {
            "gentle": "ElevenLabs_ID_01",
            "mischievous": "ElevenLabs_ID_02",
            "stoic": "ElevenLabs_ID_03"
        }

    def run(self, script_scenes, character_type="gentle"):
        voice_id = self.voice_map.get(character_type, "default")
        print(f"[{self.name}] 使用 {character_type} 性格配置 (ID: {voice_id}) 合成语音...")
        results = []
        for scene in script_scenes:
            # 这里模拟调用 ElevenLabs API
            audio_path = f"output/audio_scene_{scene['id']}.mp3"
            results.append({"scene_id": scene['id'], "audio_path": audio_path})
        return results