from unittest import TestCase, main as main_test
from fastapi.testclient import TestClient
from main import app


class TestBackend(TestCase):
    
    def setUp(self) -> None:
        self.app = TestClient(app)
    

    def test_get_all_users_posts(self):
        response = self.app.get("/get_all_users_posts")
        self.assertEqual(response.status_code, 200)
    

    def test_create_user_post(self):
        data = {
            "id": 1323,
            "author": "test-author",
            "content": "test-content",
            "theme": "test-theme"
        }
        response = self.app.post("/create_user_post", json=data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()







if __name__ == "__main__":
    main_test()