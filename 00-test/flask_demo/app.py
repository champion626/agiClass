from flask import Flask, render_template, request

app = Flask(__name__)

# 定义根路由，返回首页
@app.route('/')
def index():
    return render_template('index.html')

# 定义处理表单提交的路由，使用 POST 方法
@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单中的数据
    name = request.form.get('name')
    age = request.form.get('age')
    # 将数据传递给 result.html 模板进行渲染
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)