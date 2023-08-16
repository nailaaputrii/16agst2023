from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import date
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
import uuid, random, string
from django.core.exceptions import ValidationError
from django.db.models import Q



# -----------------Registrasi------------------------

class User(AbstractUser):
   ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Pelanggan', 'Pelanggan'),
        ('Pegawai', 'Pegawai'),
        ('Manajer', 'Manajer'),
    )
   role = models.CharField(max_length=20, choices=ROLE_CHOICES)
   status = models.CharField(max_length=10, choices=(('Aktif', 'Aktif'), ('Nonaktif', 'Nonaktif')), default='Aktif')
   def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lupa_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
# --------------------Kelola Pelanggan-----------------------------
    
# class Pelanggan(models.Model):
#     JENIS_KELAMIN_PELANGGAN_CHOICES = [
#         ('Laki-laki', 'Laki-laki'),
#         ('Perempuan', 'Perempuan'),
#     ]
    
#     nama_pelanggan = models.CharField(max_length=255)
#     jenis_kelamin_pelanggan = models.CharField(max_length=50, choices=JENIS_KELAMIN_PELANGGAN_CHOICES)
#     alamat_pelanggan = models.CharField(max_length=255)
#     no_telepon_pelanggan = models.CharField(max_length=15, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')])
#     no_ktp_pelanggan = models.CharField(max_length=16, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')])
#     foto_ktp = models.ImageField(upload_to='ktp_images', null=True, blank=True)
#     tanggal_input = models.DateField(auto_now_add=True)
    

#     def __str__(self):
#         return self.nama_pelanggan
        
#-----------------Kelola Kamar----------------------

