# Gemini Multi-Turn Chat

A Python application that demonstrates multi-turn conversations with Google's Gemini AI model. This project showcases how to maintain context across multiple interactions with the Gemini API.

## Features

- Multi-turn conversation support with context preservation
- Secure API key management using environment variables
- Error handling and graceful failure management
- Interactive command-line interface
- Configurable temperature settings for response generation

## Prerequisites

- Python 3.7 or higher
- A Google Cloud account with Gemini API access
- A valid Gemini API key

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/satyamkumarjha2002/gemini-multi-turn-chat>
cd gemini-multi-turn-chat
```

2. Install the required dependencies:
```bash
pip install google-generativeai python-dotenv
```

3. Create a `.env` file in the project root directory:
```bash
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

1. Make sure your `.env` file is properly configured with your API key.

2. Run the script:
```bash
python context_aware_gemini_chat.py
```

3. The program will prompt you for input twice, maintaining context between interactions.

## Project Structure

- `context_aware_gemini_chat.py`: Main application file
- `.env`: Environment variables file (not tracked in git)
- `README.md`: This documentation file

## Code Components

- **API Configuration**: Sets up the Gemini API with proper error handling
- **User Input Handling**: Manages user input with input validation
- **Model Response Generation**: Handles API calls with error management
- **Context Management**: Maintains conversation history between turns

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key secure and private
- The project uses environment variables for sensitive data

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- API configuration issues
- Response generation failures
- Invalid user inputs