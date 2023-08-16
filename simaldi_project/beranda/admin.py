from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Kamar, Pegawai, Keuangan, Jadwal, Presensi, Pemesanan, Pembayaran, Pengeluaran, Kunci

# ---------------Registrasi--------------------

admin.site.register(User)

# ---------------Kelola Kamar--------------------

@admin.register(Kamar)
class KamarAdmin(admin.ModelAdmin):
    list_display = ['jenis_kamar', 'kapasitas', 'kasur', 'tarif','gambar_kamar']
    list_filter = ['kapasitas']
    search_fields = ['jenis_kamar', 'kasur']
    ordering = ['jenis_kamar']
    list_per_page = 10

    def display_gambar_kamar(self, obj):
        return obj.gambar_kamar.url if obj.gambar_kamar else ''
    display_gambar_kamar.short_description = 'Gambar Kamar'

# ---------------Kelola Pelanggan--------------------

# class PelangganAdmin(admin.ModelAdmin):
#     list_display = ['nama_pelanggan', 'jenis_kelamin_pelanggan', 'alamat_pelanggan', 'no_telepon_pelanggan', 'no_ktp_pelanggan','foto_ktp']
#     list_filter = ['jenis_kelamin_pelanggan']
#     search_fields = ['nama_pelanggan', 'no_ktp_pelanggan']

# admin.site.register(Pelanggan, PelangganAdmin)

#----------------Kelola Pemesanan-------------------

@admin.register(Pemesanan)
class PemesananAdmin(admin.ModelAdmin):
    list_display = ['nama_pelanggan', 'jenis_kelamin_pelanggan', 'alamat_pelanggan', 'no_telepon_pelanggan', 'no_ktp_pelanggan','foto_ktp', 'kamar', 'no_kamar_id', 'tanggal_checkin', 'tanggal_checkout', 'metode_pembayaran', 'status_konfirmasi']
    list_filter = ['status_konfirmasi']
    search_fields = ['pelanggan__nama', 'kamar__nomor_kamar', 'no_kamar_id__nomor_kamar']
    readonly_fields = ['jumlah_pembayaran', 'waktu_konfirmasi']

    fieldsets = (
        (None, {
            'fields': ('pelanggan', 'kamar', 'no_kamar_id')
        }),
        ('Tanggal Pemesanan', {
            'fields': ('tanggal_checkin', 'tanggal_checkout')
        }),
        ('Informasi Tambahan', {
            'fields': ('metode_pembayaran', 'jumlah_pembayaran', 'status_konfirmasi', 'waktu_konfirmasi')
        }),
    )

#----------------Kelola Pembayaran-------------------

@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = ['pemesanan', 'tanggal_pembayaran', 'status_pembayaran', 'status_konfirmasi_pembayaran']
    list_filter = ['status_pembayaran', 'status_konfirmasi_pembayaran']
    search_fields = ['pemesanan__pelanggan__nama']
    ordering = ['-tanggal_pembayaran']
    list_per_page = 10
    
    def display_bukti_pembayaran(self, obj):
        return obj.bukti_pembayaran.url if obj.bukti_pembayaran else ''
    display_bukti_pembayaran.short_description = 'Bukti Pembayaran'

# ---------------Kelola Pegawai--------------------

@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_kelamin', 'alamat', 'posisi', 'no_telepon', 'shift')
    list_filter = ('jenis_kelamin', 'posisi')
    search_fields = ('nama', 'posisi')

# ---------------Kelola Keuangan--------------------

class KeuanganAdmin(admin.ModelAdmin):
    list_display = ['tanggal','kategori','keterangan','pembayaran','pengeluaran','saldo']
    search_fields = ['tanggal','kategori']
    list_filter = ['kategori']
    list_per_page = 4

admin.site.register(Keuangan, KeuanganAdmin)

# --------------Presensisi--------------------

class ShiffAdmin(admin.ModelAdmin):
    list_display = ['shift', 'jam_masuk', 'jam_keluar']
    search_fields = ['shift']
    list_filter = ['shift']
    list_per_page = 4

admin.site.register(Jadwal, ShiffAdmin)

@admin.register(Presensi)
class PresensiAdmin(admin.ModelAdmin):
    list_display = ('pegawai', 'tanggal', 'jam_masuk', 'status','bukti_absen')
    list_filter = ('tanggal', 'status')
    search_fields = ('pegawai__nama',)
    readonly_fields = ('tanggal', 'jam_masuk', 'status')
    
@admin.register(Pengeluaran)
class PengeluaranAdmin(admin.ModelAdmin):
    list_display = ('tanggal_pengeluaran', 'keterangan_pengeluaran', 'jumlah_pengeluaran')
    search_fields = ('tanggal_pengeluaran',)
    
@admin.register(Kunci)
class KunciAdmin(admin.ModelAdmin):
    list_display = ( 'pemesanan', 'ktp_status', 'kunci_status', 'waktu_input')
    list_filter = ('ktp_status', 'kunci_status', 'waktu_input')