# YouTube Transcript Extractor

A command line tool to extract transcripts from YouTube videos using the youtube-transcript-api.

## Installation

```bash
pip install youtube-transcript-api
```

## Usage

```bash
python -m yt_transcript <youtube_url>
```

The tool will extract the video ID from the URL and fetch the transcript using youtube-transcript-api.

## Features

- Extract transcripts from YouTube videos using just the URL
- Clean interface abstraction for future transcript modes
- Uses argparse for robust CLI argument handling
