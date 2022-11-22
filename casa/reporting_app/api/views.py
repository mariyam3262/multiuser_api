from rest_framework.views import APIView
from .serializers import LeaveReportSerializer, ExpenseSerializer,FeedbackSerializer,AttendanceSerializer, HotProjectSerializer
from reporting_app.models import LeaveReport, Expense,  Feedback, Attendance, HotProject
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsMarketingPerson, IsDealer



class LeaveReportListView(APIView):
    permission_classes = [IsMarketingPerson]
    
    def get(self, request):
        if request.user.is_superuser:
            leaves = LeaveReport.objects.all()
        else:
            leaves =  LeaveReport.objects.filter(user_id = request.user.id)
        serializer = LeaveReportSerializer(leaves , many=True)
        return Response(serializer.data)


    def post(self, request):
        
        serializer = LeaveReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class LeaveReportDetailView(APIView):
    permission_classes = [IsMarketingPerson]
    def get(self, request, pk):
        print(pk)

        try:
            leave = LeaveReport.objects.get(pk=pk)
        except LeaveReport.DoesNotExist:
            return Response({'Error':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = LeaveReportSerializer(leave)
        return Response(serializer.data)
    

    def patch(self, request, pk):
        leave = LeaveReport.objects.get(pk=pk)
        serializer = LeaveReportSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
       leave = LeaveReport.objects.get(pk=pk)
       leave.delete()
       return Response(status=status.HTTP_204_NO_CONTENT )

#----------------------------------HOTPROJECT---------------------------------

class HotProjectListView(APIView):
    permission_classes = [IsDealer]
    
    def get(self, request):
        if request.user.is_superuser:
            project = HotProject.objects.all()
        else:
            project =  HotProject.objects.filter(user_id = request.user.id)
        serializer = HotProjectSerializer(project , many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = HotProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class HotProjectDetailView(APIView):
    permission_classes = [IsDealer]
    def get(self, request, pk):
        print(pk)

        try:
            project = HotProject.objects.get(pk=pk)
        except HotProject.DoesNotExist:
            return Response({'Error':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = HotProjectSerializer(project)
        return Response(serializer.data)
    

    def patch(self, request, pk):
        project = HotProject.objects.get(pk=pk)
        serializer = HotProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
       project = HotProject.objects.get(pk=pk)
       project.delete()
       return Response(status=status.HTTP_204_NO_CONTENT )


# --------------------------------  EXPENSE ------------------------------------


class ExpenseListView(APIView):
    permission_classes = [IsMarketingPerson]
    def get(self, request):
        if request.user.is_superuser:
            expense = Expense.objects.all()
        else:
            expense = Expense.objects.filter(user_id = request.user.id)
        serializer = ExpenseSerializer(expense, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = ExpenseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ExpenseDetailView(APIView):
    permission_classes = [IsMarketingPerson]
    def get(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({'Error':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)


    def patch(self, request, pk):

        expense = Expense.objects.get(pk=pk)
        serializer = ExpenseSerializer(expense , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        expense =  Expense.objects.get(pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )

#---------------------FEEDBACK-------------------------

class FeedbackListView(APIView):
    permission_classes = [IsDealer]
    def get(self, request):

        if  request.user.is_superuser:
            feed = Feedback.objects.all()
        else:
            feed = Feedback.objects.filter(user_id = request.user.id)

        serializer = FeedbackSerializer(feed, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FeedbackDetailView(APIView):
    permission_classes = [IsDealer]
    def get(self, request, pk):

        try:
            feed = Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            return Response({'error':'record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeedbackSerializer(feed)
        return Response(serializer.data)

    def patch(self, request, pk):

        feed = Feedback.objects.get(pk=pk)
        serializer = FeedbackSerializer(feed, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        feed = Feedback.objects.get(pk=pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#-------------------Attandence------------------------

class AttendanceListView(APIView):
    permission_classes = [IsMarketingPerson]
    def get(self, request):
        
        if request.user.is_superuser:
            attendance = Attendance.objects.all()
        else:
            attendance = Attendance.objects.filter(userid_id= request.user.id)
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class AttendanceDetailView(APIView):
    permission_classes = [IsMarketingPerson]
    def get(self, request, pk):

        try:
            attendance = Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            return Response({'error':'record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def patch(self, request, pk):

        attendance = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(attendance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        attendance = Attendance.objects.get(pk=pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

