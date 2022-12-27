from datetime import datetime
import pytz

class EstimasiWaktuPerjalanan:
  def main_menu():
    print('+'+'-'*100+'+')
    print('|'+'SELAMAT DATANG DI PROGRAM'.center(100,' ')+'|')
    print('|'+'PENGHITUNG ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    print('|'+'Fitur'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    print('|'+'1. Surabaya - Jakarta*'.ljust(100,' ')+'|')
    print('|'+'2. Surabaya - Jogja*'.ljust(100,' ')+'|')
    print('|'+'3. Jakarta - Jogja*'.ljust(100,' ')+'|')
    print('|'+'4. Jakarta - Malang*'.ljust(100,' ')+'|')
    print('|'+'5. Custom '.ljust(100,' ')+'|')
    print('|'+'6. Mencari Jarak (Kecepatan Dan Waktu Perjalanan Diketahui)'.ljust(100,' ')+'|')
    print('|'+'7. Mencari Kecepatan (Jarak Dan Waktu Perjalanan Diketahui)'.ljust(100,' ')+'|')
    print('|'+'8. Exit Program'.ljust(100,' ')+'|')
    print('|'+' '*100+'|')
    print('|'+'NB: *Sering Dicari'.rjust(100,' ')+'|')
    print('|'+' '*100+'|')
    zona = pytz.timezone('Asia/Jakarta') 
    tanggal_waktu = datetime.now(zona)
    gabungan = tanggal_waktu.strftime('%A, %d %B %Y, %I:%M:%S %p')
    print('|'+gabungan.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.pilih_fitur()
    
  def pilih_fitur():
    pilihan = int(input('Pilih fitur yang diinginkan [1-8]: '))
    if pilihan == 1:
      EstimasiWaktuPerjalanan.fitur_1()
    elif pilihan == 2:
      EstimasiWaktuPerjalanan.fitur_2()
    elif pilihan == 3:
      EstimasiWaktuPerjalanan.fitur_3()
    elif pilihan == 4:
      EstimasiWaktuPerjalanan.fitur_4()
    elif pilihan == 5:
      EstimasiWaktuPerjalanan.fitur_5()
    elif pilihan == 6:
      EstimasiWaktuPerjalanan.fitur_6()
    elif pilihan == 7:
      EstimasiWaktuPerjalanan.fitur_7()
    elif pilihan == 8:
      EstimasiWaktuPerjalanan.fitur_exit()
    else:
      print('+'+'-'*100+'+')
      print('|'+'Maaf, fitur yang anda pilih tidak tersedia.'.ljust(100,' ')+'|')
      print('+'+'-'*100+'+')
      EstimasiWaktuPerjalanan.pilih_fitur()

  def fitur_1():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Surabaya - Jakarta'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    jarak = 720
    print('|'+'Jarak Surabaya - Jakarta adalah {} km'.format(jarak).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = int(input('Masukkan rata-rata kecepatan kereta api (Km/Jam): '))
    waktu = jarak/kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) '.format(kecepatan).center(100,' ')+'|')
    print('|'+'Estimasi waktu perjalanan anda dari Surabaya - Jakarta adalah {} jam'.format('%.2f'%waktu).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_2():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Surabaya - Jogja'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    jarak = 330
    print('|'+'Jarak Surabaya - Jogja adalah {} km'.format(jarak).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = int(input('Masukkan rata-rata kecepatan kereta api (Km/Jam): '))
    waktu = jarak/kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) '.format(kecepatan).center(100,' ')+'|')
    print('|'+'Estimasi waktu perjalanan anda dari Surabaya - Jogja adalah {} jam'.format('%.2f'%waktu).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_3():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Jakarta - Jogja'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    jarak = 520
    print('|'+'Jarak Jakarta - Jogja adalah {} km'.format(jarak).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = int(input('Masukkan rata-rata kecepatan kereta api (Km/Jam): '))
    waktu = jarak/kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) '.format(kecepatan).center(100,' ')+'|')
    print('|'+'Estimasi waktu perjalanan anda dari Jakarta - Jogja adalah {} jam'.format('%.2f'%waktu).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_4():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Jakarta - Malang'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    jarak = 910
    print('|'+'Jarak Jakarta - Malang adalah {} km'.format(jarak).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = int(input('Masukkan rata-rata kecepatan kereta api (Km/Jam): '))
    waktu = jarak/kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) '.format(kecepatan).center(100,' ')+'|')
    print('|'+'Estimasi waktu perjalanan anda dari Jakarta - Malang adalah {} jam'.format('%.2f'%waktu).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_5():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Custom'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    asal = str(input('Masukkan kota keberangkatan: '))
    tujuan = str(input('Masukkan kota tujuan: '))
    jarak = float(input('Masukkan jarak perjalanan via kereta api (Km): '))
    print('+'+'-'*100+'+')
    print('|'+'Jarak {} - {} adalah {} km'.format(asal, tujuan, jarak).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = int(input('Masukkan rata-rata kecepatan kereta api (Km/Jam): '))
    waktu = jarak/kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) '.format(kecepatan).center(100,' ')+'|')
    print('|'+'Estimasi waktu perjalanan anda dari {} - {} adalah {} jam'.format(asal, tujuan, '%.2f'%waktu).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_6():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Mencari Jarak (Kecepatan Dan Waktu Perjalanan Diketahui)'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    asal = str(input('Masukkan kota keberangkatan: '))
    tujuan = str(input('Masukkan kota tujuan: '))
    waktu = float(input('Masukkan berapa lama perjalanan yang telah ditempuh kereta api (Jam): '))
    print('+'+'-'*100+'+')
    print('|'+'Waktu yang ditempuh dari {} - {} adalah {} jam'.format(asal, tujuan, waktu).center(100,' ')+'|')
    print('|'+'Rata-rata kecepatan kereta api di Indonesia adalah 80 (Km/Jam) sampai dengan 90 (Km/Jam)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    kecepatan = float(input('Masukkan kecepatan kereta api (Km/Jam): '))
    jarak = waktu*kecepatan
    print('+'+'-'*100+'+')
    print('|'+'Dengan kecepatan kereta api {} (Km/Jam) dan durasi perjalanan {} jam '.format(kecepatan, waktu).center(100,' ')+'|')
    print('|'+'Estimasi jarak yang telah anda tempuh dari {} - {} adalah {} (Km)'.format(asal, tujuan, '%.2f'%jarak).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_7():
    print('+'+'-'*100+'+')
    print('|'+'ESTIMASI WAKTU PERJALANAN'.center(100,' ')+'|')
    print('|'+'Mencari Kecepatan (Jarak Dan Waktu Perjalanan Diketahui)'.center(100,' ')+'|')
    print('|'+'(Via Kereta Api)'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    asal = str(input('Masukkan kota keberangkatan: '))
    tujuan = str(input('Masukkan kota tujuan: '))
    jarak = float(input('Masukkan jarak yang telah ditempuh kereta api (Km): '))
    waktu = float(input('Masukkan berapa lama perjalanan yang telah ditempuh kereta api (Jam): '))
    kecepatan = jarak/waktu
    print('+'+'-'*100+'+')
    print('|'+'Dengan jarak yang ditempuh kereta api {} (Km) dan durasi perjalanan {} jam '.format(jarak, waktu).center(100,' ')+'|')
    print('|'+'Estimasi kecepatan kendaraan yang telah anda tempuh dari {} - {} adalah {} (Km/Jam)'.format(asal, tujuan, '%.2f'%kecepatan).center(100,' ')+'|')
    print('|'+' '.center(100,' ')+'|')
    print('|'+'Jangan lupa untuk mengecek kesehatan anda sebelum melakukan melakukan perjalanan'.center(100,' ')+'|')
    print('|'+'dan pastikan datang ke stasiun kereta sesuai dengan jadwal yang telah diberikan.'.center(100,' ')+'|')
    print('|'+'Terima Kasih'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    EstimasiWaktuPerjalanan.kembali_menu_utama()

  def kembali_menu_utama():
    lagi = input('Apakah anda ingin kembali ke halaman menu utama? (y/n): ')
    if lagi == 'y':
      EstimasiWaktuPerjalanan.main_menu()
    elif lagi == 'n':
      EstimasiWaktuPerjalanan.fitur_exit()
    else:
      print('+'+'-'*100+'+')
      print('|'+'Maaf, fitur yang anda pilih tidak tersedia.'.ljust(100,' ')+'|')
      print('+'+'-'*100+'+')
      EstimasiWaktuPerjalanan.kembali_menu_utama()

  def fitur_exit():
    print('+'+'-'*100+'+')
    print('|'+'EXIT PROGRAM'.center(100,' ')+'|')
    print('+'+'-'*100+'+')
    print('|'+'Berhasil keluar . . .'.ljust(100,' ')+'|')
    print('+'+'-'*100+'+')


EstimasiWaktuPerjalanan.main_menu()
