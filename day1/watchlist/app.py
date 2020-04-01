from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')

def index():
    name = "Queen"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"七龙珠","year":"2019"},
        {"title":"海贼王","year":"2018"},
        {"title":"火影忍者","year":"2017"},
        {"title":"速度与激情","year":"2019"},
    ]
    return render_template('index.html',name=name,movies=movies)
# #动态URL
# @app.route('/index/<name>')
# def home(name):
#     #print(url_for("home",name="queen"))
#     return "<h1>Hello,%s</h1>"%name


if __name__ == '__main__':
    app.run()