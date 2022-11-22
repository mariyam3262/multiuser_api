from rest_framework.serializers import ModelSerializer
from order.models import OrderGeneration


class OrderSerializer(ModelSerializer):
    
    class Meta:
        mode = OrderGeneration
        fields = "__all__"
