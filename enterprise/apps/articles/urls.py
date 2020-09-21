from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/leave_comment/', views.leave_comment, name="leave_comment"),
    path('subjects/<int:subject_id>/', views.sub_detail, name="sub_detail"),
    path('subjects/', views.sub_list, name="sub_list"),
    path('contacts', views.contacts, name="contacts"),
    path('account/', views.personal_page, name="personal_page"),
    path('test_case/<int:test_case_id>', views.test_case, name="test_case"),
    path('test_case/<int:test_case_id>/testing', views.testing, name="testing"),
    path('done/', views.done, name="done"),


]
