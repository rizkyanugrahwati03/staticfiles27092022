from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judulft = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]

    konteks = {
        'titleft' : judulft,
    }
    return render(request, 'ft/index.html', konteks)