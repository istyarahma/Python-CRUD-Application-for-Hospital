data_pasien = [
    {'ID Pasien': 'PE1', 'Nama': 'Retno Eko', 'Usia': 32, 'Jenis Kelamin': 'P', 'Domisili': 'Jakarta', 'Berat Badan': 70, 'Tinggi Badan': 160, 'Poli': 'Penyakit Dalam', 'Diagnosis': 'Artritis', 'Tindak Lanjut': 'Rawat Jalan'},
    {'ID Pasien': 'GI2', 'Nama': 'Amelia Sari', 'Usia': 18, 'Jenis Kelamin': 'P', 'Domisili': 'Bekasi', 'Berat Badan': 55, 'Tinggi Badan': 155, 'Poli': 'Gigi', 'Diagnosis': 'Gingivitis', 'Tindak Lanjut': 'Rawat Jalan'},
    {'ID Pasien': 'SA3', 'Nama': 'Tono Usman', 'Usia': 60, 'Jenis Kelamin': 'L', 'Domisili': 'Depok', 'Berat Badan': 58, 'Tinggi Badan': 165, 'Poli': 'Saraf', 'Diagnosis': 'Epilepsi', 'Tindak Lanjut': 'Rawat Jalan'},
    {'ID Pasien': 'KA4', 'Nama': 'Ardisa Dewi', 'Usia': 29, 'Jenis Kelamin': 'P', 'Domisili': 'Tangerang', 'Berat Badan': 70, 'Tinggi Badan': 162, 'Poli': 'Kandungan', 'Diagnosis': 'Ekiesis', 'Tindak Lanjut': 'Operasi'},
    {'ID Pasien': 'AN5', 'Nama': 'Ethan', 'Usia': 2, 'Jenis Kelamin': 'L', 'Domisili': 'Jakarta', 'Berat Badan': 15, 'Tinggi Badan': 85, 'Poli': 'Anak', 'Diagnosis': 'Pneumonia', 'Tindak Lanjut': 'Rawat Inap'},
    {'ID Pasien': 'PE6', 'Nama': 'Ujang Sudirman', 'Usia': 44, 'Jenis Kelamin': 'L', 'Domisili': 'Tangerang', 'Berat Badan': 64, 'Tinggi Badan': 160, 'Poli': 'Penyakit Dalam', 'Diagnosis': 'Tuberculosis', 'Tindak Lanjut': 'Rawat Inap'},
    {'ID Pasien': 'PE7', 'Nama': 'Kartika', 'Usia': 29, 'Jenis Kelamin': 'P', 'Domisili': 'Tangerang', 'Berat Badan': 90, 'Tinggi Badan': 165, 'Poli': 'Penyakit Dalam', 'Diagnosis': 'Diabetes Mellitus', 'Tindak Lanjut': 'Rawat Jalan'},
    {'ID Pasien': 'AN8', 'Nama': 'Antonio Kennedy', 'Usia': 8, 'Jenis Kelamin': 'L', 'Domisili': 'Bogor', 'Berat Badan': 30, 'Tinggi Badan': 120, 'Poli': 'Anak', 'Diagnosis': 'Dermatitis Atopik', 'Tindak Lanjut': 'Rawat Jalan'},
    {'ID Pasien': 'BE9', 'Nama': 'Yanti Iriani', 'Usia': 65, 'Jenis Kelamin': 'P', 'Domisili': 'Bekasi', 'Berat Badan': 50, 'Tinggi Badan': 153, 'Poli': 'Bedah', 'Diagnosis': 'Anuerisma', 'Tindak Lanjut': 'Operasi'},
    {'ID Pasien': 'BE10', 'Nama': 'Andi Wirjawan', 'Usia': 24, 'Jenis Kelamin': 'L', 'Domisili': 'Depok', 'Berat Badan': 70, 'Tinggi Badan': 170, 'Poli': 'Bedah', 'Diagnosis': 'Apendisitis', 'Tindak Lanjut': 'Operasi'}
]

