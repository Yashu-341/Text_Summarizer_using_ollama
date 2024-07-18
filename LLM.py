import requests
import json

def summarize_text(input_text):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "qwen2:0.5b",
        "prompt": input_text,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        return f"Error: {response.text} (Status Code: {response.status_code})"

def main():
    user_input = input("Enter the text or the name of the text file: ")
    try:
        with open(user_input, "r") as file:
            text = file.read()
    except FileNotFoundError:
        text = user_input

    summary = summarize_text(text)
    print(f"Summary:\n{summary}")

if __name__ == "__main__":
    main()
