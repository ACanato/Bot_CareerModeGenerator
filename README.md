# Discord Bot - Career Mode Idea Generator (FIFA & FOOTBALL MANAGER)

This is a Discord bot that generates career mode ideas/challenges.

---

## Features

- When the `!generate` command is used, the bot sends a message with two reaction options:  
  ⚽️ EA FC (FIFA)  
  💻 Football Manager (FM)

- By reacting to that message with one of the options, the bot deletes the original message and sends a new message with a random idea related to the chosen game.

---

## How it works

1. **`!generate` command**  
   Sends a message with reaction options (⚽️ and 💻) for the user to choose the type of game idea they want to receive.

2. **Reaction to the bot**  
   When a reaction is clicked, the bot identifies which reaction it was, deletes the original message, and sends a new message with a random idea for the respective game.

3. **Idea lists**  
   The bot has two predefined lists of ideas:  
   - `ideias_fifa`: challenges and scenarios for EA FC (FIFA)  
   - `ideias_fm`: challenges and scenarios for Football Manager

---

## Requirements

- Python 3.8+  
- `discord.py` library installed (`pip install discord.py`)

---

## Setup

1. Create an application and bot on the Discord Developer Portal: https://discord.com/developers/applications  
2. Get the bot token and replace `TOKEN` in the script with the actual token.  
3. Give the bot necessary permissions to read messages, send messages, manage reactions, etc.
