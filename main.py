from agents.script_agent import ScriptAgent
from agents.storyboard_agent import StoryboardAgent
from agents.voice_agent import VoiceAgent

class VideoPipelineOrchestrator:
    def __init__(self):
        self.script_agent = ScriptAgent()
        self.storyboard_agent = StoryboardAgent()
        self.voice_agent = VoiceAgent()

    def execute(self, theme):
        print("--- 启动多 Agent 协作流水线 ---")
        
        # Step 1: 脚本创作
        script = self.script_agent.run(theme)
        
        # Step 2: 分镜设计
        storyboard = self.storyboard_agent.run(script['scenes'])
        
        # Step 3: 语音合成
        voice_files = self.voice_agent.run(script['scenes'], character_type="gentle")
        
        print("\n--- 任务完成 ---")
        print(f"生成标题: {script['title']}")
        for i, scene in enumerate(script['scenes']):
            print(f"分镜 {i+1} Prompt: {storyboard[i]['prompt']}")
            print(f"分镜 {i+1} 音频路径: {voice_files[i]['audio_path']}")

if __name__ == "__main__":
    orchestrator = VideoPipelineOrchestrator()
    orchestrator.execute("父爱与告别")