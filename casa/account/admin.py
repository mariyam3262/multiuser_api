from dataclasses import field, fields
from django.contrib import admin
from .models import MarketingPersonProfile
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User
from account.models import MarketingPersonProfile, DealerProfile, CustomeUser,MarketingPersonAdditional, DealerProfileAdditional
from reporting_app.models import LeadGenration
from reporting_app.models import (LeadGenration, Expense, LeaveReport, HotProject, Feedback)



#-----------------INLINES---------------------------

class LeadGenrationInline(admin.TabularInline):
    model = LeadGenration


class ExpenseInline(admin.TabularInline):
    model = Expense


class LeaveReportInline(admin.TabularInline):
    model = LeaveReport

class HotProjectInline(admin.TabularInline):
    model = HotProject


class FeedbackInline(admin.TabularInline):
    model = Feedback




@admin.register(MarketingPersonProfile)
class MarketingPersonProfile(admin.ModelAdmin):
    list_display = ['username','full_name','is_staff']
    fieldsets = (
                (None,{'fields' : ('username','password','type')}),
                ('Info',{'classes':('collapse',),
                            'fields':('lname','fname','email','mobile','alt_mobile','current_add','permanent_add','adhar_num','dob','state','city','district','pincode','blood_grp','sex')}),
                )
    search_fields = ('username','type',)
    # inlines = [LeadGenrationInline, ExpenseInline, LeaveReportInline, HotProjectInline,FeedbackInline]

    def full_name(self,obj):
        return f'{obj.fname} {obj.lname}'


@admin.register(DealerProfile)
class DealerProfile(admin.ModelAdmin):
    list_display = ['username','full_name','is_staff']
    fieldsets = (
                (None,{'fields' : ('username','password','type')}),
                ('Info',{'classes':('collapse',),
                            'fields':('lname','fname','email','mobile','alt_mobile','current_add','permanent_add','adhar_num','dob','state','city','district','pincode','blood_grp','sex')}),
                )
    search_fields = ('username','type',)
    # inlines = [LeadGenrationInline, ExpenseInline, LeaveReportInline, HotProjectInline,FeedbackInline]

    def full_name(self,obj):
        return f'{obj.fname} {obj.lname}'






@admin.register(CustomeUser)
class CustomeUser(admin.ModelAdmin):
    model = CustomeUser
    list_display = ['username','full_name','is_staff']
    fieldsets = (
                (None,{'fields' : ('username','password','type')}),
                ('Info',{'classes':('collapse',),
                            'fields':('lname','fname','email','mobile','alt_mobile','current_add','permanent_add','adhar_num','dob','state','city','district','pincode','blood_grp','sex')}),
                )
    search_fields = ('username','type',)
    # inlines = [LeadGenrationInline, ExpenseInline, LeaveReportInline, HotProjectInline,FeedbackInline]

    def full_name(self,obj):
        return f'{obj.fname} {obj.lname}'

    
        


@admin.register(MarketingPersonAdditional)
class MarketingPersonAdditional(admin.ModelAdmin):
    list_display = ['user','company_email']

@admin.register(DealerProfileAdditional)
class DealerProfileAdditional(admin.ModelAdmin):
    list_display = ['user','created_by']


