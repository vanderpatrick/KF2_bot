# Welcome to My First Project

This repository contains the first project I've completed since finishing my bootcamp. Feedback is highly appreciated!

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Troubleshooting](#troubleshooting)
6. [Future Plans](#future-plans)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This project is a bot for [Killing Floor](https://www.tripwireinteractive.com/games/killing-floor-2) that helps in-game by automating certain actions. The bot is designed to improve gameplay by handling repetitive tasks efficiently.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Install dependencies**
   Install the necessary Python libraries using \`pip\`. The project requires \`pyautogui\` and \`pynput\`.
   ```bash
   pip install pyautogui pynput
   ```
## Usage

1. **Configure the bot**  
   Open the script and modify the `keyDown` and `keyUp` parameters to your preferred keys.

2. **Position your character**  
   Crouch and aim at the top ceiling to avoid bile damage from Hans and BFB (Big Fat Boy).

3. **Run the script**
   ```bash
   python main.py

## Configuration

You can customize key bindings and other settings directly in the script:

- **Key Bindings:** Modify the `keyDown` and `keyUp` parameters.
- **Game Settings:** Ensure you are in the correct map and position.

## Troubleshooting

If you encounter issues:

1. **Check Dependencies:** Ensure `pyautogui` and `pynput` are correctly installed.
2. **Run as Administrator:** Some scripts may require elevated permissions.
3. **Game Compatibility:** Ensure your game version matches the bot's requirements.


## Future Plans

- [ ] Add dependency management via `requirements.txt` or `pyproject.toml`.
- [ ] Include a server link in the usage instructions.
- [ ] Improve error handling and logging.
- [ ] Add functionality to change perks when level 25 is reached.
- [ ] Implement bash scripts in order to run this on a server.

# this project is not done, half of this read me is not available currently