from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq

# Initialize Flask app
app = Flask(__name__)

# Initialize the LLM (ChatGroq) with your model and API key
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key="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"
)


# Home route to render the chatbot interface
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle the chat requests
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']

    # Get the response from the LLM
    response = llm.invoke(user_message)

    return jsonify({'response': response.content})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
