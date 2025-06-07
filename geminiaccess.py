import requests
import os

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
API_KEY = os.environ.get('GOOGLE_API')

def gemini_text_to_tts_ready(prompt: str) -> str:
    """
    Sends a prompt to the Gemini model and returns a TTS-friendly response.
    """
    if not API_KEY:
        raise ValueError("Google Gemini API key not found. Please set the 'GOOGLE_API' environment variable.")
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": f"Transform this text into something readable by TTS: {prompt}"}]}
        ]
    }
    params = {"key": API_KEY}
    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()
    # Extract the generated text
    return result["candidates"][0]["content"]["parts"][0]["text"]

# Example usage:
# tts_ready_text = gemini_text_to_tts_ready("Ths is a txt with errrs.")
# print(tts_ready_text)


# ...existing code...

def gemini_text_to_tts_ready(prompt: str) -> str:
    """
    Sends a prompt to the Gemini model and returns a TTS-friendly response.
    """
    if not API_KEY:
        raise ValueError("Google Gemini API key not found. Please set the 'GOOGLE_API' environment variable.")
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    params = {"key": API_KEY}
    
    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()
    
    return result["candidates"][0]["content"]["parts"][0]["text"]