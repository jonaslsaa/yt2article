import argparse
import re
import sys
import os
from urllib.parse import urlparse, parse_qs
from .youtube_extractor import YouTubeExtractor
from .openai_processor import OpenAIProcessor
from .pdf_renderer import PDFRenderer
from .html_renderer import HTMLRenderer

def extract_video_id(url: str) -> str:
    """Extract video ID from YouTube URL"""
    # Handle different URL formats
    if match := re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url):
        return match.group(1)
    raise ValueError("Could not extract video ID from URL")

def main():
    parser = argparse.ArgumentParser(description='Extract and process YouTube video transcripts', prog='yt2article')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('--raw', action='store_true', help='Output raw transcript without processing')
    parser.add_argument('--renderer', choices=['html', 'pdf', 'text'], default='html', 
                       help='Output renderer to use (default: html)')
    parser.add_argument('--output-dir', default='output', help='Directory for output files (default: output)')
    parser.add_argument('--title', help='Title for the article (defaults to video title)')
    args = parser.parse_args()
    
    try:
        video_id = extract_video_id(args.url)
        extractor = YouTubeExtractor()
        transcript, video_title, channel_name = extractor.extract(video_id)
        
        print("Video information:")
        print(" * Title:", video_title)
        print(" * Channel:", channel_name)
        
        # Use video title as default title if not specified
        if args.title == None:
            args.title = video_title
            
        # Create safe filename from title
        safe_filename = "".join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_filename = safe_filename.replace(' ', '_')
        
        if args.raw:
            # Print raw transcript entries
            for entry in transcript:
                print(f"[{entry['start']:.2f}s] {entry['text']}")
        else:
            print("Processing transcript...")
            # Process with OpenAI
            processor = OpenAIProcessor()
            processed_text = processor.process_transcript(transcript, video_title, channel_name)
            
            if args.renderer == 'pdf':
                # Generate PDF and open it
                renderer = PDFRenderer(output_dir=args.output_dir)
                pdf_path = renderer.render_and_open(processed_text, filename=safe_filename)
                print(f"PDF generated: {pdf_path}")
            elif args.renderer == 'html':
                # Generate HTML and open it
                model_name = processor.model_name
                renderer = HTMLRenderer(output_dir=args.output_dir)
                html_path = renderer.render_and_open(processed_text, filename=safe_filename, title=args.title, 
                                                   author=f"{channel_name} & {model_name}")
                print(f"HTML generated: {html_path}")
            elif args.renderer == 'text':
                print(processed_text)
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
