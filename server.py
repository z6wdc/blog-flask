from post import Post
from data import sample_posts
from flask import Flask, render_template

post_objects = []
for post in sample_posts:
    post_obj = Post(post_id=post["id"],
                    title=post["title"],
                    subtitle=post["subtitle"],
                    body=post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
