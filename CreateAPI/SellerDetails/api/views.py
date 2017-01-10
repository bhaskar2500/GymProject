from rest_framework.generics import ListAPIView

from .serializers import SerializeSeller

from SellerDetails.Models import Seller 



class SellerListAPI(ListAPIView):
    queryset=Seller.objects.all()
    serializer_class=SerializeSeller





