from flask import Flask, request, jsonify
import openai
from gtts import gTTS
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "🤖 Namaste Robot Backend is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("text", "Hello")

    # Ask GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Namaste Robot, a friendly talking assistant."},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message["content"]
    print("GPT:", answer)

    # Convert to speech (optional, you can remove this if not needed)
    tts = gTTS(answer)
    tts.save("response.mp3")

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
