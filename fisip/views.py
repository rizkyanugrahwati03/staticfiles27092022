from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from fisip.forms import FormDosen
from fisip.forms import FormTendik
from fisip.forms import FormMahasiswa

# Create your views here.
def prodi4(request):
    judulfisip = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintahan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlefisip' : judulfisip,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'fisip/index.html', konteks)

