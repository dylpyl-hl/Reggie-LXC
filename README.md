# R.E.G.G.I.E- Proxmox integrated AI

****Basically, I made my server talk and gave it a face.**   

This is my first real project. I wanted to run a local AI that could actually talk to me, so I set up Ollama and Piper in a Proxmox container. But, instead of just having a boring terminal, I gave it an animated ASCII face that shows up on my actual server monitor.

Rather than showing logs and terminal text, you can see state, mood, and intent this way. Reggie's "brain" runs inside a Debian container, while his "face" displays directly on my Proxmox host's physical screen on my mini rack.

<img src="https://github.com/user-attachments/assets/342b2f25-2f44-49fb-b575-61bfb65625b2" width="600">
<br><br>
*R.E.G.G.I.E = Real Easy Graphical GUI Interface Entity

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

<img width="359" height="810" alt="Image" src="https://github.com/user-attachments/assets/fe75d633-5fbc-48f5-934d-471fd8607ac1" />

(some faces are for future use)

Perfect for:
- Monitors connected to your Proxmox host
- Extra displays you have lying around
- That old screen you wanted to do something with
<br><br>


## Setup process
1. Run setup_host.sh on your Proxmox host
2. Install your AI model and Piper TTS on your LXC, and openbox on your proxmox shell <sub>(piper has loads of different voices, i use en_US-lessac-low the best)
3. Pass your sound devices through to your LXC container
4. Put ai_control.py inside your container & ai_face.py on your proxmox shell. 
Edit the script with your host's IP address

> **IMPORTANT:**  
> Reggie's size depends on your monitor and font size. If he looks weird or off-center, open `ai_face.py` and find this line: `print(line.center(50))`. Change the `50` to match your screen width:  
> Small screen, try 40 | Normal screen, try 80 | Big screen, try 100 or 120. Just mess with the number until Reggie looks centered!

<br>

<img width="1045" height="137" alt="Image" src="https://github.com/user-attachments/assets/87c2fcf2-7b21-4948-aa54-5a012fcbdb67" />

<br>

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


### System Commands
| Command | Purpose |
| --- | --- |
| `pkill -f ai_face.py` | Terminate the face process safely. |
| `startx` | Refresh the display and restart Openbox. |
| `skill` | Older "one-word" command for process management. |

## W.I.P project
I'm still going to add more features, but the foundation is built!!

**ideas for the future**
- emotions based on your system health
- Having Reggie react to the mood of the AI's responses
<br><br>



