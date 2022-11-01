from django.forms import ModelForm
from pascasarjana.models import Dosen
from pascasarjana.models import Tendik
from pascasarjana.models import Mahasiswa

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        fields = '__all__'      

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'           