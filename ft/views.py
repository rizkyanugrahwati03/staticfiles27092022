from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from ft.forms import FormDosen
from ft.forms import FormTendik
from ft.forms import FormMahasiswa

# Create your views here.
def prodi7(request):
    judulft = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titleft' : judulft,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'ft/index.html', konteks)
