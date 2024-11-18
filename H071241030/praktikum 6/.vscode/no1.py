inventory = {}

def tambah_barang():
    kode = input("Masukkan Kode Barang: ")
    nama = input("Masukkan Nama Barang: ")
    jumlah = int(input("Masukkan Jumlah Barang: "))
    harga = int(input("Masukkan harga per unit: "))
    inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan Kode Barang yang akan dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_barang():
    if not inventory:
        print("Inventory kosong.")
        return
    print("Daftar Barang:")
    for kode, data in inventory.items():
        print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']}")

def cari_barang():
    kode = input("Masukkan Kode Barang yang dicari: ")
    if kode in inventory:
        data = inventory[kode]
        print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, harga: {data['harga']}")
    else:
        print("Barang tidak ditemukan.")

def update_barang():
    kode = input("Masukkan Kode Barang yang akan diupdate: ")
    if kode in inventory:
        nama = input("masukkan nama barang baru: ")
        jumlah = int(input("Masukkan jumlah baru: "))
        harga = int(input("Masukkan harga per unit baru: "))
        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print("Barang berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def menu():
    while True:
        print("Menu Inventory Barang")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program inventory")
            break
        else:
            print("Pilihan tidak valid.")

menu()
