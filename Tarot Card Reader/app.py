import requests
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Your Google Gemini API Key
api_key = "AIzaSyCU8FtKMqofZ7MIzPrCo365f1Xg5jZo2Mw"

class GeminiModel:
    def __init__(self, api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"):
        self.api_key = api_key
        self.base_url = base_url

    def generate_text(self, prompt):
        """ Call the Gemini API to generate text based on a prompt """
        url = f"{self.base_url}models/gemini-2.5/text:predict"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the request body
        body = {
            "instances": [
                {"content": prompt}
            ],
            "parameters": {
                "temperature": 0.7,
                "max_output_tokens": 150
            }
        }

        # Send the POST request to Gemini API
        response = requests.post(url, headers=headers, json=body)
        
        # Check for successful response
        if response.status_code == 200:
            # Extract the generated text from the response
            result = response.json()
            generated_text = result['predictions'][0]['content']
            return generated_text
        else:
            # Handle error
            return f"Error: {response.status_code}, {response.text}"

# Initialize the Gemini model with your API Key
gemini_model = GeminiModel(api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['question']
    
    # Tarot prompt to simulate a reading
    prompt = f"Tarot card reading for: {user_input}. Provide a mystical and insightful prediction."

    # Generate Tarot reading using Google Gemini API
    tarot_reading = gemini_model.generate_text(prompt)

    return jsonify({
        'reading': tarot_reading
    })

if __name__ == "__main__":
    app.run(debug=True)
