from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {"id": 1, "Name": "Kartikey", "Contact": "9711249305", "done": False},
    {"id": 2, "Name": "Abhayjeet", "Contact": "9953160550", "done": False},
]


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/data", methods=["GET", "POST"])
def add_task():
    if request.method == "GET":
        return jsonify({"data": contacts})

    if request.method == "POST":
        if not request.json:
            return jsonify(
                {"status": "error", "message": "Please provide the data!"}, 400
            )

        contact = {
            "id": contacts[-1]["id"] + 1,
            "Name": request.json["Name"],
            "Contact": request.json.get("Contact", ""),
            "done": False,
        }
        contacts.append(contact)
        return jsonify({"status": "success", "message": "Contact added succesfully!"})


if __name__ == "__main__":
    app.run(debug=True)
