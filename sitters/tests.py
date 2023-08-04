from rest_framework.test import APITestCase
from . import models
from users.models import User

# Create your tests here.


# class TestServices(APITestCase):
#     NAME = "Service test"
#     DESC = "Service description test"

#     URL = "/sitters/services/"

#     def setUp(self):
#         models.Service.objects.create(
#             service_name=self.NAME,
#             description=self.DESC,
#         )

#     def test_all_services(self):
#         response = self.client.get("/sitters/services/")
#         data = response.json()

#         self.assertEqual(
#             response.status_code,
#             200,
#             "Status code isn't 200",
#         )

#         self.assertIsInstance(
#             data,
#             list,
#         )
#         self.assertEqual(
#             len(data),
#             1,
#         )
#         self.assertEqual(
#             data[0]["service_name"],
#             self.NAME,
#         )
#         self.assertEqual(
#             data[0]["description"],
#             self.DESC,
#         )

#     def test_create_service(self):
#         new_service_name = "New Service"
#         new_description = "New Amenity desc."

#         response = self.client.post(
#             self.URL,
#             data={
#                 "service_name": new_service_name,
#                 "description": new_description,
#             },
#         )

#         data = response.json()

#         self.assertEqual(
#             response.status_code,
#             200,
#             "Not 200 status code",
#         )
#         self.assertEqual(
#             data["description"],
#             new_description,
#         )

#         response = self.client.post(self.URL)
#         data = response.json()

#         self.assertEqual(response.status_code, 400)
#         self.assertIn("service_name", data)


# class TestDetailService(APITestCase):
#     NAME = "Service test"
#     DESC = "Service description test"

#     def setUp(self):
#         models.Service.objects.create(
#             service_name=self.NAME,
#             description=self.DESC,
#         )

#     def test_services_not_found(self):
#         response = self.client.get("/sitters/services/1")

#         self.assertEqual(response.status_code, 200)

#     def test_get_service(self):
#         response = self.client.get("/sitters/services/5")

#         self.assertEqual(response.status_code, 404)

#         data = response.json()

#         # self.assertEqual(
#         #     data["service_name"],
#         #     self.NAME,
#         # )
#         # self.assertEqual(
#         #     data["description"],
#         #     self.DESC,
#         # )

#     def test_delete_service(self):
#         response = self.client.delete("/sitters/services/1")

#         self.assertEqual(response.status_code, 204)


# class TestSitters(APITestCase):
#     def test_create_room(self):
#         response = self.client.post("/sitters/")

#         self.assertEqual(
#             response.status_code,
#             403,
#         )

#         user = User.objects.create(
#             username="test",
#         )
#         user.set_password("123")
#         user.save()
#         self.user = user

#         self.assertEqual(response.status_code, 403)

#         self.client.force_login(
#             self.user,
#         )

#         response = self.client.post("/sitters/")
#         print(response)
