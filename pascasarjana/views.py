from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judulpascasarjana = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]
    
    konteks = {
        'titlepascasarjana' : judulpascasarjana,
        
    }
    return render(request, 'pascasarjana/index.html', konteks)

from . models import Dosen, Mahasiswa, Tendik

# Create your views here.
def prodi8(request):
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana/index.html', konteks)
