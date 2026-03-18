
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key="GROQ_API_KEY"
)

@app.route("/", methods=["GET","POST"])
def home():
    response = ""

    if request.method == "POST":
        prompt = request.form["prompt"]

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile"
        )

        response = chat_completion.choices[0].message.content

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7860)