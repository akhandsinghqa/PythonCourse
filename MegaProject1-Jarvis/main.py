import speech_recognition as sr

from function import speak, process_command

recognizer = sr.Recognizer()

if __name__ == "__main__":
    speak("Jarvis is online.")

    with sr.Microphone() as source:
        print("Initial calibration... please be quiet.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        recognizer.energy_threshold = 300

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=3)

        word = recognizer.recognize_google(audio).lower()
        print(f"Heard: {word}")

        if "hello" in word or "jarvis" in word:
            speak("Yes?")

            with sr.Microphone() as source:
                print("Listening for command...")
                command_audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            command = recognizer.recognize_google(command_audio)
            print(f"Command: {command}")
            process_command(command)

    except sr.WaitTimeoutError:
        pass  # Silent ignore if no one speaks
    except sr.UnknownValueError:
        print("... (Listening) ...")
    except Exception as e:
        print(f"Error: {e}")
