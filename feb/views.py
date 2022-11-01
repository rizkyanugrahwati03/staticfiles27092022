from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from feb.forms import FormDosen
from feb.forms import FormTendik
from feb.forms import FormMahasiswa

# Create your views here.
def prodi2(request):
    judulfeb = ["Sarjana Managemen", "Sarjana Akuntansi", "Sarjana Ilmu Ekonomi Pembangunan", "Sarjana Ekonomi Syariah", "Diploma III Akuntansi", "Diploma III Marketing", "Diploma III Perpajakan", "Diploma III Keuangan Perbankan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlefeb' : judulfeb,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'feb/index.html', konteks)
