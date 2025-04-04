from flask import Flask, render_template, request

app = Flask(__name__)

# 仮の行事リストを保存
events = []

@app.route("/")
def index():
    return render_template("index.html", events=events)

@app.route("/add", methods=["POST"])
def add_event():
    name = request.form.get("name")
    date = request.form.get("date")
    events.append({"name": name, "date": date})
    return index()

if __name__ == "__main__":
    # 他のPCからアクセスできるようにホストを0.0.0.0に設定
    app.run(host="0.0.0.0", port=5000, debug=True)
