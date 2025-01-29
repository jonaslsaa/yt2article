import argparse
import re
from urllib.parse import urlparse, parse_qs
from .youtube_extractor import YouTubeExtractor

def extract_video_id(url: str) -> str:
    """Extract video ID from YouTube URL"""
    # Handle different URL formats
    if match := re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url):
        return match.group(1)
    raise ValueError("Could not extract video ID from URL")

def main():
    parser = argparse.ArgumentParser(description='Extract YouTube video transcripts')
    parser.add_argument('url', help='YouTube video URL')
    args = parser.parse_args()
    
    try:
        video_id = extract_video_id(args.url)
        extractor = YouTubeExtractor()
        transcript = extractor.extract(video_id)
        
        # Print transcript entries
        for entry in transcript:
            print(f"[{entry['start']:.2f}s] {entry['text']}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
