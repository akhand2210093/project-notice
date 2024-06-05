from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_akgec_email(value):
        if not value.endswith('@akgec.ac.in'):
            raise ValidationError(
                _('Only college email id is allowed.'),
                params={'value': value},
            )
        
def validate_Student_digits(value):
    min_digits = 7  
    max_digits = 8  
    value_str = str(value)
    if len(value_str) < min_digits or len(value_str) > max_digits:
        raise ValidationError(
            f"Student number must have 7 or 8 digits."
        )
    
class User(AbstractUser):
    CSE = 'CSE'
    CS = 'CS'
    CSE_AIML = 'CSE(AIML)'
    CSE_DS = 'CSE(DS)'
    CSE_Hindi = 'CSE(Hindi)'
    AIML='AIML'
    IT ='IT'
    CSIT ='CSIT'
    ECE ='ECE'
    EN='EN'
    ME = 'ME'
    CIVIL = 'CIVIL'
    ROLE_CHOICES = (
        ('administrator', 'administrator'),
        ('staff', 'staff'),
        ('student', 'student'),
    )
    Branch = [
        (CSE, 'CSE'),
        (CS, 'CS'),
        (CSE_AIML, 'CSE-AIML'),
        (CSE_DS, 'CSE-DS'),
        (CSE_Hindi,'CS(Hindi)'),
        (AIML,'AIML'),
        (IT,'IT'),
        (CSIT,'CS&IT'),
        (ECE,'ECE'),
        (EN,'EN'),
        (ME, 'ME'),
        (CIVIL,'CE'),
    ]
    created = models.DateTimeField(auto_now_add=True)
    email=models.EmailField(max_length=60,validators=[validate_akgec_email], null=False, unique=True )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    student_no=models.IntegerField(validators=[validate_Student_digits],unique=True,blank=True, null=True)#
    branch = models.CharField(max_length=10, blank=True,null=True , choices=Branch)
    year = models.CharField(max_length=10, blank=True,null = True)
    otp = models.CharField(max_length=4, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)