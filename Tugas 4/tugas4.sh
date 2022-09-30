#!/bin/bash

read -p "Input: " angka

until [ ! $angka -gt 0 ]
do
  echo $angka
  angka=$((angka - 2))
done
