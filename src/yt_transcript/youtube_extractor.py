from typing import List, Dict
from youtube_transcript_api import YouTubeTranscriptApi
from .transcript_interface import TranscriptExtractor

class YouTubeExtractor(TranscriptExtractor):
    """YouTube transcript extraction implementation"""
    
    def extract(self, video_id: str) -> List[Dict[str, str]]:
        """
        Extract transcript using youtube_transcript_api
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            List of transcript entries
        """
        return YouTubeTranscriptApi.get_transcript(video_id)
