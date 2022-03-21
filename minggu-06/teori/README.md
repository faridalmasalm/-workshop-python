# BAB 8. Errors and Exceptions (Kesalahan errors dan Pengecualian exceptions)

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contoh Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaks dan pengecualian.

# 8.1. Kesalahan Sintaks

Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian, mungkin adalah jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Parser mengulangi garis yang menyinggung dan menampilkan sedikit 'panah' yang menunjuk pada titik paling awal di garis tempat kesalahan terdeteksi. Kesalahan ini disebabkan oleh (atau setidaknya terdeteksi pada) token sebelum panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua () hilang sebelum itu. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari jika input berasal dari skrip.':'

# 8.2. Pengecualian

Bahkan jika pernyataan atau ekspresi secara sintaksis benar, itu dapat menyebabkan kesalahan ketika upaya dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar bagaimana menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenis dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama pengecualian bawaan yang terjadi. Ini berlaku untuk semua pengecualian bawaan, tetapi tidak perlu benar untuk pengecualian yang ditentukan pengguna (meskipun ini adalah konvensi yang berguna). Nama pengecualian standar adalah pengidentifikasi bawaan (bukan kata kunci yang dicadangkan).

Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.

Bagian sebelumnya dari pesan kesalahan menunjukkan konteks di mana pengecualian terjadi, dalam bentuk stack traceback. Secara umum berisi garis sumber daftar stack traceback; namun, itu tidak akan menampilkan garis yang dibaca dari input standar.

# 8.3. Penanganan Pengecualian

Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Lihatlah contoh berikut, yang meminta input pengguna sampai bilangan bulat yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk mengganggu program (menggunakan atau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan menaikkan pengecualian KeyboardInterrupt.Control-C

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan percobaan berfungsi sebagai berikut.

* Pertama, klausa coba (pernyataan antara coba dan kecuali kata kunci) dijalankan.

* Jika tidak ada pengecualian terjadi, klausa kecuali dilewati dan eksekusi pernyataan coba selesai.

* Jika pengecualian terjadi selama eksekusi klausa percobaan, sisa klausa dilewati. Kemudian, jika jenisnya cocok dengan pengecualian yang dinamai kata kunci kecuali, klausa kecuali dijalankan, dan kemudian eksekusi berlanjut setelah blok try / except.

* Jika pengecualian terjadi yang tidak sesuai dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke pernyataan percobaan luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak ditangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan coba mungkin memiliki lebih dari satu kecuali klausa, untuk menentukan penangan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Penangan hanya menangani pengecualian yang terjadi dalam klausa coba yang sesuai, bukan di penangan lain dari pernyataan yang sama. Klausa kecuali dapat menyebutkan beberapa pengecualian sebagai tuple kurung, misalnya:try

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class). For example, the following code will print B, C, D in that order:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika klausa kecuali dibalik (kecuali B terlebih dahulu), itu akan mencetak B, B, B - klausa kecuali pencocokan pertama dipicu.

Semua pengecualian mewarisi dari BaseException, sehingga dapat digunakan untuk berfungsi sebagai wildcard. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman nyata dengan cara ini! Ini juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian (memungkinkan penelepon untuk menangani pengecualian juga):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Atau klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari sys.exc_info()[1].

Cobalah ... kecuali pernyataan memiliki klausa lain opsional, yang, ketika ada, harus mengikuti semua kecuali klausa. Ini berguna untuk kode yang harus dijalankan jika klausa coba tidak menimbulkan pengecualian. Misalnya:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa lain lebih baik daripada menambahkan kode tambahan ke klausa percobaan karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dinaikkan oleh kode yang dilindungi oleh ... kecuali pernyataan.

Ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai argumen pengecualian. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

Penggunaan klausa lain lebih baik daripada menambahkan kode tambahan ke klausa percobaan karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dinaikkan oleh kode yang dilindungi oleh ... kecuali pernyataan.

Ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai argumen pengecualian. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

