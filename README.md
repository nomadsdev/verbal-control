# VerbalControl 
 
**VerbalControl** is a Python-based project that allows users to control system commands using voice commands. It listens for specific voice phrases and executes predefined commands based on the recognized phrases. 
 
## Features 
 
- **Voice Command Recognition:** Utilizes Google's Speech Recognition API to understand spoken commands. 
- **Command Execution:** Executes system commands as specified in a configuration file. 
- **Customizable Commands:** Commands and trigger phrases are configurable via text files. 
- **Command Logging:** Logs executed commands to a file for history tracking. 
- **Error Handling:** Includes basic error handling for speech recognition and command execution. 
 
## Installation 
 
1. **Clone the repository:** 
```bash 
git clone https://github.com/nomadsdev/verbal-control.git 
``` 
 
2. **Navigate to the project directory:** 
```bash 
cd verbal-control 
``` 
 
3. **Install the required dependencies:** 
```bash 
pip install -r requirements.txt 
``` 
 
## Configuration 
 
1. **Create `commands.txt`:** This file should contain the voice phrases that trigger the commands. Each phrase should be on a new line. 
```plaintext 
run command 
execute script 
``` 
 
2. **Create `command.config`:** This file should contain the system command(s) that you want to execute when a phrase is recognized. 
```plaintext 
python test.py 
``` 
 
3. **Create `config.json`:** This file should contain configuration settings for the project. 
```json 
{ 
"phrases_file": "commands.txt", 
"command_file": "command.config", 
"language": "en-US" 
} 
``` 
 
## Usage 
 
1. **Run the script:** 
```bash 
python voice_command.py 
``` 
 
2. **Speak one of the phrases listed in `commands.txt`.** If recognized, the corresponding command from `command.config` will be executed. 
 
## Command History 
- **Viewing Command History:** The script maintains a log of executed commands in `command_log.txt`. After each command execution, the history is updated. 
```bash 
python voice_command.py 
``` 
 
## Troubleshooting 
 
- **"Sorry, I did not understand that."**: Ensure you are speaking clearly and that the microphone is functioning correctly. 
- **"Error executing command:"**: Verify that the command in `command.config` is correct and executable in your environment. 
- **"Error reading from file:"**: Check that your `commands.txt`, `command.config`, and `config.json` files are correctly formatted and present in the project directory. 
 
## Dependencies 
- `speech_recognition`: For recognizing spoken commands. 
- `pyaudio`: For accessing the microphone. 
- `subprocess`: For executing system commands. 
 
You can install these dependencies via: 
```bash 
pip install speech_recognition pyaudio 
``` 
 
## Contributing 
If you would like to contribute to VerbalControl, please fork the repository and submit a pull request. Contributions are welcome! 
 
## License 
This project is licensed under the MIT License. 
 
## Contact 
For any questions or feedback, please reach out to support@jmmentertainment.com or open an issue on the GitHub repository. 
