# other_file.py

from assist import speak, wishMe, takeCommand

if __name__ == "__main__":
    text_to_speak = "Hello, this is EROS. How can I help you"
    speak(text_to_speak)
    wishMe()
    user_query = takeCommand()
    print(f"User's command: {user_query}")
