from django.urls import path


from .views import (ExpenseDetailView, ExpenseListView, LeaveReportListView, FeedbackListView, LeaveReportDetailView, FeedbackDetailView, AttendanceListView, AttendanceDetailView,
HotProjectListView,HotProjectDetailView)


urlpatterns = [

    # --------------------------LEADGENRATION-------------------------------

    path('leave-list/', LeaveReportListView.as_view(), name = 'leave-list'),
    path('<int:pk>/leave-detail/', LeaveReportDetailView.as_view(), name= 'leave-detail'),

   #-------------------------------EXPENSE----------------------------------------

   path('expense-list/', ExpenseListView.as_view(), name='expense-list'),
   path('<int:pk>/expense-detail/', ExpenseDetailView.as_view(), name='expense-detail'),

    #------------------------------FEEDBACK-------------------------------------------

    path('feedback-list/', FeedbackListView.as_view(), name='feedback-list'),
    path('<int:pk>/feedback-detail/', FeedbackDetailView.as_view(), name='feedback-detail'),

    #------------------------------ATTENDACE-------------------------------------

    path('attendance-list/', AttendanceListView.as_view(), name='attendace-list'),
    path('<int:pk>/attendance-detail/', AttendanceDetailView.as_view(), name='attendace-detail'),

    #------------------------------HOTPROJECT----------------------------- 

    path('hotproject-list/', HotProjectListView.as_view(), name='hotproject-list'),
    path('<int:pk>/hotproject-detail/', HotProjectDetailView.as_view(), name='hotproject-detail') 
]