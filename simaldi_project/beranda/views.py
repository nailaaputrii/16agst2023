from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from beranda.models import User
from .models import Kamar, Pegawai, Keuangan, Presensi, Pemesanan, Profile, Pembayaran, Notifikasi, Pengeluaran, Nomor_Kamar, Kunci, Notification, Notifikasiadmin, Notifikasipembayaran
from .forms import LoginForm, SignUpForm, FormKamar, FormPegawai, FormKeuangan, FormPresensi, FormPemesanan, FormPembayaran, FormPengeluaran, FormNomorKamar, FormKunci
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from django.utils import timezone
from .helpers import send_lupa_password_mail
import uuid
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.db.models import Sum
from django.http import Http404
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from datetime import datetime, date
import base64
from django.core.files.base import ContentFile
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from django.db.models import Q


# ------------------------Halaman Utama----------------------

def index(request):
    return render(request, 'index.html')

def tentang(request):
    return render(request, 'tentang.html')

def kamar(request):
    return render(request, 'kamar.html')

def fasilitas(request):
    return render(request, 'fasilitas.html')

def kontak(request):
    return render(request, 'kontak.html')

# --------------Registrasi---------------

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Akun berhasil dibuat.')
            return redirect('loginview')
        else:
            messages.success(request, 'Form tidak valid.')
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.status == 'Nonaktif':
                    # Akun nonaktif, berikan pesan kesalahan
                    form.add_error(None, 'Akun tidak aktif.')
                else:
                    login(request, user)
                    # Redirect sesuai dengan peran pengguna
                    if user.role == 'Admin':
                        return redirect('dbadmin')
                    elif user.role == 'Pelanggan':
                        return redirect('berandapelanggan')
                    elif user.role == 'Pegawai':
                        return redirect('pegawai')
                    elif user.role == 'Manajer':
                        return redirect('manajer')
            else:
                # Username atau password salah
                form.add_error(None, 'Username atau password salah.')
        else:
            messages.success(request, 'Form validasi error.')

    return render(request, 'login.html', {'form': form, 'msg': msg})

def logoutview(request):
    logout(request)
    request.session.flush()
    return redirect('loginview')

def ganti_password(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token=token).first()
        if not profile_obj:
            raise Http404("Profil tidak ditemukan")

        context = {'user_id': profile_obj.user.id}
        if request.method == 'POST':
            newpassword = request.POST.get('newpassword')
            confirmpassword = request.POST.get('confirmpassword')
            user_id = request.POST.get('user_id')
            
            if user_id is None:
                messages.success(request='User tidak ditemukan')
                return redirect(f'/ganti_password/{token}/')
            if newpassword != confirmpassword:
                messages.success(request='Password tidak sama.')
                return redirect(f'/ganti_password/{token}/')
            
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(newpassword)
            user_obj.save()
            return redirect('loginview')

    except Exception as e:
        print(e)
        raise Http404("Terjadi kesalahan")

    return render(request, 'ganti_password.html', context)

def lupa_password(request):
    try:
        if request.method == 'POST':
            username=request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request='Tidak ada akun dengan username ini.')
                return redirect('lupa_password')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_lupa_password_mail(user_obj, token)
            messages.success(request='Email telah dikirim, silahkan dicek.')
            return redirect('lupa_password')
        
    except Exception as e:
        print(e)
    return render(request, 'lupa_password.html')

# ----------------------Halaman Admin---------------------------

def dbadmin(request):
    jumlah_pelanggan = Pemesanan.objects.count()
    jumlah_pemesanan = Pemesanan.objects.count()
    total_pembayaran = Pemesanan.objects.aggregate(total=Sum('jumlah_pembayaran'))
    return render(request, 'admin.html', { 'jumlah_pelanggan': jumlah_pelanggan,'jumlah_pemesanan': jumlah_pemesanan, 'total_pembayaran': total_pembayaran['total']})


# ===================Kelola Akun=================================

def daftar_akun(request):
    users = User.objects.annotate(jumlah_user=Count('id'))
    return render(request, 'kelola_akun.html', {'users': users})

