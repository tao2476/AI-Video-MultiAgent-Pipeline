# 多 Agent 协作短视频叙事流水线

这是一个基于 Python 的多 Agent 协作框架示例，专门用于自动化短视频创作流程。

## 核心架构
1. **ScriptAgent**: 负责深度叙事脚本编写，聚焦情感内核。
2. **StoryboardAgent**: 自动生成符合 3D 动画或特定视觉风格的分镜 Prompt。
3. **VoiceAgent**: 集成角色性格引擎，支持 ElevenLabs 等平台的语音合成。
4. **Orchestrator**: 负责整个长链推理逻辑的协调。

## 运行方法
1. 安装依赖：`pip install -r requirements.txt`
2. 运行主程序：`python main.py`

## 扩展建议
- 接入真实的 OpenAI/Gemini API 实现脚本自动化生成。
- 接入 Stable Diffusion 或 Midjourney API 实现分镜图自动化渲染。
- 接入 FFmpeg 实现音画自动对齐。