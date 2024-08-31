#pip install flask

from flask import Flask,render_template,request

app = Flask(__name__)

#浏览器显示页面
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    uname=request.args.get('uname')
    #判断用户名是否正确
    return f"主页!!! 欢迎登录{uname}"

app.run(debug=True)