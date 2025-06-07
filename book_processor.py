import geminiaccess
import easytts
import json
import re

class BookPageProcessor:
    def __init__(self):
        self.available_langs = {
            "narrator": "en-GB",
            "male_character": "en-US",
            "female_character": "en-AU",
            "child": "en-GB"
        }

    def process_page(self, page_text: str) -> dict:
        """
        Send the page to Gemini to separate it into different speaking parts
        """
        prompt = f"""
        Analyze this text and separate it into speaking parts. Format the output as JSON with:
        - "narrator" for narrative parts
        - "character_name" and "dialogue" for each speaking character
        - "character_type" as either "male_character", "female_character", or "child"
        
        Text to analyze:
        {page_text}
        """
        
        result = geminiaccess.gemini_text_to_tts_ready(prompt)
        return json.loads(result)

    def create_audio_segments(self, processed_text: dict, output_dir: str):
        """
        Create separate audio files for each segment using different voices
        """
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        segment_count = 0
        
        # Handle narrator parts
        for narrator_text in processed_text.get("narrator", []):
            filename = f"{output_dir}/segment_{segment_count}_narrator.mp3"
            easytts.text_to_audio(narrator_text, filename, self.available_langs["narrator"])
            segment_count += 1
            
        # Handle character dialogues
        for dialogue in processed_text.get("dialogues", []):
            character_type = dialogue["character_type"]
            filename = f"{output_dir}/segment_{segment_count}_{dialogue['character_name']}.mp3"
            easytts.text_to_audio(
                dialogue["dialogue"],
                filename,
                self.available_langs[character_type]
            )
            segment_count += 1