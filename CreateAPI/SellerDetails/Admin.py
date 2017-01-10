from django.contrib import admin
from django.db import models
from  .Models import Seller

class SellerAdmin(admin.ModelAdmin):
    class Meta:
        model=Seller

admin.site.register(Seller,SellerAdmin)





