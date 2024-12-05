from flask import Flask, request, jsonify

app = Flask(__name__)

jokes = [
    {"id": 1, "setup": "Knock, knock.", "punchline": "Who’s there? Cat’s got your tongue?"},
    {"id": 2, "setup": "Knock, knock.", "punchline": "Who’s there? Kitten. Kitten who? Quit kitten around and let me in!"},
    {"id": 3, "setup": "Knock, knock.", "punchline": "Who’s there? Catnip. Catnip who? Catnip and relax, it’s just a joke!"},
    {"id": 4, "setup": "Knock, knock.", "punchline": "Who’s there? Meow. Meow who? Meow you doing today?"},
    {"id": 5, "setup": "Knock, knock.", "punchline": "Who’s there? Purr. Purr who? Purr-haps you should open the door!"},
    {"id": 6, "setup": "Knock, knock.", "punchline": "Who’s there? Tabby. Tabby who? Tabby or not to be, that is the question."},
    {"id": 7, "setup": "Knock, knock.", "punchline": "Who’s there? Whiskers. Whiskers who? Whiskers me later, I’m busy!"},
    {"id": 8, "setup": "Knock, knock.", "punchline": "Who’s there? Fur. Fur who? Fur real, open the door already!"},
    {"id": 9, "setup": "Knock, knock.", "punchline": "Who’s there? Paw. Paw who? Paw-don me, but I’m here!"},
    {"id": 10, "setup": "Knock, knock.", "punchline": "Who’s there? Litter. Litter who? Litter-ally, open the door!"},
    {"id": 11, "setup": "Knock, knock.", "punchline": "Who’s there? Scratch. Scratch who? Scratch meow-t off your to-do list!"},
    {"id": 12, "setup": "Knock, knock.", "punchline": "Who’s there? Felix. Felix who? Felix the door is locked, let me in!"},
    {"id": 13, "setup": "Knock, knock.", "punchline": "Who’s there? Mittens. Mittens who? Mittens the cat who loves to play!"},
    {"id": 14, "setup": "Knock, knock.", "punchline": "Who’s there? Cattitude. Cattitude who? Cattitude is everything!"},
    {"id": 15, "setup": "Knock, knock.", "punchline": "Who’s there? Roar. Roar who? Roar you serious, it’s me!"},
    {"id": 16, "setup": "Knock, knock.", "punchline": "Who’s there? Fluffy. Fluffy who? Fluffy the cat who wants a snack!"},
    {"id": 17, "setup": "Knock, knock.", "punchline": "Who’s there? Claw. Claw who? Claw-ver me, I’m hilarious!"},
    {"id": 18, "setup": "Knock, knock.", "punchline": "Who’s there? Paws. Paws who? Paws for a moment and let me in!"},
    {"id": 19, "setup": "Knock, knock.", "punchline": "Who’s there? Alley. Alley who? Alley cat who wants to come inside!"},
    {"id": 20, "setup": "Knock, knock.", "punchline": "Who’s there? Chester. Chester who? Chester cat who loves these jokes!"},
]

@app.route('/')
def home():
    return "Welcome to the Cat Knock-Knock Jokes API!"

@app.route('/jokes', methods=['GET'])
def get_jokes():
    return jsonify({"jokes": jokes})

@app.route('/jokes/<int:joke_id>', methods=['GET'])
def get_joke(joke_id):
    joke = None  
    for j in jokes:
        if j["id"] == joke_id:  
            joke = j           
            break             

    if joke:
        return jsonify(joke)
    else:
        return jsonify({"error": "Joke not found"}), 404

@app.route('/jokes', methods=['POST'])
def add_joke():
    data = request.get_json()
    if "setup" not in data or "punchline" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_joke = {
        "id": len(jokes) + 1,  
        "setup": data["setup"],
        "punchline": data["punchline"]
    }
    jokes.append(new_joke)
    return jsonify(new_joke), 201

if __name__ == '__main__':
    app.run(debug=True)
