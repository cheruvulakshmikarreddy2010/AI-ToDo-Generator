from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json

        goal = data.get("goal", "")
        deadline = data.get("deadline", "")
        priority = data.get("priority", "Medium")

        tasks = [
            f"🎯 Define your goal: {goal}",
            "📝 Break the goal into smaller tasks.",
            f"⭐ Focus on {priority} priority tasks first.",
            "📅 Complete at least one task every day.",
            f"⏰ Finish all tasks before {deadline}.",
            "✅ Review your progress and celebrate your achievement."
        ]

        return jsonify({
            "tasks": "\n".join(tasks)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)