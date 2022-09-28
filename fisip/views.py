from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judulfisip = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintahan"]

    konteks = {
        'titlefisip' : judulfisip,
        
    }
    return render(request, 'fisip/index.html', konteks)
