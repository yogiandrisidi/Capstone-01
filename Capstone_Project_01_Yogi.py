# Capstone Project 01
# Yogi Andrian Sidiyanto

# Stock Awal
inventory = {
    "e001": {
        'Kode Produk': 'e001',
        'Nama Produk': 'televisi',
        'Kondisi': 'baru',
        'Garansi': '3 tahun',
        'Warna': 'hitam',
        'Rak': 'besar',
        'Jumlah Produk': 1000},
    "e002": {
        'Kode Produk': 'e002',
        'Nama Produk': 'laptop',
        'Kondisi': 'baru',
        'Garansi': '2 tahun',
        'Warna': 'perak',
        'Rak': 'kecil',
        'Jumlah Produk': 500},
    "e003": {
        'Kode Produk': 'e003',
        'Nama Produk': 'handphone',
        'Kondisi': 'baru',
        'Garansi': '2 tahun',
        'Warna': 'biru',
        'Rak': 'kecil',
        'Jumlah Produk': 400},
    "e004": {
        'Kode Produk': 'e004',
        'Nama Produk': 'kulkas',
        'Kondisi': 'baru',
        'Garansi': '3 tahun',
        'Warna': 'hitam',
        'Rak': 'besar',
        'Jumlah Produk': 600},
    "e005": {
        'Kode Produk': 'e005',
        'Nama Produk': 'mesin cuci',
        'Kondisi': 'baru',
        'Garansi': '2 tahun',
        'Warna': 'putih',
        'Rak': 'besar',
        'Jumlah Produk': 650},
    "e006": {
        'Kode Produk': 'e006',
        'Nama Produk': 'speaker',
        'Kondisi': 'baru',
        'Garansi': '1 tahun',
        'Warna': 'hitam',
        'Rak': 'kecil',
        'Jumlah Produk': 100}
}

#Fungsi

# Read
def menu_awal():
    print ('Berikut Ini Daftar Barang yang Tersedia di Gudang\n')
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for i in inventory.keys():
         print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')

def show_rak():
    rak = input('Masukan nama rak yang ingin ditampilkan: ')
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for i in inventory.keys():
        if rak.lower()  in inventory[i]["Rak"]:
            print('{}\t\t| {}\t| {}\t\t| {}\t| {}\t\t| {}\t\t|{}'.format(inventory[i]["Kode Produk"],inventory[i]["Nama Produk"],inventory[i]["Kondisi"],inventory[i]["Garansi"],inventory[i]["Warna"],inventory[i]["Rak"],inventory[i]["Jumlah Produk"]))
        else:
            continue

def show_warna():
    warna= input('Masukan warna yang ingin ditampilkan: ')
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for i in inventory.keys():
        if warna.lower() in inventory[i]["Warna"]:
            print('{}\t\t| {}\t| {}\t\t| {}\t| {}\t\t| {}\t\t|{}'.format(inventory[i]["Kode Produk"],inventory[i]["Nama Produk"],inventory[i]["Kondisi"],inventory[i]["Garansi"],inventory[i]["Warna"],inventory[i]["Rak"],inventory[i]["Jumlah Produk"]))
        else:
            continue

def show_produk():
    produk= input('Masukan nama produk yang ingin ditampilkan: ')
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for i in inventory.keys():
        if produk.lower() in inventory[i]["Nama Produk"]:
            print('{}\t\t| {}\t| {}\t\t| {}\t| {}\t\t| {}\t\t|{}'.format(inventory[i]["Kode Produk"],inventory[i]["Nama Produk"],inventory[i]["Kondisi"],inventory[i]["Garansi"],inventory[i]["Warna"],inventory[i]["Rak"],inventory[i]["Jumlah Produk"]))
        else:
            continue

