import { Link } from '@inertiajs/react';
import type { ReactNode } from 'react';

import { formatRupiah } from '@/lib/utils';

import MermaidDiagram from './MermaidDiagram';
import { Callout, DataTable, H2, H3, Kbd, Steps } from './primitives';

export interface GuideHeading {
    id: string;
    label: string;
}

export interface GuidePage {
    slug: string;
    title: string;
    group: string;
    summary: string;
    keywords: string[];
    updated: string;
    headings: GuideHeading[];
    content: ReactNode;
}

export const GUIDE_GROUPS = [
    'Mulai',
    'Akun & keanggotaan',
    'Guru & admin',
    'Bantuan',
] as const;

const upgradeChart = `flowchart LR
    subgraph P["Pengajuan"]
        direction TB
        A["Anggota Gratis"] --> B["Pilih paket"] --> C["Kirim pengajuan"] --> D["Kode GC-XXXXXX"]
    end
    subgraph V["Verifikasi admin"]
        direction TB
        E["Transfer bank"] --> F{"Verifikasi"}
        F -->|"Setujui"| G["Paket aktif"] --> I["Paket lama kedaluwarsa"]
        F -->|"Tolak"| H["Ditolak + catatan"]
    end
    D --> E`;

const playChart = `flowchart LR
    A["Tombol Bermain"] --> B{"Pilih mode"}
    B -->|"Pribadi"| C["Tulis satu nama pemain"]
    B -->|"Kelompok"| D["Nama kelompok dan 2-8 pemain"]
    C --> E["Sesi aktif di topbar"]
    D --> E
    E --> F["Pilih mapel dan bab"]`;

