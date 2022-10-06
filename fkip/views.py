from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judulfkip = ["Pendidikan Nonformal", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Biologi", "Pendidikan Matematika", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru PAUD", "Bimbingan dan Konseling", "Pendidikan Fisika", "Pendidikan Ilmu Pengetahuan Alam", "Pendidikan Kimia", "Pendidikan Khusus", "Pendidikan Pancasila dan Kewarganegaraan", "Pendidikan Sejarah", "Pendidikan Seni dan Pertunjukan", "Pendidikan Sosiologi", "Pendidikan Vokasional Teknik Elektro", "Pendidikan Vokasional Teknik Mesin"]
   
    konteks = {
        'titlefkip' : judulfkip,

    }
    return render(request, 'fkip/index.html', konteks)

from . models import Dosen, Mahasiswa, Tendik

# Create your views here.
def prodi6(request):
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip/index.html', konteks)
