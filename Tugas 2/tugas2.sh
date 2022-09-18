#!/bin/bash
read -p "Masukan nama anda: " nama
echo "Selamat datang $nama di program latihan soal aritmatika dengan bash"
echo "Pilih soal yang ingin anda kerjakan"
echo -e "1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian"
read -p "Masukan pilihan anda: " pilih

a=$(( $RANDOM % 10 + 1 ))
b=$(( $RANDOM % 10 + 1 ))
let penjumlahan=$a+$b
let pengurangan=$a-$b
let perkalian=$a*$b
let pembagian=$a/$b

if [ $pilih == 1 ]; then
  read -p "hasil dari $a + $b adalah " hasiljumlah
  if [ $hasiljumlah == $penjumlahan ]; then
    echo "Selamat, kamu benar"
  else
    echo -e "Maaf, coba lagi ya\nHasil dari $a + $b adalah $penjumlahan"
  fi
elif [ $pilih == 2 ]; then
  read -p "hasil dari $a - $b adalah " hasilkurang
  if [ $hasilkurang == $pengurangan ]; then
    echo "Selamat, kamu benar"
  else
    echo -e "Maaf, coba lagi ya\nHasil dari $a - $b adalah $pengurangan"
  fi
elif [ $pilih == 3 ]; then
  read -p "hasil dari $a * $b adalah " hasilkali
  if [ $hasilkali == $perkalian ]; then
    echo "Selamat, kamu benar"
  else
    echo -e "Maaf, coba lagi ya\nHasil dari $a * $b adalah $perkalian"
  fi
elif [ $pilih == 4 ]; then
  read -p "hasil dari $a / $b adalah " hasilbagi
  if [ $hasilbagi == $pembagian ]; then
    echo "Selamat, kamu benar"
  else
    echo -e "Maaf, coba lagi ya\nHasil dari $a / $b adalah $pembagian"
  fi
else
  echo "Maaf, anda belum memilih latihan soal"
fi
