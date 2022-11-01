from django.shortcuts import render, redirect
from . models import Dosen, Mahasiswa, Tendik
from faperta.forms import FormDosen, FormTendik, FormMahasiswa
from django.contrib import messages


# Create your views here.
def prodi1(request):
    judulfaperta = ["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'titlefaperta' : judulfaperta,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'faperta/index.html', konteks)    

def hapus_tendik(request, id_tendik):
    tendik = Tendik.objects.filter(id=id_tendik) 
    tendik.delete()

    return redirect('tendik')   


def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen) 
    dosen.delete()

    return redirect('dosen')   

def ubah_tendik(request, id_tendik):
    tendik = Tendik.objects.get(id=id_tendik)
    template = 'ubah-tendik.html'
    if request.POST:
        form = FormTendik(request.POST, instance=tendik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_tendik', id_tendik=id_tendik)
    else:   
        form = FormTendik(instance=tendik)
        konteks = {
            'form': form,
            'tendik': tendik,
        }  
        return render(request, 'faperta/ubah-tendik.html', konteks)    

def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:   
        form = FormDosen(instance=dosen)
        konteks = {
            'form': form,
            'dosen': dosen,
        }  
        return render(request, 'faperta/ubah-dosen.html', konteks)

def tambah_dosen(request):   
    if request.POST: 
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data Berhasil Disimpan"

            konteks ={
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'faperta/tambah-dosen.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form' : form,
    }
    return render(request, 'faperta/tambah-dosen.html', konteks)

def tambah_tendik(request): 
    if request.POST:   
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data Berhasil Disimpan"

            konteks ={
                'form': form,
                'pesan':pesan,
            }
            return render(request, 'faperta/tambah-tendik.html', konteks)
    else:
        form = FormTendik()

    konteks = {
        'form' : form,
    }
    return render(request, 'faperta/tambah-tendik.html', konteks)

def tambah_mahasiswa(request):
    form = FormMahasiswa()
    konteks ={
        'form' : form,
    }    
    return render(request, 'faperta/tambah-mahasiswa.html', konteks)