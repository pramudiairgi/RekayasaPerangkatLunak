# Nama: [Irgi Pramudia]
# NIM: [G.231.22.0173]

# Program Menampilkan Bilangan Ganjil / Genap

def main():
  print("=== Program Menampilkan Bilangan Ganjil / Genap ===")

  while True:
      print("\nMenu:")
      print("1. Tampilkan bilangan ganjil")
      print("2. Tampilkan bilangan genap")
      print("3. Keluar")

      pilihan = input("Masukkan pilihan (1/2/3): ")

      if pilihan == "1" or pilihan == "2":
          n = int(input("Masukkan batas angka: "))

          if pilihan == "1":
              print(f"Bilangan ganjil dari 1 sampai {n}:")
              for i in range(1, n+1):
                  if i % 2 != 0:
                      print(i, end=' ')
          else:
              print(f"Bilangan genap dari 1 sampai {n}:")
              for i in range(1, n+1):
                  if i % 2 == 0:
                      print(i, end=' ')

          print("\n") 
      elif pilihan == "3":
          print("Terima kasih! Program selesai.")
          break
      else:
          print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
  main()
