from rest_framework.serializers  import *

from SellerDetails.Models import Seller 
class SerializeSeller(ModelSerializer):
    class Meta:
        model=Seller

        fields=['sellerName' 		,
        		'id'				,
                'purchasedQty' 		,
                'address' 			,
                'phoneNumber' 		,
                'purchasedThings' ,]