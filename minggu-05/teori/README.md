#  Pemformatan Output yang Lebih Mewah

ada dua cara untuk menuli nilai : pernyataan ekspresi dan fungsi print()

Untuk menggunakan literal string yang diformat, mulailah string dengan atau sebelum tanda kutip pembuka atau tanda kutip tiga kali lipat. Di dalam string ini, Anda dapat menulis ekspresi Python antara dan karakter yang dapat merujuk ke variabel atau nilai literal.fF{}

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

Metode string str.format() membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan dan menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.{}

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

Anda dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pemotongan string dan penggabungan untuk membuat tata letak apa pun yang dapat Anda bayangkan. Jenis string memiliki beberapa metode yang melakukan operasi yang berguna untuk padding string ke lebar kolom tertentu.

Fungsi str()  untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr() untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi tertentu untuk konsumsi manusia, str() akan mengembalikan nilai yang sama dengan repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi yang berbeda.

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```
# Literal String Yang Diformat

Literal string yang diformat (juga disebut f-string untuk jangka pendek) memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan memulai string dengan atau dan menulis ekspresi sebagai .fF{expression}

Contoh berikut membulatkan pi ke tiga tempat setelah desimal:
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
Melewati bilangan bulat setelah will menyebabkan bidang itu menjadi jumlah minimum karakter yang lebar. Ini berguna untuk membuat kolom berbaris.':'

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. berlaku ascii(), berlaku str(), dan berlaku repr():'!a''!s''!r'

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

#Metode format String()

Penggunaan dasar metode str.format() 

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang diteruskan ke metode str.format().

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

Jika argumen kata kunci digunakan dalam metode str.format(), nilai-nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Argumen posisional dan kata kunci dapat digabungkan secara sewenang-wenang:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```

Jika Anda memiliki string format yang sangat panjang yang tidak ingin Anda pisahkan, alangkah baiknya jika Anda dapat mereferensikan variabel yang akan diformat berdasarkan nama, bukan berdasarkan posisi. Ini dapat dilakukan dengan hanya melewati saluran dan menggunakan tanda kurung siku untuk mengakses kunci.'[]'

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini juga bisa dilakukan dengan meneruskan tabel sebagai argumen kata kunci dengan notasi '**'.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

ni sangat berguna dalam kombinasi dengan fungsi built-in vars(), yang mengembalikan kamus yang berisi semua variabel lokal.

contoh

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

# Pemformatan String Manual

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Ada metode lain, str.zfill(), yang pads string numerik di sebelah kiri dengan nol. Ini memahami tentang tanda plus dan minus

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

# Pemformatan string lama

Operator % (modulo) juga dapat digunakan untuk pemformatan string. Mengingat, instance in diganti dengan nol atau lebih elemen . Operasi ini umumnya dikenal sebagai interpolasi string. Misalnya:'string' % values%stringvalues

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
# Membaca dan Menulis File

open() mengembalikan objek file, dan paling sering digunakan dengan dua argumen: .open(filename, mode)

```python
>>> f = open('workfile', 'w')
```

setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir. membuka file untuk membaca dan menulis. Argumen mode bersifat opsional; akan diasumsikan jika dihilangkan.'r''w''a''r+''r'

Dalam mode teks, default saat membaca adalah mengonversi akhiran garis spesifik platform (di Unix, di Windows) menjadi hanya . Saat menulis dalam mode teks \n\r\n\n\nJPEGEXE

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
Jika Anda tidak menggunakan kata kunci dengan, maka Anda harus menelepon untuk menutup file dan segera membebaskan sumber daya sistem yang digunakan olehnya.f.close()

Setelah objek file ditutup, baik dengan pernyataan dengan atau dengan memanggil, upaya untuk menggunakan objek file akan secara otomatis gagal.f.close()

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

# Metode Objek File

Untuk membaca konten file, call, yang membaca beberapa jumlah data dan mengembalikannya sebagai string (dalam mode teks) atau byte objek (dalam mode biner).paling banyak ukuran karakter (dalam mode teks) atau ukuran byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, akan mengembalikan string kosong ().f.read(size)f.read()''

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

f.readline() membaca satu baris dari file; karakter baris baru () tersisa di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak berakhir di baris baru. Ini membuat nilai pengembalian tidak ambigu; jika mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh , string yang hanya berisi satu baris baru.\nf.readline()'\n'

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, Anda dapat mengulang objek file.

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

f.write(string) menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.

```python
>>> f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi - baik ke string (dalam mode teks) atau objek byte (dalam mode biner) - sebelum menulisnya:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

f.tell() mengembalikan bilangan bulat yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file ketika dalam mode biner dan angka buram saat dalam mode teks.

Untuk mengubah posisi objek file, gunakan . Posisi dihitung dari menambahkan offset ke titik referensi; titik referensi dipilih oleh argumen dari mana. Nilai dari mana 0 mengukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi.f.seek(offset, whence)

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

Dalam file teks (yang dibuka tanpa dalam string mode), hanya mencari relatif terhadap awal file yang diizinkan (pengecualian yang mencari ke ujung file dengan ) dan satu-satunya nilai offset yang valid adalah yang dikembalikan dari , atau nol. Nilai offset lainnya menghasilkan perilaku yang tidak terdefinisi.bseek(0, 2)f.tell()

# Menyimpan data terstruktur dengan json

String dapat dengan mudah ditulis dan dibaca dari file. Angka membutuhkan sedikit lebih banyak usaha, karena metode ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int()

Jika Anda memiliki objek, Anda dapat melihat representasi string JSON-nya dengan baris kode sederhana:x

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
```
Varian lain dari fungsi dumps(), yang disebut dump(), hanya serialisasi objek ke file teks. Jadi jika ada objek file teks yang dibuka untuk ditulis, kita dapat melakukan ini:f

```python
json.dump(x, f)
```

Untuk memecahkan kode objek lagi, jika adalah objek file teks yang telah dibuka untuk dibaca:f

```python
x = json.load(f)
```

Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi serialisasi instans kelas arbitrer di JSON membutuhkan sedikit usaha ekstra. Referensi untuk modul json berisi penjelasan tentang hal ini.