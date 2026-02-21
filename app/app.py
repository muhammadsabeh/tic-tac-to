from flask import Flask, jsonify
from game import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route("/")
def home():
    return "<h1>Tic Tac Toe Running</h1>"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/reset")
def reset():
    game.reset()
    return jsonify({"board": game.board})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)