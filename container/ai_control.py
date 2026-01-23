import subprocess
import os

# (enter your specific host ip of course)
HOST_IP = "192.168.1.x"
MODEL = "llama3.2:1b"
VOICE_ONNX = "en_US-lessac-low.onnx"

# functions
def set_remote_state(state):
    """Updates the face state on the Proxmox host via SSH."""
    states = {
        "talking": "rm -f /tmp/ai_thinking && touch /tmp/ai_talking",
        "thinking": "rm -f /tmp/ai_talking && touch /tmp/ai_thinking",
        "idle": "rm -f /tmp/ai_talking /tmp/ai_thinking"
    }
    cmd = states.get(state, states["idle"])
    # Now this line can safely see 'HOST_IP'
    subprocess.Popen(["ssh", "-f", f"root@{HOST_IP}", cmd])

def set_remote_state(state):
    """Updates the face state on the Proxmox host via SSH"""
    # We use a single function to clear old states and set the new one
    if state == "talking":
        cmd = "rm -f /tmp/ai_thinking && touch /tmp/ai_talking"
    elif state == "thinking":
        cmd = "rm -f /tmp/ai_talking && touch /tmp/ai_thinking"
    else: # idle/clear
        cmd = "rm -f /tmp/ai_talking /tmp/ai_thinking"
    
    # 'ssh -f' runs the command in the background so the script doesn't hang
    subprocess.run(["ssh", "-f", f"root@{HOST_IP}", cmd])

def chat_with_reggie(prompt):
    # 1. Start thinking immediately
    set_remote_state("thinking")
    print(f"\nThinking...")
    
    # 2. Get response from Ollama
    result = subprocess.run(
        ["ollama", "run", MODEL, f"You are Reggie, a mini ai model. you're a hard worker and a real go getter. you are not afraid to speak your mind (do not use asterisk acting). Answer this: {prompt}"],
        capture_output=True, text=True
    )
    response = result.stdout.strip() or "I'm stuck."
    print(f"Reggie: {response}")

    # 3. Switch to talking
    set_remote_state("talking")

    # 4. Speak
    speaker_cmd = f'echo "{response}" | /root/piper/piper ... | aplay -D plughw:0,0 ...'
    subprocess.run(speaker_cmd, shell=True)

    # 5. Back 2 idle
set_remote_state("idle")    
    
    response = result.stdout.strip()
    if not response:
        response = "I'm having trouble thinking right now."

    print(f"Reggie says: {response}")

    # 3. Switch to Talking Animation
    set_remote_state("talking")

    # 4. Speak via Piper
    speaker_cmd = (
        f'echo "{response}" | /root/piper/piper --model /root/piper/{VOICE_ONNX} '
        f'--thread 1 --length_scale 1.8 --sentence_silence 0.5 --output_raw | '
        f'aplay -D plughw:0,0 -t raw -r 22050 -f S16_LE'
    )
    subprocess.run(speaker_cmd, shell=True)

    # 5. Back to Idle
    set_remote_state("idle")
# MAIN LOOP
print("--- REGGIE IS ONLINE ---")
try:
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            set_remote_state("idle")
            break
        chat_with_reggie(user_input)
except KeyboardInterrupt:
    set_remote_state("idle")
    print("\nShutting down...")
