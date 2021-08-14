from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from config import settings


class VerifyEmailMixin:
    email_template_name = 'user/registration_verification.html'
    token_generator = default_token_generator

    def send_verification_email(self, user, finish_meassage):
        token = self.token_generator.make_token(user)
        url = self.build_verification_link(user, token)
        subject = '회원가입을 축하드립니다.'
        message = '다음 주소로 이동하셔서 인증하세요. {}'.format(url)
        html_message = render(self.request, self.email_template_name, {'url': url}).content.decode('utf-8')
        user.email_user(subject, message, from_email=settings.EMAIL_HOST_USER,html_message=html_message)
        messages.info(self.request, finish_meassage)

    def build_verification_link(self, user, token):
        return '{}/user/{}/verify/{}/'.format(self.request.META.get('HTTP_ORIGIN'), user.pk, token)