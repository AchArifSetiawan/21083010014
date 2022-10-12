#!/bin/bash
echo "------------------------------------------------------------"
read -p "Berapa Banyak Semester Yang Telah Anda Tempuh ? " semester
echo "------------------------------------------------------------"

declare -a ips

i=0
let banyak=$semester-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  read -p "Nilai Semester $angka : " nilaisemester
  ips[$i]=$nilaisemester;
  let jumlah=jumlah+$nilaisemester;
  let i=$i+1;
done

echo "------------------------------------------------------------"
let ipk=$jumlah/$semester
echo "Nilai Tiap Semester Secara Berurutan :" ${ips[@]}
echo "Nilai IPS :" $jumlah "/" $semester
echo "Nilai IPK :" $ipk
echo "------------------------------------------------------------"
