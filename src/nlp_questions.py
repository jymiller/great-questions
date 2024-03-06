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
#                {"role": "system", "content": "You are a helpful assistant."},
                 {"role": "system", "content": "You are a helpful assistant."},

                # {"role": "user", "content": f"Extract all questions from the following text: {text}"}

                # This prompt was generated through some back and forth with ChatGPT 3.5 and 4.0.  V4.0 refined the prompt to work with V3.5  which is cool
                 {"role": "user", "content": f"Please read the provided article and extract only the direct questions that are aimed at prompting reflection or strategic thinking about an organization's future, capabilities, market adaptation, and service personalization. Focus on questions that challenge the reader to consider how advancements in AI could transform their organizational strategies, enable new possibilities, broaden their market reach, or enhance customization and personalization efforts. Ignore any direct questions that do not directly relate to these themes.: {text}"}
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
