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
        t = Token.objects.create(user=u)
        t.save()
        UploadFile.objects.create(owner=u, file=open(r'.\media\covid_worldwide.csv').name).save()
        UploadFile.objects.create(owner=u, file=open(r'.\media\Survey_AI.csv').name).save()

    def test_unauthorized(self):
        url = reverse('upload')
        client = APIClient()
        f = open(r'..\test_datasets\prc_hpi_a__custom_3617733_page_linear.csv')
        data = {'datafile': f}
        response = client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(UploadFile.objects.count(), 2)

    def test_authorized(self):
        url = reverse('upload')
        f = open(r'..\test_datasets\prc_hpi_a__custom_3617733_page_linear.csv')
        data = {'datafile': f}
        token = Token.objects.get(user__username='test_user')
        #client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UploadFile.objects.count(), 3)
        self.assertEqual(response.data.get('owner'), 1)


    def test_get_files_list(self):
        url = reverse('upload')
        client = APIClient()
        response = self.client.get(url, format='json')
        assert False
