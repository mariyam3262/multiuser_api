from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegistrationSerializer,MarketingPersonSerializer, CustomeUserSerializer, DealerSerializer
from ..models import CustomeUser, MarketingPersonProfile, MarketingPersonAdditional, DealerProfileAdditional
from reporting_app.models import Attendance
from rest_framework.views import APIView
from .. import models
from django.contrib.auth.models import User
import datetime
from reporting_app.api.permissions import IsMarketingPerson, IsDealer
from rest_framework.pagination import PageNumberPagination
from .tasks import send_notifications
from django.http import HttpResponse
from account.models import CustomeUser



@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        print(request.user.id)
        market_person = MarketingPersonProfile.objects.get(user_id =request.user.id )
        print(market_person)
        market_person_attendance = Attendance.objects.filter(userid_id = market_person.id).last()
        attendance = Attendance(pk=market_person_attendance.id)
        attendance.logout_time = datetime.datetime.now()
        attendance.save()
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST',])
def registration_view(request):  

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful"
            data['email'] = account.email

            token = Token.objects.get(user=account).key 
            data['token'] = token

            user = request.data
            print(user)
            def cid():
                cid = f"CIM{(user['state'][0:2]).upper()}{(user['city'][0:3]).upper()}0{str(account.id)}"
                return cid

            data['username'] = cid()

            old_user = CustomeUser.objects.get(pk = account.id)
            print("user ",old_user.type)
            cid_user = CustomeUser(pk = account.id)
            CID = cid()                

            cid_user.email = old_user.email 
            cid_user.username = CID
            cid_user.fname = old_user.fname
            cid_user.lname = old_user.lname
            cid_user.dob = old_user.dob
            cid_user.mobile = old_user.mobile
            cid_user.alt_mobile = old_user.alt_mobile
            cid_user.permanent_add = old_user.permanent_add
            cid_user.current_add = old_user.current_add
            cid_user.state = old_user.state
            cid_user.district = old_user.district
            cid_user.city = old_user.city
            cid_user.pincode = old_user.pincode
            cid_user.blood_grp = old_user.blood_grp
            cid_user.sex = old_user.sex
            cid_user.adhar_num = old_user.adhar_num
            cid_user.password = old_user.password
            cid_user.type = old_user.type

            if old_user.type == 'MARKETING_PERSON':
                cid_user.is_staff = True

            elif old_user.type == 'ADMIN':
                cid_user.is_superuser = True
                cid_user.is_staff = True

            cid_user.save()
            
            if cid_user.type == 'MARKETING_PERSON':

                market_person = MarketingPersonAdditional(pk = cid_user.id)
                market_person.user_id = cid_user.id                 
                market_person.save()

            if cid_user.type == 'DEALER':
                dealer = DealerProfileAdditional(pk = cid_user.id)
                dealer.user_id = cid_user.id

                if request.user.type == user['type']:
                    dealer.created_by_id = cid_user.id 
                else:
                    dealer.created_by_id = request.user.id

                dealer.save()

        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)


class CustomeUserListView(APIView):
    permission_classes = [IsMarketingPerson]

    def get(self, request):
        user = CustomeUser.objects.all()
        serializer = CustomeUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CustomeUserDetailView(APIView):
    permission_classes = [IsMarketingPerson]

    def get(self, request, pk):
        try:
            profile = CustomeUser.objects.get(pk=pk)
        except CustomeUser.DoesNotExist:
            return Response({'Error':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = CustomeUserSerializer(profile)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        profile = CustomeUser.objects.get(pk=pk)
        serializer = CustomeUserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
       profile = CustomeUser.objects.get(pk=pk)
       profile.delete()
       return Response(status=status.HTTP_204_NO_CONTENT )
    


class MarketingPersonProfileListView(APIView):
    permission_classes = [IsMarketingPerson]
    
    def get(self, request):

        if request.user.is_superuser == True:
            person = MarketingPersonAdditional.objects.all()
        else:
            person = MarketingPersonAdditional.objects.filter(user_id = request.user.id)

        serializer = MarketingPersonSerializer(person , many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MarketingPersonProfileDetailView(APIView):
    permission_classes = [IsMarketingPerson]

    def get(self, request, pk):
        try:
            profile = MarketingPersonAdditional.objects.get(pk=pk)
        except MarketingPersonAdditional.DoesNotExist:
            return Response({'Error':'record not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = MarketingPersonSerializer(profile)
        return Response(serializer.data)
    

    def patch(self, request, pk):
        profile = MarketingPersonAdditional.objects.get(pk=pk)
        serializer = MarketingPersonSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
       profile = MarketingPersonAdditional.objects.get(pk=pk)
       profile.delete()
       return Response(status=status.HTTP_204_NO_CONTENT )


class DealerListView(APIView):
    permission_classes = [IsDealer]

    def get(self, request):
        if request.user.is_superuser:
            person = MarketingPersonAdditional.objects.all()
        else:
            person = MarketingPersonAdditional.objects.filter(user_id = request.user.id)
        pagination = PageNumberPagination()
        pagination.page_query_param = 'p'
        pagination.page_size_query_param = 'size'
        pagination.max_page_size = 5
        # pagination.last_page_strings = 'end'
        result = pagination.paginate_queryset(person, request)
        serializer = DealerSerializer(result,many=True ,context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
  

class DealerDetailView(APIView):
     permission_classes = [IsDealer]

     def get(self, request, pk):
        try:
            dealer= DealerProfileAdditional.objects.get(pk=pk)

        except DealerProfileAdditional.DoesNotExist:
            return Response({'error': 'Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer= DealerSerializer(dealer,context={'request':request})
        return Response(serializer.data)    

     def patch(self, request,pk):
        dealer=DealerProfileAdditional.objects.get(pk=pk)
        serializer= DealerSerializer(dealer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

     def delete(self, request, pk):
        dealer= DealerProfileAdditional.objects.get(pk=pk)
        dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           


def test(request):
    send_notifications.delay()
    return HttpResponse("<h1>Done</h1>")

  
