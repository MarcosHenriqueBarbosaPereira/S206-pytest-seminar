from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados em memória
tasks = []

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or 'title' not in data or not data['title'].strip():
        return jsonify({"error": "The 'title' field is required and cannot be empty."}), 400

    task = {"id": len(tasks) + 1, "title": data["title"], "status": "pending"}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = data["status"]
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)