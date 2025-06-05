from gtts import gTTS
from io import BytesIO

def text_to_speech(text, lang='en'):
    """
    Converts text to speech using gTTS and returns the audio as BytesIO.
    :param text: The text to convert to speech.
    :param lang: Language for the speech (default is 'en').
    :return: BytesIO object containing the mp3 audio.
    """
    tts = gTTS(text=text, lang=lang)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

def save_audio_to_file(audio_bytes, filename):
    """
    Saves the audio from BytesIO to a file.
    :param audio_bytes: BytesIO object containing the mp3 audio.
    :param filename: The name of the file to save the audio to.
    """
    with open(filename, 'wb') as f:
        f.write(audio_bytes.getbuffer())

def text_to_audio(pront,filename, lang='en'):
    byte = text_to_speech(pront,lang)
    save_audio_to_file(byte,filename)
