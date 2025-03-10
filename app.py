from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# New blog route with dynamic posts list
@app.route("/blog")
def blog():
    posts = [
        {
            "title": "Sample Blog Post",
            "date": "2023-10-20",
            "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "link": "#"
        }
        # ...add additional posts as needed...
    ]
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
