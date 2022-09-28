from django.shortcuts import render

# Create your views here.
def prodi3(request):
    judulfh = ["Ilmu Hukum"]

    konteks = {
        'titlefh' : judulfh,
        
    }
    return render(request, 'fh/index.html', konteks)