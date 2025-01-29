import argparse
import re
import sys
import os
from urllib.parse import urlparse, parse_qs
from .youtube_extractor import YouTubeExtractor
from .openai_processor import OpenAIProcessor
from .pdf_renderer import PDFRenderer

def extract_video_id(url: str) -> str:
    """Extract video ID from YouTube URL"""
    # Handle different URL formats
    if match := re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url):
        return match.group(1)
    raise ValueError("Could not extract video ID from URL")

def main():
    parser = argparse.ArgumentParser(description='Extract and process YouTube video transcripts')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('--raw', action='store_true', help='Output raw transcript without processing')
    parser.add_argument('--pdf', action='store_true', help='Generate and open PDF output')
    parser.add_argument('--output-dir', default='output', help='Directory for PDF output (default: output)')
    args = parser.parse_args()
    
    try:
        video_id = extract_video_id(args.url)
        extractor = YouTubeExtractor()
        transcript = extractor.extract(video_id)
        
        if args.raw:
            # Print raw transcript entries
            for entry in transcript:
                print(f"[{entry['start']:.2f}s] {entry['text']}")
        else:
            # Process with OpenAI
            processor = OpenAIProcessor()
            processed_text = processor.process_transcript(transcript)
            
            if args.pdf:
                # Generate PDF and open it
                renderer = PDFRenderer(output_dir=args.output_dir)
                video_id = extract_video_id(args.url)
                pdf_path = renderer.render_and_open(processed_text, filename=video_id)
                print(f"PDF generated: {pdf_path}")
            else:
                print(processed_text)
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
