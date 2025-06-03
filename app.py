from flask import Flask, render_template_string, request

app = Flask(__name__)

KEY_ACTIVATION = "quorabotai-keyact"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Quora Bot - Connexion</title>
</head>
<body>
    <h2>Connexion au bot Quora</h2>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        Clé d'activation: <input type="text" name="key" required><br><br>
        <button type="submit">Se connecter</button>
    </form>
</body>
</html>
"""

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Quora Bot - Utilisation</title>
</head>
<body>
    <h2>Bienvenue au bot Quora</h2>
    <form method="POST">
        Email Quora: <input type="email" name="email" required><br><br>
        Mot de passe Quora: <input type="password" name="password" required><br><br>
        Mot-clé à chercher: <input type="text" name="keyword" required><br><br>
        Réponse à poster: <br>
        <textarea name="answer" rows="5" cols="40" required></textarea><br><br>
        <button type="submit">Lancer le bot (simulation)</button>
    </form>
    {% if message %}
        <p style="color:green;">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        key = request.form.get("key")
        if key == KEY_ACTIVATION:
            return render_template_string(HTML_FORM)
        else:
            return render_template_string(HTML_PAGE, error="Clé d'activation invalide.")
    return render_template_string(HTML_PAGE)

@app.route("/run", methods=["POST"])
def run_bot():
    email = request.form.get("email")
    password = request.form.get("password")
    keyword = request.form.get("keyword")
    answer = request.form.get("answer")
    # Ici, tu pourrais intégrer l'automatisation réelle avec Selenium plus tard
    # Pour le moment on simule juste un succès
    message = f"Bot lancé avec succès pour l'utilisateur {email}. Réponse postée sur la question contenant '{keyword}'."
    return render_template_string(HTML_FORM, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
