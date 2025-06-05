from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# Activation key
KEY_ACTIVATION = os.getenv("KEY_ACTIVATION")

# HTML Interface in English
html = """
<!DOCTYPE html>
<html>
<head>
    <title>QuoraBot Login</title>
    <style>
        body { font-family: Arial; background-color: #f4f4f4; text-align: center; padding-top: 100px; }
        input { padding: 10px; font-size: 16px; margin-top: 10px; }
        button { padding: 10px 20px; font-size: 16px; margin-top: 20px; }
        .container { background-color: white; padding: 40px; border-radius: 10px; width: 300px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to QuoraBot</h2>
        <form method="post">
            <input type="password" name="key" placeholder="Enter your activation key" required><br>
            <button type="submit">Activate</button>
        </form>
        {% if error %}
            <p style="color: red; margin-top: 20px;">{{ error }}</p>
        {% endif %}
        {% if success %}
            <p style="color: green; margin-top: 20px;">{{ success }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    error = ""
    success = ""
    if request.method == "POST":
        key = request.form.get("key")
        if key == KEY_ACTIVATION:
            success = "✅ Activation successful. Welcome to the bot!"
        else:
            error = "❌ Invalid activation key. Please try again."
    return render_template_string(html, error=error, success=success)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
