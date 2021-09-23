from flask import Flask, render_template, url_for

app = Flask(__name__)

myprojects = [ 
    {
        'name': "Foxy: Nightmares",
        'description': "A game I've made with a friend long ago",
        'imgsrc': "Nightmareslogo.png",
        'href': "https://play.google.com/store/apps/details?id=com.HotKoreetz.DDA&hl=en&gl=US"
    },
    {
        'name': "Shodo Master",
        'description': "My personal half-developed abandoned project",
        'imgsrc': "shodologo.png",
        'href': "https://play.google.com/store/apps/details?id=com.Jidake.ShodoMaster&hl=en&gl=US"
    }
]

@app.route("/")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/projects")
def projects():
    return render_template('projects.html', title = 'Projects', projects = myprojects)

@app.route("/about")
def about():
    return "<h1>About me</h1>"