# teknik looping

nama_band = ['Wanna One',
             'Exo',
             'Stray Kids',
             'IU',
             'Twice',
             'Red Velvet']

kumpulan_lagu = ['Beautiful',
        'Monster',
        'Thunderous',
        'Bbibbi',
        'Yes or Yes',
        'Pyscho']

# enumerate

for index,band in enumerate(nama_band):
    print(index,':',band)

# zip

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)

# set
playlist = {'Mood', 'Happy', 'Sad', 'Ride', 'Dance', 'Party', 'Boom!', 'Sentimental'}

for lagu in sorted(playlist):
    print(lagu)

# dictionary

print('='*100)

playlist2 = {'Wanna One': 'Beautiful',
             'Exo':'Monster',
             'Twice':'Yes or Yes',
             }

for i,v in playlist2.items():
    print(i,'lagunya:',v)

for i in reversed(range(1,10,1)):
    print(i)