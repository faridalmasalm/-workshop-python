Jika Anda berhenti dari interpreter Python dan memasukkannya lagi, definisi yang telah Anda buat (fungsi dan variabel) hilang. Oleh karena itu, jika Anda ingin menulis program yang agak lebih panjang, Anda lebih baik menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankannya dengan file itu sebagai input sebagai gantinya. Ini dikenal sebagai membuat skrip. Seiring bertambahnya program Anda, Anda mungkin ingin membaginya menjadi beberapa file untuk perawatan yang lebih mudah.

 Anda mungkin juga ingin menggunakan fungsi praktis yang telah Anda tulis dalam beberapa program tanpa menyalin definisinya ke dalam setiap program.Untuk mendukung hal ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif penerjemah. File seperti itu disebut modul; definisi dari modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat Anda akses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran ditambahkan. Dalam modul, nama modul (sebagai string) tersedia sebagai nilai variabel global. Misalnya, gunakan editor teks favorit Anda untuk membuat file yang dipanggil di direktori saat ini dengan konten berikut:.py__name__fibo.py

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:

```python
>>> import fibo
```

Ini tidak memasukkan nama fungsi yang ditentukan secara langsung dalam tabel simbol saat ini; itu hanya memasukkan nama modul di sana. Dengan menggunakan nama modul, Anda dapat mengakses fungsi:fibofibo

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika Anda berniat untuk menggunakan fungsi sering Anda dapat menetapkannya ke nama lokal:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

# 6.1. Lebih lanjut tentang Modul¶

Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya pertama kali nama modul ditemui dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dijalankan sebagai skrip.)

Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, penulis modul dapat menggunakan variabel global dalam modul tanpa khawatir tentang bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan, Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk pada fungsinya, .modname.itemname

Modul dapat mengimpor modul lain. Adalah kebiasaan tetapi tidak diperlukan untuk menempatkan semua pernyataan impor di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor.

Ada varian dari pernyataan impor yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Misalnya:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini tidak memperkenalkan nama modul dari mana impor diambil dalam tabel simbol lokal (jadi dalam contoh, tidak didefinisikan).fibo

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan modul:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (). Dalam kebanyakan kasus programmer Python tidak menggunakan fasilitas ini karena memperkenalkan satu set nama yang tidak diketahui ke dalam interpreter, mungkin menyembunyikan beberapa hal yang telah Anda definisikan._

Perhatikan bahwa secara umum praktik mengimpor dari modul atau paket tidak disukai, karena sering menyebabkan kode yang tidak dapat dibaca dengan baik. Namun, tidak apa-apa menggunakannya untuk menyimpan mengetik di sesi interaktif.*

Jika nama modul diikuti oleh , maka nama berikut terikat langsung ke modul yang diimpor.asas

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Ini secara efektif mengimpor modul dengan cara yang sama seperti yang akan dilakukan, dengan satu-satunya perbedaan yang tersedia sebagai .import fibofib

Ini juga dapat digunakan saat memanfaatkan dengan efek serupa:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
# 6.1.1. Menjalankan modul sebagai skrip¶

Saat Anda menjalankan modul Python dengan

```python
python fibo.py <arguments>
```
kode dalam modul akan dieksekusi, seolah-olah Anda mengimpornya, tetapi dengan set ke . Itu berarti bahwa dengan menambahkan kode ini di akhir modul Anda:__name__"__main__"

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
anda dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mengurai baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
Jika modul diimpor, kode tidak dijalankan:

```python
>>> import fibo
>>>
```

Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul sebagai skrip mengeksekusi test suite).

# 6.1.2. Jalur Pencarian Modul¶

Ketika modul bernama diimpor, interpreter pertama mencari modul built-in dengan nama itu. Jika tidak ditemukan, maka cari file yang disebutkan dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinsialisasi dari lokasi ini:spamspam.py

Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).

PYTHONPATH (daftar nama direktori, dengan sintaks yang sama dengan variabel shell ).PATH

Default yang bergantung pada instalasi (berdasarkan konvensi termasuk direktori, ditangani oleh modul situs).site-packages

Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti bahwa skrip dalam direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori pustaka. Ini adalah kesalahan kecuali penggantian dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.

# 6.1.3. File Python "Dikompilasi"¶