# Fungsi

def header_tabel():
    print(f'{'ID Pasien':<9} | {'Nama':<15} | {'Usia':<5} | {'Jenis Kelamin':<14} | {'Domisili':<10} | {'Berat Badan':<11} | {'Tinggi Badan':<12} | {'Poli':<15} | {'Diagnosis':<20} | {'Tindak Lanjut'}')
    print('-' * 155)

def row_tabel(data):
    print(f'{data['ID Pasien']:<9} | {data['Nama']:<15} | {data['Usia']:<5} | {data['Jenis Kelamin']:<14} | {data['Domisili']:<10} | {data['Berat Badan']:<11} | {data['Tinggi Badan']:<12} | {data['Poli']:<15} | {data['Diagnosis']:<20} | {data['Tindak Lanjut']}')

def cari_pasien_di_database (kolom, cari):
    hasil_cari = []
    for pasien in data_pasien:
        if kolom in ['ID Pasien', 'Nama', 'Poli', 'Jenis Kelamin', 'Domisili', 'Diagnosis', 'Tindak Lanjut']:
            if cari.lower() in pasien[kolom].lower():
                hasil_cari.append(pasien)

        elif kolom in ['Usia', 'Berat Badan', 'Tinggi Badan']:
            try:
                if pasien[kolom] == int(cari):
                    hasil_cari.append(pasien)
            except ValueError:
                pass
    return hasil_cari

def get_input_angka(input_user):
    while True:
        text_input = input(input_user).strip()
        try:
            angka = int(text_input)
            return angka
        except ValueError:
            print('Input tidak valid. Harap masukkan angka.')

def get_input_text(input_user, opsi_valid = None):
    while True:
        text_input = input(input_user).strip()
        if opsi_valid:
            if text_input.upper() in [p.upper() for p in opsi_valid]:
                return text_input
            else:
                print(f'Pilihan tidak valid. Harap masukkan salah satu dari {",".join(opsi_valid)}.')
        else: 
            return text_input
        
def menu_confirm(pesan):
    while True:
        print(pesan)
        pilih_raw = input('Masukkan Pilihan Anda: ').strip()
        try:
            pilih_angka = int(pilih_raw)
            if pilih_angka in [1,2,3]:
                return pilih_angka
            else:
                print('Pilihan tidak valid.')
        except ValueError:
            print('Input tidak Valid. Harap masukkan angka')

#Login
login_info = {'username': 'admin', 'password': 'rumahsehat'}

def login():
    percobaan = 5
    while percobaan > 0:
        print('\n=== Login ===')
        username = input('Username: ').strip()
        password = input('Password: ').strip()

        if username == login_info ['username'] and password == login_info['password']:
            print('Login Berhasil!')
            return True
        else:
            percobaan -= 1
            print(f'Login Gagal. Sisa Percobaan: {percobaan}')

            if percobaan == 0:
                print('Anda telah melebihi batas percobaan login.')
                return False
    
    return False

# Statistik Pasien
def stat_usia():
    if not data_pasien:
        print('Tidak Ada Data Pasien')
        return
    
    list_usia = []
    for pasien in data_pasien:
        list_usia.append(pasien['Usia'])

    print('\n=== Statistik Usia ===')
    print(f'Pasien Tertua: {max(list_usia)} tahun')
    print(f'Pasien Termuda: {min(list_usia)} tahun')
    print(f'Rata-Rata Usia Pasien: {sum(list_usia)/len(list_usia)} tahun')