export const GUIDE_PAGES: GuidePage[] = [
    {
        slug: 'pengenalan',
        title: 'Pengenalan Ruang Belajar',
        group: 'Mulai',
        summary:
            'Apa itu Ruang Belajar, siapa saja penggunanya, dan ke mana harus mulai.',
        keywords: [
            'pengenalan',
            'beranda',
            'tamu',
            'siswa',
            'guru',
            'admin',
            'peran',
            'mulai',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'apa-itu', label: 'Apa itu Ruang Belajar?' },
            { id: 'peran', label: 'Peta peran dan akses' },
            { id: 'mulai-cepat', label: 'Mulai dalam tiga langkah' },
        ],
        content: (
            <>
                <H2 id="apa-itu">Apa itu Ruang Belajar?</H2>
                <p>
                    <strong>Ruang Belajar — Game Center</strong> adalah ruang
                    belajar berbasis permainan untuk jenjang PAUD sampai SMK.
                    Materi disusun per jenjang, kelas, dan mata pelajaran,
                    lengkap dengan bab serta latihan bertingkat.
                </p>
                <ul>
                    <li>
                        <strong>Jelajah materi</strong> — pilih jenjang, kelas,
                        dan mode permainan dari topbar.
                    </li>
                    <li>
                        <strong>Bermain</strong> — main pribadi dengan satu nama
                        pemain atau kelompok berisi 2–8 pemain.
                    </li>
                    <li>
                        <strong>Keanggotaan</strong> — akun memiliki paket
                        Gratis otomatis dan dapat mengajukan paket berbayar.
                    </li>
                    <li>
                        <strong>Panel guru/admin</strong> — kelola materi, paket,
                        dan pengajuan keanggotaan lewat Filament.
                    </li>
                </ul>
                <Callout tone="tips" title="Tamu bisa langsung bermain">
                    <p>
                        Kamu tidak wajib punya akun untuk menjelajah materi dan
                        bermain. Akun diperlukan untuk mengajukan keanggotaan
                        berbayar dan tampil dengan identitas di topbar.
                    </p>
                </Callout>

                <H2 id="peran">Peta peran dan akses</H2>
                <p>
                    Hak akses ditentukan oleh peran akun. Tamu tetap dapat
                    mencoba hampir seluruh pengalaman bermain.
                </p>
                <DataTable
                    caption="Hubungan peran pengguna dengan fitur utama."
                    head={['Peran', 'Bisa melakukan']}
                    rows={[
                        [
                            <strong key="tamu">Tamu</strong>,
                            'Menjelajah katalog, mencari materi, bermain pribadi/kelompok, membuka halaman keanggotaan.',
                        ],
                        [
                            <strong key="siswa">Siswa</strong>,
                            'Semua akses tamu, ditambah pengajuan dan pemantauan keanggotaan.',
                        ],
                        [
                            <strong key="guru">Guru</strong>,
                            'Semua akses siswa, ditambah masuk panel Filament untuk mengelola materi.',
                        ],
                        [
                            <strong key="admin">Admin</strong>,
                            'Semua akses guru, ditambah pengelolaan paket dan verifikasi pengajuan keanggotaan.',
                        ],
                    ]}
                />

                <H2 id="mulai-cepat">Mulai dalam tiga langkah</H2>
                <Steps
                    steps={[
                        <>
                            Buka <Link href="/">Beranda</Link>, lalu pilih
                            jenjang, kelas, dan mode permainan pada menu topbar.
                        </>,
                        <>
                            Tekan tombol <strong>Bermain</strong> untuk memulai
                            sesi pribadi atau kelompok, lalu pilih kartu mapel.
                        </>,
                        <>
                            Ingin paket berbayar?{' '}
                            <Link href="/daftar">Daftar akun</Link>, lalu ajukan
                            upgrade dari <Link href="/keanggotaan">halaman
                            keanggotaan</Link>.
                        </>,
                    ]}
                />
            </>
        ),
    },
    {
        slug: 'menjelajah-materi',
        title: 'Menjelajah materi',
        group: 'Mulai',
        summary:
            'Memakai menu jenjang, kelas, mode permainan, pencarian, dan panel bab.',
        keywords: [
            'materi',
            'katalog',
            'jenjang',
            'kelas',
            'mapel',
            'mode',
            'pencarian',
            'pagination',
            'bab',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'pilih-filter', label: 'Pilih jenjang, kelas, mode' },
            { id: 'cari', label: 'Cari materi lebih cepat' },
            { id: 'buka-bab', label: 'Membuka bab dan latihan' },
            { id: 'halaman', label: 'Pagination dan jumlah kartu' },
        ],
        content: (
            <>
                <H2 id="pilih-filter">Pilih jenjang, kelas, dan mode</H2>
                <p>
                    Semua filter utama berada di <strong>menu topbar</strong>:
                    jenjang, kelas, dan mode permainan. Nilai yang sedang aktif
                    selalu terlihat pada tombol menu, sehingga area konten bisa
                    dipenuhi kartu materi.
                </p>
                <ol>
                    <li>Buka menu <strong>Jenjang</strong> dan pilih PAUD–SMK.</li>
                    <li>
                        Pilih <strong>Kelas</strong> yang sesuai. Daftar kelas
                        mengikuti jenjang yang aktif.
                    </li>
                    <li>
                        Tentukan <strong>Mode permainan</strong> untuk melihat
                        jumlah soal pada tiap mapel.
                    </li>
                </ol>
                <Callout tone="catatan" title="Kartu tanpa konten">
                    <p>
                        Mapel yang belum memiliki bab tetap tampil dengan label
                        <strong> Segera</strong> agar katalog terlihat utuh dan
                        mudah direncanakan.
                    </p>
                </Callout>

                <H2 id="cari">Cari materi lebih cepat</H2>
                <p>
                    Tekan ikon pencarian di topbar atau pintasan <Kbd>/</Kbd>{' '}
                    untuk membuka palet pencarian. Ketik nama mapel atau bab,
                    lalu pilih hasilnya. Tekan <Kbd>Esc</Kbd> untuk menutup
                    palet.
                </p>

                <H2 id="buka-bab">Membuka bab dan latihan</H2>
                <p>
                    Klik kartu mapel untuk membuka panel bab di sisi kanan.
                    Setiap bab menampilkan jumlah materi dan assessment. Di
                    ponsel, panel ini tampil selebar layar agar mudah dibaca.
                </p>
                <ul>
                    <li>
                        Tingkat kesulitan latihan dibedakan lewat penanda
                        merah/hitam.
                    </li>
                    <li>
                        Jumlah soal pada kartu mengikuti mode permainan yang
                        sedang aktif.
                    </li>
                </ul>

                <H2 id="halaman">Pagination dan jumlah kartu</H2>
                <p>
                    Ringkasan seperti <strong>“Menampilkan 1–12 dari 133
                    mapel”</strong> dan tombol halaman menyatu di footer. Jumlah
                    kartu per halaman menyesuaikan tinggi layar, dan halaman
                    otomatis kembali ke 1 saat jenjang, kelas, rumpun, atau
                    pencarian berubah.
                </p>
            </>
        ),
    },
    {
        slug: 'bermain',
        title: 'Bermain pribadi & kelompok',
        group: 'Mulai',
        summary:
            'Membuat sesi main pribadi, bermain kelompok 2–8 pemain, dan mengakhiri sesi aktif.',
        keywords: [
            'bermain',
            'main',
            'pribadi',
            'kelompok',
            'sesi',
            'pemain',
            'localstorage',
            'akhiri',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'pribadi', label: 'Main pribadi' },
            { id: 'kelompok', label: 'Bermain kelompok' },
            { id: 'sesi', label: 'Sesi aktif dan penyimpanan' },
        ],
        content: (
            <>
                <p>
                    Tombol merah <strong>Bermain</strong> di topbar membuka dua
                    mode sesi. Sesi aktif selalu terlihat di topbar supaya kamu
                    tahu sedang bermain sebagai siapa.
                </p>
                <MermaidDiagram
                    chart={playChart}
                    caption="Dua jalur pembuatan sesi bermain."
                />

                <H2 id="pribadi">Main pribadi</H2>
                <Steps
                    steps={[
                        'Tekan tombol Bermain di topbar, lalu pilih Main pribadi.',
                        'Tulis satu nama pemain. Nama ini yang tampil pada sesi aktif.',
                        'Mulai bermain: pilih kartu mapel dan buka bab yang diinginkan.',
                    ]}
                />

                <H2 id="kelompok">Bermain kelompok</H2>
                <Steps
                    steps={[
                        'Tekan Bermain, lalu pilih Bermain kelompok.',
                        'Isi nama kelompok dan masukkan 2–8 nama pemain. Gunakan tombol tambah/hapus baris sesuai kebutuhan.',
                        'Mulai sesi; topbar menampilkan nama kelompok dan jumlah pemain.',
                    ]}
                />
                <Callout tone="penting" title="Batas pemain">
                    <p>
                        Satu kelompok menerima minimal 2 dan maksimal 8 pemain.
                        Batas ini berlaku untuk semua paket keanggotaan.
                    </p>
                </Callout>

                <H2 id="sesi">Sesi aktif dan penyimpanan</H2>
                <p>
                    Sesi disimpan di <strong>localStorage</strong> peramban
                    dengan kunci <code>gamecenter.play-session</code>, sehingga
                    tetap ada setelah halaman dimuat ulang. Sesi tidak
                    tersinkron ke akun dan tidak terbawa ke perangkat lain.
                </p>
                <ul>
                    <li>
                        Buka menu <strong>Bermain</strong> lagi untuk melihat
                        ringkasan sesi.
                    </li>
                    <li>
                        Pilih <strong>Akhiri sesi</strong> untuk menghapus sesi
                        aktif.
                    </li>
                    <li>
                        Mode penyamaran atau pembersihan data situs akan
                        menghapus sesi lebih cepat.
                    </li>
                </ul>
            </>
        ),
    },
    {
        slug: 'akun',
        title: 'Daftar dan masuk',
        group: 'Akun & keanggotaan',
        summary:
            'Membuat akun siswa, masuk dengan email atau username, dan keluar dengan aman.',
        keywords: [
            'akun',
            'daftar',
            'register',
            'masuk',
            'login',
            'keluar',
            'logout',
            'password',
            'username',
            'email',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'membuat-akun', label: 'Membuat akun' },
            { id: 'masuk', label: 'Masuk dengan email atau username' },
            { id: 'keluar', label: 'Keluar dari akun' },
            { id: 'keamanan', label: 'Keamanan akun' },
        ],
        content: (
            <>
                <H2 id="membuat-akun">Membuat akun</H2>
                <p>
                    Buka halaman <Link href="/daftar">Daftar</Link>. Isi nama
                    lengkap, username, email, dan kata sandi minimal 8 karakter
                    beserta konfirmasinya. Akun baru otomatis berperan{' '}
                    <strong>siswa</strong> dan langsung masuk setelah
                    pendaftaran berhasil.
                </p>
                <DataTable
                    head={['Kolom', 'Ketentuan']}
                    rows={[
                        ['Nama lengkap', 'Nama yang tampil di menu akun.'],
                        [
                            'Username',
                            'Unik, dipakai sebagai alternatif saat masuk.',
                        ],
                        ['Email', 'Unik dan valid, dapat dipakai untuk masuk.'],
                        [
                            'Kata sandi',
                            'Minimal 8 karakter dan harus sama dengan konfirmasi.',
                        ],
                    ]}
                />

                <H2 id="masuk">Masuk dengan email atau username</H2>
                <p>
                    Di halaman <Link href="/masuk">Masuk</Link>, isi kolom
                    “Email atau username”. Sistem mendeteksi otomatis apakah
                    isian berupa email atau username.
                </p>
                <ul>
                    <li>
                        Maksimal <strong>5 percobaan gagal</strong> per
                        kombinasi login dan alamat IP. Setelah itu, tunggu
                        hitungan detik yang tertera sebelum mencoba lagi.
                    </li>
                    <li>
                        Akun yang dinonaktifkan admin tidak dapat masuk meskipun
                        kata sandinya benar.
                    </li>
                    <li>
                        Jika kamu membuka halaman terkunci sebagai tamu, kamu
                        akan dikembalikan ke halaman tersebut setelah masuk.
                    </li>
                </ul>

                <H2 id="keluar">Keluar dari akun</H2>
                <p>
                    Buka menu akun di kanan topbar, lalu pilih{' '}
                    <strong>Keluar</strong>. Sesi server dihapus dan token
                    keamanan diperbarui.
                </p>

                <H2 id="keamanan">Keamanan akun</H2>
                <ul>
                    <li>Gunakan kata sandi unik yang tidak dipakai di layanan lain.</li>
                    <li>
                        Jangan bagikan kredensial. Guru dan admin tidak pernah
                        meminta kata sandi melalui pesan.
                    </li>
                    <li>
                        Fitur atur ulang kata sandi mandiri belum tersedia;
                        hubungi guru atau admin untuk bantuan.
                    </li>
                </ul>
            </>
        ),
    },
    {
        slug: 'paket',
        title: 'Paket keanggotaan',
        group: 'Akun & keanggotaan',
        summary:
            'Perbandingan paket Gratis, Standard, Professional, dan Enterprise beserta siklus tagihannya.',
        keywords: [
            'paket',
            'keanggotaan',
            'membership',
            'gratis',
            'standard',
            'professional',
            'enterprise',
            'harga',
            'bulanan',
            'tahunan',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'daftar-paket', label: 'Empat paket' },
            { id: 'siklus', label: 'Siklus bulanan dan tahunan' },
            { id: 'paket-gratis', label: 'Gratis aktif otomatis' },
        ],
        content: (
            <>
                <H2 id="daftar-paket">Empat paket</H2>
                <p>
                    Harga di bawah adalah nilai awal yang disemai. Admin dapat
                    memperbaruinya kapan saja; nominal yang ditagihkan selalu
                    mengikuti harga saat pengajuan dibuat.
                </p>
                <DataTable
                    head={['Paket', 'Bulanan', 'Tahunan', 'Sasaran']}
                    rows={[
                        [
                            <strong key="free">Gratis</strong>,
                            formatRupiah(0),
                            formatRupiah(0),
                            'Semua pengunjung',
                        ],
                        [
                            <strong key="standard">Standard</strong>,
                            formatRupiah(29000),
                            formatRupiah(290000),
                            'Pelajar perorangan',
                        ],
                        [
                            <strong key="professional">Professional</strong>,
                            formatRupiah(99000),
                            formatRupiah(990000),
                            'Guru / kelas aktif',
                        ],
                        [
                            <strong key="enterprise">Enterprise</strong>,
                            formatRupiah(499000),
                            formatRupiah(4990000),
                            'Sekolah / lembaga',
                        ],
                    ]}
                />
                <Callout tone="catatan" title="Benefit bertanda (segera)">
                    <p>
                        Fitur seperti riwayat hasil di akun, ruang guru, dan
                        laporan kelas sedang disiapkan bertahap. Benefit yang
                        sudah berjalan saat ini adalah status anggota, badge
                        paket, dan dukungan terkait keanggotaan.
                    </p>
                </Callout>

                <H2 id="siklus">Siklus bulanan dan tahunan</H2>
                <p>
                    Setiap paket berbayar memiliki dua siklus. Harga tahunan
                    sama dengan <strong>10× harga bulanan</strong>, sehingga dua
                    bulan efektif gratis dibanding membayar bulanan.
                </p>
                <ul>
                    <li>
                        Masa aktif dihitung dari waktu persetujuan admin, bukan
                        dari waktu pengajuan.
                    </li>
                    <li>
                        Paket bulanan aktif selama 1 bulan; paket tahunan aktif
                        selama 12 bulan.
                    </li>
                    <li>
                        Harga dan siklus disalin ke data pengajuan sebagai
                        snapshot agar riwayat tidak berubah saat admin mengedit
                        katalog.
                    </li>
                </ul>

                <H2 id="paket-gratis">Gratis aktif otomatis</H2>
                <p>
                    Semua akun—dan seluruh pengunjung—mendapat akses paket
                    Gratis tanpa pengajuan. Paket berbayar menandai status
                    anggota dan menyiapkan akses fitur tambahan pada fase
                    berikutnya. Paket Gratis tidak dapat diajukan karena sudah
                    menjadi bawaan akun.
                </p>
            </>
        ),
    },
    {
        slug: 'upgrade',
        title: 'Alur upgrade paket',
        group: 'Akun & keanggotaan',
        summary:
            'Dari memilih paket sampai transfer bank dan persetujuan admin, langkah demi langkah.',
        keywords: [
            'upgrade',
            'pengajuan',
            'transfer',
            'bank',
            'referensi',
            'admin',
            'setujui',
            'bayar',
            'profesional',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'prasyarat', label: 'Prasyarat' },
            { id: 'diagram', label: 'Diagram alur' },
            { id: 'langkah', label: 'Langkah demi langkah' },
            { id: 'aturan', label: 'Aturan yang berlaku' },
        ],
        content: (
            <>
                <H2 id="prasyarat">Prasyarat</H2>
                <ul>
                    <li>Sudah masuk ke akun (bukan tamu).</li>
                    <li>Tidak sedang memiliki pengajuan berstatus pending.</li>
                    <li>
                        Paket tujuan berbayar dan <strong>lebih tinggi</strong>{' '}
                        dari paket aktif saat ini.
                    </li>
                </ul>

                <H2 id="diagram">Diagram alur</H2>
                <MermaidDiagram
                    chart={upgradeChart}
                    caption="Alur upgrade manual dengan persetujuan admin."
                />

                <H2 id="langkah">Langkah demi langkah</H2>
                <Steps
                    steps={[
                        <>
                            Buka <Link href="/keanggotaan">Keanggotaan</Link>.
                            Anggota Gratis dapat menekan{' '}
                            <strong>Upgrade sekarang</strong> di hero atau{' '}
                            <strong>Upgrade keanggotaan</strong> dari menu akun.
                        </>,
                        'Pilih siklus Bulanan atau Tahunan. Kartu paket menampilkan harga sesuai siklus.',
                        'Tekan CTA pada kartu paket. Dialog pengajuan menampilkan rekening yayasan, nominal, dan kolom catatan opsional.',
                        'Kirim pengajuan. Sistem membuat kode referensi unik berformat GC-XXXXXX.',
                        'Transfer nominal tepat sesuai yang tertera. Cantumkan kode referensi pada berita transfer.',
                        'Tunggu admin memverifikasi. Status pengajuan tampil di banner halaman keanggotaan.',
                    ]}
                />
                <Callout tone="penting" title="Hanya transfer ke rekening resmi">
                    <p>
                        Rekening tujuan selalu ditampilkan di halaman
                        keanggotaan dan diatur oleh admin melalui konfigurasi
                        sistem. Jangan mentransfer ke rekening pribadi yang
                        dikirim lewat pesan tidak resmi.
                    </p>
                </Callout>

                <H2 id="aturan">Aturan yang berlaku</H2>
                <ul>
                    <li>
                        Hanya boleh ada <strong>satu pengajuan pending</strong>{' '}
                        per akun.
                    </li>
                    <li>
                        Paket tujuan harus lebih tinggi dari paket aktif. Paket
                        setara atau lebih rendah ditolak server.
                    </li>
                    <li>
                        Nominal dan siklus disimpan sebagai snapshot saat
                        pengajuan dibuat.
                    </li>
                    <li>
                        Admin dapat menyetujui atau menolak. Penolakan wajib
                        disertai catatan alasan.
                    </li>
                    <li>
                        Saat disetujui, paket aktif lama otomatis kedaluwarsa,
                        dan paket baru mulai berlaku pada waktu persetujuan.
                    </li>
                </ul>
            </>
        ),
    },
    {
        slug: 'status',
        title: 'Status & riwayat keanggotaan',
        group: 'Akun & keanggotaan',
        summary:
            'Arti status pending, active, expired, dan rejected, serta cara memperpanjang atau naik paket.',
        keywords: [
            'status',
            'pending',
            'active',
            'expired',
            'rejected',
            'riwayat',
            'perpanjang',
            'tolak',
            'kode referensi',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'arti-status', label: 'Arti setiap status' },
            { id: 'riwayat', label: 'Paket aktif dan riwayat' },
            { id: 'lanjutan', label: 'Memperpanjang atau naik paket' },
            { id: 'ditolak', label: 'Jika pengajuan ditolak' },
        ],
        content: (
            <>
                <H2 id="arti-status">Arti setiap status</H2>
                <DataTable
                    head={['Status', 'Artinya', 'Tindakan']}
                    rows={[
                        [
                            <strong key="pending">Pending</strong>,
                            'Pengajuan sudah masuk dan menunggu verifikasi admin.',
                            'Transfer sesuai nominal, lalu tunggu. Kode referensi dapat disalin dari banner.',
                        ],
                        [
                            <strong key="active">Active</strong>,
                            'Paket sedang berlaku dan tercatat pada akun.',
                            'Nikmati akses paket; periksa tanggal berakhir di menu akun.',
                        ],
                        [
                            <strong key="expired">Expired</strong>,
                            'Masa aktif paket sudah berakhir.',
                            'Ajukan paket baru bila diperlukan; akun kembali memakai paket Gratis.',
                        ],
                        [
                            <strong key="rejected">Rejected</strong>,
                            'Pengajuan ditolak admin dengan catatan alasan.',
                            'Baca catatan admin, perbaiki, lalu kirim pengajuan baru.',
                        ],
                    ]}
                />

                <H2 id="riwayat">Paket aktif dan riwayat</H2>
                <p>
                    Menu akun menampilkan badge paket beserta tanggal berakhir
                    bila paket berbayar sedang aktif. Halaman keanggotaan
                    menampilkan hingga 12 riwayat terakhir untuk status active,
                    expired, dan rejected.
                </p>

                <H2 id="lanjutan">Memperpanjang atau naik paket</H2>
                <ul>
                    <li>
                        <strong>Naik paket</strong> dapat diajukan selama paket
                        aktif belum memasuki tier tujuan. Paket sebelumnya
                        otomatis kedaluwarsa saat persetujuan.
                    </li>
                    <li>
                        <strong>Perpanjangan paket yang sama</strong> dan
                        penurunan paket belum tersedia lewat layanan mandiri.
                        Hubungi admin untuk pengaturan khusus.
                    </li>
                    <li>
                        Setelah paket kedaluwarsa, pengajuan baru dapat dibuat
                        kembali karena perhitungan tier kembali ke paket Gratis.
                    </li>
                </ul>

                <H2 id="ditolak">Jika pengajuan ditolak</H2>
                <p>
                    Status akan berubah menjadi <strong>rejected</strong> dan
                    catatan admin tampil pada riwayat. Pengajuan baru bisa
                    dikirim setelah membaca catatan tersebut. Pastikan bukti
                    transfer dan kode referensi sudah benar agar verifikasi
                    berikutnya lebih lancar.
                </p>
            </>
        ),
    },
    {
        slug: 'panel-admin',
        title: 'Panel guru & admin',
        group: 'Guru & admin',
        summary:
            'Akses panel Filament, pembagian peran, dan pengelolaan katalog paket.',
        keywords: [
            'panel',
            'admin',
            'guru',
            'filament',
            'resource',
            'paket',
            'kelola',
            '403',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'akses', label: 'Masuk ke panel' },
            { id: 'peran', label: 'Peran di panel' },
            { id: 'kelola-paket', label: 'Mengelola paket' },
        ],
        content: (
            <>
                <H2 id="akses">Masuk ke panel</H2>
                <p>
                    Panel tersedia di <code>/admin</code> dan memakai kredensial
                    akun yang sama. Hanya akun berperan{' '}
                    <strong>guru</strong> atau <strong>admin</strong> yang aktif
                    yang dapat masuk. Siswa akan menerima halaman 403.
                </p>

                <H2 id="peran">Peran di panel</H2>
                <DataTable
                    head={['Peran', 'Akses panel']}
                    rows={[
                        [
                            <strong key="admin">Admin</strong>,
                            'Seluruh menu, termasuk Keanggotaan: paket dan pengajuan upgrade.',
                        ],
                        [
                            <strong key="teacher">Guru</strong>,
                            'Panel materi dan pengaturan profil; menu Keanggotaan tidak tampil.',
                        ],
                        [
                            <strong key="student">Siswa</strong>,
                            'Tidak memiliki akses panel.',
                        ],
                    ]}
                />

                <H2 id="kelola-paket">Mengelola paket</H2>
                <p>
                    Admin membuka grup <strong>Keanggotaan → Paket</strong>.
                    Daftar paket menampilkan harga, status unggulan, dan
                    urutan. Lewat aksi edit, admin dapat mengubah nama, slug,
                    tier, harga bulanan/tahunan, daftar fitur, status unggulan,
                    status aktif, dan urutan tampil.
                </p>
                <ul>
                    <li>Harga disimpan sebagai bilangan bulat rupiah tanpa desimal.</li>
                    <li>Paket nonaktif tidak muncul di katalog publik.</li>
                    <li>Perubahan harga tidak mengubah pengajuan yang sudah ada.</li>
                </ul>
                <Callout tone="catatan" title="Urutan tampil">
                    Paket diurutkan memakai kolom urutan. Nilai lebih kecil
                    tampil lebih dahulu di halaman keanggotaan.
                </Callout>
            </>
        ),
    },
    {
        slug: 'verifikasi',
        title: 'Memverifikasi pengajuan',
        group: 'Guru & admin',
        summary:
            'Menyetujui atau menolak pengajuan upgrade di panel admin beserta efeknya.',
        keywords: [
            'verifikasi',
            'persetujuan',
            'approve',
            'reject',
            'pengajuan',
            'antrean',
            'admin_note',
            'badge',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'antrean', label: 'Antrean pengajuan' },
            { id: 'setujui', label: 'Menyetujui pengajuan' },
            { id: 'tolak', label: 'Menolak pengajuan' },
            { id: 'efek', label: 'Efek persetujuan' },
        ],
        content: (
            <>
                <p>
                    Hanya admin yang melihat menu ini. Badge angka pada navigasi
                    menunjukkan jumlah pengajuan berstatus pending.
                </p>

                <H2 id="antrean">Antrean pengajuan</H2>
                <p>
                    Buka <strong>Keanggotaan → Pengajuan upgrade</strong>. Tabel
                    menampilkan pengguna, paket tujuan, siklus, nominal, status,
                    kode referensi yang dapat disalin, dan waktu pengajuan.
                    Gunakan filter status untuk berfokus pada antrean pending.
                </p>

                <H2 id="setujui">Menyetujui pengajuan</H2>
                <Steps
                    steps={[
                        'Pastikan dana sudah masuk ke rekening yayasan dan nominalnya sesuai snapshot pengajuan.',
                        'Buka aksi Setujui pada baris pengajuan.',
                        'Isi catatan admin bila perlu (opsional), lalu konfirmasi Setujui.',
                        'Sistem mengaktifkan paket dalam satu transaksi dan menampilkan notifikasi hasil.',
                    ]}
                />

                <H2 id="tolak">Menolak pengajuan</H2>
                <Steps
                    steps={[
                        'Buka aksi Tolak pada baris pengajuan.',
                        'Tulis catatan admin yang menjelaskan alasan penolakan. Kolom ini wajib diisi.',
                        'Konfirmasi Tolak pengajuan.',
                        'Status berubah menjadi rejected dan catatan tampil di riwayat pengguna.',
                    ]}
                />

                <H2 id="efek">Efek persetujuan</H2>
                <ul>
                    <li>Status pengajuan berubah menjadi active.</li>
                    <li>
                        Masa aktif dimulai saat persetujuan dan berakhir sesuai
                        siklus (1 atau 12 bulan).
                    </li>
                    <li>Paket aktif sebelumnya otomatis berstatus expired.</li>
                    <li>
                        Waktu dan admin yang menyetujui tercatat untuk jejak
                        audit.
                    </li>
                </ul>
                <Callout tone="penting" title="Satu transaksi">
                    <p>
                        Aktivasi paket baru dan kedaluwarsanya paket lama
                        dijalankan dalam satu transaksi database. Jika salah
                        satu gagal, tidak ada perubahan yang tersimpan
                        setengah jalan.
                    </p>
                </Callout>
            </>
        ),
    },
    {
        slug: 'faq',
        title: 'Pertanyaan umum',
        group: 'Bantuan',
        summary:
            'Jawaban singkat untuk pertanyaan yang paling sering muncul.',
        keywords: [
            'faq',
            'pertanyaan',
            'bantuan',
            'akun',
            'gratis',
            'bayar',
            'ganti password',
            'tamu',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'akun-faq', label: 'Akun' },
            { id: 'bermain-faq', label: 'Bermain' },
            { id: 'anggota-faq', label: 'Keanggotaan' },
        ],
        content: (
            <>
                <H2 id="akun-faq">Akun</H2>
                <H3>Apakah harus punya akun untuk bermain?</H3>
                <p>
                    Tidak. Tamu dapat menjelajah materi dan bermain. Akun
                    diperlukan untuk mengajukan keanggotaan berbayar dan tampil
                    dengan identitas di topbar.
                </p>
                <H3>Bisakah masuk memakai username?</H3>
                <p>
                    Bisa. Kolom masuk menerima email atau username, dan sistem
                    mendeteksi jenisnya otomatis.
                </p>
                <H3>Bagaimana cara mengganti kata sandi?</H3>
                <p>
                    Pengaturan mandiri belum tersedia. Hubungi guru atau admin;
                    mereka dapat membantu proses pemulihan akun.
                </p>

                <H2 id="bermain-faq">Bermain</H2>
                <H3>Berapa pemain maksimal dalam satu kelompok?</H3>
                <p>
                    Minimal 2 dan maksimal 8 pemain. Jumlah ini sama untuk semua
                    paket keanggotaan.
                </p>
                <H3>Mengapa sesi bermain hilang?</H3>
                <p>
                    Sesi disimpan di localStorage peramban. Mode penyamaran,
                    pembersihan data situs, atau perangkat lain akan memulai
                    sesi baru.
                </p>

                <H2 id="anggota-faq">Keanggotaan</H2>
                <H3>Apakah paket Gratis perlu diajukan?</H3>
                <p>
                    Tidak. Paket Gratis aktif otomatis untuk semua akun. Kamu
                    hanya mengajukan paket berbayar yang lebih tinggi.
                </p>
                <H3>Kenapa tombol upgrade tidak bisa dipakai?</H3>
                <p>
                    Kemungkinan penyebab: masih ada pengajuan pending, paket
                    tujuan setara/lebih rendah, atau kamu belum masuk. Periksa
                    banner status dan menu akun.
                </p>
                <H3>Apakah pembayaran otomatis?</H3>
                <p>
                    Belum. Pembayaran memakai transfer manual ke rekening
                    yayasan, lalu admin menyetujui pengajuan. Kode referensi
                    membantu admin mencocokkan transfer.
                </p>
                <H3>Bisakah turun paket?</H3>
                <p>
                    Penurunan paket belum tersedia lewat layanan mandiri.
                    Hubungi admin untuk kebutuhan khusus.
                </p>
            </>
        ),
    },
    {
        slug: 'masalah-umum',
        title: 'Masalah umum',
        group: 'Bantuan',
        summary:
            'Langkah cepat saat login, panel, pengajuan, atau tampilan tidak berjalan seperti seharusnya.',
        keywords: [
            'masalah',
            'error',
            'tidak bisa',
            'login',
            '403',
            'diagram',
            'gelap',
            'terang',
            'hilang',
            'bantuan',
        ],
        updated: '15 November 2026',
        headings: [
            { id: 'login', label: 'Tidak bisa masuk' },
            { id: 'panel', label: 'Panel tidak bisa dibuka' },
            { id: 'pengajuan', label: 'Pengajuan upgrade gagal' },
            { id: 'tampilan', label: 'Tampilan dan diagram' },
            { id: 'kontak', label: 'Menghubungi pengelola' },
        ],
        content: (
            <>
                <H2 id="login">Tidak bisa masuk</H2>
                <ul>
                    <li>Pastikan email atau username tidak salah ketik.</li>
                    <li>
                        Periksa pesan “terlalu banyak percobaan”. Tunggu sesuai
                        hitungan detik sebelum mencoba lagi.
                    </li>
                    <li>
                        Akun yang dinonaktifkan tidak dapat masuk; hubungi admin
                        untuk mengaktifkan kembali.
                    </li>
                </ul>

                <H2 id="panel">Panel tidak bisa dibuka</H2>
                <p>
                    Panel di <code>/admin</code> hanya untuk guru dan admin yang
                    aktif. Akun siswa akan mendapat 403. Jika kamu guru tetapi
                    tetap ditolak, pastikan akun tidak dinonaktifkan.
                </p>

                <H2 id="pengajuan">Pengajuan upgrade gagal</H2>
                <ul>
                    <li>Paket Gratis tidak dapat diajukan.</li>
                    <li>Paket tujuan harus lebih tinggi dari paket aktif.</li>
                    <li>Selesaikan atau tunggu pengajuan pending yang ada.</li>
                    <li>Pastikan paket yang dituju masih aktif di katalog.</li>
                </ul>

                <H2 id="tampilan">Tampilan dan diagram</H2>
                <ul>
                    <li>
                        Muat ulang halaman bila tema gelap/terang tidak langsung
                        berubah; preferensi disimpan di peramban yang sama.
                    </li>
                    <li>
                        Diagram Mermaid memerlukan JavaScript. Bila gagal
                        dimuat, penjelasan teks di sekitar diagram tetap dapat
                        dibaca.
                    </li>
                    <li>
                        Gunakan peramban modern (Chrome, Edge, Firefox, Safari)
                        versi terbaru.
                    </li>
                </ul>

                <H2 id="kontak">Menghubungi pengelola</H2>
                <p>
                    Untuk masalah akun atau pembayaran, hubungi guru/admin
                    sekolah. Sertakan <strong>username</strong> dan{' '}
                    <strong>kode referensi</strong> (bila ada) agar penanganan
                    lebih cepat.
                </p>
            </>
        ),
    },
];

export function findGuidePage(slug?: string | null): GuidePage | null {
    if (!slug) {
        return null;
    }

    return GUIDE_PAGES.find((page) => page.slug === slug) ?? null;
}

export function guideNeighbours(slug: string): {
    previous: GuidePage | null;
    next: GuidePage | null;
} {
    const index = GUIDE_PAGES.findIndex((page) => page.slug === slug);

    return {
        previous: index > 0 ? GUIDE_PAGES[index - 1] : null,
        next:
            index >= 0 && index < GUIDE_PAGES.length - 1
                ? GUIDE_PAGES[index + 1]
                : null,
    };
}
