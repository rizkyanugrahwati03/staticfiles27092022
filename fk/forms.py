from django.forms import ModelForm
from fk.models import Dosen
from fk.models import Tendik
from fk.models import Mahasiswa

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