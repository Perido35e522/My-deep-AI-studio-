import gradio as gr

# Your all-in-one DeepReal Studio
with gr.Blocks(title="DeepReal Studio - Free AI Media Tools") as demo:
    gr.Markdown("# 🧠 DeepReal Studio\nOne app for realistic face swap, lip sync, voice cloning, watermark removal & more")
    
    with gr.Tabs():
        
        with gr.Tab("🔄 Face Swap (Image)"):
            gr.Interface.load("spaces/ALSv/FaceSwapAll")  # All-in-one face swapping (best free one)
        
        with gr.Tab("🗣️ Voice Clone + Text-to-Speech"):
            gr.Interface.load("spaces/tonyassi/voice-clone")  # Upload voice → clone → TTS
        
        with gr.Tab("💬 Image to Talking Video (Lip Sync)"):
            gr.Interface.load("spaces/KlingTeam/LivePortrait")  # or SadTalker if you prefer
        
        with gr.Tab("🎥 Video Lip Sync + Face Swap"):
            gr.Interface.load("spaces/Uniaff/mainmainminavoiceclone")  # Cloned voice + lip sync + face options
        
        with gr.Tab("🚫 Watermark Remover (No Blur)"):
            gr.Interface.load("spaces/ucalyptus/watermark-remover-app")  # Clean AI removal
        
        with gr.Tab("🖼️ Text to Realistic Image"):
            gr.Interface.load("spaces/stabilityai/stable-diffusion-3.5-large")  # or any top SDXL space

demo.launch()