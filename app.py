from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Personal AI Agent is alive!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in request."}), 400

    message = data["message"].lower()

    # Basic logic (can be replaced with AI later)
    if "plan my day" in message:
        response = (
            "🗓️ Here's a simple plan for your day:\n"
            "- Wake up at 7:00 AM\n"
            "- Workout at 7:30 AM\n"
            "- Deep work from 9 AM to 12 PM\n"
            "- Lunch at 1 PM\n"
            "- Light walk at 5 PM\n"
            "- Reflect and relax after 8 PM"
        )
    elif "how am i" in message:
        response = "🧠 I'm still learning about you, but you're doing great. Want to talk about anything?"
    else:
        response = f"🤖 You said: '{message}'. I’m still learning how to help you best!"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
