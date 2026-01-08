## Command-Line Language Translator (Python)
### Project Overview

This project demonstrates how to build a command-line based language translator using Python.
Instead of relying entirely on interactive input during execution, the project uses command-line arguments to configure how the program should behave before it starts running. This approach makes the script more suitable for automation, scripting, and CLI tools, where programs are expected to start, run, and finish without unnecessary human interaction.

The translator accepts the source language and target language as command-line arguments using the argparse module, and then translates the user-provided text using the Translator class from the translate module. This design clearly separates program configuration (via command-line arguments) from program content (text entered at runtime).


## Modules Used in This Project
### This project mainly uses two modules:

1️⃣ argparse
2️⃣ Translator (from the translate package)

## Why argparse Instead of input()?

Normally, Python programs use input() to take user input. However, input() is interactive, meaning the program pauses and waits for the user. This behavior is not suitable for scripts, servers, CI tools, or command-line utilities that should run without blocking.

Using argparse, we pass inputs at runtime from the command line, which allows the program to:

Start immediately

Validate inputs automatically

Provide a built-in --help message

Run consistently in automated environments

This is exactly the approach used in this project.

### To validate the functionality, I tested the translator using my own native language as the source and English as the target language, and the translations produced were accurate and reliable.
<img width="673" height="101" alt="Screenshot 2026-01-08 at 3 05 17 PM" src="https://github.com/user-attachments/assets/8e696249-ebe4-48b1-852a-d1f6785f7ba3" />
