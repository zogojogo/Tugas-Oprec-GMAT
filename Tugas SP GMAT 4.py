#!/usr/bin/env python
# coding: utf-8

# In[138]:


class ShoppingCart(object):
    def awal(self):
        self.items = dict()

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.items:
            self.items[kodeProduk] = self.items[kodeProduk] + kuantitas
        elif kodeProduk != None and kuantitas >= 1:
            self.items.update({kodeProduk : kuantitas})
    
    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.items:
            del self.items[kodeProduk]
        else:
            pass

    def tampilkanCart(self):
        for key, val in self.items.items():
            print("%s (%s)" % (key, val))


# In[139]:


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

