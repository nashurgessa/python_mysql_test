from flask import Flask, jsonify, request
from flask_cors import CORS

from db_config import DBConfig
from person_repository_impl import PersonRepositoryImpl
from person_service import PersonService

app = Flask(__name__)
CORS(app)

todos = []

# Create instances of the repository and service
db_config = DBConfig.get_instance().db_config
person_repo = PersonRepositoryImpl(db_config)
person_service = PersonService(person_repo)

@app.get("/todos")
def get_all_todos():
    print("Yes")
    return jsonify(todos), 200

@app.post("/todos")
def add_todo():
    todo = request.json
    print("Todo: ", todo)
    todos.append(todo)
    # Save this to local Database
    
    return jsonify (todo), 201

@app.route("/person", methods=["POST"])
def add_person():
    person_data  = request.json
    person_id = person_service.create_person(person_data)
    return jsonify({"id" : person_id}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)