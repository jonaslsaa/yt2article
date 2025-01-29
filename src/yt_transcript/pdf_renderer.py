import markdown
from weasyprint import HTML
import os
import subprocess

class PDFRenderer:
    """Renders markdown to PDF and opens it"""
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize PDF renderer
        
        Args:
            output_dir: Directory to save PDFs (default: "output")
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def render_and_open(self, markdown_text: str, filename: str = "transcript") -> str:
        """
        Convert markdown to PDF and open it
        
        Args:
            markdown_text: Markdown formatted text
            filename: Name for the PDF file (without extension)
            
        Returns:
            Path to generated PDF
        """
        # Convert markdown to HTML
        html = markdown.markdown(markdown_text)
        
        # Create PDF path
        pdf_path = os.path.join(self.output_dir, f"{filename}.pdf")
        
        # Generate PDF
        HTML(string=html).write_pdf(pdf_path)
        
        # Open PDF with default application
        if os.path.exists(pdf_path):
            if os.uname().sysname == "Darwin":  # macOS
                subprocess.run(["open", pdf_path])
            elif os.uname().sysname == "Linux":
                subprocess.run(["xdg-open", pdf_path])
            elif os.uname().sysname == "Windows":
                subprocess.run(["start", pdf_path], shell=True)
                
        return pdf_path
