from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from users.models import User


# class UserModelTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.test_user = get_user_model().objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             first_name="Nakyung",
#             last_name="KIM",
#             name="Nakyung Kim",
#             is_sitter=False,
#             avatar="https://example.com/avatar.jpg",
#         )

#     def test_user_creation(self):
#         # Test if the user is created correctly
#         user = get_user_model().objects.get(username="testuser")
#         self.assertEqual(user.email, "testuser@example.com")
#         self.assertEqual(user.first_name, "Nakyung")
#         self.assertEqual(user.last_name, "KIM")
#         self.assertEqual(user.name, "Nakyung Kim")
#         self.assertFalse(user.is_sitter)
#         self.assertEqual(user.avatar, "https://example.com/avatar.jpg")

#     def test_str_representation(self):
#         # Test the string representation of the user object
#         self.assertEqual(str(self.test_user), "Nakyung Kim")

#     def test_user_authentication(self):
#         # Test user authentication
#         user = get_user_model().objects.get(username="testuser")
#         self.assertTrue(user.check_password("testpassword"))
#         self.assertFalse(user.check_password("wrongpassword"))


# class TokenAuthenticationTestCase(APITestCase):
#     def setUp(self):
#         self.user_data = {
#             "username": "testuser",
#             "password": "testpassword",
#             "first_name": "Test",
#             "last_name": "User",
#             "name": "Test User",
#             "is_sitter": True,
#             "avatar": "https://example.com/avatar.jpg",
#         }
#         self.user = User.objects.create_user(**self.user_data)
#         self.login_url = reverse("token-login")

#     def test_token_login_successful(self):
#         response = self.client.post(self.login_url, self.user_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("token", response.data)

#     def test_token_login_wrong_password(self):
#         wrong_user_data = self.user_data.copy()
#         wrong_user_data["password"] = "wrongpassword"
#         response = self.client.post(self.login_url, wrong_user_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertNotIn("token", response.data)

#     def test_token_login_missing_username_password(self):
#         response = self.client.post(
#             self.login_url, {"username": "", "password": ""}, format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertNotIn("token", response.data)
