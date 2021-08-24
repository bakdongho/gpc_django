from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, FormView
from django.contrib import messages
from user.forms import CustomUserCreationForm, VerificationEmailForm
from user.mixins import VerifyEmailMixin
# Create your views here.

class ResendVerifyEmailView(VerifyEmailMixin, FormView):
    model = get_user_model()
    form_class = VerificationEmailForm
    success_url = '/user/login'
    template_name = 'user/resend_verify_form.html'
    finish_message='작성하신 이메일주소로 인증메일을 발송했으니 확인 후 인증해주세요.'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            messages.error(self.request, '알 수 없는 사용자 입니다.')
        else:
            self.send_verification_email(user,self.finish_message)
        return super().form_valid(form)


class UserRegistrationView(VerifyEmailMixin,CreateView):
    model=get_user_model()
    template_name = 'user/registration_form.html'
    success_url='/user/login'
    form_class=CustomUserCreationForm
    verify_url = '/user/verify'
    finish_message='회원가입을 축하드립니다. 가입하신 이메일주소로 인증메일을 발송했으니 확인 후 인증해주세요.'

    def form_valid(self, form):
        response = super().form_valid(form)
        if form.instance:
            self.send_verification_email(form.instance, self.finish_message)
        return response

class UserLoginView(LoginView):
    template_name = 'user/login_form.html'
    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, 'login fail',extra_tags='danger')
        return super().form_invalid(form)

class UserVerificationView(TemplateView):

    model = get_user_model()
    redirect_url = '/user/login'
    token_generator = default_token_generator

    def get(self, request, *args, **kwargs):
        if self.is_valid_token(**kwargs):
            messages.info(request, '인증이 완료되었습니다. 해당 아이디로 로그인하여 서비스를 이용하실 수 있습니다')
        else:
            messages.error(request, '인증이 실패되었습니다. 인증이메일 재발송 버튼을 눌러서 다시 시도 부탁드립니다. ')
        return HttpResponseRedirect(self.redirect_url)   # 인증 성공여부와 상관없이 무조건 로그인 페이지로 이동

    def is_valid_token(self, **kwargs):
        pk = kwargs.get('user_pk')
        token = kwargs.get('email_token')
        user = self.model.objects.get(pk=pk)
        is_valid = self.token_generator.check_token(user, token)
        if is_valid:
            user.is_active = True
            user.save()     # 데이터가 변경되면 반드시 save() 메소드 호출
        return is_valid