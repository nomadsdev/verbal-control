import speech_recognition as sr
import subprocess

def r(l):
    try:
        with open(l, 'r') as f:
            c = f.read().strip()
        return c
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None

def x(l):
    try:
        with open(l, 'r') as f:
            p = f.read().strip().split('\n')
        return p
    except Exception as e:
        print(f"Error reading phrases from file: {e}")
        return []

def e(c):
    try:
        subprocess.run(c, shell=True, check=True)
        print("Executed.")
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")

def lfc():
    rzn = sr.Recognizer()
    m = sr.Microphone()

    p = x('commands.txt')
    if not p:
        print("No phrases.")
        return

    with m as s:
        print("Noise adjustment...")
        rzn.adjust_for_ambient_noise(s)
        print("Listening...")
        a = rzn.listen(s)

    try:
        t = rzn.recognize_google(a)
        print(f"Recognized: {t}")
        if any(ph.lower() in t.lower() for ph in p):
            c = r('command.config')
            if c:
                e(c)
            else:
                print("No command.")
        else:
            print("Command not supported.")
    except sr.UnknownValueError:
        print("Not understood.")
    except sr.RequestError as e:
        print(f"Service error: {e}")

if __name__ == "__main__":
    lfc()