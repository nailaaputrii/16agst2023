-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Jun 2023 pada 17.44
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simaldi_diamond`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add jadwal', 7, 'add_jadwal'),
(26, 'Can change jadwal', 7, 'change_jadwal'),
(27, 'Can delete jadwal', 7, 'delete_jadwal'),
(28, 'Can view jadwal', 7, 'view_jadwal'),
(29, 'Can add kamar', 8, 'add_kamar'),
(30, 'Can change kamar', 8, 'change_kamar'),
(31, 'Can delete kamar', 8, 'delete_kamar'),
(32, 'Can view kamar', 8, 'view_kamar'),
(33, 'Can add keuangan', 9, 'add_keuangan'),
(34, 'Can change keuangan', 9, 'change_keuangan'),
(35, 'Can delete keuangan', 9, 'delete_keuangan'),
(36, 'Can view keuangan', 9, 'view_keuangan'),
(37, 'Can add pegawai', 10, 'add_pegawai'),
(38, 'Can change pegawai', 10, 'change_pegawai'),
(39, 'Can delete pegawai', 10, 'delete_pegawai'),
(40, 'Can view pegawai', 10, 'view_pegawai'),
(41, 'Can add pelanggan', 11, 'add_pelanggan'),
(42, 'Can change pelanggan', 11, 'change_pelanggan'),
(43, 'Can delete pelanggan', 11, 'delete_pelanggan'),
(44, 'Can view pelanggan', 11, 'view_pelanggan'),
(45, 'Can add profile', 12, 'add_profile'),
(46, 'Can change profile', 12, 'change_profile'),
(47, 'Can delete profile', 12, 'delete_profile'),
(48, 'Can view profile', 12, 'view_profile'),
(49, 'Can add presensi', 13, 'add_presensi'),
(50, 'Can change presensi', 13, 'change_presensi'),
(51, 'Can delete presensi', 13, 'delete_presensi'),
(52, 'Can view presensi', 13, 'view_presensi'),
(53, 'Can add pemesanan', 14, 'add_pemesanan'),
(54, 'Can change pemesanan', 14, 'change_pemesanan'),
(55, 'Can delete pemesanan', 14, 'delete_pemesanan'),
(56, 'Can view pemesanan', 14, 'view_pemesanan'),
(57, 'Can add pembayaran', 15, 'add_pembayaran'),
(58, 'Can change pembayaran', 15, 'change_pembayaran'),
(59, 'Can delete pembayaran', 15, 'delete_pembayaran'),
(60, 'Can view pembayaran', 15, 'view_pembayaran'),
(61, 'Can add notifikasi', 16, 'add_notifikasi'),
(62, 'Can change notifikasi', 16, 'change_notifikasi'),
(63, 'Can delete notifikasi', 16, 'delete_notifikasi'),
(64, 'Can view notifikasi', 16, 'view_notifikasi'),
(65, 'Can add pengeluaran', 17, 'add_pengeluaran'),
(66, 'Can change pengeluaran', 17, 'change_pengeluaran'),
(67, 'Can delete pengeluaran', 17, 'delete_pengeluaran'),
(68, 'Can view pengeluaran', 17, 'view_pengeluaran'),
(69, 'Can add nomor_ kamar', 18, 'add_nomor_kamar'),
(70, 'Can change nomor_ kamar', 18, 'change_nomor_kamar'),
(71, 'Can delete nomor_ kamar', 18, 'delete_nomor_kamar'),
(72, 'Can view nomor_ kamar', 18, 'view_nomor_kamar'),
(73, 'Can add kunci', 19, 'add_kunci'),
(74, 'Can change kunci', 19, 'change_kunci'),
(75, 'Can delete kunci', 19, 'delete_kunci'),
(76, 'Can view kunci', 19, 'view_kunci');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_jadwal`
--

