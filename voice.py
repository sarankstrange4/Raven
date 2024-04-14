from pathlib import Path
from openai import OpenAI
import pygame
import os

client = OpenAI(api_key='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')

def generate_and_save_audio(text):
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text,
)

    response.stream_to_file("output.mp3")
    #play_audio(audio_data)
from playsound import playsound as playsounds

def play_audio(filename):
    playsound(filename)

# Example usage:
audio_file_path = "output.mp3"  # Update this with the path to your audio file
play_audio(audio_file_path)


# Example usage:
#audio_file_path = "output.mp3"  # Update this with the path to your audio file
#play_audio(audio_file_path)


# Example usage:
#text_to_convert = 'i am good how are you,h, right, yes you can do this now'
#audio_file_path = generate_and_save_audio(text_to_convert)
#play_audio('output.mp3')
