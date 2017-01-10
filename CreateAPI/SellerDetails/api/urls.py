from django.conf.urls import include, url
from   .views import SellerListAPI
                      

urlpatterns=[

    url(r'^$',SellerListAPI.as_view(),name="list"),
    
    ]
