```python
import openai
import time
from ratelimiter import RateLimiter

# Load the OpenAI API key
openai.api_key = 'openai_api_key'

# Define a rate limiter with a maximum of 60 requests per minute
rate_limiter = RateLimiter(max_calls=60, period=60)

def openai_integration(text_input, task):
    """
    Function to integrate OpenAI GPT-3/GPT-4 for advanced language tasks.
    """
    # Check the task type and call the appropriate OpenAI API
    if task == 'translation':
        return translate_text(text_input)
    elif task == 'summarization':
        return summarize_text(text_input)
    elif task == 'question_answering':
        return answer_question(text_input)
    else:
        raise ValueError("Invalid task type. Choose from 'translation', 'summarization', 'question_answering'.")

def translate_text(text_input):
    """
    Function to translate text using OpenAI.
    """
    with rate_limiter:
        response = openai.Translation.create(
            engine="text-davinci-002",
            text=text_input,
            target_language="en"
        )
    return response.choices[0].text

def summarize_text(text_input):
    """
    Function to summarize text using OpenAI.
    """
    with rate_limiter:
        response = openai.Summarization.create(
            engine="text-davinci-002",
            text=text_input,
            max_tokens=100
        )
    return response.choices[0].text

def answer_question(text_input):
    """
    Function to answer questions using OpenAI.
    """
    with rate_limiter:
        response = openai.QuestionAnswering.create(
            engine="text-davinci-002",
            text=text_input,
            max_tokens=100
        )
    return response.choices[0].text
```