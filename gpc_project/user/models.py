from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField('이메일', unique=True)
    name = models.CharField('닉네임', max_length=30, blank=True, unique=True)
    is_staff= models.BooleanField('스태프 권한', default=False)
    is_active= models.BooleanField('사용중', default=False)
    date_joined= models.DateTimeField('가입일', default=timezone.now)
    date_edit= models.DateTimeField('정보수정일', default=timezone.now)

    objects= UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)