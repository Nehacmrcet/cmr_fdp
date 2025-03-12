import os
from groq import Groq

def ask_question(api_key):
    """Ask a straightforward question to the Groq API."""
    client = Groq(api_key=api_key)
    question = "What are the top 5 places to visit in hyderabad"
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="mixtral-8x7b-32768"
    )
    
    print("Question:", question)
    print("\nResponse:", response.choices[0].message.content)
  
def main():
    api_key = "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"
    ask_question(api_key)

if __name__ == "__main__":
    main()
