*penjelasan Source Data dari berbagai produk*
 JSON adalah turunan JavaScript yang digunakan dalam transfer dan penyimpanan data. Kekinian, bahasa ini sering dimanfaatkan dalam pembuatan aplikasi web.

 Berbeda dengan XML (extensive markup language) dan format lainnya yang memiliki fungsi serupa, JSON memiliki struktur data yang sederhana dan mudah dipahami. Itulah mengapa JSON sering digunakan pada API.

JSON sendiri terdiri dari dua struktur, yaitu:

* Kumpulan value yang saling berpasangan. Dalam JSON, contohnya adalah object. 
* Daftar value yang berurutan, seperti array.

```python
{
            "Product": "Alice Mutton",
            "Customer": "ANTON",
            "Qtr 2": "$702.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "BERGS",
            "Qtr 1": "$312.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "BOLID",
            "Qtr 4": "$1,170.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "BOTTM",
            "Qtr 1": "$1,170.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "ERNSH",
            "Qtr 1": "$1,123.20",
            "Qtr 4": "$2,607.15"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "GODOS",
            "Qtr 2": "$280.80"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "HUNGC",
            "Qtr 1": "$62.40"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "PICCO",
            "Qtr 2": "$1,560.00",
            "Qtr 3": "$936.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "RATTC",
            "Qtr 2": "$592.80"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "REGGC",
            "Qtr 4": "$741.00"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "SAVEA",
            "Qtr 3": "$3,900.00",
            "Qtr 4": "$789.75"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "SEVES",
            "Qtr 2": "$877.50"
        },
        {
            "Product": "Alice Mutton",
            "Customer": "WHITC",
            "Qtr 4": "$780.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "ALFKI",
            "Qtr 4": "$60.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "BOTTM",
            "Qtr 4": "$200.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "ERNSH",
            "Qtr 4": "$180.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "LINOD",
            "Qtr 1": "$544.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "QUICK",
            "Qtr 2": "$600.00"
        },
        {
            "Product": "Aniseed Syrup",
            "Customer": "VAFFE",
            "Qtr 3": "$140.00"
        },
        ```
        nama produk Aniseed Syrup, nama customer, dan qtr ( star harga produk )

```python
{
            "Product": "Boston Crab Meat",
            "Customer": "ANTON",
            "Qtr 2": "$165.60"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "BERGS",
            "Qtr 2": "$920.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "BONAP",
            "Qtr 2": "$248.40",
            "Qtr 3": "$524.40"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "BOTTM",
            "Qtr 1": "$551.25"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "BSBEV",
            "Qtr 1": "$147.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "FRANS",
            "Qtr 4": "$18.40"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "HILAA",
            "Qtr 2": "$92.00",
            "Qtr 3": "$1,104.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "LAZYK",
            "Qtr 1": "$147.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "LEHMS",
            "Qtr 2": "$515.20"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "MAGAA",
            "Qtr 4": "$55.20"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "OTTIK",
            "Qtr 3": "$368.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "PERIC",
            "Qtr 1": "$308.70"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "QUEEN",
            "Qtr 1": "$26.46",
            "Qtr 3": "$419.52",
            "Qtr 4": "$110.40"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "QUICK",
            "Qtr 3": "$1,223.60"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "RANCH",
            "Qtr 1": "$294.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "SAVEA",
            "Qtr 3": "$772.80",
            "Qtr 4": "$736.00"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "TRAIH",
            "Qtr 2": "$36.80"
        },
        {
            "Product": "Boston Crab Meat",
            "Customer": "VAFFE",
            "Qtr 1": "$294.00",
            "Qtr 4": "$736.00"
        },
```
 nama produk Boston Crab Meat, nama customer, dan qtr ( star harga produk )

 ```python
{
            "Product": "Camembert Pierrot",
            "Customer": "ANATR",
            "Qtr 3": "$340.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "AROUT",
            "Qtr 4": "$510.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "BERGS",
            "Qtr 3": "$680.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "BOTTM",
            "Qtr 4": "$1,700.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "CHOPS",
            "Qtr 2": "$323.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "FAMIA",
            "Qtr 2": "$346.80"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "FRANK",
            "Qtr 3": "$612.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "FURIB",
            "Qtr 1": "$544.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "GOURL",
            "Qtr 4": "$340.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "LEHMS",
            "Qtr 2": "$892.50"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "MEREP",
            "Qtr 3": "$2,261.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "OTTIK",
            "Qtr 3": "$1,020.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "QUEEN",
            "Qtr 4": "$510.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "QUICK",
            "Qtr 2": "$2,427.60",
            "Qtr 3": "$1,776.50"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "RICAR",
            "Qtr 1": "$1,088.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "RICSU",
            "Qtr 1": "$1,550.40"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "SAVEA",
            "Qtr 3": "$2,380.00"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "WARTH",
            "Qtr 2": "$693.60"
        },
        {
            "Product": "Camembert Pierrot",
            "Customer": "WOLZA",
            "Qtr 3": "$510.00"
        },
        
 ```
 nama produk Boston Crab Meat, nama customer, dan qtr ( star harga produk )

 ```python
 {
            "Product": "Carnarvon Tigers",
            "Customer": "BLONP",
            "Qtr 2": "$956.25"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "BONAP",
            "Qtr 1": "$1,500.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "FOLIG",
            "Qtr 3": "$3,125.00",
            "Qtr 4": "$1,875.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "HANAR",
            "Qtr 3": "$1,250.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "HUNGO",
            "Qtr 2": "$1,406.25"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "LETSS",
            "Qtr 4": "$562.50"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "QUICK",
            "Qtr 3": "$2,000.00",
            "Qtr 4": "$1,500.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "SANTG",
            "Qtr 3": "$500.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "SPLIR",
            "Qtr 4": "$1,050.00"
        },
        {
            "Product": "Carnarvon Tigers",
            "Customer": "WELLI",
            "Qtr 3": "$225.00"
 ```
 nama produk Carnarvon Tigers Meat, nama customer, dan qtr ( star harga produk )

 