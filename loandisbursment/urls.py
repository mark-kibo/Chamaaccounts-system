from django.urls import path
from . import views


urlpatterns=[
    path('', views.new, name="home"),
    path('loan', views.loan, name="loan"),
    path('chama', views.table, name="table"),
    path('new_table', views.new_table, name="new_table"),
    
    path('addmember', views.addmember, name="addmember"),
    path('deletemember', views.deletemember, name="deletemember"),
    path('chamaaccounts', views.accounts, name="accounts")

]