def stat_berat_badan():
    if not data_pasien:
        print('Tidak Ada Data Pasien')
        return
    
    list_berat_badan = []
    for pasien in data_pasien:
        list_berat_badan.append(pasien['Berat Badan'])

    print('\n=== Statistik Berat Badan ===')
    print(f'Berat Badan Pasien Terbesar: {max(list_berat_badan)} kg')
    print(f'Berat Badan Pasien Terkecil: {min(list_berat_badan)} kg')
    print(f'Rata-Rata Berat Badan Pasien: {sum(list_berat_badan)/len(list_berat_badan)} kg')

def stat_tinggi_badan():
    if not data_pasien:
        print('Tidak Ada Data Pasien')
        return
    
    list_tinggi_badan = []
    for pasien in data_pasien:
        list_tinggi_badan.append(pasien['Tinggi Badan'])

    print('\n=== Statistik Tinggi Badan ===')
    print(f'Pasien Tertinggi: {max(list_tinggi_badan)} cm')
    print(f'Pasien Terendah: {min(list_tinggi_badan)} cm')
    print(f'Rata-Rata Tinggi Badan Pasien: {sum(list_tinggi_badan)/len(list_tinggi_badan)} cm')

def stat_diagnosis():
    if not data_pasien:
        print('Tidak Ada Data Pasien')
        return
    
    list_diagnosis = {}
    for pasien in data_pasien:
        diagnosis = pasien['Diagnosis']
        if diagnosis in list_diagnosis:
            list_diagnosis[diagnosis] += 1
        else:
            list_diagnosis[diagnosis] =1

    print('\n=== Statistik Diagnosis ===')
    for diagnosa, jumlah in list_diagnosis.items():
        print(f'{diagnosa}: {jumlah} pasien')

def tampilkan_stat():
    stat_usia()
    stat_berat_badan()
    stat_tinggi_badan()
    stat_diagnosis()

# CRUD

# 1. Tambah Data Pasien (Create)
def tambah_data():
    while True:
        print('''
============================================
            TAMBAH DATA PASIEN
============================================
1. Tambah Data Pasien
2. Kembali ke Menu Utama
            ''')
        opsi_menu_tambah_data = get_input_angka('Masukkan Pilihan Anda [1 - 2]: ')

        if opsi_menu_tambah_data == 1:
            while True:
                print('\n=== Masukkan Data Pasien Baru ===')
                id_pasien_baru = get_input_text('Masukkan ID Pasien: ').upper()

                # Cek ID Pasien apakah sudah ada dalam database
                if cari_pasien_di_database ('ID Pasien', id_pasien_baru):
                    print('\nID pasien yang Anda Input sudah ada di database.')
                    opsi_confirm = menu_confirm('''
1. Masukkan Ulang ID Pasien
2. Kembali ke Menu Utama
''')
                    if opsi_confirm == 1:
                        continue
                    else:
                        return
                
                nama_baru = get_input_text('Nama Pasien: ').title()
                usia_baru = get_input_angka(f'Usia Pasien A.N. {nama_baru} [dalam angka]: ')
                jenis_kelamin_baru = get_input_text(f'Jenis Kelamin Pasien A.N. {nama_baru}: ', ['L', 'P']).upper()
                domisili_baru = get_input_text (f'Domisili Pasien A.N. {nama_baru}: ').title()
                berat_badan_baru = get_input_angka(f'Berat Badan Pasien A.N. {nama_baru} [dalam kg]: ')
                tinggi_badan_baru = get_input_angka(f'Tinggi Badan Pasien A.N. {nama_baru} [dalam cm]: ')
                poli_baru = get_input_text(f'Poli Pasien A.N. {nama_baru}: ').title()
                diagnosis_baru = get_input_text(f'Diagnosis Pasien A.N. {nama_baru}: ').title()
                tindak_lanjut_baru = get_input_text (f'Tindak Lanjut Pasien A.N. {nama_baru}: ').title()

                data_pasien_baru = {
                    'ID Pasien': id_pasien_baru,
                    'Nama': nama_baru,
                    'Usia': usia_baru,
                    'Jenis Kelamin': jenis_kelamin_baru,
                    'Domisili': domisili_baru,
                    'Berat Badan': berat_badan_baru,
                    'Tinggi Badan': tinggi_badan_baru,
                    'Poli': poli_baru,
                    'Diagnosis': diagnosis_baru,
                    'Tindak Lanjut': tindak_lanjut_baru 
                }

                print('\n=== Data Pasien Baru ===')
                header_tabel()
                row_tabel(data_pasien_baru)

                opsi_confirm = menu_confirm('''
Apakah data yang dimasukkan sudah sesuai?
1. Ya, Simpan Data
2. Input Data Ulang
3. Kembali ke Menu Utama
                            ''')
                if opsi_confirm == 1:
                    data_pasien.append(data_pasien_baru)
                    print(f'\nData pasien A.N. {nama_baru} berhasil ditambahkan ke database Rumah Sakit Mitra Sehat.')
                    break
                elif opsi_confirm == 2:
                    continue
                else:
                    print('\nPenambahan Data Dibatalkan. Kembali ke Menu Utama.')
                    break
            break

        elif opsi_menu_tambah_data == 2:
            print('\nKembali ke Menu Utama.')
            break
        else:
            print('\nPilihan Tidak Valid. Silahkan Coba Lagi')

