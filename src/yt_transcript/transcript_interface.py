from abc import ABC, abstractmethod
from typing import List, Dict

class TranscriptExtractor(ABC):
    """Base interface for transcript extraction implementations"""
    
    @abstractmethod
    def extract(self, video_id: str) -> List[Dict[str, str]]:
        """
        Extract transcript for a given video ID
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            List of transcript entries with text and timing
        """
        pass