def tambah_akun(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil ditambahkan.')
            return redirect('daftar_akun') 
    else:
        form = SignUpForm()
    
    return render(request, 'tambah_akun.html', {'form': form})

def ubah_akun(request, user_id):
    user = get_object_or_404(User, id= user_id)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil diubah.')
            return redirect('daftar_akun')
    else:
        form = SignUpForm(instance=user)
    return render(request, 'edit_akun.html', {'form': form})

def hapus_akun(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'Akun berhasil dihapus.')
    return redirect('daftar_akun')

# ==========================Kelola Kamar==========================

def kelola_nomor_kamar(request):
    nomor_kamar_list = Nomor_Kamar.objects.all()
    context = {
        'nomor_kamar_list': nomor_kamar_list
    }
    return render(request, 'kelola_nomorkamar.html', context)

def tambah_nomor_kamar(request):
    if request.method == 'POST':
        form = FormNomorKamar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data nomor kamar berhasil ditambahkan.')
            return redirect('kelola_nomor_kamar')
    else:
        form = FormNomorKamar()
    return render(request, 'tambah_nomorkamar.html', {'form': form})

def ubah_nomor_kamar(request, nomor_kamar_id):
    nomor_kamar = get_object_or_404(Nomor_Kamar, id=nomor_kamar_id)
    if request.method == 'POST':
        form = FormNomorKamar(request.POST, request.FILES, instance=nomor_kamar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data nomor kamar berhasil diubah.')
            return redirect('kelola_nomor_kamar')
    else:
        form = FormNomorKamar(instance=nomor_kamar)
    return render(request, 'edit_nomorkamar.html', {'form': form})

def daftar_kamar(request):
    kamar_list = Kamar.objects.all()
    return render(request, 'kelola_kamar.html', {'kamar_list': kamar_list})

def tambah_kamar(request):
    if request.method == 'POST':
        form = FormKamar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kamar berhasil ditambahkan.')
            return redirect('daftar_kamar')
    else:
        form = FormKamar()
    return render(request, 'tambah_kamar.html', {'form': form})

def ubah_kamar(request, kamar_id):
    kamar = get_object_or_404(Kamar, id=kamar_id)
    if request.method == 'POST':
        form = FormKamar(request.POST, request.FILES, instance=kamar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kamar berhasil diubah.')
            return redirect('daftar_kamar')
    else:
        form = FormKamar(instance=kamar)
    return render(request, 'edit_kamar.html', {'form': form})

def hapus_kamar(request, kamar_id):
    kamar = get_object_or_404(Kamar, id=kamar_id)
    kamar.delete()
    messages.success(request, 'Data kamar berhasil dihapus.')
    return redirect('daftar_kamar')

# ==============================Kelola Pelanggan=====================================

def daftar_pelanggan(request):
    pelangganss = Pemesanan.objects.annotate(jumlah_pelanggan=Count('id'))
    return render(request, 'kelola_pelanggan.html', {'Pelangganss': pelangganss})

def tambah_pelanggan(request):
    if request.method == 'POST':
        form = FormPemesanan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pelanggan berhasil ditambahkan.')
            return redirect('daftar_pelanggan')
    else:
        form = FormPemesanan()
    return render(request, 'tambah_pelanggan.html', {'form': form})

def ubah_pelanggan(request, pelanggan_id):
    pelanggan = Pemesanan.objects.get(id=pelanggan_id)
    if request.method == 'POST':
        form = FormPemesanan(request.POST, instance=pelanggan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pelanggan berhasil diubah.')
            return redirect('daftar_pelanggan')
    else:
        form = FormPemesanan(instance=pelanggan)
    return render(request, 'edit_pelanggan.html', {'form': form})

def hapus_pelanggan(request, pelanggan_id):
    pelanggan = Pemesanan.objects.get(id=pelanggan_id)
    pelanggan.delete()
    messages.success(request, 'Data pelanggan berhasil ditambahkan dihapus.')
    return redirect('daftar_pelanggan')

# =========================Kelola Pemesenan===========================

def kelola_pemesanan(request):
    jumlah_pemesanan = Pemesanan.objects.count()
    pemesanan_list = Pemesanan.objects.all()
    notifications = Notifikasiadmin.objects.filter(dibaca=False)
    unread_count = notifications.count()
    return render(request, 'kelola_pemesanan.html', {
        'pemesanan_list': pemesanan_list,
        'jumlah_pemesanan': jumlah_pemesanan,
        'notifications': notifications,
        'unread_count': unread_count
    })
    
def tandai_sudah_dibaca(request):
    if request.method == 'POST':
        notifikasi_id = request.POST.get('notifikasi_id')
        notifikasi = Notifikasiadmin.objects.get(id=notifikasi_id)
        notifikasi.dibaca = True
        notifikasi.save()
        return redirect('kelola_pemesanan')

def tambah_pemesanan(request):
    if request.method == 'POST':
        form = FormPemesanan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pemesanan berhasil ditambahkan.')
            return redirect('kelola_pemesanan')
    else:
        form = FormPemesanan()
    context = {'form': form}
    return render(request, 'tambah_pemesanan.html', context)

def ubah_pemesanan(request, pemesanan_id):
    pemesanan = Pemesanan.objects.get(id=pemesanan_id)
    if request.method == 'POST':
        form = FormPemesanan(request.POST, instance=pemesanan)
        if form.is_valid():
            messages.success(request, 'Data pemesanan berhasil diubah.')
            form.save()
            return redirect('kelola_pemesanan')
    else:
        form = FormPemesanan(instance=pemesanan)
    context = {'form': form}
    return render(request, 'edit_pemesanan.html', context)

def hapus_pemesanan(request, pemesanan_id):
    pemesanan = Pemesanan.objects.get(id=pemesanan_id)
    pemesanan.delete()
    messages.success(request, 'Data pemesanan berhasil dihapus.')
    return redirect('kelola_pemesanan')

# =========================Kelola Pembayaran===========================

def kelola_pembayaran(request):
    pembayarans = Pembayaran.objects.all()
    notifications = Notifikasipembayaran.objects.filter(dibaca=False)
    jumlah_belum_dibaca = notifications.count()
    print(jumlah_belum_dibaca)
    return render(request, 'kelola_pembayaran.html', {
        'pembayarans': pembayarans,
        'notifications': notifications,
        'jumlah_belum_dibaca': jumlah_belum_dibaca
    })

def tambah_pembayaran(request):
    if request.method == 'POST':
        form = FormPembayaran(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pembayaran berhasil ditambahkan.')
            return redirect('kelola_pembayaran')
    else:
        form = FormPembayaran()
    return render(request, 'tambah_pembayaran.html', {'form': form})

def ubah_pembayaran(request, pembayaran_id):
    pembayaran = Pembayaran.objects.get(id=pembayaran_id)
    if request.method == 'POST':
        form = FormPembayaran(request.POST, instance=pembayaran)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pembayaran berhasil diubah.')
            return redirect('kelola_pembayaran')
    else:
        form = FormPembayaran(instance=pembayaran)
    return render(request, 'edit_pembayaran.html', {'form': form})

def hapus_pembayaran(request, pembayaran_id):
    pembayaran = Pembayaran.objects.get(id=pembayaran_id)
    pembayaran.delete()
    messages.success(request, 'Data pembayaran berhasil dihapus.')
    return redirect('kelola_pembayaran')

# ------------------------Halaman Manajer--------------------------------

def manajer(request):
    jumlah_tepat_waktu = Presensi.objects.filter(status='Tepat waktu').count()
    jumlah_terlambat = Presensi.objects.filter(status='Terlambat').count()
    return render(request, 'manajer.html', {'jumlah_tepat_waktu': jumlah_tepat_waktu, 'jumlah_terlambat': jumlah_terlambat})

# ===========================Kelola Pegawai==============================

def daftar_pegawai(request):
    pegawais = Pegawai.objects.all()
    jumlah_tepat_waktu = Presensi.objects.filter(status='Tepat waktu').count()
    jumlah_terlambat = Presensi.objects.filter(status='Terlambat').count()
    return render(request, 'kelola_pegawai.html', {'pegawais': pegawais, 'jumlah_tepat_waktu': jumlah_tepat_waktu, 'jumlah_terlambat': jumlah_terlambat})

def tambah_pegawai(request):
    if request.method == 'POST':
        form = FormPegawai(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pegawai berhasil ditambahkan.')
            return redirect('daftar_pegawai')
    else:
        form = FormPegawai()
    return render(request, 'tambah_pegawai.html', {'form': form})

def ubah_pegawai(request, pegawai_id):
    pegawai = Pegawai.objects.get(id=pegawai_id)
    if request.method == 'POST':
        form = FormPegawai(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pegawai berhasil diubah.')
            return redirect('daftar_pegawai')
    else:
        form = FormPegawai(instance=pegawai)
    return render(request, 'edit_pegawai.html', {'form': form})

def hapus_pegawai(request, pegawai_id):
    pegawai = Pegawai.objects.get(id=pegawai_id)
    pegawai.delete()
    messages.success(request, 'Data pegawai berhasil dihapus.')
    return redirect('daftar_pegawai')

# ===============================Kelola Laporan===============================

def daftar_laporan(request):
    Pelangganss = Pemesanan.objects.all()
    return render(request, 'kelola_laporan.html', {'Pelangganss': Pelangganss})

def get_nama_laporan(jenis):
    if jenis == 'pelanggan':
        return 'Laporan Data Pelanggan'
    elif jenis == 'pemesanan':
        return 'Laporan Data Pemesanan'
    elif jenis == 'pembayaran':
        return 'Laporan Data Pembayaran'
    else:
        return 'Laporan'

def preview_laporan(request, jenis):
    data_laporan = generate_data_laporan(jenis, request)

    # Render template preview laporan dengan data laporan
    context = {'data_laporan': data_laporan, 'jenis': jenis}
    return render(request, 'preview_laporan.html', context)

from .models import Pemesanan, Pembayaran

def tampilkan_data_terfilter(request, jenis):
    if jenis == 'pembayaran':
        tanggal_awal = request.GET.get('tanggal_awal')
        tanggal_akhir = request.GET.get('tanggal_akhir')
        if tanggal_awal and tanggal_akhir:
            data_laporan = Pembayaran.objects.filter(tanggal_pembayaran__range=[tanggal_awal, tanggal_akhir])
        else:
            data_laporan = Pembayaran.objects.all()
    elif jenis == 'pemesanan':
        tanggal_checkin_awal = request.GET.get('tanggal_checkin_awal')
        tanggal_checkin_akhir = request.GET.get('tanggal_checkin_akhir')
        if tanggal_checkin_awal and tanggal_checkin_akhir:
           data_laporan = Pemesanan.objects.filter(tanggal_checkin__range=[tanggal_checkin_awal, tanggal_checkin_akhir]).select_related('no_kamar_id')
        else:
            data_laporan = Pemesanan.objects.all().select_related('no_kamar_id')
    elif jenis == 'pelanggan':
        tanggal_input_awal = request.GET.get('tanggal_input_awal')
        tanggal_input_akhir = request.GET.get('tanggal_input_akhir')
        if tanggal_input_awal and tanggal_input_akhir:
            data_laporan = Pemesanan.objects.filter(tanggal_input__range=[tanggal_input_awal, tanggal_input_akhir])
        else:
            data_laporan = Pemesanan.objects.all()

    context = {'data_laporan': data_laporan, 'jenis': jenis}
    return render(request, 'preview_laporan.html', context)


def generate_data_laporan(jenis, request):
    data_laporan = []
    
    if jenis == 'pelanggan':
        tanggal_input_awal = request.GET.get('tanggal_input_awal')
        tanggal_input_akhir = request.GET.get('tanggal_input_akhir')
        if tanggal_input_awal and tanggal_input_akhir:
            data_pelanggan = Pemesanan.objects.filter(tanggal_input__range=[tanggal_input_awal, tanggal_input_akhir])
        else:
            data_pelanggan = Pemesanan.objects.all()

        for pelanggan in data_pelanggan:
            data_laporan.append({
                'nama_pelanggan': pelanggan.nama_pelanggan,
                'jenis_kelamin_pelanggan': pelanggan.jenis_kelamin_pelanggan,
                'alamat_pelanggan': pelanggan.alamat_pelanggan,
                'no_telepon_pelanggan': pelanggan.no_telepon_pelanggan,
                'no_ktp_pelanggan': pelanggan.no_ktp_pelanggan,
                'tanggal_input': pelanggan.tanggal_input,
            })

    elif jenis == 'pemesanan':
        tanggal_checkin_awal = request.GET.get('tanggal_checkin_awal')
        tanggal_checkin_akhir = request.GET.get('tanggal_checkin_akhir')
        if tanggal_checkin_awal and tanggal_checkin_akhir:
            data_pemesanan = Pemesanan.objects.filter(tanggal_checkin__range=[tanggal_checkin_awal, tanggal_checkin_akhir]).select_related('no_kamar_id')
        else:
            data_pemesanan = Pemesanan.objects.all().select_related('no_kamar_id')

        for pemesanan in data_pemesanan:
            data_laporan.append({
                'id_pemesanan': pemesanan.id_pemesanan,
                'tanggal_checkin': pemesanan.tanggal_checkin,
                'tanggal_checkout': pemesanan.tanggal_checkout,
                'nama_pelanggan': pemesanan.nama_pelanggan,
                'no_kamar': pemesanan.no_kamar_id.no_kamar,
                'metode_pembayaran': pemesanan.metode_pembayaran,
                'jumlah_pembayaran': pemesanan.jumlah_pembayaran,
            })

    elif jenis == 'pembayaran':
        tanggal_awal = request.GET.get('tanggal_awal')
        tanggal_akhir = request.GET.get('tanggal_akhir')
        if tanggal_awal and tanggal_akhir:
            data_pembayaran = Pembayaran.objects.filter(tanggal_pembayaran__range=[tanggal_awal, tanggal_akhir])
        else:
            data_pembayaran = Pembayaran.objects.all()

        for pembayaran in data_pembayaran:
            data_laporan.append({
                'id_pembayaran': pembayaran.pemesanan.id_pembayaran,
                'tanggal_pembayaran': pembayaran.tanggal_pembayaran,
                'nama_pelanggan': pembayaran.pemesanan.nama_pelanggan,
                'no_kamar': pembayaran.pemesanan.no_kamar_id.no_kamar,
                'jumlah_pembayaran': pembayaran.jumlah_pembayaran,
                'status_pembayaran': pembayaran.status_pembayaran,
            })

    return data_laporan

def cetak_laporan(request, jenis):
    if request.method == 'GET':
        data_laporan = [                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ]

        response = HttpResponse(content_type='application/pdf')
        nama_laporan = get_nama_laporan(jenis)
        response['Content-Disposition'] = f'attachment; filename="{nama_laporan}.pdf"'

        p = canvas.Canvas(response, pagesize=A4)
        canvas_width, canvas_height = A4

        draw_laporan(p, data_laporan, jenis, canvas_width, canvas_height)

        p.showPage()
        p.save()

        return response
    else:
        return render(request, 'preview_laporan.html', {'jenis': jenis})

def draw_laporan(canvas, data_laporan, jenis, canvas_width, canvas_height):
    if jenis == 'pelanggan':
        judul = 'Laporan Data Pelanggan Hotel Diamond'
        header = ['nama_pelanggan', 'jenis_kelamin_pelanggan', 'alamat_pelanggan', 'no_telepon_pelanggan', 'no_ktp_pelanggan','tanggal_input']
        custom_header = ['Nama', 'Jenis Kelamin', 'Alamat', 'No. Telepon', 'NIK','Tanggal nput']
        table_data = [custom_header] + [[pelanggan[field] for field in header] for pelanggan in data_laporan]

        # Menggambar judul laporan
        draw_judul(canvas, canvas_width, judul)

        # Membuat objek Table
        table = Table(table_data)

        # Membuat objek TableStyle untuk mengatur tampilan tabel
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ])

        # Mengatur style tabel
        table.setStyle(table_style)

        # Menggambar tabel pada canvas
        table.wrapOn(canvas, canvas_width, canvas_height)
        table.drawOn(canvas, 70, 700)  # Mengganti koordinat tabel

        # Menambahkan template footer laporan
        footer_template(canvas, canvas_width, canvas_height)

    elif jenis == 'pemesanan':
        judul = 'Laporan Data Pemesanan Hotel Diamond'
        header = ['nama_pelanggan', 'no_kamar', 'tanggal_checkin', 'tanggal_checkout', 'metode_pembayaran', 'jumlah_pembayaran']
        custom_header = ['Nama', 'No Kamar', 'Check-In', 'Check-Out', 'Metode Pembayaran', 'Jumlah Pembayaran']
        table_data = [custom_header] + [[pemesanan[field] for field in header] for pemesanan in data_laporan]

        # Menggambar judul laporan
        draw_judul(canvas, canvas_width, judul)

        # Membuat objek Table
        table = Table(table_data)

        # Membuat objek TableStyle untuk mengatur tampilan tabel
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ])

        # Mengatur style tabel
        table.setStyle(table_style)

        # Menggambar tabel pada canvas
        table.wrapOn(canvas, canvas_width, canvas_height)
        table.drawOn(canvas, 50, 700)  # Mengganti koordinat tabel

        # Menambahkan template footer laporan
        footer_template(canvas, canvas_width, canvas_height)

    elif jenis == 'pembayaran':
        judul = 'Laporan Data Pembayaran Hotel Diamond'
        header = ['id_pembayaran', 'tanggal_pembayaran', 'jumlah_pembayaran', 'status_pembayaran']
        custom_header = ['Id Pembayaran', 'Tanggal Pembayaran', 'Jumlah Pembayaran', 'Status Pembayaran']
        table_data = [custom_header] + [[pembayaran[field] for field in header] for pembayaran in data_laporan]

        # Menggambar judul laporan
        draw_judul(canvas, canvas_width, judul)

        # Membuat objek Table
        table = Table(table_data)

        # Membuat objek TableStyle untuk mengatur tampilan tabel
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ])

        # Mengatur style tabel
        table.setStyle(table_style)

        # Menggambar tabel pada canvas
        table.wrapOn(canvas, canvas_width, canvas_height)
        table.drawOn(canvas, 60, 700)  # Mengganti koordinat tabel

        # Menambahkan template footer laporan
        footer_template(canvas, canvas_width, canvas_height)

def footer_template(canvas, canvas_width, canvas_height):
    # Mengatur posisi dan properti footer
    footer_x = 50
    footer_y = 30

    # Menggambar footer laporan
    canvas.setFont("Helvetica", 12)
    canvas.drawString(footer_x, footer_y, "Laporan Hotel Diamond")

def draw_judul(canvas, canvas_width, judul):
    judul_x = 100
    judul_y = 800
    canvas.setFont("Helvetica-Bold", 20)
    canvas.drawString(judul_x, judul_y, judul)


# ==========================Lihat Presensi===============================

def lihat_presensi(request):
    presensis = Presensi.objects.all()
    jumlah_terlambat = presensis.filter(status='Terlambat').count()
    jumlah_tepat_waktu = presensis.filter(status='Tepat waktu').count()

    context = {
        'presensis': presensis,
        'jumlah_terlambat': jumlah_terlambat,
        'jumlah_tepat_waktu': jumlah_tepat_waktu
    }

    return render(request, 'lihat_presensi.html', context)

# ----------------------------Halaman Pegawai---------------------------------

def pegawai(request):
    return render(request, 'pegawai.html')

# ==========================Presensi=========================================

def presensi(request):
    if request.method == 'POST' and request.POST.get('image_data'):
        image_data = request.POST['image_data']

        # Menentukan status (terlambat atau tepat waktu)
        pegawai = Pegawai.objects.get(id=14)  # Ganti dengan logika pengambilan data pegawai yang sesuai
        jadwal_masuk = pegawai.shift.jam_masuk
        jam_masuk_sekarang = datetime.now().time()

        if datetime.combine(date.today(), jam_masuk_sekarang) > datetime.combine(date.today(), jadwal_masuk):
            status = "Terlambat"
        else:
            status = "Tepat waktu"

        # Simpan gambar ke dalam folder media/absen
        image_data = image_data.split(",")[1]  # Menghapus bagian "data:image/png;base64,"
        image_data = base64.b64decode(image_data)  # Mendecode base64 menjadi bytes

        # Membuat nama unik untuk gambar
        image_name = f"absen_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        image_path = os.path.join(settings.MEDIA_ROOT, 'absen', image_name)

        with open(image_path, 'wb') as f:
            f.write(image_data)

        # Simpan informasi presensi ke dalam database
        presensi = Presensi(
            pegawai=pegawai,
            bukti_absen=f"absen/{image_name}",
            status=status
        )
        presensi.save()

        return redirect('presensisukses')

    form = FormPresensi()
    context = {'form': form}
    return render(request, 'presensi.html', context)

def presensisukses(request):
    return render(request, 'suksespresensi.html')

# ------------------Helaman Pelanggan---------------------------

def beranda_pelanggan(request):
    return render(request,'berandapelanggan.html')

def kamar_pelanggan(request):
    kamar_list = Kamar.objects.all()
    
    if request.method == 'POST' and 'kamar_id' in request.POST:
        kamar_id = request.POST['kamar_id']
        request.session['kamar_id'] = kamar_id
    
    return render(request, 'kamarpelanggan.html', {'kamar_list': kamar_list})

def get_available_room(jenis_kamar, tanggal_checkin, tanggal_checkout, pemesanan_pk=None):
    available_rooms = Nomor_Kamar.objects.filter(jenis_kamar=jenis_kamar)
    
    existing_reservations = Pemesanan.objects.filter(
        Q(no_kamar_id__jenis_kamar=jenis_kamar) &
        (
            Q(tanggal_checkin__lte=tanggal_checkin, tanggal_checkout__gt=tanggal_checkin) |
            Q(tanggal_checkin__lt=tanggal_checkout, tanggal_checkout__gte=tanggal_checkout)
        ) &
        ~Q(status_konfirmasi='Ditolak')
    )


    if pemesanan_pk:
        existing_reservations = existing_reservations.exclude(pk=pemesanan_pk)

    booked_rooms = existing_reservations.values_list('no_kamar_id', flat=True)
    available_rooms = available_rooms.exclude(id__in=booked_rooms)

    return available_rooms.first()

def form_pemesanan(request, kamar_id):
    kamar_list = Kamar.objects.all()
    kamar = get_object_or_404(Kamar, id=kamar_id)
    jenis_kamar = kamar.jenis_kamar.jenis_kamar

    if request.method == 'POST':
        form = FormPemesanan(request.POST, request.FILES)
        if form.is_valid():
            pemesanan = form.save(commit=False)
            available_room = get_available_room(jenis_kamar, pemesanan.tanggal_checkin, pemesanan.tanggal_checkout, pemesanan.pk)

            if pemesanan.status_konfirmasi == 'Ditolak':
                if not available_room:
                    messages.error(request, 'Tidak ada nomor kamar yang tersedia untuk jenis kamar ini pada tanggal check-in yang diberikan.')
                    return render(request, 'form_pemesanan.html', {'form': form, 'kamar': kamar})
                pemesanan.no_kamar_id = available_room
            else:
                if not available_room:
                    messages.error(request, 'Tidak ada nomor kamar yang tersedia untuk jenis kamar ini pada tanggal check-in yang diberikan.')
                    return render(request, 'form_pemesanan.html', {'form': form, 'kamar': kamar})
                pemesanan.no_kamar_id = available_room

                pemesanan.kamar = kamar
                pemesanan.save()

                # Tambahkan notifikasi pesanan berhasil dibuat ke tabel Notifikasi
                pesan_notifikasi = f"Pesanan dengan ID {pemesanan.id} telah berhasil dibuat."
                notifikasi = Notifikasiadmin(pemesanan=pemesanan, pesan=pesan_notifikasi, dibaca=False, created_at=datetime.now())
                notifikasi.save()

                messages.success(request, 'Pesanan Anda telah berhasil dibuat, silahkan tunggu konfirmasi admin.')
                return redirect('pesanan_saya')
        else:
            messages.error(request, 'Terjadi kesalahan dalam mengisi formulir.')
    else:
        form = FormPemesanan()

    return render(request, 'form_pemesanan.html', {'form': form, 'kamar': kamar})

def update_status_kamar():
    pemesanans = Pemesanan.objects.all()
    
    for pemesanan in pemesanans:
        if pemesanan.tanggal_checkout == date.today():
            pemesanan.status_kamar = 'Booking Completed'
            pemesanan.save()

def buat_notifikasi(message):
    notification = Notification(message=message, is_read=False)
    notification.save()
    return notification

from django.shortcuts import render
from django.contrib import messages

def pesanan_saya(request):
    pemesanan_list = Pemesanan.objects.all()
    notifications = Notification.objects.filter(is_read=False)
    unread_count = notifications.count()

    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')  # ID notifikasi yang sudah dibaca
        notification = get_object_or_404(Notification, id=notification_id)
        notification.mark_as_read()
        messages.success(request, 'Notifikasi berhasil ditandai sebagai dibaca.')

    return render(request, 'pesanan_saya.html', {'pemesanan_list': pemesanan_list, 'notifications': notifications, 'unread_count': unread_count})


from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

def mark_as_read(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        notification = get_object_or_404(Notification, id=notification_id)
        notification.mark_as_read()
        messages.success(request, 'Notifikasi berhasil ditandai sebagai dibaca.')
        return redirect('pesanan_saya')



def cetak_bukti_pembayaran(request, pemesanan_id):
    # Ambil data pembayaran berdasarkan ID pemesanan atau model Anda
    pembayaran = Pembayaran.objects.get(pemesanan_id=pemesanan_id)

    # Ambil data pemesanan berdasarkan ID
    pemesanan = pembayaran.pemesanan

    # Buat response PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bukti_pesanan.pdf"'

    # Buat buffer BytesIO untuk menampung data PDF
    buffer = BytesIO()

    # Buat canvas PDF
    p = canvas.Canvas(buffer)

    # Buat card dengan konten bukti pembayaran
    card_width = 430
    card_height = 300
    card_x = (p._pagesize[0] - card_width) / 2
    card_y = p._pagesize[1] - card_height - 50

    # Gambar card
    p.setStrokeColorRGB(0.5, 0.5, 0.5)  # Warna garis card
    p.setLineWidth(2)  # Lebar garis card
    p.rect(card_x, card_y, card_width, card_height)

    # Tambahkan kata-kata "Bukti Pembayaran" di atas card
    p.setFont("Helvetica", 16)
    p.drawString(card_x + 50, card_y + card_height - 20, "BUKTI PESANAN KAMAR HOTEL DIAMOND")

    # Tambahkan konten ke card
    p.setFont("Helvetica", 12)
    p.drawString(card_x + 20, card_y + card_height - 60, "Id. Pemesanan: {}".format(pemesanan.id_pemesanan))
    p.drawString(card_x + 20, card_y + card_height - 80, "Pelanggan: {}".format(pemesanan.nama_pelanggan))
    p.drawString(card_x + 20, card_y + card_height - 110, "Jenis Kamar: {}".format(pemesanan.no_kamar_id.jenis_kamar))
    p.drawString(card_x + 20, card_y + card_height - 130, "No. Kamar: {}".format(pemesanan.no_kamar_id.no_kamar))
    p.drawString(card_x + 20, card_y + card_height - 160, "Check-In: {}".format(pemesanan.tanggal_checkin))
    p.drawString(card_x + 20, card_y + card_height - 180, "Check-Out: {}".format(pemesanan.tanggal_checkout))
    p.drawString(card_x + 20, card_y + card_height - 210, "Jumlah Pembayaran: Rp. {}".format(pembayaran.jumlah_pembayaran))
    p.drawString(card_x + 20, card_y + card_height - 230, "Metode Pembayaran: {}".format(pemesanan.metode_pembayaran))
    p.drawString(card_x + 20, card_y + card_height - 250, "Id. Pembayaran: {}".format(pemesanan.id_pembayaran))

    # Tambahkan gambar bukti pembayaran
    if pembayaran.bukti_pembayaran:
        bukti_pembayaran_path = settings.MEDIA_ROOT + '/' + str(pembayaran.bukti_pembayaran)
        p.drawImage(bukti_pembayaran_path, card_x + 240, card_y + card_height - 240, width=160, height=200)

    # Selesai membuat canvas
    p.showPage()
    p.save()

    # Ambil data dari buffer BytesIO dan kirimkan sebagai response PDF
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def cetak_pesanan(request, pemesanan_id):
    # Ambil data pemesanan berdasarkan ID
    pemesanan = Pemesanan.objects.get(id=pemesanan_id)

    # Buat response PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bukti_pesanan.pdf"'

    # Buat buffer BytesIO untuk menampung data PDF
    buffer = BytesIO()

    # Buat canvas PDF
    p = canvas.Canvas(buffer)

    # Buat card dengan konten bukti pembayaran
    card_width = 430
    card_height = 300
    card_x = (p._pagesize[0] - card_width) / 2
    card_y = p._pagesize[1] - card_height - 50

    # Gambar card
    p.setStrokeColorRGB(0.5, 0.5, 0.5)  # Warna garis card
    p.setLineWidth(2)  # Lebar garis card
    p.rect(card_x, card_y, card_width, card_height)

    # Tambahkan kata-kata "Bukti Pembayaran" di atas card
    p.setFont("Helvetica", 16)
    p.drawString(card_x + 50, card_y + card_height - 20, "BUKTI PESANAN KAMAR HOTEL DIAMOND")

    # Tambahkan konten ke card
    p.setFont("Helvetica", 12)
    p.drawString(card_x + 20, card_y + card_height - 60, "Id. Pemesanan: {}".format(pemesanan.id_pemesanan))
    p.drawString(card_x + 20, card_y + card_height - 80, "Pelanggan: {}".format(pemesanan.nama_pelanggan))
    p.drawString(card_x + 20, card_y + card_height - 110, "Jenis Kamar: {}".format(pemesanan.no_kamar_id.jenis_kamar))
    p.drawString(card_x + 20, card_y + card_height - 130, "No. Kamar: {}".format(pemesanan.no_kamar_id.no_kamar))
    p.drawString(card_x + 20, card_y + card_height - 160, "Check-In: {}".format(pemesanan.tanggal_checkin))
    p.drawString(card_x + 20, card_y + card_height - 180, "Check-Out: {}".format(pemesanan.tanggal_checkout))
    p.drawString(card_x + 20, card_y + card_height - 210, "Jumlah Pembayaran: Rp. {}".format(pemesanan.jumlah_pembayaran))
    p.drawString(card_x + 20, card_y + card_height - 230, "Metode Pembayaran: {}".format(pemesanan.metode_pembayaran))
    p.drawString(card_x + 20, card_y + card_height - 250, "Id. Pembayaran: {}".format(pemesanan.id_pembayaran))
    
    # Selesai membuat canvas
    p.showPage()
    p.save()

    # Ambil data dari buffer BytesIO dan kirimkan sebagai response PDF
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def form_pembayaran(request, pemesanan_id):
    pemesanan = get_object_or_404(Pemesanan, id=pemesanan_id)

    if request.method == 'POST':
        form = FormPembayaran(request.POST, request.FILES)
        if form.is_valid():
            pembayaran = form.save(commit=False)
            pembayaran.pemesanan = pemesanan
            pembayaran.status_pembayaran = 'Sudah Dibayar'  # Set status_pembayaran to 'Belum Dibayar' by default
            pembayaran.status_konfirmasi_pembayaran = 'Pending'  # Set status_konfirmasi_pembayaran to 'Pending' by default
            pembayaran.save()
            
            # Tandai notifikasi sebagai sudah dibaca
            notifikasi = Notification.objects.get(pemesanan=pemesanan)
            notifikasi.is_read = True
            notifikasi.save()
            
             # Tambahkan notifikasi pesanan berhasil dibuat ke tabel Notifikasi
            pesan_notifikasi = f"Bukti pembayaran dengan ID {pemesanan.id} telah berhasil dikirim."
            notifikasi = Notifikasipembayaran(pembayaran=pembayaran, pesan=pesan_notifikasi, dibaca=False, created_at=datetime.now())
            notifikasi.save()
            
            messages.success(request, 'Bukti pembayaran berhasil dikirim, silahkan tunggu konfirmasi admin.')

            return redirect('pesanan_saya')  # Ganti 'pesanan_saya' dengan URL atau nama halaman pesanan_saya
    else:
        form = FormPembayaran()

    return render(request, 'form_pembayaran.html', {'form': form, 'pemesanan': pemesanan})

def setuju_pembayaran(request, pembayaran_id):
    pembayaran = get_object_or_404(Pembayaran, id=pembayaran_id)

    if pembayaran.status_konfirmasi_pembayaran == 'Pending':
        pembayaran.status_konfirmasi_pembayaran = 'Disetujui'
        pembayaran.save()
        
        # Tambahkan cetakan untuk memeriksa nilai variabel
        print("Nilai pembayaran:", pembayaran)

        # Buat notifikasi dan cek apakah berhasil dibuat
        notification = Notification.objects.create(
            pemesanan=pembayaran.pemesanan,
            message='Pembayaran Anda diterima, silahkan datang ke Hotel Diamond',
            is_read=False
        )
        
        # Tandai notifikasi sebagai sudah dibaca
        notifikasi = Notifikasipembayaran.objects.get(pembayaran=pembayaran)
        notifikasi.dibaca = True
        notifikasi.save()
        
        print("Notifikasi berhasil dibuat:", notification)

        messages.success(request, 'Konfirmasi pembayaran berhasil disetujui.')

    return redirect('kelola_pembayaran')


def tolak_pembayaran(request, pembayaran_id):
    pembayaran = get_object_or_404(Pembayaran, id=pembayaran_id)

    if pembayaran.status_konfirmasi_pembayaran == 'Pending':
        pembayaran.status_konfirmasi_pembayaran = 'Ditolak'
        pembayaran.save()
        
         # Tambahkan cetakan untuk memeriksa nilai variabel
        print("Nilai pembayaran:", pembayaran)
        
        notification=Notification.objects.create(
            pemesanan=pembayaran.pemesanan,
            message='>Maaf, bukti pembayaran tidak valid. Silahkan pesan ulang.',
            is_read=False
        )
        
        # Tandai notifikasi sebagai sudah dibaca
        notifikasi = Notifikasipembayaran.objects.get(pembayaran=pembayaran)
        notifikasi.dibaca = True
        notifikasi.save()
        
        print("Notifikasi berhasil dibuat:", notification)
        
        messages.success(request, 'Konfirmasi pembayaran berhasil ditolak.')

    return redirect('kelola_pembayaran')

def setuju(request, id):
    pemesanan = get_object_or_404(Pemesanan, id=id)

    if pemesanan.status_konfirmasi == 'Pending':
        pemesanan.status_konfirmasi = 'Disetujui'
        pemesanan.save()
        
         # Tambahkan cetakan untuk memeriksa nilai variabel
        print("Nilai pemesanan:", pemesanan)
        
        notification=Notification.objects.create(
            pemesanan=pemesanan,
            message='Pesanan diterima, silahkan kirim bukti pembayaran.',
            is_read=False
        )
        
        # Tandai notifikasi sebagai sudah dibaca
        notifikasi = Notifikasiadmin.objects.get(pemesanan=pemesanan)
        notifikasi.dibaca = True
        notifikasi.save()
        
        print("Notifikasi berhasil dibuat:", notification)
        
        messages.success(request, 'Pesanan berhasil disetujui.')

    return redirect('kelola_pemesanan')

def tolak(request, id):
    pemesanan = get_object_or_404(Pemesanan, id=id)

    if pemesanan.status_konfirmasi == 'Pending':
        pemesanan.status_konfirmasi = 'Ditolak'
        pemesanan.save()
        
         # Tambahkan cetakan untuk memeriksa nilai variabel
        print("Nilai pemesanan:", pemesanan)
        
        notification=Notification.objects.create(
            pemesanan=pemesanan,
            message='Maaf, pesanan Anda ditolak. Silahkan pesan ulang.',
            is_read=False
        )
        
        # Tandai notifikasi sebagai sudah dibaca
        notifikasi = Notifikasiadmin.objects.get(pemesanan=pemesanan)
        notifikasi.dibaca = True
        notifikasi.save()
        
        print("Notifikasi berhasil dibuat:", notification)
        
        messages.success(request, 'Pesanan berhasil ditolak.')

    return redirect('kelola_pemesanan')

def daftar_kunci(request):
    kuncis = Kunci.objects.all()
    return render(request, 'kelola_kunci.html', {'kuncis': kuncis})

def tambah_kunci(request):
    if request.method == 'POST':
        form = FormKunci(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kunci berhasil ditambahkan.')
            return redirect('daftar_kunci')
    else:
        form = FormKunci()
    return render(request, 'tambah_kunci.html', {'form': form})

def ubah_kunci(request, kunci_id):
    kunci = get_object_or_404(Kunci, id=kunci_id)
    if request.method == 'POST':
        form = FormKunci(request.POST, request.FILES, instance=kunci)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kunci berhasil diubah.')
            return redirect('daftar_kunci')
    else:
        form = FormKunci(instance=kunci)
    return render(request, 'edit_kunci.html', {'form': form})