```python
>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak ditangani.

Penangan pengecualian tidak hanya menangani pengecualian jika terjadi segera dalam klausa percobaan, tetapi juga jika terjadi di dalam fungsi yang disebut (bahkan secara tidak langsung) dalam klausa coba. Misalnya:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

#8.4. Raising Exceptions 

The raise statement allows the programmer to force a specified exception to occur. For example:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk menaikkan menunjukkan pengecualian yang akan diajukan. Ini harus berupa instans pengecualian atau kelas pengecualian (kelas yang berasal dari Pengecualian). Jika kelas pengecualian dilewatkan, itu akan secara implisit dibuat dengan memanggil konstruktornya tanpa argumen:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika Anda perlu menentukan apakah pengecualian diajukan tetapi tidak berniat untuk menanganinya, bentuk pernyataan kenaikan yang lebih sederhana memungkinkan Anda untuk menaikkan kembali pengecualian:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

# 8.5. Chaining Pengecualian

Pernyataan kenaikan memungkinkan opsional dari mana memungkinkan pengecualian rantai. Misalnya:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

This can be useful when you are transforming exceptions. For example:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Exception chaining happens automatically when an exception is raised inside an except or finally section. This can be disabled by using from None idiom:

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

# 8.6. Pengecualian yang ditentukan pengguna

Program dapat menyebutkan pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk lebih lanjut tentang kelas Python). Pengecualian biasanya harus berasal dari kelas Pengecualian, baik secara langsung maupun tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.

Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan "Kesalahan", mirip dengan penamaan pengecualian standar.

Banyak modul standar mendefinisikan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka definisikan. Informasi lebih lanjut tentang kelas disajikan dalam bab Kelas.

# 8.7. Mendefinisikan Tindakan Pembersihan

Pernyataan coba memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam segala keadaan. Misalnya:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Jika klausa akhirnya ada, klausa akhirnya akan dijalankan sebagai tugas terakhir sebelum pernyataan percobaan selesai. Klausa akhirnya berjalan apakah pernyataan percobaan menghasilkan pengecualian atau tidak. Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi:

 * Jika pengecualian terjadi selama pelaksanaan klausa percobaan, pengecualian dapat ditangani oleh klausa kecuali. Jika pengecualian tidak ditangani oleh klausa kecuali, pengecualian dinaikkan kembali setelah klausa akhirnya dieksekusi.
* Pengecualian dapat terjadi selama eksekusi klausul kecuali atau lainnya. Sekali lagi, pengecualian dinaikkan kembali setelah klausa akhirnya dieksekusi.

* Jika klausa akhirnya mengeksekusi pernyataan istirahat, lanjutkan atau kembali, pengecualian tidak dinaikkan kembali.

* Jika pernyataan coba mencapai pernyataan istirahat, lanjutkan, atau kembalikan, klausa terakhir akan dieksekusi tepat sebelum jeda, melanjutkan, atau mengembalikan eksekusi pernyataan.

* Jika klausa akhirnya menyertakan pernyataan pengembalian, nilai yang dikembalikan akan menjadi salah satu dari pernyataan pengembalian klausul akhirnya, bukan nilai dari pernyataan pengembalian klausul percobaan.

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```
A more complicated example:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang Anda lihat, klausa akhirnya dijalankan dalam hal apa pun. TypeError yang dinaikkan dengan membagi dua string tidak ditangani oleh klausa kecuali dan oleh karena itu dinaikkan kembali setelah klausa akhirnya dieksekusi.

Dalam aplikasi dunia nyata, klausa akhirnya berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya berhasil.

# 8.8. Tindakan Pembersihan yang Telah Ditentukan

Beberapa objek menentukan tindakan pembersihan standar yang akan dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah dengan kode ini adalah bahwa ia membiarkan file terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan dengan memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dijalankan, file f selalu ditutup, bahkan jika masalah ditemui saat memproses baris. Objek yang, seperti file, memberikan tindakan pembersihan yang telah ditentukan akan menunjukkan hal ini dalam dokumentasi mereka.