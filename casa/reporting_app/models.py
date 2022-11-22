from django.db import models
import datetime
from account.models import MarketingPersonProfile
from account.models import CustomeUser
from django.utils.translation import gettext_lazy as _


class LeaveReport(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    type = models.CharField(_('Type'),max_length=20)
    total_leave = models.IntegerField(_('Total leave'),default = 0)
    past_total_leave = models.IntegerField(_('Past total Leave'),default=0)
    date = models.DateField(_('Date'),default= datetime.datetime.now())
    end_date = models.DateField(_('End Date'),null = True)
    no_days_cleave = models.IntegerField(_('No. of days of current leave'),default = 0)
    reason  = models.CharField(_('Reason'),max_length=300,  blank=True)
    charge_handed_to = models.CharField(_('Charge Handed to '),max_length=50, blank=True)
    handed_fname = models.CharField(_('Full Name of charge handed  '),max_length=50,  blank=True)
    handed_designation = models.CharField(_('Designation of charge handed'),max_length=50, blank=True)
    handed_date = models.DateField(_('Charge Handed Date'),null = True)
    handed_end_date = models.DateField(_('End date of Charge Handed'),null = True)
    approval = models.BooleanField(_('Approval'),default = False)
    attachment   = models.FileField(_('Attachments'),null = True)

    def __str__(self):
        return self.user.username 


class Expense(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    type = models.CharField(_('Type'),max_length= 50)
    date = models.DateField(_('Date'))
    time = models.TimeField(_('Time'),default= datetime.datetime.now())
    payment_method = models.CharField(_('Payment Method'),max_length=50)
    purpose = models.CharField(_('Purpose'),max_length= 300)
    approval_by = models.CharField(_('Approved By'),max_length= 100 , blank= True)
    decline_reason = models.CharField(_('Decline Reason'),max_length=300, blank=True)
    approved = models.BooleanField(_('Is Approved'),default= False)
    approval_date_finance = models.DateField(_('Approval Date by Finanace Department'))
    approval_date_managment = models.DateField(_('Approval Date by management Department'))
    attachment = models.FileField(_('Attachments'),null = True)
    
    def __str__(self):
        return self.user.username

class LeadGenration(models.Model): 
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    executive_name = models.CharField(_('Executivr Name'),max_length=30)
    oreder_dispatch_mon = models.DateField(_('Order Dispatch Month'))
    site_name = models.CharField(_('Site Name '),max_length=100)
    involved_dealer = models.CharField(_('Involved Dealer'),max_length=50)
    location = models.CharField(_('Location'),max_length = 800)
    dev_arch = models.CharField(_('Developer/Architecture '),max_length=50)
    dev_arch_name = models.CharField(_('Developer/Architecture Full Name '),max_length=100)
    order_value = models.BigIntegerField(_('Order Value '),default = 0)
    pro_total_value = models.BigIntegerField(_('Project Total Value '),default = 0)
    total_unit = models.IntegerField(_('Total Unit '),default = 0)
    total_wall_sqft = models.BigIntegerField(_('Total sqft of Wall'),default = 0)
    total_floor = models.IntegerField(_('Total Floor'),default = 0)
    remark = models.CharField(_('Remarks'),max_length=300)
    attachment_front = models.FileField(_('Attachment Front'),null = True)
    attachment_back = models.FileField(_('Attachment Back'),null = True)
    auto_location = models.CharField(_('Auto location '),max_length = 800)

    def __str__(self):
        return self.user.username

class HotProject(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    executive_name = models.CharField(_('Executive Name'),max_length=30)
    visit_date = models.DateField(_('Visit Date'))
    site_name = models.CharField(_('Site Name'),max_length=100)
    involved_dealer = models.CharField(_('Involved Dealer Name'),max_length=50)
    location = models.CharField(_('Location'),max_length = 800)
    dev_arch = models.CharField(_('Developer/Architecture'),max_length=50)
    dev_arch_name = models.CharField(_('Developer/Architecture Full Name'),max_length=100)
    order_value = models.BigIntegerField(_('Order Value'),default = 0)
    pro_total_value = models.BigIntegerField(_('Project Total Value'),default = 0)
    total_unit = models.IntegerField(_('Total Unit'),default = 0)
    total_wall_sqft = models.BigIntegerField(_('Total sqft of Wall'),default = 0)
    total_floor = models.IntegerField(_('Total Floors'),default = 0)
    remark = models.CharField(_('Remarks'),max_length=300)
    constraction_stage = models.CharField(_('Constraction Stage'),max_length=50)
    status = models.CharField(_('Status'),max_length=50)
    contact_person = models.CharField(_('Contact Person Name'),max_length=50)
    contact_num = models.CharField(_('Contact Mobile Number'),max_length=20)
    total_floor_sqft = models.BigIntegerField(_('Total sqft of Floor'),default = 0)
    site_type = models.CharField(_('Site Type'),max_length=30)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    challanges = models.CharField(_('Challanges'),max_length = 500)
    subject = models.CharField(_('Subject'),max_length = 100)
    feedback = models.CharField(_('Feedback'),max_length = 800) 
    attachment = models.FileField(('Attachment'),null = True)

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    userid = models.OneToOneField(CustomeUser, on_delete=models.CASCADE)
    auto_location = models.CharField(_('Auto location'),max_length = 800)
    date = models.DateField(_('Date'))
    time = models.TimeField(_('Time'))
    logout_time = models.TimeField(_('Logout Time'))

    def __str__(self):
        return self.userid.username
    









