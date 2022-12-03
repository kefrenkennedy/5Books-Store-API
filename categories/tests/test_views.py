from rest_framework.test import APITestCase
from rest_framework.views import status
from users.serializers import User


class TestCategoriesViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.default_URL = "/api/categories/"
        cls.correct_category_data = {
            "name": "Drama",
        }
        cls.incorrect_category_data = {}

    def setUp(self) -> None:
        user = {
            "username": "teste",
            "password": "1234",
            "first_name": "teste",
            "last_name": "test",
            "email": "teste@gmail.com",
            "cpf": "1234699",
        }

        User.objects.create_superuser(**user)

        login_superuser = self.client.post(
            "/api/login/",
            {"username": "teste", "password": "1234"},
        )

        self.token = login_superuser.data["token"]

    def test_can_create_an_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        res = self.client.post(
            f"{self.default_URL}",
            self.correct_category_data,
        )
        expected_status_code = status.HTTP_201_CREATED
        expected_keys = {"id", "name"}

        returned_keys = set(res.data)
        self.assertEqual(res.status_code, expected_status_code)
        self.assertSetEqual(expected_keys, returned_keys)

    def test_can_list_categories(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        self.client.post(f"{self.default_URL}", self.correct_category_data)
        self.client.post(f"{self.default_URL}", {"name": "Horror"})

        res = self.client.get(
            f"{self.default_URL}",
        )

        expected_len = 2
        res_len = len(res.data)
        self.assertEqual(res_len, expected_len)

    def test_can_list_categories(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        self.client.post(f"{self.default_URL}", self.correct_category_data)
        self.client.post(f"{self.default_URL}", {"name": "Horror"})

        res = self.client.get(
            f"{self.default_URL}",
        )
        res_len = len(res.data)

        expected_len = 2
        expected_status_code = status.HTTP_200_OK

        self.assertEqual(res_len, expected_len)
        self.assertEqual(res.status_code, expected_status_code)

    def test_cant_create_category_without_body(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        res = self.client.post(f"{self.default_URL}", self.incorrect_category_data)
        returned_keys = set(res.data)
        expected_status_code = status.HTTP_400_BAD_REQUEST
        expected_keys = {"name"}

        self.assertEqual(res.status_code, expected_status_code)
        self.assertSetEqual(expected_keys, returned_keys)

    def test_can_update_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        category = self.client.post(f"{self.default_URL}", {"name": "Horror"})

        patched_body = {"name": "Terror"}
        category_id = category.data["id"]
        res = self.client.patch(f"{self.default_URL}{category_id}/", patched_body)

        print(category_id)
        returned_keys = set(res.data)

        expected_keys = {"id", "name"}
        expected_status_code = status.HTTP_200_OK

        self.assertEqual(res.status_code, expected_status_code)
        self.assertSetEqual(expected_keys, returned_keys)
        self.assertEqual(res.data["name"], patched_body["name"])

    def test_cant_create_without_token(self):
        res = self.client.post(f"{self.default_URL}", {"name": "Horror"})

        msg = "Authentication credentials were not provided."
        expected_status_code = status.HTTP_401_UNAUTHORIZED

        self.assertEqual(res.data["detail"], msg)
        self.assertEqual(res.status_code, expected_status_code)
