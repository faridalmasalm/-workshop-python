# 12. Lingkungan dan Paket Virtual

# 12.1. Pendahuluan

Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari perpustakaan standar. Aplikasi kadang-kadang akan membutuhkan versi tertentu dari perpustakaan, karena aplikasi mungkin memerlukan bahwa bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka perpustakaan.

Ini berarti mungkin tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk menyelesaikan contoh persyaratan yang saling bertentangan sebelumnya, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 diinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B mengharuskan pustaka ditingkatkan ke versi 3.0, ini tidak akan memengaruhi lingkungan aplikasi A.

# 12.2. Menciptakan Lingkungan Virtual

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan atau versi mana pun yang Anda inginkan.python3

Untuk membuat lingkungan virtual, putuskan direktori tempat Anda ingin menempatkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:

```python
python3 -m venv tutorial-env
```
Ini akan membuat direktori jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.tutorial-env

Lokasi direktori umum untuk lingkungan virtual adalah . Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian keluar dari jalan sambil memberikan nama yang menjelaskan mengapa direktori ada. Ini juga mencegah bentrok dengan file definisi variabel lingkungan yang didukung oleh beberapa perkakas..venv.env

Setelah membuat lingkungan virtual, Anda dapat mengaktifkannya.

Di Windows, jalankan:

```python
tutorial-env\Scripts\activate.bat
```

Di Unix atau MacOS, jalankan:

```python
source tutorial-env/bin/activate
``` 

(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau cangkang ikan, ada alternatif dan skrip yang harus Anda gunakan sebagai gantinya.)activate.cshactivate.fish

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga berjalan akan memberi Anda versi dan instalasi Python tertentu. Misalnya:python

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

# 12.3. Mengelola Paket dengan pip

Anda dapat menginstal, meningkatkan, dan menghapus paket menggunakan program yang disebut pip. Secara default akan menginstal paket dari Indeks Paket Python, <https://pypi.org>. Anda dapat menelusuri Indeks Paket Python dengan melakukannya di browser web Anda.pip

pip memiliki sejumlah subkomman: "instal", "uninstall", "freeze", dll. (Lihat panduan Menginstal Modul Python untuk dokumentasi lengkap untuk .)pip

Anda dapat menginstal versi terbaru paket dengan menentukan nama paket:

```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

Anda juga dapat menginstal versi tertentu dari paket dengan memberikan nama paket diikuti oleh dan nomor versi:==

```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika Anda menjalankan kembali perintah ini, akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau Anda dapat menjalankan untuk meningkatkan paket ke versi terbaru:pippip install --upgrade

```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

pip uninstall diikuti oleh satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.

pip show akan menampilkan informasi tentang paket tertentu:

```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```
pip list akan menampilkan semua paket yang diinstal di lingkungan virtual:

```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

pip freeze akan menghasilkan daftar paket yang diinstal serupa, tetapi outputnya menggunakan format yang diharapkan. Konvensi umum adalah memasukkan daftar ini ke dalam file:pip installrequirements.txt

```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

Kemudian dapat berkomitmen untuk kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan:requirements.txtinstall -r

```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

pip Memiliki lebih banyak pilihan. Lihat panduan Menginstal Modul Python untuk dokumentasi lengkap untuk . Ketika Anda telah menulis paket dan ingin membuatnya tersedia di Indeks Paket Python, lihat panduan Mendistribusikan Modul Python.pip