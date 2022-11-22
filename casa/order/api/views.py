from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import OrderGeneration
from .serializers import OrderSerializer
from rest_framework import status


class OrderListView(APIView):

    def get(self, request):
        
        orders = OrderGeneration.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class OrderDetailView(APIView):

    def get(self, request, pk):

        try:
            order =  OrderGeneration.objects.get(pk=pk)
        except OrderGeneration.DoesNotExist:

            return Response({'error':'record not found'},status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def patch(self, request, pk):
        order =  OrderGeneration.objects.get(pk=pk)
        serializer = OrderSerializer(order, data = request.data)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        old_order = OrderGeneration.objects.get(pk=pk)
        deleted_order = OrderGeneration(    pk=pk,
                                            user_id = old_order.user_id,
                                            order_date = old_order.order_date,
                                            order_total_weight = old_order.           order_total_weight,
                                            order_total_box = old_order.order_total_box,
                                            product = old_order.product,
                                            price_ind = old_order.price_ind,
                                            total_price = old_order.total_price,
                                            is_deleted = True
                                        )
        deleted_order.save()
        return Response(status=status.HTTP_204_NO_CONTENT )









         