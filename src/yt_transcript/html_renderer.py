import markdown
import os
import subprocess
from datetime import datetime
from pathlib import Path

class HTMLRenderer:
    """Renders markdown to HTML with Medium-like styling"""
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize HTML renderer
        
        Args:
            output_dir: Directory to save HTML files (default: "output")
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def render_and_open(self, markdown_text: str, filename: str = "transcript", title: str = "Article", author: str = "AI") -> str:
        """
        Convert markdown to HTML and open it
        
        Args:
            markdown_text: Markdown formatted text
            filename: Name for the HTML file (without extension)
            title: Title for the article
            
        Returns:
            Path to generated HTML
        """
        # Convert markdown to HTML
        html_content = markdown.markdown(markdown_text, extensions=['extra'])
        
        # Create HTML path
        html_path = os.path.join(self.output_dir, f"{filename}.html")
        
        # Get current date
        current_date = datetime.now().strftime("%B %d, %Y")
        
        # HTML template with Medium-like styling
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            line-height: 1.6;
            color: #292929;
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 600;
            margin-top: 2em;
            margin-bottom: 0.5em;
        }}
        h1 {{
            font-size: 2.5em;
            margin-top: 1em;
        }}
        p {{
            margin-bottom: 1.5em;
            font-size: 18px;
        }}
        .meta {{
            color: #757575;
            font-size: 0.9em;
            margin-bottom: 2em;
            border-bottom: 1px solid #eee;
            padding-bottom: 1em;
            display: flex;
            justify-content: space-between;
        }}
        blockquote {{
            border-left: 3px solid #292929;
            margin-left: 0;
            padding-left: 20px;
            font-style: italic;
            color: #666;
        }}
        code {{
            background-color: #f8f8f8;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Menlo, Monaco, "Courier New", monospace;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        img {{
            max-width: 100%;
            height: auto;
            margin: 2em 0;
        }}
        a {{
            color: #1a8917;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <article>
        <h1>{title}</h1>
        <div class="meta">
            <span class="date">{current_date}</span>
            <span class="author">By {author}</span>
        </div>
        {html_content}
    </article>
</body>
</html>
"""
        
        # Write HTML file
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        # Open HTML with default browser
        if os.path.exists(html_path):
            if os.uname().sysname == "Darwin":  # macOS
                subprocess.run(["open", html_path])
            elif os.uname().sysname == "Linux":
                subprocess.run(["xdg-open", html_path])
            elif os.uname().sysname == "Windows":
                subprocess.run(["start", html_path], shell=True)
                
        return html_path
