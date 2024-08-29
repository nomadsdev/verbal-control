import speech_recognition as sr
import subprocess
import json

def r(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
        return content
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None

def x(file_path):
    try:
        with open(file_path, 'r') as f:
            phrases = f.read().strip().split('\n')
        return phrases
    except Exception as e:
        print(f"Error reading phrases from file: {e}")
        return []

def log_command(command, log_file='command_log.txt'):
    try:
        with open(log_file, 'a') as f:
            f.write(f"{command}\n")
    except Exception as e:
        print(f"Error logging command: {e}")

def e(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print("Executed.")
        log_command(command)
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {}

def show_command_log(log_file='command_log.txt'):
    try:
        with open(log_file, 'r') as f:
            commands = f.readlines()
        if commands:
            print("Command History:")
            for command in commands:
                print(command.strip())
        else:
            print("No commands in history.")
    except Exception as e:
        print(f"Error reading command log: {e}")

def lfc():
    config = load_config('config.json')
    rzn = sr.Recognizer()
    m = sr.Microphone()

    phrases_file = config.get('phrases_file', 'commands.txt')
    command_file = config.get('command_file', 'command.config')
    language = config.get('language', 'en-US')

    phrases = x(phrases_file)
    if not phrases:
        print("No phrases.")
        return

    with m as s:
        print("Noise adjustment...")
        rzn.adjust_for_ambient_noise(s)
        print("Listening...")
        audio = rzn.listen(s)

    try:
        text = rzn.recognize_google(audio, language=language)
        print(f"Recognized: {text}")
        if any(phrase.lower() in text.lower() for phrase in phrases):
            command = r(command_file)
            if command:
                e(command)
            else:
                print("No command.")
        else:
            print("Command not supported.")
    except sr.UnknownValueError:
        print("Not understood.")
    except sr.RequestError as e:
        print(f"Service error: {e}")

    show_command_log()

if __name__ == "__main__":
    lfc()