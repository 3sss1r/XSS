import html
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

current_message = ""


@app.route('/', methods=["GET", "POST"])
def save_message():
    global current_message
    if request.method == "GET":
        return render_template("send_message.html")
    else:
        current_message = request.form.get("message")
        return redirect('xss')


@app.route('/xss')
def view_message():
    escaped_message = current_message.translate({ord(c): ('\\'+c) for c in "\"\'<>&"})
    protect_message = html.escape(current_message)
    context = dict(message=html.escape(escaped_message), protect_message=protect_message)
    return render_template("view_message.html", **context)


if __name__ == '__main__':
    app.run()
