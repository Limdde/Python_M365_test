from flask import Flask, render_template

app = Flask(__name__)

# 메뉴 데이터
menu = {
    'Home': ['menu1', 'menu2', 'menu3', 'menu4', 'menu5'],
    'Product': ['menu1', 'menu2', 'menu3', 'menu4', 'menu5'],
    'Service': ['menu1', 'menu2', 'menu3', 'menu4', 'menu5'],
    'Support': ['menu1', 'menu2', 'menu3', 'menu4', 'menu5']
}

# 라우팅
@app.route('/')
def index():
    # 차트 데이터
    chart_data = [10, 20, 30, 40, 50]

    return render_template('index.html', menu=menu, chart_data=chart_data)

# 실행
if __name__ == '__main__':
    app.run()
