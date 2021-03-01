from data import sample_posts
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", all_posts=sample_posts)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/post/<int:post_index>")
def show_post(post_index):
    requested_post = None
    for blog_post in sample_posts:
        if blog_post["id"] == post_index:
            requested_post = blog_post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
