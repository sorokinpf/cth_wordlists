#!/bin/bash

echo 'removing /api/'
sed 's/\/api\//\//g' $1 > temp2.txt
echo 'removing /apis/'
sed 's/\/apis\//\//g' temp2.txt > temp.txt
echo 'removing /rest/api/'
sed 's/\/rest\/api\//\//g' temp.txt > temp2.txt
echo 'removing /rest/'
sed 's/\/rest\//\//g' temp2.txt > temp.txt
echo 'removing /v1alpha'
sed 's/\/v[0-9]*alpha\//\//g' temp.txt > temp2.txt
echo 'removing /v1alpha1/'
sed 's/\/v[0-9]*alpha[0-9]*\//\//g' temp2.txt > temp.txt
echo 'removing /v1beta'
sed 's/\/v[0-9]*beta\//\//g' temp.txt > temp2.txt
echo 'removing /v1beta1/'
sed 's/\/v[0-9]*beta[0-9]*\//\//g' temp2.txt > temp.txt
echo 'removing /v1.1/'
sed 's/\/v[0-9]*\.[0-9]*\//\//g' temp.txt > temp2.txt
echo 'removing /v1/'
sed 's/\/v[0-9]*\//\//g' temp2.txt > $2
echo 'cleaning up'
rm temp.txt temp2.txt
echo 'done'