Untuk mempercepat pemuatan modul, Python menyimpan versi yang dikompilasi dari setiap modul dalam direktori dengan nama , di mana versi mengkodekan format file yang dikompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi kompilasi spam.py akan di-cache sebagai . Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.__pycache__module.version.pyc__pycache__/spam.cpython-33.pyc

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah sudah ketinggalan zaman dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus ada di direktori sumber, dan tidak boleh ada modul sumber.

Beberapa tips untuk para ahli:

  * Anda dapat menggunakan sakelar -O atau -OO pada perintah Python untuk mengurangi ukuran modul yang dikompilasi. Switch menghapus pernyataan assert, switch menghapus pernyataan assert dan string __doc__. Karena beberapa program mungkin bergantung pada tersedianya ini, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki tag dan biasanya lebih kecil. Rilis di masa depan dapat mengubah efek optimasi.-O-OOopt-
  * Sebuah program tidak berjalan lebih cepat ketika dibaca dari file daripada ketika dibaca dari file; satu-satunya hal yang lebih cepat tentang file adalah kecepatan mereka dimuat..pyc.py.pyc
  * Modul compileall dapat membuat file .pyc untuk semua modul dalam direktori.
  * Ada lebih detail tentang proses ini, termasuk bagan alur keputusan, di PEP 3147.

# 6.2. Modul Standar¶

Python dilengkapi dengan perpustakaan modul standar, dijelaskan dalam dokumen terpisah, Referensi Perpustakaan Python ("Referensi Perpustakaan" selanjutnya). Beberapa modul dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke primitif sistem operasi seperti panggilan sistem. Set modul tersebut adalah opsi konfigurasi yang juga tergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya disediakan pada sistem Windows. Satu modul tertentu layak mendapat perhatian: sys, yang dibangun ke dalam setiap interpreter Python. Variabel dan menentukan string yang digunakan sebagai prompt primer dan sekunder:sys.ps1sys.ps2

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel ini hanya ditentukan jika interpreter berada dalam mode interaktif.

Variabel adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinsialisasi ke jalur default yang diambil dari variabel lingkungan PYTHONPATH, atau dari default bawaan jika PYTHONPATH tidak diatur. Anda dapat memodifikasinya menggunakan operasi daftar standar:sys.path

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

# 6.3. Fungsi dir()¶

Fungsi bawaan dir() digunakan untuk mengetahui nama mana yang ditentukan modul. Ini mengembalikan daftar string yang diurutkan:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```
Tanpa argumen, dir() mencantumkan nama yang telah Anda tentukan saat ini:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Perhatikan bahwa itu daftar semua jenis nama: variabel, modul, fungsi, dll.

dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftar itu, mereka didefinisikan dalam modul standar builtins:

```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

# 6.4. Paket

Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul putus-putus". Misalnya, nama modul menunjuk submodul yang disebutkan dalam paket bernama . Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari keharusan khawatir tentang nama variabel global masing-masing, penggunaan nama modul putus-putus menyelamatkan penulis paket multi-modul seperti NumPy atau Pillow dari keharusan khawatir tentang nama modul masing-masing.A.BBA

Misalkan Anda ingin merancang koleksi modul ("paket") untuk penanganan seragam file suara dan data suara. Ada banyak format file suara yang berbeda (biasanya dikenali oleh ekstensi mereka, misalnya: , , ), sehingga Anda mungkin perlu membuat dan memelihara koleksi modul yang berkembang untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, menciptakan efek stereo buatan), jadi Anda juga akan menulis aliran modul yang tidak pernah berakhir untuk melakukan operasi ini. Berikut adalah struktur yang mungkin untuk paket Anda (dinyatakan dalam hal sistem file hierarkis):.wav.aiff.au

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimpor paket, Python mencari melalui direktori untuk mencari subdirektori paket.sys.path

File diperlukan untuk membuat direktori memperlakukan Python yang berisi file sebagai paket. Ini mencegah direktori dengan nama umum, seperti , secara tidak sengaja menyembunyikan modul valid yang terjadi kemudian pada jalur pencarian modul. Dalam kasus yang paling sederhana, hanya bisa menjadi file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau mengatur variabel, dijelaskan kemudian.__init__.pystring__init__.py__all__

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:

```python
import sound.effects.echo
```

Ini memuat submodul . Itu harus dirujuk dengan nama lengkapnya.sound.effects.echo

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Cara alternatif untuk mengimpor submodul adalah:

```python
from sound.effects import echo
```

Ini juga memuat submodul , dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:echo

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:

```python
from sound.effects.echo import echofilter
```
Sekali lagi, ini memuat submodul , tetapi ini membuat fungsinya tersedia secara langsung:echoechofilter()

```python
echofilter(input, output, delay=0.7, atten=4)
```

Perhatikan bahwa saat menggunakan, item dapat berupa submodul (atau subpackage) dari paket, atau beberapa nama lain yang didefinisikan dalam paket, seperti fungsi, kelas atau variabel. Pernyataan pertama menguji apakah item didefinisikan dalam paket; jika tidak, ia mengasumsikan itu adalah modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian ImportIr akan dinaikkan.from package import itemimport

Sebaliknya, saat menggunakan sintaks seperti , setiap item kecuali yang terakhir harus menjadi paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.import item.subitem.subsubitem

# 6.4.1. Mengimpor * Dari Paket

Sekarang apa yang terjadi ketika pengguna menulis? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimpor secara eksplisit.from sound.effects import *

Satu-satunya solusi adalah bagi penulis paket untuk memberikan indeks eksplisit dari paket. Pernyataan impor menggunakan konvensi berikut: jika kode paket menentukan daftar bernama , itu dianggap sebagai daftar nama modul yang harus diimpor ketika ditemui. Terserah penulis paket untuk menjaga daftar ini tetap up-to-date ketika versi baru dari paket dirilis. Penulis paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimpor * dari paket mereka. Misalnya, file dapat berisi kode berikut:__init__.py__all__from package import *sound/effects/__init__.py

```python
__all__ = ["echo", "surround", "reverse"]
```

Ini berarti bahwa akan mengimpor tiga submodul yang disebutkan dari paket.from sound.effects import *sound

Jika tidak didefinisikan, pernyataan tidak mengimpor semua submodul dari paket ke ruang nama saat ini; itu hanya memastikan bahwa paket telah diimpor (mungkin menjalankan kode inisialisasi apa pun ) dan kemudian mengimpor nama apa pun yang ditentukan dalam paket. Ini termasuk nama apa pun yang didefinisikan (dan submodul yang dimuat secara eksplisit) oleh . Ini juga mencakup submodul paket yang secara eksplisit dimuat oleh pernyataan impor sebelumnya. Pertimbangkan kode ini:__all__from sound.effects import *sound.effectssound.effects__init__.py__init__.py

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
Dalam contoh ini, dan modul diimpor di namespace saat ini karena didefinisikan dalam paket saat pernyataan dijalankan. (Ini juga berfungsi ketika didefinisikan.)echosurroundsound.effectsfrom...import__all__

Meskipun modul tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu saat Anda menggunakannya, modul tersebut masih dianggap sebagai praktik buruk dalam kode produksi.import *

Ingat, tidak ada yang salah dengan menggunakan! Bahkan, ini adalah notasi yang direkomendasikan kecuali modul pengimpor perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.from package import specific_submodule

# 6.4.2. Referensi Intra-paket

Ketika paket disusun menjadi subpackages (seperti paket dalam contoh), Anda dapat menggunakan impor absolut untuk merujuk ke submodules paket saudara kandung. Misalnya, jika modul perlu menggunakan modul dalam paket, modul dapat menggunakan .soundsound.filters.vocoderechosound.effectsfrom sound.effects import echo

Anda juga dapat menulis impor relatif, dengan bentuk pernyataan impor. Impor ini menggunakan titik-titik utama untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul misalnya, Anda dapat menggunakan:from module import namesurround

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Perhatikan bahwa impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu , modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor absolut."__main__"

# 6.4.3. Paket di Beberapa Direktori

Paket mendukung satu lagi atribut khusus, __path__. Ini diinkusialisasi menjadi daftar yang berisi nama direktori yang memegang paket sebelum kode dalam file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu mempengaruhi pencarian masa depan untuk modul dan subpackages yang terkandung dalam paket.__init__.py

Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas set modul yang ditemukan dalam paket.