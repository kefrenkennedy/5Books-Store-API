from rest_framework.test import APITestCase
from rest_framework.views import status
from users.serializers import User
from rest_framework.authtoken.models import Token




class TestAuthorView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.default_URL = "/api/authors/"
        cls.correct_author_data = {
            "name": "John Green",
        }

    
        cls.user = {
            "username": "teste",
            "password": "1234",
            "first_name": "teste",
            "last_name": "test",
            "email": "teste@gmail.com",
            "cpf": "1234699",
        }

        cls.admin = User.objects.create_superuser(**cls.user)
        cls.token_admin = Token.objects.create(user=cls.admin)

    def test_create_author_with_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin.key)

        response = self.client.post(
            self.default_URL, data=self.correct_author_data)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertIn('id', response.data)
        self.assertIn("name",  response.data)

    def test_create_product_without_token(self):
        response = self.client.post(
            self.default_URL, data=self.correct_author_data)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(
            response.data["detail"], "Authentication credentials were not provided."
        )

    def test_create_with_wrong_keys(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin.key)

        response = self.client.post(
            self.default_URL, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(
            response.data["name"][0], "This field is required."
        )

    def test_can_filter_author(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin.key)
        author = self.client.post(f'{self.default_URL}', {"name": "Jorge Amado"})

        author_id = author.data["id"]
        response = self.client.get(f"{self.default_URL}{author_id}/")


        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(len(response.data.keys()), 2)


    def test_can_update_author(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_admin.key)
        author = self.client.post(f'{self.default_URL}', {"name": "Jorge Amado"})

        patched_body = {"name": "Author atualizado"}
        author_id = author.data["id"]
        response = self.client.patch(f"{self.default_URL}{author_id}/", patched_body)


        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(len(response.data.keys()), 2)

