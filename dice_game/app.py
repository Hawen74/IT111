from flask import Flask, render_template, jsonify
from games.dice_game import DiceGame
import random

app = Flask(__name__)
game = DiceGame()

@app.route("/")
def index():
    return render_template("dice.html")

@app.route("/roll")
def roll():
    global game
    
    if game.finished:
        return jsonify({
            "finished": True,
            "message": "Game is over. Restart to play agian."
        })
        
    roll = random.randint(1, 6) + random.randint(1, 6)
    game.play_turn(roll)
    
    return jsonify({
        "turn": game.turn,
        "roll": roll,
        "point": game.point,
        "result": game.result,
        "finished": game.finished
    })
    
@app.route("/restart")
def restart():
    global game
    game = DiceGame()
    return jsonify({"message": "Game restarted"})

if __name__ == "__main__":
    app.run(debug=True)