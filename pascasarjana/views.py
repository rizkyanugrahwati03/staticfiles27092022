from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from pascasarjana.forms import FormDosen
from pascasarjana.forms import FormTendik
from pascasarjana.forms import FormMahasiswa

# Create your views here.
def prodi8(request):
    judulpascasarjana = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlepascasarjana' : judulpascasarjana,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'pascasarjana/index.html', konteks)

