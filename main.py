import tkinter as tk

# Fungsi untuk menambah barang ke gudang
def tambah_barang():
    barang = barang_entry.get()
    jumlah = int(jumlah_entry.get())
    if barang in gudang:
        gudang[barang] += jumlah
    else:
        gudang[barang] = jumlah
    result_label.config(text=f"Barang {barang} berhasil ditambahkan. Jumlah saat ini: {gudang[barang]}")

# Fungsi untuk menghapus barang dari gudang
def hapus_barang():
    barang = barang_entry.get()
    if barang in gudang:
        del gudang[barang]
        result_label.config(text=f"Barang {barang} berhasil dihapus.")
    else:
        result_label.config(text=f"Barang {barang} tidak ditemukan.")

# Fungsi untuk menampilkan daftar barang di gudang
def daftar_barang():
    result_label.config(text="Daftar Barang di Gudang:\n" + "\n".join([f"{barang}: {jumlah}" for barang, jumlah in gudang.items()]))

# Fungsi untuk mengubah jumlah barang di gudang
def ubah_barang():
    barang = barang_entry.get()
    jumlah = int(jumlah_entry.get())
    if barang in gudang:
        gudang[barang] = jumlah
        result_label.config(text=f"Jumlah barang {barang} berhasil diubah menjadi {jumlah}")
    else:
        result_label.config(text=f"Barang {barang} tidak ditemukan.")

# Program Utama
gudang = {}

root = tk.Tk()
root.title("Program Pencatatan Gudang")

# Label
label = tk.Label(root, text="Selamat datang di Program Pencatatan Gudang!")
label.pack()

# Entry dan Label untuk nama barang
barang_label = tk.Label(root, text="Nama Barang:")
barang_label.pack()
barang_entry = tk.Entry(root)
barang_entry.pack()

# Entry dan Label untuk jumlah barang
jumlah_label = tk.Label(root, text="Jumlah:")
jumlah_label.pack()
jumlah_entry = tk.Entry(root)
jumlah_entry.pack()

# Tombol-tombol
tambah_button = tk.Button(root, text="Tambah Barang", command=tambah_barang)
tambah_button.pack()

hapus_button = tk.Button(root, text="Hapus Barang", command=hapus_barang)
hapus_button.pack()

daftar_button = tk.Button(root, text="Daftar Barang", command=daftar_barang)
daftar_button.pack()

ubah_button = tk.Button(root, text="Ubah Jumlah Barang", command=ubah_barang)
ubah_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

keluar_button = tk.Button(root, text="Keluar", command=root.quit)
keluar_button.pack()

root.mainloop()
