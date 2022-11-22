from dataclasses import fields
from django.contrib import admin
from .models import LeaveReport, Expense,  Feedback, Attendance, LeadGenration, HotProject
# from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.


@admin.register(LeaveReport)
class LeaveReportAdmin(admin.ModelAdmin):
    model = LeaveReport
    search_fields = ('user__username',)
    list_display = ['user','type','date','end_date','charge_handed_to']
    list_filter = ('user','type','date','charge_handed_to')
    fieldsets = (
        (None, {'fields':('user','type')}),
        ('Leave info',{'fields':('date','end_date','no_days_cleave','total_leave','past_total_leave','reason')}),
        ('Additional Detail',{'classes':('collapse',),'fields':('charge_handed_to','handed_fname',  'handed_designation','handed_date','handed_end_date','approval','attachment')})
    )

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    search_fields = ('user__username',)
    list_display = ['user','type','date','purpose']
    list_filter = ('user','date','approved')
    fieldsets = (
        (None, {'fields':('user','type')}),
        ('Expense info',{'fields':('date','payment_method','purpose','approval_by')}),
        ('Additional Detail',{'classes':('collapse',),
                              'fields':('decline_reason','approved','approval_date_finance','approval_date_managment','attachment')})
    )

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    search_fields = ('user__username',)
    list_display = ['user','feedback']
    list_filter = ('user','subject')
    fieldsets = (
        (None, {'fields':('user','feedback','attachment')}),
        ('Feedback info',{'fields':('challanges','subject',)})
    )

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    model = Attendance
    search_fields = ('userid__username',)
    list_display = ['userid','date','time','logout_time']
    fieldsets = (
        ('Attendance info', {'fields':('userid','date','time','logout_time')}),
    )

@admin.register(LeadGenration)
class LeadGenrationAdmin(admin.ModelAdmin):
    model = LeadGenration
    search_fields = ('user__username',)
    list_display = ['user','executive_name','site_name','involved_dealer','location','dev_arch_name','pro_total_value','remark']
    fieldsets = (
        ('Lead Generation Info', {'fields':('user','executive_name','oreder_dispatch_mon','site_name')}),
        ('Dealer Info',{'fields':('involved_dealer','dev_arch','dev_arch_name')}),
        ('Project Detail',{'classes':('collapse',),
                           'fields':('order_value','pro_total_value','total_unit','total_wall_sqft',           'total_floor','attachment_front','attachment_back','location','auto_location')})
    )
    

@admin.register(HotProject)
class HotProjectAdmin(admin.ModelAdmin):
    model = HotProject
    search_fields = ('user__username',)
    list_display = ['user','executive_name','site_name','involved_dealer','location','dev_arch_name','pro_total_value','remark']
    fieldsets = (
        ('Hot Project Info', {'fields':('user','executive_name','visit_date','site_name','site_type')}),
        ('Dealer Info',
        {'fields':('involved_dealer','dev_arch','dev_arch_name','contact_person','contact_num')}),
        ('Project Detail',{'classes':('collapse',),'fields':('order_value','pro_total_value','total_unit','total_wall_sqft','total_floor','location','total_floor_sqft')})
    )
    