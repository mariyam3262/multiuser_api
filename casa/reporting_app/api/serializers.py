from rest_framework import serializers
from ..models import (Attendance, LeaveReport, Expense, LeadGenration, HotProject, Feedback)

class LeaveReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveReport
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__" 


class LeadGenrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadGenration
        fields = "__all__"


class HotProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotProject
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"