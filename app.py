import os
from flask import Flask, request, jsonify

app = Flask(__name__)

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

@app.route("/")
def home():
    return {"message": "Todo API running on Railway 🚀"}

@app.route("/tasks", methods=["GET"])
def view_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.json

    if not data or "task" not in data or not data["task"].strip():
        return {"error": "Task cannot be empty"}, 400

    tasks.append(data["task"].strip())
    save_tasks(tasks)

    return {"message": "Task added successfully"}

@app.route("/tasks/<int:index>", methods=["DELETE"])
def remove_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        return {"error": "Invalid task index"}, 400

    removed = tasks.pop(index)
    save_tasks(tasks)

    return {"message": f"Task '{removed}' removed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