class Nomor_Kamar(models.Model):
    JENIS_KAMAR_CHOISES = [
        ('VVIP', 'VVIP'),
        ('Executive Class', 'Executive Class'),
        ('Superior Room', 'Superior Room'),
        ('Deluxe Room', 'Deluxe Room'),
        ('Family Room', 'Family Room'),
        ('Single Room', 'Single Room'),
    ]
    
    jenis_kamar = models.CharField(max_length=50, choices=JENIS_KAMAR_CHOISES)
    no_kamar = models.CharField(max_length=50, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')])

    def __str__(self):
        return self.no_kamar

class Kamar(models.Model):
    jenis_kamar = models.ForeignKey(Nomor_Kamar, on_delete=models.CASCADE, null=True, related_name='kamar')
    kapasitas = models.IntegerField(null=True)
    kasur = models.CharField(max_length=50, null=True)
    fasilitas_lainnya = models.CharField(max_length=255, null=True, blank=True)
    tarif = models.IntegerField(null=True)
    gambar_kamar = models.ImageField(upload_to='kamar_images', null=True, blank=True)

    def __str__(self):
        return str(self.tarif)

# ---------------Kelola Pemesanan----------------------

class Pemesanan(models.Model):
    
    JENIS_KELAMIN_PELANGGAN_CHOICES = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ]
    
    nama_pelanggan = models.CharField(max_length=255, null=True)
    jenis_kelamin_pelanggan = models.CharField(max_length=50, choices=JENIS_KELAMIN_PELANGGAN_CHOICES, null=True)
    alamat_pelanggan = models.CharField(max_length=255, null=True)
    no_telepon_pelanggan = models.CharField(max_length=15, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')], null=True)
    no_ktp_pelanggan = models.CharField(max_length=16, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')], null=True)
    foto_ktp = models.ImageField(upload_to='foto_ktp', null=True, blank=True)
    tanggal_input = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_pelanggan
    
    METODE_PEMBAYARAN_CHOICES = [
        ('Transfer Via BRI', 'Transfer Via BRI'),
        ('Bayar Di Tempat', 'Bayar Di Tempat'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]
    
    STATUS_KAMAR_CHOICES = [
        ('Full Booked', 'Full Booked'),
        ('Booked', 'Booked'),
        ('Empty Room', 'Empty Room'),
        ('Booking Completed', 'Booking Completed'),
        ('Booking Rejected', 'Booking Rejected'),
    ]

    def generate_uuid():
        return str(uuid.uuid4().fields[-1])[:8]
    
    id_pemesanan = models.CharField(default=generate_uuid, max_length=8, editable=False)
    id_pembayaran = models.CharField(default=generate_uuid, max_length=32, editable=False)
    # pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, null=True)
    kamar = models.ForeignKey(Kamar, on_delete=models.CASCADE, null=True, related_name='pemesanan')
    no_kamar_id = models.ForeignKey(Nomor_Kamar, on_delete=models.CASCADE, null=True)
    tanggal_checkin = models.DateField(default=timezone.now())
    tanggal_checkout = models.DateField(default=timezone.now())
    metode_pembayaran = models.CharField(max_length=50, choices=METODE_PEMBAYARAN_CHOICES)
    jumlah_pembayaran = models.IntegerField(null=True, default=0)
    status_konfirmasi = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    waktu_konfirmasi = models.DateTimeField(null=True)
    status_kamar = models.CharField(max_length=20, choices=STATUS_KAMAR_CHOICES, default='Empty Room')

    def save(self, *args, **kwargs):
        if not self.no_kamar_id:
            available_room = self.get_available_room()

            if available_room:
                self.no_kamar_id = available_room
                self.status_kamar = 'Booked'
            else:
                raise Exception("Tidak ada nomor kamar yang tersedia untuk jenis kamar ini pada tanggal check-in yang diberikan.")

        if self.status_konfirmasi == 'Disetujui':
            if self.metode_pembayaran == 'Transfer Via BRI':
                if not self.waktu_konfirmasi:
                    self.waktu_konfirmasi = timezone.now()
                self.status_kamar = 'Booked'
            elif self.metode_pembayaran == 'Bayar Di Tempat':
                self.status_kamar = 'Full Booked'
        elif self.status_konfirmasi == 'Ditolak':
            self.status_kamar = 'Booking Rejected'
        else:  # Tambahkan kondisi untuk status_konfirmasi 'Pending'
            self.status_kamar = 'Empty Room'
        
        jenis_kamar = self.kamar.jenis_kamar  # Akses jenis_kamar dari objek Kamar
        jenis_kamar.save()  # Simpan kembali objek Jenis_Kamar

        selisih_hari = (self.tanggal_checkout - self.tanggal_checkin).days
        self.jumlah_pembayaran = selisih_hari * self.kamar.tarif
            
        super().save(*args, **kwargs)

            
# -----------------Notifikasi------------------

class Notifikasi(models.Model):
    pengirim = models.ForeignKey(User, on_delete=models.CASCADE)
    penerima = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifikasi_penerima')
    pesan = models.TextField()
    dibaca = models.BooleanField(default=False)

    def __str__(self):
        return self.pesan

class Notifikasiadmin(models.Model):
    pemesanan = models.ForeignKey('Pemesanan', on_delete=models.CASCADE)
    pesan = models.CharField(max_length=255)
    dibaca = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pesan
    
class Notification(models.Model):
    pemesanan = models.ForeignKey('Pemesanan', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def mark_as_read(self):
        self.is_read = True
        self.save()

    def __str__(self):
        return self.message
            
#-------------------Kelola Pembayaran---------------------------

class Pembayaran(models.Model):
    STATUS_PEMBAYARAN_CHOICES = [
        ('Lunas', 'Lunas'),
        ('Sudah Dibayar', 'Sudah Dibayar'),
    ]
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Disetujui','Disetujui'),
        ('Ditolak','Ditolak'),
    ]
    tanggal_pembayaran = models.DateField(auto_now_add=True)
    bukti_pembayaran = models.ImageField(upload_to='bukti_pembayaran/', null=True)
    status_pembayaran = models.CharField(max_length=50, choices=STATUS_PEMBAYARAN_CHOICES, default='Belum Dibayar')
    pemesanan = models.ForeignKey(Pemesanan, on_delete=models.CASCADE, null=True)
    jumlah_pembayaran = models.IntegerField(null=True, default=0)
    status_konfirmasi_pembayaran = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        if self.status_konfirmasi_pembayaran == 'Disetujui':
            self.status_pembayaran = 'Lunas'
            self.pemesanan.status_kamar = 'Full Booked'
            self.pemesanan.save()
        else:
            self.status_pembayaran = 'Sudah Dibayar'

        self.pemesanan.kamar.jenis_kamar.save()
        self.jumlah_pembayaran = self.pemesanan.jumlah_pembayaran

        super().save(*args, **kwargs)
        
class Notifikasipembayaran(models.Model):
    pembayaran = models.ForeignKey('Pembayaran', on_delete=models.CASCADE)
    pesan = models.CharField(max_length=255)
    dibaca = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pesan

class Kunci(models.Model):
    KTP_CHOICES = (
        ('submitted', 'Submitted'),
        ('not_submitted', 'Not Submitted'),
    )

    KUNCI_CHOICES = (
        ('delivered', 'Delivered'),
        ('not_delivered', 'Not Delivered'),
    )
    pemesanan = models.ForeignKey(Pemesanan, on_delete=models.CASCADE, null=True)
    ktp_status = models.CharField(max_length=15, choices=KTP_CHOICES, default='not_submitted')
    kunci_status = models.CharField(max_length=15, choices=KUNCI_CHOICES, default='not_delivered')
    waktu_input = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.waktu_input = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Kunci - {self.pelanggan.nama_pelanggan}"     
     
class Pengeluaran(models.Model):
    pembayaran = models.ForeignKey(Pembayaran, on_delete=models.CASCADE, null=True)
    tanggal_pengeluaran = models.DateField()
    keterangan_pengeluaran = models.CharField(max_length=255)
    jumlah_pengeluaran = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.tanggal_pengeluaran

# ------------------------Kelola Keuangan--------------------------------
     
class Keuangan(models.Model):
    tanggal = models.DateField()
    kategori = models.CharField(max_length=100, choices=[('pemasukan', 'Pemasukan'), ('pengeluaran', 'Pengeluaran')])
    keterangan = models.TextField()
    pembayaran = models.ForeignKey(Pembayaran, on_delete=models.CASCADE, null=True)
    pengeluaran = models.ForeignKey(Pengeluaran, on_delete=models.CASCADE, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.kategori} - {self.tanggal}"

    def save(self, *args, **kwargs):
        if self.saldo is None:
            self.saldo = 0

        if self.kategori == 'pemasukan':
            self.pengeluaran = None
            self.saldo += (self.pembayaran.jumlah_pembayaran or 0)
        elif self.kategori == 'pengeluaran':
            self.pembayaran = None
            self.saldo -= (self.pengeluaran.jumlah_pengeluaran or 0)
        super().save(*args, **kwargs)

        # Update saldo berdasarkan saldo sebelumnya
        if self.pk:
            previous_keuangan = Keuangan.objects.filter(tanggal__lt=self.tanggal).order_by('-tanggal').first()
            if previous_keuangan:
                self.saldo += previous_keuangan.saldo
        
# ---------------Presensi----------------------------

class Jadwal(models.Model):
    SHIFT_CHOICES = [
        ('Pagi', 'Pagi'),
        ('Siang', 'Siang'),
        ('Malam', 'Malam'),
    ]
    shift = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    jam_masuk = models.TimeField()
    jam_keluar = models.TimeField()
    
    def __str__(self):
        return self.shift

class Pegawai(models.Model):
    GENDER_CHOICES = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ]
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=50, choices=GENDER_CHOICES)
    alamat = models.CharField(max_length=255)
    posisi = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=15, validators=[RegexValidator(r'^[0-9]*$', 'Hanya angka yang diperbolehkan')])
    shift = models.ForeignKey(Jadwal, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nama

class Presensi(models.Model):
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, default=1)
    tanggal = models.DateField(auto_now_add=True)
    jam_masuk = models.TimeField(auto_now_add=True)
    bukti_absen = models.ImageField(upload_to='absen/', null=True, blank=True)
    url = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        jadwal_masuk = self.pegawai.shift.jam_masuk
        jam_masuk_sekarang = datetime.now().time()

        if datetime.combine(date.today(), jam_masuk_sekarang) > datetime.combine(date.today(), jadwal_masuk):
            self.status = "Terlambat"
        else:
            self.status = "Tepat waktu"

        self.url = self.bukti_absen.url if self.bukti_absen else ''

        super().save(*args, **kwargs)

    def __str__(self):
        return self.url
