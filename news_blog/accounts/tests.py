from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

from django.urls import reverse

class SignUpPageTests(TestCase):
    def test_url_exist_at_correct_location_signupView(self):
        response =self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response =self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
         response =self.client.get(reverse('signup'), {'username': "michael", 'email':"michaelolayiwola@gmail.com", 'password' : 'Mykel@8888'},)
         self.assertEqual(response.status_code, 302)
         self.assertEqual(get_user_model().objects.all().count(), 1) #"it will all the whole user  "
         self.assertEqual(get_user_model().objects.all()[0], 'michael') # is will test if thr name "michael" is truely zin first user
         self.assertEqual(get_user_model().objects.all()[0], 'email')