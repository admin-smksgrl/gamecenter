<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Rekening Transfer Manual
    |--------------------------------------------------------------------------
    |
    | Tujuan transfer yang ditampilkan pada halaman keanggotaan setelah user
    | mengajukan upgrade. Admin memverifikasi mutasi lalu menyetujui pengajuan
    | dari panel Filament.
    |
    */

    'bank' => [
        'name' => env('MEMBERSHIP_BANK_NAME', 'Bank BCA'),
        'account_number' => env('MEMBERSHIP_BANK_NUMBER', '1234567890'),
        'account_holder' => env('MEMBERSHIP_BANK_HOLDER', 'Yayasan Ruang Belajar'),
    ],

];
