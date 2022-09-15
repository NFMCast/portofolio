from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobre_mim', views.sobre_mim_page_view, name='sobre_mim'),

    path('blog', views.blog_page_view, name='blog'),
    path('novo_post', views.novo_post_view, name='novo_post'),
    path('editar_post/<int:post_id>', views.editar_post_view, name='editar_post'),
    path('apagar_post/<int:post_id>', views.apagar_post_view, name='apagar_post'),

    path('contacto', views.contacto_page_view, name='Contacto'),

    path('licenciatura', views.licenciatura_page_view, name='Licenciatura'),

    path('tfc', views.tfc_page_view, name='TFC'),

    path('video', views.video_page_view, name='video')
     
]
