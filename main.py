import os 
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("OPENAIROUTER_API_KEY")

    response = completion(
        model="tngtech/deepseek-r1t-chimera:free",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        api_key=api_key
    )
    print(response['choices'][0]['message']['content'])

    if __name__ == "__main__":
        main()