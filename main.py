from flask import Flask

letters = { 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "Y", 10: "R"}

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Главная страничка"

@app.route('/get_letter/<int:index>')
def page_letter(index):
    letter = letters.get(index)
    return letter


@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_masssages():
    return "Сообщения пользователя"

@app.route("/users/<int:uid>")
def profile(uid):
    print(uid)
    print(type(uid))

    return ""

if __name__ == '__main__':
    app.run(debug=True)
