from django.contrib import admin
from django.db.models import F
from .models import member,destinaton

# Register your models 
class memberAdmin(admin.ModelAdmin):
    list_display = ['name']
    actions = ['bulk_update']
    def bulk_update(self,request,queryset):
        my_objects = member.objects.all()
        my_objects1 = destinaton.objects.all()
        for obj in my_objects:
            if obj.year <= 3:
                member.objects.filter(idno=obj.idno).update(year=obj.year + 1)
                print('***************************')
                   
            else:
                print('-------------------------------')
                
                target_instance = destinaton(
                name=obj.name,  
                gender=obj.gender,
                registerno=obj.registerno,
                idno=obj.idno,
                aadharno = obj.aadharno,
                year= 'alumini', 
                image= obj.image
                )
                target_instance.save()
                member.objects.filter(year=obj.year).delete()
                 
                
                

                    
    bulk_update.short_description = "update year"
      

    
admin.site.register(member,memberAdmin)