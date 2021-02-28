"""
Provide model user and user-account related models.
"""
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from spark_18.libs.accounts.validators import validate_password


class UserManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        # email = self.normalize_email(email)
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Store User account details.
    """
    # Use either of the username fields below:
    username = models.CharField(
        _('username'),
        max_length=255,
        unique=True,
        help_text=_('Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    password = models.CharField(
        _('password'),
        max_length=128,
        validators=[validate_password],
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
        help_text=_('Required. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid email. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _('A user with that email already exists.'),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    name = models.CharField(_('name'), max_length=60, null=True, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    # Modify USERNAME_FIELD and REQUIRED_FIELDS as required.
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (

        )
        # ordering = ['username'] # Set it as required.

    # Use Either one of __str__ methods.
    def __str__(self):
        return '{email}'.format(email=self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


# post_save.connect(register_user_activity, sender=User)