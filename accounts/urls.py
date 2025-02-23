from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name='accounts'
urlpatterns=[
   path('login',views.login,name="login"),
   path('register',views.register,name="register"),
   path('logout',views.logout,name="logout"),
   path('studata',views.studata,name="studata"),
   path('drop',views.drop,name="drop"),
   path('adddata',views.adddata,name="adddata"),
   path('filter',views.filter,name="filter"),
   path('alumini',views.alumini,name="alumini"),
   path('odrequest',views.odrequest,name="odrequest"),
   path('odform',views.odform,name="odform")
   
 
  ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 