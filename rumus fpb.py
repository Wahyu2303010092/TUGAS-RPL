def hitung_fpb(a, b):
    """
    Menghitung Faktor Persekutuan Terbesar (FPB) menggunakan algoritma Euclidean.
    
    Args:
    - a (int): Bilangan pertama.
    - b (int): Bilangan kedua.
    
    Returns:
    - int: FPB dari a dan b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)  # FPB selalu positif


# Contoh penggunaan
print("=== Kalkulator FPB ===")
try:
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    
    fpb = hitung_fpb(bilangan1, bilangan2)
    print(f"FPB dari {bilangan1} dan {bilangan2} adalah: {fpb}")
except ValueError:
    print("Masukkan angka yang valid!")
