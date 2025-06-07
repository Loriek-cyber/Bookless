from book_processor import BookPageProcessor

# Example page from a book
test_page = '''
"Where are you going?" asked Alice, watching the White Rabbit scurry past.
The White Rabbit looked at his pocket watch nervously. "Oh dear! Oh dear! I shall be late!"
Alice felt curious about this strange creature. She had never seen a rabbit with a waistcoat and watch before.
"Please, wait!" she called out, but the rabbit had already disappeared down a large rabbit hole.
'''

# Process the page
processor = BookPageProcessor()

try:
    # Process the text
    segments = processor.process_page(test_page)
    
    # Create audio files
    processor.create_audio_segments(segments, "output_audio")
    print("Audio files created successfully!")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")


