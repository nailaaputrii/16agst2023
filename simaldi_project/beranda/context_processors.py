from beranda.models import Notification

def unread_notifications(request):
    notifications = Notification.objects.filter(is_read=False)
    unread_count = notifications.count()
    return {'unread_count': unread_count}

from beranda.models import Notifikasiadmin

def unread_notification_count(request):
    count = Notifikasiadmin.objects.filter(dibaca=False).count()
    return {'count': count}

from beranda.models import Notifikasipembayaran

def notifikasi_belum_dibaca(request):
    notifications = Notifikasipembayaran.objects.filter(dibaca=False)
    jumlah_belum_dibaca = notifications.count()
    return {
        'jumlah_belum_dibaca': jumlah_belum_dibaca
    }
