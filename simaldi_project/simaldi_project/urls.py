"""
URL configuration for simaldi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beranda.views import *
from django.contrib.auth.views import LoginView, LogoutView
from beranda import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from beranda.views import mark_as_read
from django.urls import path, re_path

urlpatterns = [
    
    # --------------Halaman Utama-------------------
    
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('beranda/', views.index, name= 'index'),
    path('tentang/', views.tentang, name= 'tentang'),
    path('kamar/', views.kamar, name= 'kamar'),
    path('fasilitas/', views.fasilitas, name= 'fasilitas'),
    path('kontak/', views.kontak, name= 'kontak'),
    
    # -------------------Registrasi--------------------
    
    path('login/', views.login_view, name='loginview'),
    path('daftar/', views.register, name='register'),
    path('logout/', views.logoutview, name='logoutview'),
    path('lupa_password/', views.lupa_password, name="lupa_password"),
    path('ganti_password/<token>/', views.ganti_password, name="ganti_password"),
    
    # ----------------Halaman Admin---------------------
    
    path('dashboard_admin/', views.dbadmin, name= 'dbadmin'),
    
    # --------------------Kelola Akun--------------------
    
    path('kelola_akun/', views.daftar_akun, name= 'daftar_akun'),
    path('tambah_akun/', views.tambah_akun, name= 'tambah_akun'),
    path('ubah_akun/<int:user_id>/', views.ubah_akun, name= 'ubah_akun'),
    path('hapus_akun/<int:user_id>/', views.hapus_akun, name='hapus_akun'),
    
    # --------------------Kelola Pelanggan--------------------
    
    path('kelola_pelanggan/', views.daftar_pelanggan, name= 'daftar_pelanggan'),
    path('tambah_pelanggan/', views.tambah_pelanggan, name= 'tambah_pelanggan'),
    path('ubah_pelanggan/<int:pelanggan_id>/', views.ubah_pelanggan, name= 'ubah_pelanggan'),
    path('hapus_pelanggan/<int:pelanggan_id>/', views.hapus_pelanggan, name='hapus_pelanggan'),
    
     # --------------------Kelola Nomor_Kamar--------------------
    
    path('kelola_nomor_kamar/', views.kelola_nomor_kamar, name='kelola_nomor_kamar'),
    path('tambah_nomor_kamar/', views.tambah_nomor_kamar, name='tambah_nomor_kamar'),
    path('ubah_nomor_kamar/<int:nomor_kamar_id>/', views.ubah_nomor_kamar, name='ubah_nomor_kamar'),
    
    
    # --------------------Kelola Kamar--------------------
    
    path('kelola_kamar/', views.daftar_kamar, name='daftar_kamar'),
    path('tambah_kamar/', views.tambah_kamar, name='tambah_kamar'),
    path('ubah_kamar/<int:kamar_id>/', views.ubah_kamar, name='ubah_kamar'),
    path('hapus_kamar/<int:kamar_id>/', views.hapus_kamar, name='hapus_kamar'),
    
    # --------------------Kelola Pemesanan--------------------
    
    path('kelola_pemesanan/', views.kelola_pemesanan, name= 'kelola_pemesanan'),
    path('tandai_sudah_dibaca/', views.tandai_sudah_dibaca, name='tandai_sudah_dibaca'),
    path('tambah_pemesanan/', views.tambah_pemesanan, name= 'tambah_pemesanan'),
    path('ubah_pemesanan/<int:pemesanan_id>/', views.ubah_pemesanan, name= 'ubah_pemesanan'),
    path('hapus_pemesanan/<int:pemesanan_id>/', views.hapus_pemesanan, name='hapus_pemesanan'),
    path('setuju/<int:id>/', views.setuju, name='setuju'),
    path('tolak/<int:id>/', views.tolak, name='tolak'),
    
    # --------------------Kelola Pembayaran--------------------
    
    path('kelola_pembayaran/', views.kelola_pembayaran, name= 'kelola_pembayaran'),
    path('tambah_pembayaran/', views.tambah_pembayaran, name= 'tambah_pembayaran'),
    path('ubah_pembayaran/<int:pembayaran_id>/', views.ubah_pembayaran, name= 'ubah_pembayaran'),
    path('hapus_pembayaran/<int:pembayaran_id>/', views.hapus_pembayaran, name='hapus_pembayaran'),
    path('setuju_pembayaran/<int:pembayaran_id>/', views.setuju_pembayaran, name='setuju_pembayaran'),
    path('tolak_pembayaran/<int:pembayaran_id>/', views.tolak_pembayaran, name='tolak_pembayaran'),
    
     # --------------------Kelola Kamar--------------------
    
    path('kelola_kunci/', views.daftar_kunci, name='daftar_kunci'),
    path('tambah_kunci/', views.tambah_kunci, name='tambah_kunci'),
    path('ubah_kunci/<int:kunci_id>/', views.ubah_kunci, name='ubah_kunci'),
    
    # -------------------Halaman Manajer------------------------
    
    path('dashboard_manajer/', views.manajer, name= 'manajer'),
    
    # ---------------------Kelola Absensi----------------------
    
    path('lihat_presensi/', views.lihat_presensi, name= 'lihat_presensi'),
    
    # --------------------Kelola Laporan--------------------
    
    path('preview/<str:jenis>/', views.preview_laporan, name='preview_laporan'),
    path('cetak/<str:jenis>/', views.cetak_laporan, name='cetak_laporan'),
    path('tampilkan_data_terfilter/<str:jenis>/', views.tampilkan_data_terfilter, name='tampilkan_data_terfilter'),
    path('kelola_laporan/', views.daftar_laporan, name= 'daftar_laporan'),
    
    # --------------------Kelola Pegawai--------------------
    
    path('kelola_pegawai/', views.daftar_pegawai, name= 'daftar_pegawai'),
    path('tambah_pegawai/', views.tambah_pegawai, name= 'tambah_pegawai'),
    path('ubah_pegawai/<int:pegawai_id>/', views.ubah_pegawai, name= 'ubah_pegawai'),
    path('hapus_pegawai/<int:pegawai_id>/', views.hapus_pegawai, name='hapus_pegawai'),
    
    # --------------------Halaman Pegawai--------------------
    
    path('dashboard_pegawai/', views.pegawai, name= 'pegawai'),
    
    # --------------------Presensi--------------------
    
    path('presensi_pegawai/', views.presensi, name= 'presensi'),
    path('presensi_sukses/', views.presensisukses, name= 'presensisukses'),
    
    # --------------------Halaman Pelanggan--------------------
    
    path('dashboard_pelanggan/', views.beranda_pelanggan, name= 'berandapelanggan'),
    path('kamar_pelanggan/', views.kamar_pelanggan, name= 'kamarpelanggan'),
    # path('form_isidatadiri/<int:kamar_id>/', views.form_isidatadiri, name='form_isidatadiri'),
    path('form_pemesanan/<int:kamar_id>/', views.form_pemesanan, name='form_pemesanan'),
    path('pesanan_saya/', views.pesanan_saya, name= 'pesanan_saya'),
    path('form_pembayaran/<int:pemesanan_id>/', views.form_pembayaran, name= 'form_pembayaran'),
    path('cetak_bukti_pesanan/<int:pemesanan_id>/', views.cetak_bukti_pembayaran, name='cetak_bukti_pembayaran'),
    path('cetak_pesanan/<int:pemesanan_id>/', views.cetak_pesanan, name='cetak_pesanan'),
    re_path(r'^mark_as_read/$', mark_as_read, name='mark_as_read'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
