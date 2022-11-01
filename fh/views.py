from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from fh.forms import FormDosen
from fh.forms import FormTendik
from fh.forms import FormMahasiswa

# Create your views here.
def prodi3(request):
    judulfh = ["Ilmu Hukum"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlefh' : judulfh,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'fh/index.html', konteks)
