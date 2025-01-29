# YouTube Transcript Extractor

A command line tool to extract and process transcripts from YouTube videos using OpenAI.

## Installation

```bash
pip install youtube-transcript-api python-dotenv openai
```

Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Process transcript with OpenAI:
```bash
python -m src.yt_transcript <youtube_url>
```

Get raw transcript:
```bash
python -m src.yt_transcript --raw <youtube_url>
```

## Features

- Extract transcripts from YouTube videos using just the URL
- Process transcripts using OpenAI to improve readability
- Clean interface abstraction for future transcript modes
- Uses argparse for robust CLI argument handling
