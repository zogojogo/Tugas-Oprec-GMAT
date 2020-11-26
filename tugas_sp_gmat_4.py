# -*- coding: utf-8 -*-
"""Tugas SP GMAT 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iNp6ix4RV_Ztb8P6F5EUHoA43HZFJBg6

# Tugas SP GMAT Nomor 4
"""

class ShoppingCart(object):
    def awal(self):
        self.items = dict()

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.items:
            self.items[kodeProduk] = self.items[kodeProduk] + kuantitas ##Jika ada produk yang sama, maka hanya kuantitasnya yang bertambah
        elif kodeProduk != None and kuantitas >= 1:
            self.items.update({kodeProduk : kuantitas}) ##update dictionary jika ada produk baru
    
    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.items:
            del self.items[kodeProduk] ##Jika nama produk sesuai dengan input maka produknya dihapus dari dictionary self.items
        else:
            pass ##Jika argumen hapusProduk()nya tidak ada di dictionary maka program langsung dilanjut ke baris berikutnya

    def tampilkanCart(self):
        for key, val in self.items.items(): ##Untuk mencetak dictionary menggunakan for dan urut dari index pertama hingga paling terakhir
            print("%s (%s)" % (key, val))

##test
keranjang = ShoppingCart()
keranjang.awal()
    
keranjang.tambahProduk("Pisang Hijau",2)
keranjang.tambahProduk("Semangka Kuning", 3)
keranjang.tambahProduk("Apel Merah", 1)
keranjang.tambahProduk("Apel Merah", 4)
keranjang.tambahProduk("Apel Merah", 2)
keranjang.hapusProduk("Semangka Kuning");
keranjang.hapusProduk("Semangka Merah");

keranjang.tampilkanCart()