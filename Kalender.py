def menampilkan(tahun, bulan):
    import calendar

    print(calendar.month(tahun, bulan))

def input_tahun():
    while True:
        tahun = int(input("Masukkan Tahun : "))
        return tahun
    
def input_bulan():
    while True:
        bulan = int(input("Masukkan Bulan : "))
        return bulan

tahun = input_tahun()
bulan = input_bulan()

menampilkan(tahun, bulan)
