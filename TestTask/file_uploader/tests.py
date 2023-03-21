from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from file_uploader.models import UploadFile, User


class UploaderTests(APITestCase):

    @classmethod
    def setUp(cls):
        u = User.objects.create_user('test_user', password='test', email='test@mail.ru')
        u.save()
        print(u)

    def test_unauthorized(self):
        url = reverse('upload')
        client = APIClient()
        f = open(r'C:\Users\user\Desktop\prc_hpi_a__custom_3617733_page_linear.csv')
        data = {'datafile': f}
        response = client.post(url, data, format='multipart')
        #print(response)
        #print(UploadFile.objects.all())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized(self):
        url = reverse('upload')
        f = open(r'C:\Users\user\Desktop\prc_hpi_a__custom_3617733_page_linear.csv')
        data = {'datafile': f}
        print(User.objects.all())
        print(Token.objects.all())
        u = User.objects.create_user('test_user', password='test', email='test@mail.ru')
        u.save()
        token = Token.objects.get_or_create(user=u)
        print("AAA"+token)
        client = APIClient()
        #client.login(username='test_user', password='test')
        #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = client.post(url, data, format='multipart')
        print(response)
        print(UploadFile.objects.all())
        self.assertEqual(False, True)