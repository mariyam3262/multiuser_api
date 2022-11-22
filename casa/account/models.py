from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
import datetime
from django.utils.translation import gettext_lazy as _
import os
from uuid import uuid4



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class CustomeUserManager(UserManager):
    

    def _create_user(self, username, password, **extra_fields):
        
        if not username:
            raise ValueError("The given username must be set")
        
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
   


class CustomeUser(AbstractUser):
    class Type(models.TextChoices):
        DEALER = "DEALER", "dealer"
        MARKETING_PERSON = "MARKETING_PERSON", "marketing_person"
        ADMIN = "ADMIN","admin"
        

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    

    objects = CustomeUserManager() 

    type = models.CharField(max_length = 30, choices=Type.choices, default= Type.MARKETING_PERSON)

    fname = models.CharField(_('First Name'),max_length= 30)
    lname = models.CharField(_('Last Name'),max_length = 30)
    email = models.EmailField(_('Email Address'), unique=True)
    dob = models.DateField(_('Date Of Birth'),default= datetime.datetime.now().date())
    mobile = models.CharField(_('Phone Number'),max_length= 10, unique= True)
    alt_mobile = models.CharField(_('Alternative Number'),max_length= 10)
    permanent_add = models.TextField(_('Permanenet Address'))
    current_add = models.TextField(_('Current Address'))
    state = models.CharField(_('State'),max_length= 30)
    district = models.CharField(_('District'),max_length= 30)
    city = models.CharField(_('City'),max_length= 30)
    pincode = models.CharField(_('Pincode number'),max_length= 6)
    blood_grp = models.CharField(_('Blood group'),max_length=3)

    Male = "Male"
    Female = "Female"

    sex_type_choices = [
        (Male,'Male'),
        (Female,'Female')
    ]

    sex = models.CharField(_('Sex'),choices=sex_type_choices,max_length= 6, blank=True)
    adhar_num = models.CharField(_('Adhar Number'),max_length= 50)
    





class MarketingPersonManager(CustomeUserManager,models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type = CustomeUser.Type.MARKETING_PERSON)

  
   


class MarketingPersonProfile(CustomeUser): 
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','password']
    objects = MarketingPersonManager() 
    class Meta:
        proxy = True 


    @property
    def more(self):
        return self.marketingpersonadditional


class MarketingPersonAdditional(models.Model):
    user= models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    company_email  = models.EmailField(_('Company Email Address'))   
    refrence = models.CharField(_('Reference'),max_length= 50)
    past_job = models.CharField(_('Past Job'),max_length= 80)
    joining_date = models.DateField(_('joining Date'), default=datetime.datetime.now().date())

    Married = "Married"
    Widowed  = "Widowed"
    Separated = "Separated"
    Divorced = "Divorced"
    Single = "Single"
    marital_status_choices = [
        (Married, 'Married'),
        (Widowed, 'Widowed'),
        (Separated, 'Separated'),
        (Divorced, 'Divorced'),
        (Single, 'Single'),
    ]    

    marital_status = models.CharField(_('Maritual Status'),choices=marital_status_choices,max_length= 20)
    Anniversary_date = models.DateField(_('Annivarsary Date'), null= True)
    spouse_name = models.CharField(_('Spouse Name'),max_length= 30)
    spouse_dob = models.DateField(_('Spouse birth date'), null=True)
    emergency_contact_person = models.CharField(_('Emergency Contact Person'),max_length= 10)
    emergency_contact_num = models.CharField(_('Emergency Contact Number'),max_length=10)
   

    def __str__(self):
        return f"{self.user}"



class DealerProfileAdditional(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, related_name="created_by")
    reference=models.CharField(_('Reference'), max_length=30)
    company_name=models.CharField(_('Company name'), max_length=30)
    company_dealing_address=models.TextField(_('Company Dealing Address'))
    company_key_person_name=models.CharField(_('Company Key Person Name'), max_length=30)
    company_key_person_number=models.CharField(_('Company Key Contact Name'), max_length=10)
    gst_number = models.CharField(_('GST Number'), max_length=15, unique=True)
    pan_number = models.CharField(_('PAN Number'), max_length=10, unique=True)
    current_handling_brand_or_companies = models.TextField(_('Current Handling Brand Or Companies'))
    Fullbody = 'Fullbody'
    PGVT = 'PGVT'
    Both = 'Both'
    product_type_choices = [
        (Fullbody, 'Fullbody'),
        (PGVT, 'PGVT'),
        (Both, 'Both')
    ]
    product_type = models.CharField(_('Product Type'), max_length=8, choices=product_type_choices, default=None, null=True)
    other_branch_dealings = models.CharField(_('Other Branch Dealings'), max_length=250)
    present_showroom_sq_ft = models.CharField(_('Present Showroom Sq. Ft.'), max_length=200)
    present_godown_sq_ft = models.CharField(_('Present Godown Sq. Ft.'), max_length=200)
    distance_from_showroom_to_godown = models.CharField(_('Distance From Showrrom To Godown'), max_length=200)
    showroom_owned_or_leased = models.CharField(_('Showroom Owned Or Leased'), max_length=200)
    off_day_in_week_in_market = models.CharField(_('Off Day In Week In Market'), max_length=15)
    space_provided_to_casa = models.CharField(_('Space Provided To CASA'), max_length=250)
    def path_and_rename(instance, filename):
        upload_to = 'dealer-registration'
        ext = filename.split('.')[-1]                
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(upload_to, filename)
    photo = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)      
    past_job= models.CharField(_('Past Job'), max_length=30)
    joining_date= models.DateField(_('Joining Date'), null=True)
    Married = "Married"
    Widowed  = "Widowed"
    Separated = "Separated"
    Divorced = "Divorced"
    Single = "Single"
    marital_status_choices = [
        (Married, 'Married'),
        (Widowed, 'Widowed'),
        (Separated, 'Separated'),
        (Divorced, 'Divorced'),
        (Single, 'Single'),
    ]    
    marital_status=models.CharField(_('Marital Status'), max_length=9, choices=marital_status_choices, default=None, null = True)
    anniversary_date= models.DateField(_('Anniversary Date'), null=True)
    spouse_name = models.CharField(_('Spouse Name'), max_length=30)
    spouse_date_of_birth = models.DateField(_('Spouse Date of Birth'), null = True)
    emergency_contact_person= models.CharField(_('Emergency Contact Person'), max_length=30)
    emergency_contact_person_phone_number= models.CharField(_('Emergency Contact Person\'s Phone Number'), max_length=10)

    def __str__(self):
        return f"{self.user}"




class DealerManager(CustomeUserManager,models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type = CustomeUser.Type.DEALER)

    


class DealerProfile(CustomeUser): 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','password']
    objects = DealerManager() 
    class Meta:
        proxy = True 


    @property
    def more(self):
        return self.dealeradditional