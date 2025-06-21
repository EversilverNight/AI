from flask import Flask, request, jsonify

app = Flask(__name__)

def load_user_data():
    if not os.path.exists("user_data.json"):
        return {}
    with open("user_data.json", "r") as f:
        return json.load(f)

def save_user_data(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def home():
    return "👋 Personal AI Agent is alive!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message'."}), 400

    message = data["message"].lower()
    user = load_user_data()

    if "plan my day" in message:
        name = user.get("name", "friend")
        plan = (
            f"🗓️ Good morning {name}!\n"
            f"Wake up at {user.get('wake_up_time', '7:00 AM')}\n"
            f"Focus sessions: {', '.join(user.get('preferred_focus_blocks', []))}\n"
            "Don't forget your goals today:\n" +
            "\n".join(f"- {goal}" for goal in user.get("goals", []))
        )
        return jsonify({"response": plan})

    elif "my name is" in message:
        new_name = message.replace("my name is", "").strip().title()
        user["name"] = new_name
        save_user_data(user)
        return jsonify({"response": f"Got it! I'll remember your name is {new_name} 😊"})

    elif "i feel" in message:
        mood = message.replace("i feel", "").strip()
        user["mood"] = mood
        save_user_data(user)
        return jsonify({"response": f"Thanks for sharing. I'll be here if you need comfort or motivation 💜"})

    else:
        return jsonify({"response": f"🤖 You said: '{message}'. I'm still learning how to help you best!"})

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