# 2. Tampilkan Data (Read)

def tampilkan_data():
    while True:
        print('''
============================================
            TAMPILKAN DATA PASIEN
============================================
1. Tampilkan Seluruh Data Pasien
2. Cari Data Pasien Berdasarkan ID Pasien
3. Cari Data Pasien Berdasarkan Nama
4. Cari Data Pasien Berdasarkan Poli
5. Tampilkan Statistik Pasien
6. Kembali ke Menu Utama
            ''')
        opsi_menu_tampilkan_data = get_input_angka('Masukkan Pilihan Anda [1 - 6]: ')
        
        if opsi_menu_tampilkan_data == 1:
            if not data_pasien:
                print('\nTidak Ada Data Pasien')
            else:
                print('\n=== Data Pasien Rumah Sakit Mitra Sehat ===')
                header_tabel()
                for pasien in data_pasien:
                    row_tabel(pasien)

        elif opsi_menu_tampilkan_data == 2:
            input_id = get_input_text('\nMasukkan ID Pasien yang Ingin Ditampilkan: ').upper()
            hasil_cari = cari_pasien_di_database('ID Pasien', input_id)
            if hasil_cari:
                header_tabel()
                for pasien in hasil_cari:
                    row_tabel(pasien)
            else:
                print(f'\nData dengan ID Pasien {input_id} Tidak Ditemukan.')

        elif opsi_menu_tampilkan_data == 3:
            input_nama = get_input_text('\nMasukkan Nama Pasien yang Ingin Ditampilkan: ').title()
            hasil_cari = cari_pasien_di_database('Nama', input_nama)
            if hasil_cari:
                header_tabel()
                for pasien in hasil_cari:
                    row_tabel(pasien)
            else: 
                print(f'\nData Pasien A.N. {input_nama} Tidak Ditemukan.')

        elif opsi_menu_tampilkan_data == 4:
            input_poli = get_input_text('\nMasukkan Poli Pasien yang Ingin Ditampilkan: ').title()
            hasil_cari = cari_pasien_di_database('Poli', input_poli)
            if hasil_cari:
                header_tabel()
                for pasien in hasil_cari:
                    row_tabel(pasien)
            else:
                print(f'\nData Pasien Poli {input_poli} Tidak Ditemukan.')

        elif opsi_menu_tampilkan_data == 5:
            if not data_pasien:
                print('\nTidak Ada Data Pasien')
            else:
                print('\n=== Statistik Pasien ===')
                tampilkan_stat()

        elif opsi_menu_tampilkan_data == 6:
            print ('\nKembali ke Menu Utama.')
            break
        else:
            print('Input tidak valid. Silakan coba lagi.')