def show_garansi():
    garansi_input = input('Masukan berapa tahun garansi yang ingin ditampilkan: ')
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for i in inventory.keys():
        if garansi_input.lower() in inventory[i]["Garansi"]:
            print('{}\t\t| {}\t| {}\t\t| {}\t| {}\t\t| {}\t\t|{}'.format(inventory[i]["Kode Produk"],inventory[i]["Nama Produk"],inventory[i]["Kondisi"],inventory[i]["Garansi"],inventory[i]["Warna"],inventory[i]["Rak"],inventory[i]["Jumlah Produk"]))
        else:
            continue

# Create
def produk_baru():
    newkeys = input('Masukan kode barang elektronik baru yang ingin ditambahkan : ')
    if newkeys.lower() not in inventory.keys():
        new_kode = input('Masukan kode produk: ')
        new_nama = input('Masukkan nama produk: ')
        new_kondisi = input('Masukkan kondisi barang: ')
        new_garansi = input('Masukkan berapa tahun garansi produk: ')
        new_warna = input('Masukkan warna produk: ')
        new_rak = input('Masukkan lokasi rak produk: ')
        new_jumlah = int(input('Masukkan jumlah produk: '))
        
        print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
        print ('==================================================================================================================')
        print (f"{new_kode}\t\t| {new_nama}\t| {new_kondisi}\t\t| {new_garansi}\t| {new_warna}\t\t| {new_rak}\t\t|{new_jumlah}")

        while True:
            x=input (f'''Apakah data yang ingin ditambahkan tersebut sudah benar?
            (Y untuk ya/N untuk tidak): ''')
            if x == 'Y':
                inventory[newkeys]= {"Kode Produk": new_kode.lower(), "Nama Produk": new_nama.lower(), "Kondisi": new_kondisi.lower(), "Garansi": new_garansi.lower(), "Warna": new_warna.lower(), "Rak": new_rak.lower(), "Jumlah Produk": new_jumlah}
                print('Data produk berhasil ditambahkan')
                print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
                print ('==================================================================================================================')
                for i in inventory.keys():
                    print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                break
            elif x == 'N':
                print('Data produk batal ditambahkan')
                break
            else:
                print('Pilihan tidak ada. Harap masukan pilihan yang benar')
    else:
        print('Produk tersebut sudah ada, harap masukkan kode untuk produk yang lain')

# Update
def update_barang():
    keysupdate= input('Masukan kode produk yang mau diperbaharui: ')
    if keysupdate.lower() in inventory.keys():
        upd_kode = input('Masukan kode produk: ')
        upd_nama = input('Masukkan nama produk: ')
        upd_kondisi = input('Masukkan kondisi barang: ')
        upd_garansi = input('Masukkan berapa tahun garansi produk: ')
        upd_warna = input('Masukkan warna produk: ')
        upd_rak = input('Masukkan lokasi rak produk: ')
        upd_jumlah = int(input('Masukkan jumlah produk: '))

        print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
        print ('==================================================================================================================')
        print (f"{upd_kode}\t\t| {upd_nama}\t| {upd_kondisi}\t\t| {upd_garansi}\t| {upd_warna}\t\t| {upd_rak}\t\t|{upd_jumlah}")
        while True:
            x=input (f'''Apakah data yang ingin diperbaharui tersebut sudah benar?
            (Y untuk ya/N untuk tidak) ''')
            if x == 'Y':
                inventory[keysupdate]= {"Kode Produk": upd_kode.lower(), "Nama Produk": upd_nama.lower(), "Kondisi": upd_kondisi.lower(), "Garansi": upd_garansi.lower(), "Warna": upd_warna.lower(), "Rak": upd_rak.lower(), "Jumlah Produk": upd_jumlah}
                print('Data produk berhasil diperbaharui')
                print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
                print ('==================================================================================================================')
                for i in inventory.keys():
                    print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                break
            elif x == 'N':
                print('Data produk batal diperbaharui')
                break
            else:
                print('Pilihan tidak ada. Harap masukan pilihan yang benar')
    else:
        print('Produk yang ingin diperbaharui tidak ada, harap masukkan kode yang benar')

