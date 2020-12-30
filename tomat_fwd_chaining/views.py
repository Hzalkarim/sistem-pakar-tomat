from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from tomat_fwd_chaining.program import sistem_pakar_tomat as sp
from .models import Gejala, Penyakit

def index(request):
    return render(request, 'tomat_fwd_chaining/index.html')

def pertanyaan(request, kode):
    gejala = get_object_or_404(Gejala, pk=kode)
    return render(request, 'tomat_fwd_chaining/pertanyaan.html', {'hai' : 'Halo', 'gejala' : gejala,})

def pilih(request, kode_gejala):
    hasil = request.POST['pilih']
    gejala = get_object_or_404(Gejala, pk=kode_gejala)
    gejala.pilihan = hasil
    gejala.save()

    nomor = int(kode_gejala[1:]) + 1
    lanjut = 'B' + str(nomor)

    try:
        gejala_lanjut = Gejala.objects.get(pk=lanjut)
    except (KeyError, Gejala.DoesNotExist):
        return HttpResponseRedirect('../rekap')
    else:
        return HttpResponseRedirect('../pertanyaan/'+lanjut)

def rekap(request):
    gejala = Gejala.objects.all()
    return render(request, 'tomat_fwd_chaining/rekap.html', { 'gejala' : gejala, })

def jenis_penyakit(request):
    peny = Penyakit.objects.all()
    return render(request, 'tomat_fwd_chaining/jenis-penyakit.html', { 'penyakit' : peny })

def hasil(request):
    h = sp.cari_hasil()
    peny = Penyakit.objects.all()
    return render(request, 'tomat_fwd_chaining/hasil.html', { 'hasil' : h, 'penyakit' : peny })