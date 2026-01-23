# Reggie - Proxmox integrated AI
****Basically, I made my server talk and gave it a face.**

This is my first real project. I wanted to run a local AI that could actually talk to me, so I set up Ollama and Piper in a Proxmox container. But, instead of just having a boring terminal, I gave it an animated ASCII face that shows up on my actual server monitor.

Rather than showing logs and terminal text, you can see state, mood, and intent this way. Reggie's "brain" runs inside a Debian container, while his "face" displays directly on my Proxmox host's physical screen on my mini rack.

![Reggie Desktop Screenshot](https://raw.githubusercontent.com/YOUR_USER/REGGIE/main/resources/screenshot.png)
<br><br>


## What Reggie Does
Reggie isn't some fancy control panel or dashboard.
He's basically:

A desktop buddy for your homelab
A way to see what your AI is doing at a glance
A fun way to make a "headless" server not headless anymore lol
<br><br>


## Design Philosophy
I had this extra monitor sitting around and wanted to use it to display my AI somehow, but I didn't want it to just be another boring terminal with scrolling text. I thought it was a cool idea to actually see when the AI was thinking versus when it was talking back to me.
I kind of wanted it to be something like Eddy from Lab rats xd.

![ASCII Face Concepts](https://raw.githubusercontent.com/YOUR_USER/REGGIE/main/resources/faces-preview.png)

Perfect for:
- Monitors connected to your Proxmox host
- Extra displays you have lying around
- That old screen you wanted to do something with
<br><br>


## Setup
1. Run setup_host.sh on your Proxmox host
2. Pass your sound devices (/dev/snd) through to your LXC container
3. Put ai_control.py inside your container, ai_face.py on your proxmox shell. 
Edit the script with your host's IP address

<br><br>


## State & Logic Control
The way Reggie shows emotions is pretty simple. he looks for "flag files" in the /tmp folder. The AI container creates these files over SSH to tell Reggie what to do.

When Ollama is processing your question → call `set_remote_state("thinking")`  → Reggie looks like he's thinking
When Piper is reading the response out loud → call  `set_remote_state("talking")` → Reggie's mouth moves

Typical uses:
- Trigger **thinking** moods while Ollama processes text.
- Reflect **talking** states while Piper TTS is active.
- Automated **blinking** and idle micro-expressions.
<br><br>

### Face States
| State | Trigger | Expression |
| --- | --- | --- |
| `idle` | No active flags | Neutral eyes, random blinks. |
| `thinking` | `/tmp/ai_thinking` exists | Tilted puckered mouth, shifted eyes. |
| `talking` | `/tmp/ai_talking` exists | Rapidly alternating open/closed mouths. |
| `happy` | 1% random idle chance | Wide-eyed smile. |

<br><br>

### System Commands
| Command | Purpose |
| --- | --- |
| `pkill -f ai_face.py` | Terminate the face process safely. |
| `startx` | Refresh the display and restart Openbox. |
| `skill` | Older "one-word" command for process management. |


## W.I.P project
Reggie is currently under development

**ideas for the future**
- emotions based on your system health
- Having Reggie react to the mood of the AI's responses
<br><br>


