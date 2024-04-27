from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, connected successfully to a server!"

@app.route("/user/<username>")
def user(username):
    return f"Welcome, {username}!"

@app.route("/submit", methods=["POST", "PUT", "DELETE"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Submitted: Name - {name}, Email - {email}"
    elif request.method == "PUT":
        # Handle PUT request
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Updated: Name - {name}, Email - {email}"
    elif request.method == "DELETE":
        # Handle DELETE request
        return "Data deleted successfully!"
    else:
        return "Only POST, PUT, and DELETE requests are allowed for this route!"

@app.route("/json", methods=["POST", "PUT", "DELETE"])
def json_data():
    if request.method == "POST":
        data = request.json
        return jsonify(data)  
    elif request.method == "PUT":
        # Handle PUT request
        data = request.json
        # Process the data and return appropriate response
        return jsonify({"message": "Data updated successfully!"})
    elif request.method == "DELETE":
        # Handle DELETE request
        # Process the delete operation and return appropriate response
        return jsonify({"message": "Data deleted successfully!"})
    else:
        return "Only POST, PUT, and DELETE requests are allowed for this route!"

if __name__ == "__main__":
    app.run(debug=True)