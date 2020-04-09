from watchlistapp import app,db
from flask import render_template,flash,redirect,request,url_for
from flask_login import login_user,logout_user,login_required,current_user
from watchlistapp.models import Movie,User

# views
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        # request 在请求触发的时候才会包含数据
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash('不能为空或超过最大长度！')
            return redirect(url_for('index'))
        # 保存表单数据
        from watchlistapp.models import Movie
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash('创建成功！')
        return redirect(url_for('index'))
    from watchlistapp.models import Movie
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)
# #动态URL
# @app.route('/index/<name>')
# def home(name):
#     #print(url_for("home",name="queen"))
#     return "<h1>Hello,%s</h1>"%name
# 更新电影信息
@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        #验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash('不能为空或超过最大长度！')
            return redirect(url_for('index'))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('更新完成')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)


# 删除电影信息
@app.route('/movie/delete/<int:movie_id>',methods=['POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除成功！')
    return redirect(url_for('index'))


# 登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # request 在请求触发的时候才会包含数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 验证数据
        if not username or not password:
            flash('输入错误！')
            return redirect(url_for('login'))
        # 和数据库中的信息进行比对验证
        user = User.query.first()
        if user.username == username and user.validate_password(password):
            login_user(user)
            flash('登录成功')
            return redirect(url_for('index'))
        flash('用户名或密码错误')
        return redirect(url_for('login'))
    return render_template('login.html')

# 退出
@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash('拜拜')
    return redirect(url_for('index'))

#settings 设置
@app.route('/settings',methods=['GET','POST'])
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if not name or len(name)>20:
            flash('输入错误')
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash('名称已经更新')
        return redirect(url_for('index'))
    return render_template('settings.html')
