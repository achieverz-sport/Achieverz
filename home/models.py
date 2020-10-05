from __future__ import unicode_literals

from django.db import models
from .manager import UserManager
from django.db.models import JSONField
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
class Forgetpass(models.Model):
    email = models.CharField(max_length=20)
    key = models.CharField(max_length=20)

class Verification(models.Model):
    email = models.CharField(max_length=20)
    key = models.CharField(max_length=20)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True, db_index=True)
    mobile = models.CharField(_('Mobile Number'), max_length=15, unique=True)
    name = models.CharField(_('Full Name'), max_length=250, blank=False)
    is_organizer = models.BooleanField(_('Organizer'), default=False)
    is_active = models.BooleanField(_('Active'), default=False) # True after password is set.a
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_player = models.BooleanField(_('Player'), default=True)
    is_coach = models.BooleanField(_('Coach'), default=False)
    is_referee = models.BooleanField(_('Referee'), default=False)
    is_manager = models.BooleanField(_('Manager'), default=False)
    is_group_manager = models.BooleanField(_('Group Manager'), default=False)
    activation_key = models.CharField(_('Activation Key'), max_length=64, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    additional = JSONField(default=dict)

    avatar = models.ImageField(upload_to='static/avatars/', default="static/avatars/user.jpg")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

class Address(models.Model):
    line1 = models.CharField(_("Line 1"), max_length=200)
    line2 = models.CharField(_("Line 2 (Optional)"), max_length=200, blank=True, null=True)
    city = models.CharField(_("City"), max_length=200)
    state = models.CharField(_("State"), max_length=200)
    country = models.CharField(_("Country"), max_length=200)
    pincode = models.CharField(_("Pincode"), max_length=10)
    date_added = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    def __str__(self):
        return self.line1

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address, blank=True)
    date_of_birth = models.CharField(_("Date To Complete"), max_length=12)
    interests = JSONField(default=list)
    gender = models.CharField(_("Gender"), max_length=10)
    height = models.CharField(_("Height"), max_length=10,default = None)
    weight = models.CharField(_("Weight"), max_length=10,default = None)
    bio = models.TextField(_("Bio"))

    def __str__(self):
        return self.user

class Group(models.Model):
    primary_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(_('Name'), max_length=250, blank=False)
    email = models.EmailField(_('Email Address'), unique=True, db_index=True)
    mobile = models.CharField(_('Mobile Number'), max_length=15, unique=True)
    address = models.ManyToManyField(Address, blank=True)
    category = JSONField(default=list)
    members = models.ManyToManyField(User, related_name="Group_Members")
    is_organizer = models.BooleanField(_('Organizer'), default=False)
    is_brand = models.BooleanField(_('Brand'), default=False)
    is_team = models.BooleanField(_('Team'), default=False)
    is_academy = models.BooleanField(_('Academy'), default=False)
    is_venue = models.BooleanField(_('Venue'), default=False)
    is_institute = models.BooleanField(_('Institute'), default=False)
    is_federation = models.BooleanField(_('Federation'), default=False)
    is_government = models.BooleanField(_('Government'), default=False)
    date_added = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    additional = JSONField(default=dict)

    def __str__(self):
        return self.name

class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    team_member = models.ManyToManyField(User, blank=True, related_name="Team_Member")
    name = models.CharField(_('Team Name'), max_length=250, blank=False)
    #category = JSONField(default=list)
    date_added = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    organizer = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    name = models.CharField(_('Event Name'), max_length=250, blank=False)
    email = models.EmailField(_('Email Address'))
    mobile = models.CharField(_('Mobile Number'), max_length=15)
    details = models.TextField(_("Details"))
    category = JSONField(default=list)
    start_date = models.DecimalField(_("Event Start Date"), max_digits=12, decimal_places=2)
    end_date = models.DecimalField(_("Event End Date"), max_digits=12, decimal_places=2)
    fees = models.DecimalField(_("Fees"), max_digits=12, decimal_places=2)
    sport = models.CharField(_('Sport'), max_length=250)
    duration = models.CharField(_('Duration'), max_length=250)
    rules = models.TextField(_("Rules"))
    prizes = JSONField(default=dict)
    venue = models.TextField(_("Venue"))
    is_team = models.BooleanField(_("Team Registration"), default=False)
    is_individual = models.BooleanField(_("Individual Registration"), default=False)
    accept_registration = models.BooleanField(_("Accept Registration"), default=False)
    fixtures = JSONField(default=dict)

    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    User = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    def __str__(self):
        return self.team.name

class Payment(models.Model):
    orderid = models.CharField(_('Order ID'), max_length=200, blank=True)
    paymentid = models.CharField(_('Payment ID'), max_length=200, blank=True)
    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
    mode = models.CharField(_('Mode'), max_length=20, blank=True)
    amount = models.DecimalField(_('Amount Net'), max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #other_fields = JSONField(default=dict)

    def __str__(self):
        return self.paid_by