from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import  CustomeUser, MarketingPersonAdditional, DealerProfileAdditional



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':True}, write_only = True)
    password = serializers.CharField()
    class Meta:
        model = CustomeUser
        fields = [  'email','username','fname',
                    'lname','dob','mobile',
                    'alt_mobile','permanent_add',
                    'current_add','state','district',
                    'city','pincode','blood_grp','sex',
                    'adhar_num','type', 'password2','password']
        extre_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'P1 and P2 should be same !'})

        # if CustomeUser.objects.filter(email=self.validated_data['email']).exists():
        #     raise serializers.ValidationError({'error':'This email is already used !'})


        account = CustomeUser(  email=self.validated_data['email'], 
                                username=self.validated_data['username'],
                                fname=self.validated_data['fname'],
                                lname=self.validated_data['lname'],
                                dob=self.validated_data['dob'],
                                mobile=self.validated_data['mobile'],
                                alt_mobile=self.validated_data['alt_mobile'],
                                permanent_add=self.validated_data['permanent_add'],
                                current_add=self.validated_data['current_add'],
                                state=self.validated_data['state'],
                                district=self.validated_data['district'],
                                city=self.validated_data['city'],
                                pincode=self.validated_data['pincode'],
                                blood_grp=self.validated_data['blood_grp'],
                                sex=self.validated_data['sex'],
                                adhar_num=self.validated_data['adhar_num'],
                                type= self.validated_data['type']
                                )
        account.set_password(password)

        account.save()
        old_user = CustomeUser.objects.get(id = account.id)
        cid_user = CustomeUser(pk = account.id)
        
        def cid():
            cid = f"CIM{(self.validated_data['state'][0:2]).upper()}{(self.validated_data['city'][0:3]).upper()}0{str(account.id)}"
            return cid


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
        cid_user.save()
        return cid_user

class CustomeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomeUser
        fields = "__all__"

class MarketingPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MarketingPersonAdditional
        fields = "__all__"

class DealerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DealerProfileAdditional
        fields = "__all__"