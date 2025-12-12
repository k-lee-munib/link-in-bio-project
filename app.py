from flask import Flask, render_template # <--- We imported 'render_template'

app = Flask(__name__)

@app.route("/")
def home():
    # 1. Create variables in Python
    my_name = "Abdullah Munib"  # You can change this text to anything!
    
    # 2. Let's send a list of skills too
    my_learnings = ["Python Automation", "HTML & CSS", "Flask Server", "Debugging"]

    # 3. Send them to the HTML file
    # 'name_in_html' is the tag we will use inside the HTML file
    return render_template("index.html", name_in_html=my_name, skills_list=my_learnings)

if __name__ == "__main__":
    app.run(debug=True)