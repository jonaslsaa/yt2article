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
        :root {{
            --bg-color: #fff;
            --text-color: #292929;
            --meta-color: #757575;
            --border-color: #eee;
            --blockquote-color: #666;
            --code-bg: #f8f8f8;
            --link-color: #1a8917;
        }}
        
        [data-theme="dark"] {{
            --bg-color: #1a1a1a;
            --text-color: #e0e0e0;
            --meta-color: #a0a0a0;
            --border-color: #333;
            --blockquote-color: #999;
            --code-bg: #2d2d2d;
            --link-color: #4CAF50;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
            background-color: var(--bg-color);
            transition: all 0.3s ease;
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
            color: var(--meta-color);
            font-size: 0.9em;
            margin-bottom: 2em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1em;
            display: flex;
            justify-content: space-between;
        }}
        blockquote {{
            border-left: 3px solid #292929;
            margin-left: 0;
            padding-left: 20px;
            font-style: italic;
            color: var(--blockquote-color);
        }}
        code {{
            background-color: var(--code-bg);
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
            color: var(--link-color);
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        
        .theme-toggle {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--bg-color);
            border: 2px solid var(--text-color);
            color: var(--text-color);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
        }}
        
        .theme-toggle:hover {{
            opacity: 0.8;
        }}
    </style>
    <script>
        function toggleTheme() {{
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateButtonText();
        }}
        
        function updateButtonText() {{
            const currentTheme = document.documentElement.getAttribute('data-theme');
            document.getElementById('theme-toggle').textContent = 
                currentTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
        }}
        
        // Set initial theme from localStorage or system preference
        document.addEventListener('DOMContentLoaded', () => {{
            const savedTheme = localStorage.getItem('theme');
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const theme = savedTheme || (prefersDark ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', theme);
            updateButtonText();
        }});
    </script>
</head>
<body>
    <button onclick="toggleTheme()" id="theme-toggle" class="theme-toggle">🌙 Dark Mode</button>
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
