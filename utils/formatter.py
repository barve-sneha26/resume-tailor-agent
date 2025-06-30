import os
from datetime import datetime

def save_tailored_resume_md(content: str, output_dir: str = "outputs"):
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tailored_resume_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    # Write the content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath
