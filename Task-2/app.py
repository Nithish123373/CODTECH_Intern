from flask import Flask, render_template

app = Flask(__name__)

# Sample data for projects and blog posts
projects = [
    {
        "title": "Registration Form",
        "description": "A HTML, CSS, and JavaScript-based Registration form with exception handling mechanisms.",
        "live_demo": "https://nithishb700.github.io/RegistrationForm/",
        "github": "https://github.com/NithishB700/RegistrationForm"
    },
    {
        "title": "To-Do List",
        "description": "A basic To-Do List built with HTML, CSS, and JavaScript.",
        "live_demo": "https://nithishb700.github.io/Brainwave_Matrix_Intern/Task_1/",
        "github": "https://github.com/NithishB700/Brainwave_Matrix_Intern/tree/main/Task_1"
    },
    {
        "title": "E-Commerce Web Application",
        "description": "A Basic E-Commerce web app built using HTML, CSS, and JavaScript.",
        "live_demo": "https://nithishb700.github.io/Brainwave_Matrix_Intern/Task_2/",
        "github": "https://github.com/NithishB700/Brainwave_Matrix_Intern/tree/main/Task_2"
    },
]

blog_posts = [
    {
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "date": "2024-10-20"
    },
    {
        "title": "Learning Flask",
        "content": "In this post, I share my experiences while learning Flask.",
        "date": "2024-10-19"
    },
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
