#!/bin/bash
# reggie host setup script

echo "installing display utilities..."
apt update && apt install -y unclutter alsa-utils

echo "setting up perm audio permissions (UDEV)..."
echo 'KERNEL=="controlC*|pcm*|timer", NAME="snd/%k", MODE="0666"' > /etc/udev/rules.d/99-reggie-audio.rules
udevadm control --reload-rules && udevadm trigger

echo "Setup complete!! Please restart your container to apply audio changes."
