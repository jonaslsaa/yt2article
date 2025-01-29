import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIProcessor:
    """Processes transcripts using OpenAI API"""
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
    def process_transcript(self, transcript: List[Dict]) -> str:
        """
        Process transcript entries using OpenAI
        
        Args:
            transcript: List of transcript entries
            
        Returns:
            Processed text from OpenAI
        """
        # Combine all transcript text
        full_text = ' '.join(entry['text'] for entry in transcript)
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that processes YouTube video transcripts into clear, well-formatted text."},
                {"role": "user", "content": f"Process this transcript into clear, well-formatted text:\n\n{full_text}"}
            ]
        )
        
        return response.choices[0].message.content
