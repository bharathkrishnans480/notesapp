from django.urls import path
from mynotes import views

urlpatterns=[

    path("home",views.CreateNotesView.as_view(),name="home"),
    path('home/<int:post_id>',views.EditNotesView.as_view(),name='note-edit'),
    path('delete/<int:post_id>',views.delete,name='delete'),

]