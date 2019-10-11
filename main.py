nama = 'Muh Hamzah Tsalis N'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'jarak ={jarak / 1000} ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga kecepatan = {kecepatan} m/s')
    return jarak / waktu

# jarak =  1000
# waktu 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 15 * 60)

massa = 20
gravitasi = 9.8
berat = massa * gravitasi

print(f'massa = {massa}kg dengan gravitasi = {gravitasi }')
print(f'sehingga beratnya = {berat} N')