# Delete
def delete_produk():
    keysdelete = input('Masukan kode produk yang ingin dihapus: ').lower()

    if keysdelete in inventory.keys():
        print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
        print ('==================================================================================================================')
        for i in inventory:
            if keysdelete == i:
                print(f'{inventory[i]["Warehouse"]}\t\t| {inventory[i]["Category"]}\t\t| {inventory[i]["Rack Location"]}\t\t|{inventory[i]["Product Name"]}\t| {int(inventory[i]["Quantity (pcs)"])}')
        while True:
            x = input('''Apakah yakin untuk menghapus produk tersebut?
                (Y untuk ya/N untuk tidak): ''')
            if x == 'Y':
                del inventory[keysdelete]
                print('Produk telah dihapus dari gudang.')
                print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
                print ('==================================================================================================================')
                for i in inventory.keys():
                    print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                break
            elif x == 'N':
                print('Produk batal untuk dihapus')
                break
            else:
                print('Pilihan tidak ada. Harap masukan pilihan yang benar')
    else:
        print('Kode produk yang ingin dihapus tidak ada, harap masukkan kode yang benar')

# Pengambilan Produk    
def produk_keluar():
    keyskeluar= input('Masukan kode produk yang ingin diambil untuk didistribusikan: ')
    if keyskeluar.lower() in inventory.keys():        
        qtykeluar= int(input('Masukan jumlah produk yang keluar: '))
        if qtykeluar < inventory[keyskeluar]['Jumlah Produk']:
            print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
            print ('==================================================================================================================')
            for i in inventory:
                if keyskeluar==i:
                    print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                    while True:
                        x = input(f'''Apakah yakin untuk mengambil {inventory[i]["Nama Produk"]} sebanyak {qtykeluar}?
                        (Y untuk ya/N untuk tidak): ''')
                        if x == 'Y':
                            inventory[keyskeluar]['Jumlah Produk'] = inventory[keyskeluar]['Jumlah Produk']-qtykeluar
                            print(f'Produk {inventory[i]["Nama Produk"]} dikeluarkan sebanyak {qtykeluar}')
                            break
                        elif x == 'N':
                            print('Produk batal untuk dikeluarkan')
                            break
                        else:
                            print('Pilihan tidak ada. Harap masukan pilihan yang benar')
        elif qtykeluar == inventory[keyskeluar]['Jumlah Produk']:
            print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
            print ('==================================================================================================================')
            for i in inventory:
                if keyskeluar==i:
                    print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                    while True:
                        x = input(f'''Apakah yakin untuk mengeluarkan {inventory[i]["Nama Produk"]} sebanyak {qtykeluar} buah?
                        (Y untuk ya/N untuk tidak): ''')
                        if x == 'Y':
                            inventory[keyskeluar]['Jumlah Produk'] = inventory[keyskeluar]['Jumlah Produk']-qtykeluar
                            print(f'''Produk {inventory[i]["Nama Produk"]} dikeluarkan sebanyak {qtykeluar}
                            stok {inventory[i]["Product Name"]} sudah habis. Harap untuk menambahkannya kembali.''')                            
                            break
                        elif x == 'N':
                            print('Produk batal untuk dikeluarkan')
                            break
                        else:
                            print('Pilihan tidak ada. Harap masukan pilihan yang benar')
        elif qtykeluar > inventory[keyskeluar]['Jumlah Produk']:
            print(f'Jumlah stok produk yang tersedia tidak cukup')
        else:
            print('Mohon masukkan jumlah produk yang benar')
    else:   
        print('Kode produk yang ingin diambil tidak ada, harap masukkan kode yang benar')