CREATE TABLE `beranda_jadwal` (
  `id` bigint(20) NOT NULL,
  `shift` varchar(50) NOT NULL,
  `jam_masuk` time(6) NOT NULL,
  `jam_keluar` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_jadwal`
--

INSERT INTO `beranda_jadwal` (`id`, `shift`, `jam_masuk`, `jam_keluar`) VALUES
(1, 'Pagi', '07:00:00.000000', '15:00:00.000000'),
(2, 'Siang', '15:00:00.000000', '23:00:00.000000'),
(3, 'Malam', '23:00:00.000000', '07:00:00.000000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_kamar`
--

CREATE TABLE `beranda_kamar` (
  `id` bigint(20) NOT NULL,
  `kapasitas` int(11) DEFAULT NULL,
  `kasur` varchar(50) DEFAULT NULL,
  `fasilitas_lainnya` varchar(255) DEFAULT NULL,
  `tarif` int(11) DEFAULT NULL,
  `gambar_kamar` varchar(100) DEFAULT NULL,
  `jenis_kamar_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_kamar`
--

INSERT INTO `beranda_kamar` (`id`, `kapasitas`, `kasur`, `fasilitas_lainnya`, `tarif`, `gambar_kamar`, `jenis_kamar_id`) VALUES
(7, 2, 'Spring Bed King Size', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 825000, 'kamar_images/vvip_NMPCji2.jpg', '1'),
(8, 2, 'Double/Twin Spring Bed', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 495000, 'kamar_images/executive_PyfD6aT.jpg', '5'),
(9, 2, 'Twin Spring Bed', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 440000, 'kamar_images/superior_4ratwrK.jpg', '7'),
(10, 2, 'Double/Twin Spring Bed', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 350000, 'kamar_images/deluxe_6jyEQfQ.jpg', '15'),
(11, 2, 'Spring Bed Queen Size', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 975000, 'kamar_images/family_room_mN7MJ8Q.jpg', '25'),
(12, 2, 'Single Bed Room', 'AC, TV 42\", Kulkas, Lemari Pakaian, Kamar Mandi (Shower, Air Panas/Air Dingin, Bathtub, Closet Duduk)', 250000, 'kamar_images/single_room_DBGBwJE.jpg', '28');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_keuangan`
--

CREATE TABLE `beranda_keuangan` (
  `id` bigint(20) NOT NULL,
  `tanggal` date NOT NULL,
  `kategori` varchar(100) NOT NULL,
  `keterangan` longtext NOT NULL,
  `pengeluaran_id` bigint(20) DEFAULT NULL,
  `saldo` decimal(10,2) DEFAULT NULL,
  `pembayaran_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_kunci`
--

CREATE TABLE `beranda_kunci` (
  `id` bigint(20) NOT NULL,
  `ktp_status` varchar(15) NOT NULL,
  `kunci_status` varchar(15) NOT NULL,
  `waktu_input` datetime(6) NOT NULL,
  `pemesanan_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_kunci`
--

INSERT INTO `beranda_kunci` (`id`, `ktp_status`, `kunci_status`, `waktu_input`, `pemesanan_id`) VALUES
(6, 'submitted', 'delivered', '2023-06-23 08:30:54.652621', 52);

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_nomor_kamar`
--

CREATE TABLE `beranda_nomor_kamar` (
  `id` bigint(20) NOT NULL,
  `jenis_kamar` varchar(50) NOT NULL,
  `no_kamar` varchar(50) NOT NULL,
  `status_kamar` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_nomor_kamar`
--

INSERT INTO `beranda_nomor_kamar` (`id`, `jenis_kamar`, `no_kamar`, `status_kamar`) VALUES
(1, 'VVIP', '241', 'Full Booked'),
(4, 'VVIP', '242', 'Empty Room'),
(5, 'Executive Class', '236', 'Booked'),
(6, 'Executive Class', '102', 'Empty Room'),
(7, 'Superior Room', '201', 'Empty Room'),
(8, 'Superior Room', '202', 'Empty Room'),
(9, 'Superior Room', '203', 'Empty Room'),
(10, 'Superior Room', '208', 'Empty Room'),
(11, 'Superior Room', '221', 'Empty Room'),
(12, 'Superior Room', '223', 'Empty Room'),
(13, 'Superior Room', '234', 'Empty Room'),
(14, 'Superior Room', '235', 'Empty Room'),
(15, 'Deluxe Room', '105', 'Full Booked'),
(16, 'Deluxe Room', '106', 'Empty Room'),
(17, 'Deluxe Room', '107', 'Empty Room'),
(18, 'Deluxe Room', '108', 'Empty Room'),
(19, 'Deluxe Room', '109', 'Empty Room'),
(20, 'Deluxe Room', '204', 'Empty Room'),
(21, 'Deluxe Room', '205', 'Empty Room'),
(22, 'Deluxe Room', '207', 'Empty Room'),
(23, 'Deluxe Room', '209', 'Empty Room'),
(24, 'Deluxe Room', '210', 'Empty Room'),
(25, 'Family Room', '303', 'Booked'),
(26, 'Family Room', '304', 'Empty Room'),
(27, 'Family Room', '305', 'Empty Room'),
(28, 'Single Room', '306', 'Empty Room'),
(29, 'Single Room', '307', 'Empty Room'),
(30, 'VVIP', '205', 'Empty Room');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_notifikasi`
--

CREATE TABLE `beranda_notifikasi` (
  `id` bigint(20) NOT NULL,
  `pesan` longtext NOT NULL,
  `dibaca` tinyint(1) NOT NULL,
  `penerima_id` bigint(20) NOT NULL,
  `pengirim_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_pegawai`
--

CREATE TABLE `beranda_pegawai` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(50) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `posisi` varchar(255) NOT NULL,
  `no_telepon` varchar(15) NOT NULL,
  `shift_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_pegawai`
--

INSERT INTO `beranda_pegawai` (`id`, `nama`, `jenis_kelamin`, `alamat`, `posisi`, `no_telepon`, `shift_id`) VALUES
(13, 'ikbal', 'Laki-laki', 'Subang', 'Resepsionis', '0985643768293', 1),
(14, 'aldi', 'Laki-laki', 'Subang', 'Staff', '0855435435', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_pelanggan`
--

CREATE TABLE `beranda_pelanggan` (
  `id` bigint(20) NOT NULL,
  `nama_pelanggan` varchar(255) NOT NULL,
  `jenis_kelamin_pelanggan` varchar(50) NOT NULL,
  `alamat_pelanggan` varchar(255) NOT NULL,
  `no_telepon_pelanggan` varchar(15) NOT NULL,
  `no_ktp_pelanggan` varchar(16) NOT NULL,
  `foto_ktp` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_pelanggan`
--

INSERT INTO `beranda_pelanggan` (`id`, `nama_pelanggan`, `jenis_kelamin_pelanggan`, `alamat_pelanggan`, `no_telepon_pelanggan`, `no_ktp_pelanggan`, `foto_ktp`) VALUES
(92, 'Naila Putri Cahya Novitri', 'Perempuan', 'Subang', '083805152414', '01231425738286', 'ktp_images/watermark.png'),
(93, 'Gemawan Alfarizi', 'Laki-laki', 'Karawang', '083805152414', '01231425738286', 'ktp_images/tangkapan-layar-contoh-e-ktp-yan-20210907090725.jpg'),
(94, 'Naila', 'Laki-laki', 'Karawang', '623805152414', '01231425738286', 'ktp_images/watermark_LjaKXOg.png'),
(95, 'Naila', 'Perempuan', 'Subang', '083805152414', '01231425738286', 'ktp_images/watermark_tVJAQFa.png'),
(96, 'Susi', 'Perempuan', 'Subang', '083805152414', '01231425738286', 'ktp_images/tangkapan-layar-contoh-e-ktp-yan-20210907090725_8xuyrKR.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_pembayaran`
--

CREATE TABLE `beranda_pembayaran` (
  `id` bigint(20) NOT NULL,
  `tanggal_pembayaran` date NOT NULL,
  `bukti_pembayaran` varchar(100) DEFAULT NULL,
  `status_pembayaran` varchar(50) NOT NULL,
  `pemesanan_id` bigint(20) DEFAULT NULL,
  `jumlah_pembayaran` int(11) DEFAULT NULL,
  `status_konfirmasi_pembayaran` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_pembayaran`
--

INSERT INTO `beranda_pembayaran` (`id`, `tanggal_pembayaran`, `bukti_pembayaran`, `status_pembayaran`, `pemesanan_id`, `jumlah_pembayaran`, `status_konfirmasi_pembayaran`) VALUES
(25, '2023-06-23', 'bukti_pembayaran/bukti-transfer-bri-_OeffOCE.jpg', 'Lunas', 52, 1650000, 'Disetujui'),
(26, '2023-06-23', 'bukti_pembayaran/bukti-transfer-bri-_QW4VUzl.jpg', 'Lunas', 55, 350000, 'Disetujui'),
(27, '2023-06-23', 'bukti_pembayaran/bukti-transfer-bri-_090JpTL.jpg', 'Belum Dibayar', 56, 1950000, 'Pending');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_pemesanan`
--

CREATE TABLE `beranda_pemesanan` (
  `id` bigint(20) NOT NULL,
  `tanggal_checkin` date NOT NULL,
  `tanggal_checkout` date NOT NULL,
  `metode_pembayaran` varchar(50) NOT NULL,
  `jumlah_pembayaran` int(11) DEFAULT NULL,
  `pelanggan_id` bigint(20) DEFAULT NULL,
  `status_konfirmasi` varchar(20) NOT NULL,
  `kamar_id` bigint(20) DEFAULT NULL,
  `waktu_konfirmasi` datetime(6) DEFAULT NULL,
  `no_kamar_id_id` bigint(20) DEFAULT NULL,
  `id_pemesanan` varchar(50) NOT NULL,
  `id_pembayaran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_pemesanan`
--

INSERT INTO `beranda_pemesanan` (`id`, `tanggal_checkin`, `tanggal_checkout`, `metode_pembayaran`, `jumlah_pembayaran`, `pelanggan_id`, `status_konfirmasi`, `kamar_id`, `waktu_konfirmasi`, `no_kamar_id_id`, `id_pemesanan`, `id_pembayaran`) VALUES
(52, '2023-06-23', '2023-06-25', 'Transfer Via BRI', 1650000, 92, 'Disetujui', 7, '2023-06-23 02:13:04.999892', 1, '3KD0W0DQYW', 'DXIYBCY3C6'),
(53, '2023-06-23', '2023-06-27', 'Bayar Di Tempat', 1980000, 93, 'Ditolak', 8, NULL, 5, '3KD0W0DQYW', 'DXIYBCY3C6'),
(54, '2023-06-16', '2023-06-23', 'Transfer Via BRI', 3465000, 92, 'Disetujui', 8, '2023-06-23 02:37:45.018143', 5, '3KD0W0DQYW', 'DXIYBCY3C6'),
(55, '2023-06-23', '2023-06-24', 'Transfer Via BRI', 350000, 95, 'Disetujui', 10, '2023-06-23 08:25:01.898397', 15, 'AVDST53MIA', '4S93J2ZZ70'),
(56, '2023-06-23', '2023-06-25', 'Transfer Via BRI', 1950000, 96, 'Disetujui', 11, '2023-06-23 08:38:59.922004', 25, 'AVDST53MIA', '4S93J2ZZ70');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_pengeluaran`
--

CREATE TABLE `beranda_pengeluaran` (
  `id` bigint(20) NOT NULL,
  `tanggal_pengeluaran` date NOT NULL,
  `keterangan_pengeluaran` varchar(255) NOT NULL,
  `jumlah_pengeluaran` decimal(10,2) DEFAULT NULL,
  `pembayaran_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_presensi`
--

CREATE TABLE `beranda_presensi` (
  `id` bigint(20) NOT NULL,
  `tanggal` date NOT NULL,
  `jam_masuk` time(6) NOT NULL,
  `bukti_absen` varchar(100) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `pegawai_id` bigint(20) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_presensi`
--

INSERT INTO `beranda_presensi` (`id`, `tanggal`, `jam_masuk`, `bukti_absen`, `status`, `pegawai_id`, `url`) VALUES
(51, '2023-06-23', '15:12:07.252292', 'absen/absen_20230623151207.png', 'Terlambat', 13, '/media/absen/absen_20230623151207.png'),
(52, '2023-06-23', '15:32:38.015651', 'absen/absen_20230623153238.png', 'Terlambat', 14, '/media/absen/absen_20230623153238.png'),
(53, '2023-06-23', '15:40:25.345417', 'absen/absen_20230623154025.png', 'Terlambat', 14, '/media/absen/absen_20230623154025.png');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_profile`
--

CREATE TABLE `beranda_profile` (
  `id` bigint(20) NOT NULL,
  `lupa_password_token` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_user`
--

CREATE TABLE `beranda_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `beranda_user`
--

INSERT INTO `beranda_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`, `status`) VALUES
(1, 'pbkdf2_sha256$600000$ckA336JvkVgqCgQ3uFEgrc$+5KATnRtkbrYBQs5I5e7FBWdq512b8ObREeKyQXKm50=', '2023-06-23 07:50:29.661267', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-06-14 22:46:41.168330', '12345', 'Aktif'),
(20, 'pbkdf2_sha256$600000$NdUkyJEvxAt53g22IIOUIM$rOiN9B1gFpDeC1CxJQ+CWEU78w0xG0EaVtElTQ2XprI=', '2023-06-21 12:01:38.492575', 0, 'Gema', '', '', 'gemawanalfarizi22@gmail.com', 0, 1, '2023-06-21 12:01:26.306378', 'Admin', 'Aktif'),
(21, 'pbkdf2_sha256$600000$xzBgvzj4Jrt13Z7jslG5KL$Y4v/OeaX6awf5CSlUHJmNLvJYR0Yz9OdP/rwv+FsRRo=', '2023-06-21 12:38:04.328453', 0, 'Naila', '', '', 'nailaputricahyanovitri@gmail.com', 0, 1, '2023-06-21 12:37:40.795280', 'Pelanggan', 'Aktif'),
(22, 'pbkdf2_sha256$600000$Gy9v2RYPsVmu0lGYN7zc6Z$kZ8dyjyRE5LIVd0wlaIyKca6T8hKrxXYKzvteBWhmdw=', '2023-06-21 18:55:47.750510', 0, 'saya', '', '', 'aku@gmail.com', 0, 1, '2023-06-21 18:55:34.800580', 'Admin', 'Nonaktif'),
(23, 'pbkdf2_sha256$600000$1R2VLIvJM5Q59xHR05apBq$NterP6fp3Wg9r0v8Aj3hpiE9BRY5ZSvcSQmx2QpQuQc=', '2023-06-21 19:00:11.042933', 0, 'abdi', '', '', 'maya@gmail.com', 0, 1, '2023-06-21 19:00:10.482498', 'Admin', 'Aktif'),
(24, 'pbkdf2_sha256$600000$34qODNHxlZFziP466A7cc5$oKFd49VTc4CJIjLg0+SC2nnao+cPjiCxuKbMUYcPew0=', '2023-06-23 08:27:32.437883', 0, 'rido', '', '', 'rido@gmail.com', 0, 1, '2023-06-23 07:15:48.823000', 'Admin', 'Aktif'),
(25, 'pbkdf2_sha256$600000$K1sdW12WhVZWhTQJjfGy3N$TH7p2AN7ZogSaKO/eYtqcqCrRP4X3zWQCv6n6rkyjeg=', '2023-06-23 07:26:54.057721', 0, 'fadla', '', '', 'fadla@gmail.com', 0, 1, '2023-06-23 07:16:23.063176', 'Pegawai', 'Aktif'),
(26, 'pbkdf2_sha256$600000$DCbfWNsmDiVM4vV9oGQAS7$2YEDHxo2ZE8DFeQ+QydeMAJBaFJiyChrn4CqbdpskrU=', '2023-06-23 08:32:28.306321', 0, 'aldi', '', '', 'aldi@gmail.com', 0, 1, '2023-06-23 07:16:52.497931', 'Pegawai', 'Aktif'),
(27, 'pbkdf2_sha256$600000$5c94n83iBbYyMKFURmzlp1$OUOFkv2xTJLc3XW1fV8ZjXe5Ius4gNoXYsvsPmd0cHU=', '2023-06-23 08:32:57.896913', 0, 'manajer1', '', '', 'akun@gmail.com', 0, 1, '2023-06-23 07:29:07.790262', 'Manajer', 'Aktif'),
(28, 'pbkdf2_sha256$600000$hQ1lzrh5M2yrBzLbn3ldS5$HRT0C7Vk2sN7+dwKKQRouc7ewdef3lj4minb2EHRRZg=', '2023-06-23 08:22:56.503253', 0, 'cahya', '', '', 'nailaputricahyanovitri@gmail.com', 0, 1, '2023-06-23 08:22:45.180360', 'Pelanggan', 'Aktif');

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_user_groups`
--

CREATE TABLE `beranda_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `beranda_user_user_permissions`
--

CREATE TABLE `beranda_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-06-14 23:15:40.659853', '1', 'Pagi', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-06-14 23:15:54.536824', '2', 'Siang', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-06-14 23:16:06.788340', '3', 'Malam', 1, '[{\"added\": {}}]', 7, 1),
(4, '2023-06-14 23:16:50.132590', '1', 'Gema', 1, '[{\"added\": {}}]', 10, 1),
(5, '2023-06-14 23:17:25.487186', '2', 'Andika', 1, '[{\"added\": {}}]', 10, 1),
(6, '2023-06-14 23:18:14.832962', '3', 'Dewi', 1, '[{\"added\": {}}]', 10, 1),
(7, '2023-06-14 23:18:47.329769', '1', 'Presensi object (1)', 1, '[{\"added\": {}}]', 13, 1),
(8, '2023-06-15 06:23:32.015544', '1', 'Pembayaran object (1)', 1, '[{\"added\": {}}]', 15, 1),
(9, '2023-06-15 18:33:14.286830', '19', 'Ratna', 3, '', 11, 1),
(10, '2023-06-15 18:33:14.288871', '18', 'Janur', 3, '', 11, 1),
(11, '2023-06-15 18:33:14.288871', '17', 'Fahri', 3, '', 11, 1),
(12, '2023-06-15 18:33:14.296893', '16', 'Haruto', 3, '', 11, 1),
(13, '2023-06-15 18:33:14.296893', '15', 'Luna', 3, '', 11, 1),
(14, '2023-06-15 18:33:14.296893', '13', 'Chava', 3, '', 11, 1),
(15, '2023-06-15 18:33:14.304902', '12', 'Kanaya', 3, '', 11, 1),
(16, '2023-06-15 18:33:14.304902', '11', 'Nadia', 3, '', 11, 1),
(17, '2023-06-15 18:33:45.664997', '5', 'Pemesanan object (5)', 3, '', 14, 1),
(18, '2023-06-15 18:50:56.212468', '2', 'Pembayaran object (2)', 3, '', 15, 1),
(19, '2023-06-15 18:51:18.205115', '4', 'Pemesanan object (4)', 3, '', 14, 1),
(20, '2023-06-15 18:51:18.210136', '2', 'Pemesanan object (2)', 3, '', 14, 1),
(21, '2023-06-15 18:51:18.210136', '1', 'Pemesanan object (1)', 3, '', 14, 1),
(22, '2023-06-15 18:51:31.093509', '10', 'Joko', 3, '', 11, 1),
(23, '2023-06-15 18:51:31.101035', '9', 'galuh', 3, '', 11, 1),
(24, '2023-06-15 18:51:31.101035', '8', 'Gema', 3, '', 11, 1),
(25, '2023-06-15 18:51:31.101035', '7', 'Naila', 3, '', 11, 1),
(26, '2023-06-15 18:51:31.109109', '6', 'Naila', 3, '', 11, 1),
(27, '2023-06-15 18:51:31.109109', '4', 'andika', 3, '', 11, 1),
(28, '2023-06-15 18:51:31.117073', '3', 'Susi', 3, '', 11, 1),
(29, '2023-06-15 18:51:31.117073', '2', 'Gema', 3, '', 11, 1),
(30, '2023-06-15 18:51:31.117073', '1', 'Naila', 3, '', 11, 1),
(31, '2023-06-15 19:32:06.954714', '27', 'andika', 3, '', 11, 1),
(32, '2023-06-15 19:32:06.954714', '26', 'andika', 3, '', 11, 1),
(33, '2023-06-15 19:32:06.961748', '25', 'Wahyu', 3, '', 11, 1),
(34, '2023-06-15 19:32:06.961748', '24', 'Wahyu', 3, '', 11, 1),
(35, '2023-06-15 19:32:06.969780', '23', 'Wahyu', 3, '', 11, 1),
(36, '2023-06-15 19:32:06.969780', '22', 'Gema', 3, '', 11, 1),
(37, '2023-06-15 19:32:06.977783', '21', 'Zahra', 3, '', 11, 1),
(38, '2023-06-15 19:32:06.977783', '20', 'Naila', 3, '', 11, 1),
(39, '2023-06-16 02:59:07.757024', '1', 'Membeli bahan dapur', 2, '[]', 17, 1),
(40, '2023-06-21 05:33:09.783179', '78', 'andika', 1, '[{\"added\": {}}]', 11, 1),
(41, '2023-06-21 08:11:14.890118', '13', 'danu', 1, '[{\"added\": {}}]', 6, 1),
(42, '2023-06-21 08:14:56.593367', '14', 'lara', 1, '[{\"added\": {}}]', 6, 1),
(43, '2023-06-21 11:59:29.575854', '19', 'gilang', 3, '', 6, 1),
(44, '2023-06-21 11:59:29.578852', '18', 'wati', 3, '', 6, 1),
(45, '2023-06-21 11:59:29.581850', '17', 'gunawan', 3, '', 6, 1),
(46, '2023-06-21 11:59:29.584852', '16', 'anto', 3, '', 6, 1),
(47, '2023-06-21 11:59:29.586856', '15', 'ratna', 3, '', 6, 1),
(48, '2023-06-21 11:59:29.589848', '14', 'lara', 3, '', 6, 1),
(49, '2023-06-21 11:59:29.591850', '13', 'danu', 3, '', 6, 1),
(50, '2023-06-21 11:59:29.596872', '12', 'Fahmi', 3, '', 6, 1),
(51, '2023-06-21 11:59:29.598876', '11', 'bagus', 3, '', 6, 1),
(52, '2023-06-21 11:59:29.601872', '10', 'Susi', 3, '', 6, 1),
(53, '2023-06-21 11:59:29.603868', '9', 'prita', 3, '', 6, 1),
(54, '2023-06-21 11:59:29.606871', '8', 'yogi', 3, '', 6, 1),
(55, '2023-06-21 11:59:29.609408', '7', 'ikbal', 3, '', 6, 1),
(56, '2023-06-21 11:59:29.612414', '6', 'andikap', 3, '', 6, 1),
(57, '2023-06-21 11:59:29.614421', '5', 'dewi', 3, '', 6, 1),
(58, '2023-06-21 11:59:29.616413', '4', 'naufal', 3, '', 6, 1),
(59, '2023-06-21 11:59:29.619407', '3', 'Gema', 3, '', 6, 1),
(60, '2023-06-21 11:59:29.621413', '2', 'Alfarizi', 3, '', 6, 1),
(61, '2023-06-22 01:11:12.977512', '3', 'Kunci - Gema', 3, '', 19, 1),
(62, '2023-06-22 01:11:12.990012', '2', 'Kunci - Naila', 3, '', 19, 1),
(63, '2023-06-22 12:52:01.226157', '25', '', 3, '', 13, 1),
(64, '2023-06-22 12:52:01.234183', '24', '', 3, '', 13, 1),
(65, '2023-06-22 12:52:01.242176', '23', '', 3, '', 13, 1),
(66, '2023-06-22 12:52:01.242176', '22', '', 3, '', 13, 1),
(67, '2023-06-22 12:52:01.250181', '21', '', 3, '', 13, 1),
(68, '2023-06-22 12:52:01.258191', '20', '', 3, '', 13, 1),
(69, '2023-06-22 12:52:01.258191', '19', '', 3, '', 13, 1),
(70, '2023-06-22 12:52:01.266179', '18', '', 3, '', 13, 1),
(71, '2023-06-22 12:52:01.266179', '17', '', 3, '', 13, 1),
(72, '2023-06-22 12:52:01.274181', '16', '', 3, '', 13, 1),
(73, '2023-06-22 12:52:01.290175', '15', '', 3, '', 13, 1),
(74, '2023-06-22 12:52:01.298176', '14', '', 3, '', 13, 1),
(75, '2023-06-22 12:52:01.298176', '13', '', 3, '', 13, 1),
(76, '2023-06-22 12:52:01.298176', '12', '', 3, '', 13, 1),
(77, '2023-06-22 12:52:01.306193', '11', '', 3, '', 13, 1),
(78, '2023-06-22 12:52:01.306193', '10', '', 3, '', 13, 1),
(79, '2023-06-22 12:52:01.306193', '9', '', 3, '', 13, 1),
(80, '2023-06-22 12:52:01.314179', '8', '', 3, '', 13, 1),
(81, '2023-06-22 12:52:01.314179', '7', '', 3, '', 13, 1),
(82, '2023-06-22 12:52:01.314179', '6', '', 3, '', 13, 1),
(83, '2023-06-22 12:52:01.322179', '5', '', 3, '', 13, 1),
(84, '2023-06-22 12:52:01.322179', '4', '', 3, '', 13, 1),
(85, '2023-06-22 12:52:01.322179', '3', '', 3, '', 13, 1),
(86, '2023-06-22 12:52:01.330194', '2', '', 3, '', 13, 1),
(87, '2023-06-22 12:52:01.330194', '1', '', 3, '', 13, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'beranda', 'jadwal'),
(8, 'beranda', 'kamar'),
(9, 'beranda', 'keuangan'),
(19, 'beranda', 'kunci'),
(18, 'beranda', 'nomor_kamar'),
(16, 'beranda', 'notifikasi'),
(10, 'beranda', 'pegawai'),
(11, 'beranda', 'pelanggan'),
(15, 'beranda', 'pembayaran'),
(14, 'beranda', 'pemesanan'),
(17, 'beranda', 'pengeluaran'),
(13, 'beranda', 'presensi'),
(12, 'beranda', 'profile'),
(6, 'beranda', 'user'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-06-14 22:46:13.701696'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-06-14 22:46:13.822075'),
(3, 'auth', '0001_initial', '2023-06-14 22:46:14.198935'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-06-14 22:46:14.287100'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-06-14 22:46:14.303088'),
(6, 'auth', '0004_alter_user_username_opts', '2023-06-14 22:46:14.312666'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-06-14 22:46:14.327211'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-06-14 22:46:14.335227'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-06-14 22:46:14.351233'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-06-14 22:46:14.367213'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-06-14 22:46:14.391232'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-06-14 22:46:14.431379'),
(13, 'auth', '0011_update_proxy_permissions', '2023-06-14 22:46:14.439372'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-06-14 22:46:14.455418'),
(15, 'beranda', '0001_initial', '2023-06-14 22:46:15.586049'),
(16, 'admin', '0001_initial', '2023-06-14 22:46:15.818877'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-06-14 22:46:15.842907'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-06-14 22:46:15.866915'),
(19, 'sessions', '0001_initial', '2023-06-14 22:46:15.954535'),
(20, 'beranda', '0002_alter_pelanggan_no_telepon_pelanggan', '2023-06-15 15:48:39.797855'),
(21, 'beranda', '0003_alter_pegawai_no_telepon', '2023-06-15 15:51:46.037155'),
(22, 'beranda', '0004_alter_pemesanan_tanggal_checkin_notifikasi', '2023-06-15 18:01:23.544423'),
(23, 'beranda', '0005_pengeluaran_remove_keuangan_pemasukan_and_more', '2023-06-16 02:18:16.776131'),
(24, 'beranda', '0006_pemesanan_status_konfirmasi', '2023-06-16 03:11:25.525472'),
(25, 'beranda', '0007_nomor_kamar_remove_kamar_jenis_kamar_and_more', '2023-06-18 07:55:00.614583'),
(26, 'beranda', '0008_rename_nomor_kamar_kamar_jenis_kamar', '2023-06-18 10:23:54.437392'),
(27, 'beranda', '0009_pemesanan_no_kamar_id', '2023-06-18 11:52:05.300544'),
(28, 'beranda', '0010_rename_status_konfirmasi_pembayaran_status_konfirmasi_pembayaran', '2023-06-18 13:26:18.353915'),
(29, 'beranda', '0011_alter_nomor_kamar_jenis_kamar_and_more', '2023-06-19 01:16:01.971556'),
(30, 'beranda', '0012_alter_pemesanan_tanggal_checkin_kunci', '2023-06-20 18:09:41.972253'),
(31, 'beranda', '0013_pelanggan_foto_ktp', '2023-06-20 19:09:48.024374'),
(32, 'beranda', '0014_remove_pemesanan_pesanan_khusus', '2023-06-20 19:20:45.362884'),
(33, 'beranda', '0015_pemesanan_id_pemesanan', '2023-06-20 19:54:42.110584'),
(34, 'beranda', '0016_alter_pemesanan_id_pemesanan', '2023-06-20 20:03:04.790217'),
(35, 'beranda', '0017_pembayaran_id_pembayaran_and_more', '2023-06-20 20:08:57.704672'),
(36, 'beranda', '0018_remove_pembayaran_id_pembayaran_and_more', '2023-06-20 20:23:43.294804'),
(37, 'beranda', '0019_pelanggan_foto_pelanggan_and_more', '2023-06-21 04:35:54.986721'),
(38, 'beranda', '0020_remove_user_is_admin_remove_user_is_manajer_and_more', '2023-06-21 08:09:32.532627'),
(39, 'beranda', '0021_pelanggan_user_alter_pemesanan_id_pembayaran_and_more', '2023-06-21 12:15:15.839607'),
(40, 'beranda', '0022_remove_pelanggan_user_alter_pemesanan_id_pembayaran_and_more', '2023-06-21 14:43:08.742509'),
(41, 'beranda', '0023_remove_pelanggan_foto_pelanggan_and_more', '2023-06-21 17:23:07.603574'),
(42, 'beranda', '0024_user_status_alter_pemesanan_id_pembayaran_and_more', '2023-06-21 18:48:14.725024'),
(43, 'beranda', '0025_pengeluaran_pembayaran_alter_pemesanan_id_pembayaran_and_more', '2023-06-21 19:56:56.657237'),
(44, 'beranda', '0026_remove_kunci_pelanggan_alter_pemesanan_id_pembayaran_and_more', '2023-06-22 03:40:27.401367'),
(45, 'beranda', '0027_presensi_url_alter_pemesanan_id_pembayaran_and_more', '2023-06-22 12:09:26.035523'),
(46, 'beranda', '0028_alter_pemesanan_id_pembayaran_and_more', '2023-06-23 05:52:56.763450'),
(47, 'beranda', '0029_alter_pemesanan_id_pembayaran_and_more', '2023-06-23 07:51:51.066073');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0r2eicl7uk6tnb40xxmng8j393nn8g3a', '.eJxVjjsOwjAQRO_iGlnxyl9Kes4Qrb3rOBA5KJ8q4u4kKAW0M2-eZhMtrktp15mntidxFeDE5TeMmJ5cj4YeWLtRprEuUx_lgcizneV9JB5uJ_snKDiXfR2hQWUSKALnUJHPYBmxQWNUAM2aXIzeUKZss86QVARvGqttYAiodumLh_1Bh_X7NNj3BzuiPhs:1qCjvr:y3s2p0Hz4DmIt3viBC-RAxR9w4Vji-gyhmRFZ2ATtpg', '2023-07-07 16:46:47.354412'),
('gig3qpqlddhi76793h0fiufd4l8wcqn4', '.eJxVjs0OgjAQhN-lZ9MUYRfq0bvP0Oxut4CSYvg5Gd9dMBz0OvPNl3mZQOvShXXWKfTRXExhTr8Zkzw070W8U25HK2Nepp7tjtijne1tjDpcD_ZP0NHcbWuIKVV45kZLwJISRRQPrBDZ1VIq1uijczV7YfSEIAVKI67yoJUk3KRPHbYHLeXvUYT3BzDqPmc:1qCXba:248DoR-fbCSPHYHTJ62vGn9iBag27onCfrMPIQtQF4Y', '2023-07-07 03:37:02.154718');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeks untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeks untuk tabel `beranda_jadwal`
--
ALTER TABLE `beranda_jadwal`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `beranda_kamar`
--
ALTER TABLE `beranda_kamar`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_kamar_jenis_kamar_id_9d8150c3_fk_beranda_nomor_kamar_id` (`jenis_kamar_id`);

--
-- Indeks untuk tabel `beranda_keuangan`
--
ALTER TABLE `beranda_keuangan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_keuangan_pembayaran_id_fe70359a_fk_beranda_pembayaran_id` (`pembayaran_id`),
  ADD KEY `beranda_keuangan_pengeluaran_id_98dc7a89` (`pengeluaran_id`);

--
-- Indeks untuk tabel `beranda_kunci`
--
ALTER TABLE `beranda_kunci`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_kunci_pemesanan_id_e0bd860c_fk_beranda_pemesanan_id` (`pemesanan_id`);

--
-- Indeks untuk tabel `beranda_nomor_kamar`
--
ALTER TABLE `beranda_nomor_kamar`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `beranda_notifikasi`
--
ALTER TABLE `beranda_notifikasi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_notifikasi_penerima_id_9465ef5d_fk_beranda_user_id` (`penerima_id`),
  ADD KEY `beranda_notifikasi_pengirim_id_eefe0108_fk_beranda_user_id` (`pengirim_id`);

--
-- Indeks untuk tabel `beranda_pegawai`
--
ALTER TABLE `beranda_pegawai`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_pegawai_shift_id_451277c8_fk_beranda_jadwal_id` (`shift_id`);

--
-- Indeks untuk tabel `beranda_pelanggan`
--
ALTER TABLE `beranda_pelanggan`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `beranda_pembayaran`
--
ALTER TABLE `beranda_pembayaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_pembayaran_pemesanan_id_67192178_fk_beranda_pemesanan_id` (`pemesanan_id`);

--
-- Indeks untuk tabel `beranda_pemesanan`
--
ALTER TABLE `beranda_pemesanan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_pemesanan_pelanggan_id_f15ec6cf_fk_beranda_pelanggan_id` (`pelanggan_id`),
  ADD KEY `beranda_pemesanan_kamar_id_f9c6e0ce_fk_beranda_kamar_id` (`kamar_id`),
  ADD KEY `beranda_pemesanan_no_kamar_id_id_3f01a983_fk_beranda_n` (`no_kamar_id_id`);

--
-- Indeks untuk tabel `beranda_pengeluaran`
--
ALTER TABLE `beranda_pengeluaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_pengeluaran_pembayaran_id_16038ace_fk_beranda_p` (`pembayaran_id`);

--
-- Indeks untuk tabel `beranda_presensi`
--
ALTER TABLE `beranda_presensi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `beranda_presensi_pegawai_id_6cf95e3d_fk_beranda_pegawai_id` (`pegawai_id`);

--
-- Indeks untuk tabel `beranda_profile`
--
ALTER TABLE `beranda_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `beranda_user`
--
ALTER TABLE `beranda_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `beranda_user_groups`
--
ALTER TABLE `beranda_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beranda_user_groups_user_id_group_id_c9b64251_uniq` (`user_id`,`group_id`),
  ADD KEY `beranda_user_groups_group_id_f47edd6e_fk_auth_group_id` (`group_id`);

--
-- Indeks untuk tabel `beranda_user_user_permissions`
--
ALTER TABLE `beranda_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beranda_user_user_permis_user_id_permission_id_d5afa9d4_uniq` (`user_id`,`permission_id`),
  ADD KEY `beranda_user_user_pe_permission_id_b059efb2_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_beranda_user_id` (`user_id`);

--
-- Indeks untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeks untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT untuk tabel `beranda_jadwal`
--
ALTER TABLE `beranda_jadwal`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `beranda_kamar`
--
ALTER TABLE `beranda_kamar`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `beranda_keuangan`
--
ALTER TABLE `beranda_keuangan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `beranda_kunci`
--
ALTER TABLE `beranda_kunci`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `beranda_nomor_kamar`
--
ALTER TABLE `beranda_nomor_kamar`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT untuk tabel `beranda_notifikasi`
--
ALTER TABLE `beranda_notifikasi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `beranda_pegawai`
--
ALTER TABLE `beranda_pegawai`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT untuk tabel `beranda_pelanggan`
--
ALTER TABLE `beranda_pelanggan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT untuk tabel `beranda_pembayaran`
--
ALTER TABLE `beranda_pembayaran`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT untuk tabel `beranda_pemesanan`
--
ALTER TABLE `beranda_pemesanan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT untuk tabel `beranda_pengeluaran`
--
ALTER TABLE `beranda_pengeluaran`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `beranda_presensi`
--
ALTER TABLE `beranda_presensi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT untuk tabel `beranda_profile`
--
ALTER TABLE `beranda_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `beranda_user`
--
ALTER TABLE `beranda_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT untuk tabel `beranda_user_groups`
--
ALTER TABLE `beranda_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `beranda_user_user_permissions`
--
ALTER TABLE `beranda_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_keuangan`
--
ALTER TABLE `beranda_keuangan`
  ADD CONSTRAINT `beranda_keuangan_pembayaran_id_fe70359a_fk_beranda_pembayaran_id` FOREIGN KEY (`pembayaran_id`) REFERENCES `beranda_pembayaran` (`id`),
  ADD CONSTRAINT `beranda_keuangan_pengeluaran_id_98dc7a89_fk_beranda_p` FOREIGN KEY (`pengeluaran_id`) REFERENCES `beranda_pengeluaran` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_kunci`
--
ALTER TABLE `beranda_kunci`
  ADD CONSTRAINT `beranda_kunci_pemesanan_id_e0bd860c_fk_beranda_pemesanan_id` FOREIGN KEY (`pemesanan_id`) REFERENCES `beranda_pemesanan` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_notifikasi`
--
ALTER TABLE `beranda_notifikasi`
  ADD CONSTRAINT `beranda_notifikasi_penerima_id_9465ef5d_fk_beranda_user_id` FOREIGN KEY (`penerima_id`) REFERENCES `beranda_user` (`id`),
  ADD CONSTRAINT `beranda_notifikasi_pengirim_id_eefe0108_fk_beranda_user_id` FOREIGN KEY (`pengirim_id`) REFERENCES `beranda_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_pegawai`
--
ALTER TABLE `beranda_pegawai`
  ADD CONSTRAINT `beranda_pegawai_shift_id_451277c8_fk_beranda_jadwal_id` FOREIGN KEY (`shift_id`) REFERENCES `beranda_jadwal` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_pembayaran`
--
ALTER TABLE `beranda_pembayaran`
  ADD CONSTRAINT `beranda_pembayaran_pemesanan_id_67192178_fk_beranda_pemesanan_id` FOREIGN KEY (`pemesanan_id`) REFERENCES `beranda_pemesanan` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_pemesanan`
--
ALTER TABLE `beranda_pemesanan`
  ADD CONSTRAINT `beranda_pemesanan_kamar_id_f9c6e0ce_fk_beranda_kamar_id` FOREIGN KEY (`kamar_id`) REFERENCES `beranda_kamar` (`id`),
  ADD CONSTRAINT `beranda_pemesanan_no_kamar_id_id_3f01a983_fk_beranda_n` FOREIGN KEY (`no_kamar_id_id`) REFERENCES `beranda_nomor_kamar` (`id`),
  ADD CONSTRAINT `beranda_pemesanan_pelanggan_id_f15ec6cf_fk_beranda_pelanggan_id` FOREIGN KEY (`pelanggan_id`) REFERENCES `beranda_pelanggan` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_pengeluaran`
--
ALTER TABLE `beranda_pengeluaran`
  ADD CONSTRAINT `beranda_pengeluaran_pembayaran_id_16038ace_fk_beranda_p` FOREIGN KEY (`pembayaran_id`) REFERENCES `beranda_pembayaran` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_presensi`
--
ALTER TABLE `beranda_presensi`
  ADD CONSTRAINT `beranda_presensi_pegawai_id_6cf95e3d_fk_beranda_pegawai_id` FOREIGN KEY (`pegawai_id`) REFERENCES `beranda_pegawai` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_profile`
--
ALTER TABLE `beranda_profile`
  ADD CONSTRAINT `beranda_profile_user_id_2840018a_fk_beranda_user_id` FOREIGN KEY (`user_id`) REFERENCES `beranda_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_user_groups`
--
ALTER TABLE `beranda_user_groups`
  ADD CONSTRAINT `beranda_user_groups_group_id_f47edd6e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `beranda_user_groups_user_id_21e0827a_fk_beranda_user_id` FOREIGN KEY (`user_id`) REFERENCES `beranda_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `beranda_user_user_permissions`
--
ALTER TABLE `beranda_user_user_permissions`
  ADD CONSTRAINT `beranda_user_user_pe_permission_id_b059efb2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `beranda_user_user_pe_user_id_086b999b_fk_beranda_u` FOREIGN KEY (`user_id`) REFERENCES `beranda_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_beranda_user_id` FOREIGN KEY (`user_id`) REFERENCES `beranda_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
