from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from beranda.models import User
from django.forms import ModelForm 
from .models import Kamar, Pegawai, Keuangan, Presensi, Pemesanan, Pembayaran, Pengeluaran, Nomor_Kamar, Kunci
from django.utils import timezone

# ----------------------Registrasi--------------------------------

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    status = forms.ChoiceField(
        choices=(("Aktif", "Aktif"), ("Nonaktif", "Nonaktif")),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role','status']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
    
#-------------------Kelola Kamar----------------------------

class FormNomorKamar(forms.ModelForm):
    class Meta:
        model = Nomor_Kamar
        fields = ['jenis_kamar', 'no_kamar']
        widgets = {
            'jenis_kamar': forms.Select(attrs={'class': 'form-control'}),
            'no_kamar': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan'}),
        }

class FormKamar(forms.ModelForm):
    class Meta:
        model = Kamar
        fields = ['jenis_kamar','kapasitas', 'kasur', 'fasilitas_lainnya', 'tarif', 'gambar_kamar']
        widgets = {  
            'jenis_kamar': forms.Select(attrs={'class': 'form-control'}),
            'kapasitas': forms.NumberInput(attrs={'class': 'form-control'}),
            'kasur': forms.TextInput(attrs={'class': 'form-control'}),
            'fasilitas_lainnya': forms.Textarea(attrs={'class': 'form-control'}),
            'tarif': forms.NumberInput(attrs={'class': 'form-control'}),
            'gambar_kamar': forms.FileInput(attrs={'class': 'form-control'}),  
        }
        
#---------------------------Kelola Pelanggan---------------------------------

# class FormPelanggan(forms.ModelForm):
#     class Meta:
#         model = Pelanggan
#         fields = ['nama_pelanggan','jenis_kelamin_pelanggan','alamat_pelanggan','no_telepon_pelanggan','no_ktp_pelanggan','foto_ktp']
        
#         widgets = {
#             'nama_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
#             'jenis_kelamin_pelanggan': forms.Select(attrs={'class': 'form-control'}),
#             'alamat_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
#             'no_telepon_pelanggan': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan', 'class': 'form-control'}),
#             'no_ktp_pelanggan': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan', 'class': 'form-control'}), 
#             'foto_ktp': forms.FileInput(attrs={'class': 'form-control'}),   
#         }

        
#---------------------------Kelola Pegawai---------------------------------        

class FormPegawai(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = ['nama', 'jenis_kelamin', 'alamat', 'posisi', 'no_telepon', 'shift']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'posisi': forms.TextInput(attrs={'class': 'form-control'}),
            'no_telepon': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan'}), 
            'shift': forms.Select(attrs={'class': 'form-control'}),
        }

#---------------------------Kelola Keuangan--------------------------------

class FormKeuangan(ModelForm):
    class Meta :
        model = Keuangan
        fields='__all__'
        
        widgets = {
            'tanggal' : forms.DateInput({'class' : 'form-control'}),
            'kategori' : forms.Select({'class' : 'form-control'}),
            'keterangan' : forms.TextInput({'class' : 'form-control'}),
            'pemasukan' : forms.TextInput({'class' : 'form-control'}),
            'pengeluaran' : forms.TextInput({'class' : 'form-control'}),       
        }
        
#---------------------------Kelola Presensi---------------------------------
        
class FormPresensi(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = ['pegawai', 'bukti_absen']
        widgets = {
            'pegawai': forms.Select(attrs={'class': 'form-control'}),
            'bukti_absen': forms.HiddenInput(attrs={'class': 'form-control-file'})
        }
        
#-----------------Kelola Pemesanan-----------------------

class FormPemesanan(forms.ModelForm):
    class Meta:
        model = Pemesanan
        fields = ['nama_pelanggan','jenis_kelamin_pelanggan','alamat_pelanggan','no_telepon_pelanggan','no_ktp_pelanggan','foto_ktp', 'tanggal_checkin', 'tanggal_checkout', 'metode_pembayaran']
        widgets = {
            
            'nama_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin_pelanggan': forms.Select(attrs={'class': 'form-control'}),
            'alamat_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
            'no_telepon_pelanggan': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan', 'class': 'form-control'}),
            'no_ktp_pelanggan': forms.TextInput(attrs={'pattern': '[0-9]*', 'title': 'Hanya angka yang diperbolehkan', 'class': 'form-control'}), 
            'foto_ktp': forms.FileInput(attrs={'class': 'form-control'}), 
            
            # 'pelanggan': forms.HiddenInput(),
            'tanggal_checkin': forms.DateInput(attrs={'class': 'form-control'}),
            'tanggal_checkout': forms.DateInput(attrs={'class': 'form-control'}),
            'metode_pembayaran': forms.Select(attrs={'class': 'form-control'}),
            
        }

    # def __init__(self, *args, **kwargs):
    #     jenis_kamar = kwargs.pop('jenis_kamar', None)
    #     super().__init__(*args, **kwargs)
    #     self.set_no_kamar_choices(jenis_kamar)

    # def set_no_kamar_choices(self, jenis_kamar):
    #     self.fields['no_kamar_id'].queryset = Nomor_Kamar.objects.filter(jenis_kamar=jenis_kamar)  

#-----------------Kelola Pembayarann-----------------------

class FormPembayaran(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['bukti_pembayaran']
        widgets = {
            'bukti_pembayaran': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FormPengeluaran(forms.ModelForm):
    class Meta:
        model = Pengeluaran
        fields = '__all__'
        widgets = {
            'tanggal_pengeluaran': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'keterangan_pengeluaran': forms.Textarea(attrs={'class': 'form-control'}),
            'jumlah_pengeluaran': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormKunci(forms.ModelForm):
    class Meta:
        model = Kunci
        fields = ( 'pemesanan', 'ktp_status', 'kunci_status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ktp_status'].widget = forms.RadioSelect(choices=Kunci.KTP_CHOICES)
        self.fields['kunci_status'].widget = forms.RadioSelect(choices=Kunci.KUNCI_CHOICES)