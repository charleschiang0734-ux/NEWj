from flask import Flask, render_template

app = Flask(__name__)

# 模拟一些卖书的数据（书名、价格、简介）
BOOKS = [
    {
        "id": 1,
        "title": "Python 编程从入门到精通",
        "price": "￥59.00",
        "desc": "适合零基础小白的 Python 实战宝典。",
    },
    {
        "id": 2,
        "title": "Web 开发快速上手",
        "price": "￥45.00",
        "desc": "教你如何从零构建自己的第一个网页应用。",
    },
    {
        "id": 3,
        "title": "算法的乐趣",
        "price": "￥68.00",
        "desc": "用轻松有趣的视角带你领略代码与逻辑的美感。",
    },
]


@app.route("/")
def index():
  # 渲染前端网页，并把书本数据传过去
  return render_template("index.html", books=BOOKS)


if __name__ == "__main__":
  app.run(debug=True)
