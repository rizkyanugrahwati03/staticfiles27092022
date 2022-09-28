from django.shortcuts import render

# Create your views here.
def universitas(request):
    judulpascasarjana = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]
    
    konteks = {
        'titlepascasarjana' : judulpascasarjana,
        
    }
    return render(request, 'universitas.html', konteks)