import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

from .prompts import transcript_prompt

class OpenAIProcessor:
    """Processes transcripts using OpenAI API"""
    
    def __init__(self):
        load_dotenv(override=True)
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE_URL'))
        self.model_name = os.getenv('OPENAI_MODEL_NAME')
        if os.getenv('OPENAI_API_BASE_URL'):
            print(f"Using OpenAI API base URL: {os.getenv('OPENAI_API_BASE_URL')}")
            print(f"Using OpenAI model name: {os.getenv('OPENAI_MODEL_NAME')}")
        
    def process_transcript(self, transcript: List[Dict]) -> str:
        """
        Process transcript entries using OpenAI
        
        Args:
            transcript: List of transcript entries
            
        Returns:
            Processed text from OpenAI
        """
        # Combine all transcript text
        full_text = '\n'.join(entry['text'] for entry in transcript)
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": transcript_prompt(transcript=full_text)}
            ]
        )
        
        return response.choices[0].message.content
