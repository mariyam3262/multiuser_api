from rest_framework.authtoken.views import ObtainAuthToken
from account.api.views import (registration_view,
                                logout_view,
                                MarketingPersonProfileListView,MarketingPersonProfileDetailView,
                                CustomeUserListView,
                                CustomeUserDetailView,
                                DealerListView, 
                                DealerDetailView,
                                test)

from django.urls import path

urlpatterns = [
    
    path('login/',ObtainAuthToken.as_view(), name='login'),
    path('register/',registration_view, name='register'),
    path('logout/',logout_view, name='logout'),

#------------------------marketing person----------------------

    path('marketperson-list/', MarketingPersonProfileListView.as_view(), name = 'profile-list'),
    path('<int:pk>/marketperson-detail/', MarketingPersonProfileDetailView.as_view(), name= 'profile-detail'),

#----------------------------CustomeUser ----------------------

    path('user/', CustomeUserListView.as_view(), name='user-list'),
    path('<int:pk>/user-detail/', CustomeUserDetailView.as_view(), name= 'profile-detail'),

#-------------------------------Dealer ------------------------

    path('dealer-list/', DealerListView.as_view(), name = 'profile-list'),
    path('<int:pk>/dealer-detail/', DealerDetailView.as_view(), name= 'profile-detail'),

#--------------------------------CALARY------------------------

    path('test/', test, name='celery-test' ),
]