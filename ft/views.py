from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judulft = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]

    konteks = {
        'titleft' : judulft,
    }
    return render(request, 'ft/index.html', konteks)

from . models import Dosen, Mahasiswa, Tendik

# Create your views here.
def prodi7(request):
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'ft/index.html', konteks)
