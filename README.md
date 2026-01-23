# 🤖 Reggie AI: The Living ASCII Companion
**A playful, expressive, distributed AI face for Proxmox.**

Reggie is an animated companion for your home lab. He visualizes AI processing and system states using a living ASCII character.

Rather than showing logs and terminal text, Reggie shows state, mood, and intent, giving your server node a friendly, readable presence.

![Reggie Desktop Screenshot](https://raw.githubusercontent.com/YOUR_USER/REGGIE/main/resources/screenshot.png)
<br><br>


## What Reggie Does
Originally, I developed Reggie because I wanted to know if my Proxmox container was actually listening to me or just hanging. I wanted visual feedback to see when he was "thinking" and when he was "speaking." Since then, Reggie has grown into a personality-driven head that can reflect different moods based on your interactions.
<br><br>


## Design Philosophy
Reggie is not a control panel.

He is:
- A companion for your rack/desk
- A status glance for your LLM
- A playful way to visualize a "headless" server.

![ASCII Face Concepts](https://raw.githubusercontent.com/YOUR_USER/REGGIE/main/resources/faces-preview.png)

Perfect for:
- Proxmox Host monitors
- Secondary server displays
- Dedicated tty screens
<br><br>


## Installation
- Run the `setup_host.sh` on your Proxmox Host.
- Map your `/dev/snd` devices to your LXC container.
- Deploy `ai_control.py` inside your container.
- Configure your Host IP in the script.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br><br>


## State & Logic Control
Reggie works by monitoring "flag files" in the `/tmp` directory of the host. The Brain (Container) pushes these flags via SSH to drive Reggie's expressions directly.

Use `set_remote_state("thinking")` to trigger calculation faces. Use `set_remote_state("talking")` to trigger speech animations.

Typical uses:
- Trigger **thinking** moods while Ollama processes text.
- Reflect **talking** states while Piper TTS is active.
- Automated **blinking** and idle micro-expressions.
<br><br>


## Entities and States
This table shows the various faces Reggie can make and what triggers them.

### Face States
| State | Trigger | Expression |
| --- | --- | --- |
| `idle` | No active flags | Neutral eyes, random blinks. |
| `thinking` | `/tmp/ai_thinking` exists | Tilted puckered mouth, shifted eyes. |
| `talking` | `/tmp/ai_talking` exists | Rapidly alternating open/closed mouths. |
| `happy` | 1% random idle chance | Wide-eyed smile. |

### System Commands
| Command | Purpose |
| --- | --- |
| `pkill -f ai_face.py` | Terminate the face process safely. |
| `startx` | Refresh the display and restart Openbox. |
| `skill` | Older "one-word" command for process management. |
<br><br>


## Roadmap
Reggie is currently under active development.

**Coming Soon:**
- Volume-peak detection for synchronized mouth movement.
- "Sore throat" auto-fix for audio permissions.
- Emotional integration with LLM sentiment analysis.
<br><br>


## License
Reggie is licensed under the "MIT License."
<br><br>


## Support Reggie
If you find Reggie useful, please consider giving the repo a ⭐ to support the work!<br>
