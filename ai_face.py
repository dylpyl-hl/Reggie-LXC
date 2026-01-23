import os
import time
import random

# Some faces i have plans for but do not yet do anything
faces = {
    "idle": [
        "    ████      ████    ",
        "    ████      ████    ",
        "                      ",
        "      ▀▄▄▄▄▄▄▄▀       "
    ],
    "blink": [
        "                      ",
        "    ──────────        ",
        "                      ",
        "      ▀▄▄▄▄▄▄▄▀       "
    ],
    "think": [
        "    ████      ████    ",
        "    ████      ████    ",
        "                      ",
        "      ▀▄▀▄▀▄▀▄▀       "
    ],
    "happy": [
        "     ▄▄        ▄▄     ",
        "    █  █      █  █    ",
        "                      ",
        "     ▀▄▄▄▄▄▄▄▀        "
    ],
    "wink": [
        "    ████    ────────  ",
        "    ████              ",
        "                      ",
        "      ▀▄▄▄▄▄▄▄▀       "
    ],
    "focused": [
        "   ────────  ──────── ",
        "     ████      ████   ",
        "                      ",
        "       ━━━━━━━        "
    ],
    "surprised": [
        "    ████      ████    ",
        "    ████      ████    ",
        "         ▄▄           ",
        "        █  █          "
    ],
    "loading": [
        "    ▄▄▄▄      ▄▄▄▄    ",
        "    ▀▀▀▀      ▀▀▀▀    ",
        "                      ",
        "      ───▄▄▄───       "
],
    "error": [
        "    █  █      █  █    ",
        "     ██        ██     ",
        "                      ",
        "      ─────────       "
    ],
    "talk_1": [
        "    ████      ████    ",
        "    ████      ████    ",
        "        ▄▄████▄▄      ",
        "        ▀██████▀      "
    ],
    "talk_2": [
        "    ████      ████    ",
        "    ████      ████    ",
        "                      ",
        "      ▀█████████▀     "
    ],
}

import os
import time
import random

# ... [Your faces dictionary stays here] ...

def render(face_type):
    # I originally used os.system('clear'), but found that \033[H\033[J is faster as it avoids spawning a new process
    print("\033[H\033[J", end="")
    print("\n" * 1)
    for line in faces.get(face_type, faces["idle"]):
        print(line.center(50))

print("Starting AI Face... Press Ctrl+C to stop.")

# State Variables
last_blink = time.time()
blink_interval = random.uniform(3, 6)

try:
    while True:
        # 1. PRIORITY: Talking 
        if os.path.exists("/tmp/ai_talking"):
            render("talk_1")
            time.sleep(0.12)
            render("talk_2")
            time.sleep(0.12)
            continue 

        # 2. PRIORITY: Thinking 
        elif os.path.exists("/tmp/ai_thinking"):
            render("think")
            time.sleep(0.2) 
            continue

        # 3. IDLE STATE (micro-expressions for more character)
        else:
            rand = random.random()

            # 5% chance to blink
            if rand < 0.05:
                render("blink")
                time.sleep(0.15)

            # 1% chance for a different micro-expression (happy, wink, or focused)
            elif rand < 0.06: 
                rare_face = random.choice(["happy", "focused", "wink"])
                render(rare_face)
                time.sleep(1.5) # Let the expression linger

            # idle state
            else:
                render("idle")

            # Framerate for idle state
            time.sleep(0.1)

except KeyboardInterrupt:
    render("wink")
    time.sleep(1)
    print("\nReggie is sleeping.")

