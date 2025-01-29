from typing import List, Dict, Tuple
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from .transcript_interface import TranscriptExtractor

class YouTubeExtractor(TranscriptExtractor):
    """YouTube transcript extraction implementation"""
    
    def extract(self, video_id: str) -> Tuple[List[Dict[str, str]], str]:
        """
        Extract transcript using youtube_transcript_api
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Tuple of (transcript entries list, video title)
        """
        url = f"https://www.youtube.com/watch?v={video_id}"
        
        # Get video title using yt-dlp
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Untitled Video')
            channel = info.get('channel', 'Unknown Channel')
        
        # Get transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        return transcript, title, channel
