from tomat_fwd_chaining.models import *

def cari_hasil():
    aturan = Aturan.objects.all()
    hasil = []

    for a in aturan:
        ag = AturanGejala.objects.filter(kode_aturan=a.pk)

        ls_benar = [1 if i.kode_gejala.pilihan == 'benar' else 0 for i in ag]
        jml_benar = 0
        for i in ls_benar:
            jml_benar += i

        hasil.append('{:.2f}'.format(jml_benar / len(ls_benar)))

    return zip(aturan, hasil)