from flask import Flask, request, render_template_string
from .social_analyzer import fetch_user_posts, analyze_posts

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Mental Wellness Detection</title>
<h2>Mental Wellness Detection</h2>
<form method=post>
  <label>Select Platform:</label>
  <select name="platform">
    <option value="Reddit">Reddit</option>
    <option value="X">X</option>
  </select><br><br>
  <label>Enter Username:</label>
  <input type=text name=username required>
  <input type=submit value=Submit>
</form>
{% if report %}
<h3>Wellness Report</h3>
<div style="line-height:1.6;">
{{ report|safe }}
</div>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    report = ""
    if request.method == "POST":
        platform = request.form["platform"]
        username = request.form["username"]

        posts = fetch_user_posts(platform, username)
        depression_level, wellness_score, category = analyze_posts(posts)

        if category == "Invalid Username / No Posts Found":
            report = f"<p>⚠️ {category}. Please check the username and try again.</p>"
        else:
            report_lines = [
                f"<p><strong>Platform:</strong> {platform}</p>",
                f"<p><strong>Username:</strong> {username}</p>",
                f"<p><strong>Predicted Depression Level:</strong> {depression_level}</p>",
                f"<p><strong>Wellness Score:</strong> {wellness_score}/100</p>",
                f"<p><strong>Category:</strong> {category}</p>"
            ]
            if category == "High":
                report_lines.append("<p>✅ You are doing great! Keep positive habits.</p>")
            elif category == "Moderate":
                report_lines.append("<p>⚠️ Wellness moderate. Some improvement needed.</p>")
            else:
                report_lines.append("<p>🚨 Low wellness detected. Seek support if needed.</p>")

            report = "\n".join(report_lines)

    return render_template_string(TEMPLATE, report=report)

def run_app():
    """
    Run the Flask app.
    """
    app.run(debug=True)

if __name__ == "__main__":
    run_app()