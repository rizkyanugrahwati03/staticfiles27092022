from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik
from fkip.forms import FormDosen
from fkip.forms import FormTendik
from fkip.forms import FormMahasiswa


# Create your views here.
def prodi6(request):
    judulfkip = ["Pendidikan Nonformal", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Biologi", "Pendidikan Matematika", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru PAUD", "Bimbingan dan Konseling", "Pendidikan Fisika", "Pendidikan Ilmu Pengetahuan Alam", "Pendidikan Kimia", "Pendidikan Khusus", "Pendidikan Pancasila dan Kewarganegaraan", "Pendidikan Sejarah", "Pendidikan Seni dan Pertunjukan", "Pendidikan Sosiologi", "Pendidikan Vokasional Teknik Elektro", "Pendidikan Vokasional Teknik Mesin"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    form = FormDosen()
    form = FormTendik()
    form = FormMahasiswa()
    konteks = {
        'titlefkip' : judulfkip,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
        'form' : form,
        'form' : form,
        'form' : form,
    }
    return render(request, 'fkip/index.html', konteks)

