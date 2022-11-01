from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from fk.forms import FormDosen
from fk.forms import FormTendik
from fk.forms import FormMahasiswa

# Create your views here.
def prodi5(request):
    judulfk = ["Kedokteran", "Keperawatan S1", "Keperawatan D3", "S1 Gizi", "Ilmu Keolahragaan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlefk' : judulfk,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'fk/index.html', konteks)
