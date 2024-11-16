# AI Blog Generator

An intelligent blog post generator powered by Google's Gemini 1.5 Pro model that automatically researches topics and creates well-structured, comprehensive blog posts. The generator uses Wikipedia and DuckDuckGo search for gathering accurate information and produces markdown-formatted blog posts.

## Features

- Automatic research using Wikipedia and DuckDuckGo search
- Well-structured blog posts with headlines, introduction, main content, and conclusion
- Markdown formatting for easy publishing
- Automatic file saving with date-stamped filenames
- Interactive command-line interface

## Prerequisites

- Python 3.7 or higher
- Google API key (Gemini API access)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Atharv-Verma290/BlogGenerator.git
cd BlogGenerator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google API key:
   - Option 1: Set as environment variable:
     ```bash
     export GOOGLE_API_KEY='your-api-key-here'
     ```
   - Option 2: Enter when prompted during runtime

## Usage

Run the generator using:
```bash
python main.py
```

The program will:
1. Ask for your Google API key (if not set in environment variables)
2. Prompt you to enter a blog topic
3. Research and generate the blog post
4. Save the output to a markdown file in the `blogs` directory
5. Display the generated content in the console

### Input Example

```bash
Enter the blog topic: AI and Driving
```

### Output Example

The generator creates a markdown file with the following naming convention:
```
blogs/DD-MM-YYYY_topic-name.md
```

Example output file: `16-11-2024_ai-and-driving.md`

Sample blog post structure:
```markdown
# AI Behind the Wheel: The Road to Self-Driving Cars

The dream of self-driving cars, once a staple of science fiction, is rapidly approaching reality...

## Understanding the Levels of Autonomous Driving

The Society of Automotive Engineers (SAE) has defined six levels of driving automation...

## The Current State of Self-Driving Technology

While fully autonomous (Level 5) vehicles are still some years away...

## The Road Ahead

The future of driving is undoubtedly intertwined with AI...
```

## Project Structure

```
BlogGenerator/
├── blog_generator.py  # Main generator class
├── main.py           # Command-line interface
├── requirements.txt  # Project dependencies
└── blogs/           # Generated blog posts
```

## Dependencies

- langchain
- langchain-community
- langchain-google-genai
- google-generativeai
- wikipedia-api
- duckduckgo-search

## Error Handling

The generator includes error handling for:
- Missing API keys
- Invalid topics
- Generation failures
- File system operations