# Edit Data Pasien (Update)
def edit_data():
    if not data_pasien:
        print('\nTidak ada data pasien untuk diedit. Kembali ke menu utama.')
        return

    while True:
        print('''
============================================
            EDIT DATA PASIEN
============================================
1. Edit Data Pasien
2. Kembali ke Menu Utama
                ''')
        opsi_menu_edit_data = get_input_angka('Masukkan Pilihan Anda [1 - 2]: ')

        if opsi_menu_edit_data == 1:
            while True:
                id_pasien_edit = get_input_text('\nMasukkan ID Pasien yang Akan Diedit Datanya: ').upper()
                hasil_cari = cari_pasien_di_database('ID Pasien', id_pasien_edit)

                if not hasil_cari:
                    print(f'Data dengan ID Pasien {id_pasien_edit} tidak ditemukan.')
                    opsi_menu_edit_data_confirm = menu_confirm('''
1. Masukkan Ulang ID Pasien
2. Kembali ke Menu Utama
''')
                    if opsi_menu_edit_data_confirm == 1:
                        continue
                    elif opsi_menu_edit_data_confirm == 2:
                        return
                    else:
                        break
                
                pasien_edit = hasil_cari[0]
                print('\n=== Data Pasien yang Akan Diedit ===')
                header_tabel()
                row_tabel(pasien_edit)

                opsi_menu_edit_data_confirm = menu_confirm('''
Apakah Data Diatas Adalah Pasien yang Dimaksud?
1. Ya, Lanjut Edit Data
2. Input Ulang ID Pasien
3. Kembali ke Menu Utama
''')
                
                if opsi_menu_edit_data_confirm == 1:
                    pass
                elif opsi_menu_edit_data_confirm == 2:
                    continue
                elif opsi_menu_edit_data_confirm == 3:
                    print('\nEdit Data Gagal Disimpan. Kembali Ke Menu Utama.')
                    return

                while True:
                    print('\nPilih Variabel yang Ingin Diedit: ')
                    daftar_variabel = list(pasien_edit.keys())[1:]
                    for i, kolom in enumerate (daftar_variabel):
                        print(f'{i+1}. {kolom}')

                    opsi_edit_variabel = get_input_angka(f'Masukkan Nomor Variabel yang Ingin Diedit [1-{len(daftar_variabel)}]: ')

                    if 1 <= opsi_edit_variabel <= len(daftar_variabel):
                        nama_variabel_terpilih = daftar_variabel[opsi_edit_variabel - 1]
                    else:
                        print('Pilihan Variabel Tidak Valid')
                        continue

                    data_baru = ''
                    if nama_variabel_terpilih in ['Usia', 'Berat Badan', 'Tinggi Badan']:
                        data_baru = get_input_angka(f'\nMasukkan {nama_variabel_terpilih} baru [dalam angka]: ')
                    elif nama_variabel_terpilih == 'Jenis Kelamin':
                        data_baru = get_input_text(f'\nMasukkan {nama_variabel_terpilih} Baru [L/P]: ', ['L', 'P']).upper()
                    else:
                        data_baru = get_input_text(f'\nMasukkan {nama_variabel_terpilih} baru: ').title()

                    pasien_edit[nama_variabel_terpilih] = data_baru

                    print ('\n=== Data Pasien Update ===')
                    header_tabel()
                    row_tabel(pasien_edit)

                    opsi_menu_edit_data_confirm = menu_confirm('''
Apakah Data yang Diedit Sudah Benar
1. Ya, Simpan Data
2. Ulangi Edit Data
3. Kembali ke Menu Utama
''')

                    if opsi_menu_edit_data_confirm == 1:
                        print('\nData Berhasil Diperbaharui dan Telah Tersimpan di Database Rumah Sakit Mitra Sehat.')
                        break
                    elif opsi_menu_edit_data_confirm == 2:
                        continue
                    else:
                        print('\nEdit Data Dibatalkan. Kembali ke Menu Utama')
                        break
                break

        elif opsi_menu_edit_data == 2:
            print('\nKembali ke Menu Utama')
            break
        else:
            print('\nPilihat Tidak Valid. Silahkan Coba Lagi')

