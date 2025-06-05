import easytts
import geminiaccess


difficult_tts_text = "Th1s t3xt c0nta1ns numb3rs, symb0ls, and m1ss1ng v0w3ls: $tr@ng3 ch@r@ct3r$ & punctu@t!on."

pront_tts_text = geminiaccess.gemini_text_to_tts_ready(difficult_tts_text)
print(pront_tts_text)

easytts.text_to_audio(pront_tts_text,"test.mp3")