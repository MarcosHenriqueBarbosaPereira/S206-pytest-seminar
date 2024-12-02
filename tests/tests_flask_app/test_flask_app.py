from s206_seminar.src.flask_app.app import app, tasks


class TestFlaskApp:

    def setup_method(self, _):
        app.config["TESTING"] = True
        with app.test_client() as client:
            self.client = client

    @staticmethod
    def teardown_method(_):
        tasks.clear()

    def test_add_task(self):
        response = self.client.post("/tasks", json={"title": "Task 1"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["id"] == 1
        assert data["title"] == "Task 1"
        assert data["status"] == "pending"

    def test_add_task_without_title(self):
        response = self.client.post("/tasks", json={})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "The 'title' field is required and cannot be empty."

    def test_add_task_with_empty_title(self):
        response = self.client.post("/tasks", json={"title": ""})
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "The 'title' field is required and cannot be empty."

    def test_list_tasks(self):
        self.client.post("/tasks", json={"title": "Task 1"})
        self.client.post("/tasks", json={"title": "Task 2"})

        response = self.client.get("/tasks")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        assert data[0]["title"] == "Task 1"
        assert data[1]["title"] == "Task 2"

    def test_update_task(self):
        self.client.post("/tasks", json={"title": "Task 1"})
        response = self.client.put("/tasks/1", json={"status": "completed"})
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "completed"

    def test_update_task_not_found(self):
        response = self.client.put("/tasks/999", json={"status": "completed"})
        assert response.status_code == 404
        data = response.get_json()
        assert data["error"] == "Task not found"

    def test_delete_task(self):
        self.client.post("/tasks", json={"title": "Task 1"})
        response = self.client.delete("/tasks/1")
        assert response.status_code == 204

        response = self.client.get("/tasks")
        data = response.get_json()
        assert len(data) == 0

    def test_delete_task_not_found(self):
        response = self.client.delete("/tasks/999")
        assert response.status_code == 204

        response = self.client.get("/tasks")
        data = response.get_json()
        assert len(data) == 0
