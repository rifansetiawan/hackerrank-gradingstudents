jumlah_student = int(input())
semua_nilai = []

for x in range (jumlah_student):
    nilai_permurid = int(input().strip())

    if nilai_permurid < 38 :
        nilai_permurid = nilai_permurid

    elif (nilai_permurid + 3) % 5 == 0 or (nilai_permurid + 4) % 5 == 0:
        nilai_permurid = nilai_permurid
    elif (nilai_permurid + 2) % 5 == 0 :
        nilai_permurid = nilai_permurid + 2
    elif (nilai_permurid + 1) % 5 == 0 :
        nilai_permurid = nilai_permurid + 1
    elif nilai_permurid % 5 == 0 :
        nilai_permurid = nilai_permurid

    semua_nilai.append(nilai_permurid)

for x in range(jumlah_student):
    print(semua_nilai[x])

        
