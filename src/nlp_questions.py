import os
import openai

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_questions(text):
    """
    Uses OpenAI's API to extract questions from the given text.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Adjust according to the latest available models
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract all questions from the following text: {text}"}
            ]
        )
 #       extracted_text = response.choices[0].message["content"]
#        extracted_text = response["choices"][0]["message"]["content"]
        extracted_text = response.choices[0].message.content
        return extracted_text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_text_from_file(file_path):
    """
    Reads text from the specified file and returns it.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# File path to the text file containing the scraped text
file_path = "scraped_text.txt"

# Read the scraped text from the file
scraped_text = read_text_from_file(file_path)

# Extract questions from the scraped text
questions = extract_questions(scraped_text)
print("Extracted Questions:")
print(questions)
