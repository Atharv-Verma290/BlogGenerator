import os
import re
from datetime import datetime
import getpass
from blog_generator import BlogGenerator

def get_api_key() -> str:
    """Get the Google API key from environment variable or user input."""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("\nGoogle API key not found in environment variables.")
        api_key = getpass.getpass("Please enter your Google API key: ")
        
        if not api_key:
            raise ValueError("API key is required to run the blog generator.")
            
    return api_key

def clean_topic(title: str) -> str:
    """Convert title to a valid filename."""
    cleaned = re.sub(r'[\\/*?:"<>|]', "", title)
    cleaned = re.sub(r'\s+', "-", cleaned.strip())
    return cleaned.lower()

def save_blog_post(blog_post: str, topic: str) -> str:
    """Save the generated blog post to a file."""
    output_dir = "blogs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    date_str = datetime.now().strftime("%d-%m-%Y")
    cleaned_topic = clean_topic(topic)
    filename = f"{date_str}_{cleaned_topic}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(blog_post)
    
    return filepath

def main():
    # Get API key
    try:
        api_key = get_api_key()
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Initialize the blog generator
    print("\nInitializing blog generator...")
    generator = BlogGenerator(api_key)
    
    # Get topic from user
    topic = input("\nEnter the blog topic: ")
    
    # Generate blog
    print("\nGenerating blog post... This may take a few minutes.")
    blog_post = generator.generate_blog(topic)
    
    filepath = save_blog_post(blog_post, topic)

    # Print the generated blog
    print("\nGenerated Blog Post:")
    print("===================")
    print(blog_post)

    print(f"Blog post saved to: {filepath}")

if __name__ == "__main__":
    main()