# Restock
def restock_produk():
    restockkey= input('Masukan kode produk yang akan di restock: ')
    if restockkey.lower() in inventory.keys():        
        jumlah_restock= int(input('Masukan jumlah produk yang mau di restock: '))
        print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
        print ('==================================================================================================================')
        for i in inventory:
            if restockkey==i:
                print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                while True:
                    x = input(f'''Apakah yakin untuk menambahkan {inventory[i]["Nama Produk"]} sebanyak {jumlah_restock}?
                    (Y untuk ya/N untuk tidak): ''')
                    if x == 'Y':
                        inventory[restockkey]['Jumlah Produk'] = inventory[restockkey]['Jumlah Produk']+jumlah_restock
                        print(f'Produk {inventory[i]["Nama Produk"]} berhasil ditambahkan sebanyak {jumlah_restock}')
                        print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
                        print ('==================================================================================================================')
                        for i in inventory.keys():
                            print(f'{inventory[i]["Kode Produk"]}\t\t| {inventory[i]["Nama Produk"]}\t| {inventory[i]["Kondisi"]}\t\t| {inventory[i]["Garansi"]}\t| {inventory[i]["Warna"]}\t\t| {inventory[i]["Rak"]}\t\t| {int(inventory[i]["Jumlah Produk"])}')
                        break
                    elif x == 'N':
                        print('Produk tersebut batal untuk di restock')
                        break
                    else:
                        print('Masukan menu yang benar')
    else:   
        print('Kode produk yang ingin direstock tidak ada, harap masukkan kode yang benar')

# Sorting
def sort_stok():
    sort_stok = sorted(inventory.items(), key=lambda x: x[1]['Jumlah Produk'])
    print (' Kode Produk\t| Nama Produk\t| Kondisi\t| Garansi\t| Warna\t\t| Rak\t\t| Jumlah Produk\t')
    print ('==================================================================================================================')
    for key, value in sort_stok:
        print(f"{ value['Kode Produk']}\t\t| {value['Nama Produk']}\t| {value['Kondisi']}\t\t| {value['Garansi']}\t| {value['Warna']}\t\t| {value['Rak']}\t\t| {value['Jumlah Produk']}")
    

# Halaman Awal
while True :
    menu = input(
        '''
        Selamat Datang Di Gudang Elektronik Archipelago

        List Menu
        1. Menampilkan Stok yang Ada
        2. Menambah Produk
        3. Menghapus Produk
        4. Mengambil Produk
        5. Restock Produk
        6. Cek Stok
        7. Keluar Program

        Masukan Menu Yang Anda Inginkan : '''
    )

    if menu=='1':
        while True:
            extramenu = input(
                '''
                Apa yang ingin ditampilkan 
                1. Semua stok di gudang
                2. Semua stok berdasarkan lokasi rak
                3. Semua stok berdasarkan warna
                4. Semua stok berdasarkan garansi
                5. Semua stok berdasarkan nama produk
                6. Kembali ke menu awal
                7. Keluar

                Pilih menu yang anda inginkan: '''
            )
            if extramenu == '1':
                menu_awal()
            elif extramenu == '2':
                show_rak()
            elif extramenu == '3':
                show_warna()
            elif extramenu == '4':
                show_garansi()
            elif extramenu == '5':
                show_produk()
            elif extramenu == '6':
                break
            elif extramenu == '7':
                print('Terima Kasih. Sampai Jumpa Lagi')
                exit()
            else:
                print('Kode nomor yang anda masukkan salah. Harap masukkan kode nomor yang benar')
                continue
            input('Tekan Enter')


    elif menu=='2':
        while True:
            menu2 = input('''
                1. Menambahkan produk baru
                2. Mengubah produk yang sudah ada
                3. Kembali ke menu awal
                4. Keluar
                Pilih menu yang diinginkan: '''
            )           
            if menu2 == '1':
                produk_baru()
            elif menu2 == '2':
                update_barang()
            elif menu2 == '3':
                break
            elif menu2 == '4':
                print('Terima Kasih')
                exit()
            else:
                print('Masukan pilihan menu yang benar')
                continue
            input('Tekan Enter')

    
    elif menu=='3':
        delete_produk()

    elif menu=='4':
        produk_keluar()
    
    elif menu=='5':
        restock_produk()

    elif menu=='6':
        sort_stok()

    elif menu == '7' :
        print('Terima Kasih. Sampai Jumpa Lagi')
        break

    else : 
        print ('Kode nomor yang anda masukkan salah. Harap masukkan kode nomor yang benar')