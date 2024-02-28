from django.urls import path
from .views import index,buy,detail,bool_p

urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:pk_id>', buy, name='buy'),
    path('detail/<int:i_det>', detail, name='detail'),
    path('bool_p/<int:i_bool>', bool_p, name='bool_p'),
]