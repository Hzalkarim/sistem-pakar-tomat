from django.urls import path
from . import views

app_name='tomat'
urlpatterns = [
    path('', views.index, name='index'),
    path('pertanyaan/<str:kode>', views.pertanyaan, name='pertanyaan'),
    path('pilih/<str:kode_gejala>', views.pilih, name='pilih'),
    path('rekap/', views.rekap, name='rekap'),
    path('jenis-penyakit/', views.jenis_penyakit, name='jenis-penyakit'),
    path('hasil/', views.hasil, name='hasil'),
]