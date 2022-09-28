from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judulfk = ["Kedokteran", "Keperawatan S1", "Keperawatan D3", "S1 Gizi", "Ilmu Keolahragaan"]

    konteks = {
        'titlefk' : judulfk,

    }
    return render(request, 'fk/index.html', konteks)