# Hapus Data (Delete)

def hapus_data():
    if not data_pasien:
        print('\nTidak Ada Data Pasien Untuk Dihapus. Kembali ke Menu Utama.')
        return
    
    # Login untuk menghapus data
    print('''
=== Perhatian ===
Untuk mengakses fitur hapus data, Anda diharuskan login ke dalam akun Rumah Sakit Mitra Sehat terlebih dahulu.
          ''')

    if not login():
        return

    while True:
        print('''
============================================
            HAPUS DATA PASIEN
============================================
1. Hapus Data Pasien
2. Kembali ke Menu Utama
                ''')
        opsi_menu_hapus_data = get_input_angka('Masukkan Pilihan Anda [1 - 2]: ')

        if opsi_menu_hapus_data == 1:
            while True:
                id_pasien_hapus = get_input_text('\nMasukkan ID Pasien yang Ingin Dihapus: ') .upper()

                index_ditemukan = -1
                for i, pasien in enumerate(data_pasien):
                    if pasien['ID Pasien'] == id_pasien_hapus:
                        index_ditemukan = i
                        break
                    
                if index_ditemukan == -1:
                    print (f'\nData dengan ID Pasien {id_pasien_hapus} Tidak Ditemukan.')
                    opsi_confirm_hapus_data = menu_confirm('''
1. Input Ulang ID Pasien
2. Kembali ke Menu Utama
''')
                    
                    if opsi_confirm_hapus_data == 1:
                        continue
                    else:
                        return
                    
                pasien_dihapus = data_pasien[index_ditemukan]
                print ('\n=== Data Pasien Dihapus ===')
                header_tabel()
                row_tabel(pasien_dihapus)

                opsi_confirm_hapus_data = menu_confirm('''
Apakah Data Di Atas Data yang Anda Maksud?
1. Ya, Hapus Data
2. Input Ulang ID Pasien
3. Kembali ke Menu Utama
                                                       ''')
                
                if opsi_confirm_hapus_data == 1:
                    del data_pasien[index_ditemukan]
                    print(f'Pasien dengan ID {id_pasien_hapus} Berhasil Dihapus.')
                    break
                elif opsi_confirm_hapus_data == 2:
                    continue
                else:
                    print('Hapus Data Dibatalkan.')
                    break
            break
        
        elif opsi_menu_hapus_data == 2:
            print('\nKembali ke Menu Utama.')
            break
        else:
            print('\nInput Tidak Valid. Silahkan coba lagi.')


# Run Program
def menu_utama():
    while True:
        print('''
============================================
         SELAMAT DATANG DI PROGRAM
          RUMAH SAKIT MITRA SEHAT
============================================

Menu Utama:  
1. Tampilkan Data Pasien
2. Tambah Data Pasien
3. Edit Data Pasien
4. Hapus Data Pasien
5. Keluar dari Program
''')
        opsi_menu_utama = get_input_angka('Masukkan Pilihan Anda Untuk Menjalankan Program [1 - 5]: ')

        if opsi_menu_utama == 1:
            tampilkan_data()
        elif opsi_menu_utama == 2:
            tambah_data()
        elif opsi_menu_utama == 3:
            edit_data()
        elif opsi_menu_utama == 4:
            hapus_data()
        elif opsi_menu_utama == 5:
            print ('''
============================================
            KELUAR DARI PROGRAM
        TERIMA KASIH DAN SEHAT SELALU!
============================================''')
            break
        else:
            print('\nPilihan tidak Valid. Silahkan coba lagi dengan memasukkan angka [1 - 5]')


menu_utama()