## Tabel Kebenaran (Truth Table)

Berikut adalah tabel kebenaran dasar untuk logika **AND, OR, dan XOR** beserta pemetaan variabel dari studi kasus.

> **Keterangan:**
> **T = True / Benar**
> **F = False / Salah**

### 1. Logika AND (Konjungsi)

**Berlaku untuk kasus:** Lulus, Daftar, dan Pinjam.

> Hasil bernilai `True` hanya jika **kedua kondisi bernilai True**.

| **P** | **Q** | **Hasil (P AND Q)** |
| :---: | :---: | :-----------------: |
|   T   |   T   |        **T**        |
|   T   |   F   |        **F**        |
|   F   |   T   |        **F**        |
|   F   |   F   |        **F**        |

#### Pemetaan Variabel

* **Lulus:** P = Absen, Q = Nilai
* **Daftar:** P = Lunas, Q = Berkas
* **Pinjam:** P = Kartu, Q = Stok

---

### 2. Logika OR (Disjungsi)

**Berlaku untuk kasus:** Remed, Libur, dan Denda.

> Hasil bernilai `True` jika **minimal satu kondisi bernilai True**.

| **P** | **Q** | **Hasil (P OR Q)** |
| :---: | :---: | :----------------: |
|   T   |   T   |        **T**       |
|   T   |   F   |        **T**       |
|   F   |   T   |        **T**       |
|   F   |   F   |        **F**       |

#### Pemetaan Variabel

* **Remed:** P = Teori, Q = Praktik
* **Libur:** P = Minggu, Q = Nasional
* **Denda:** P = Telat, Q = Rusak

---

### 3. Logika XOR (Exclusive OR)

**Berlaku untuk kasus:** Ekskul, Shift, dan Rapor.

> Hasil bernilai `True` hanya jika **kedua kondisi berbeda**, yaitu hanya salah satu kondisi yang bernilai `True`.

| **P** | **Q** | **Hasil (P XOR Q)** |
| :---: | :---: | :-----------------: |
|   T   |   T   |        **F**        |
|   T   |   F   |        **T**        |
|   F   |   T   |        **T**        |
|   F   |   F   |        **F**        |

#### Pemetaan Variabel

* **Ekskul:** P = Pramuka, Q = Paskibra
* **Shift:** P = Pagi, Q = Sore
* **Rapor:** P = Cetak, Q = PDF

---

### Ringkasan

| **Logika** | **Operator Python** | **Kondisi True**            |
| :--------: | :-----------------: | --------------------------- |
|   **AND**  |        `and`        | Semua kondisi harus `True`  |
|   **OR**   |         `or`        | Minimal satu kondisi `True` |
|   **XOR**  |         `!=`        | Kedua kondisi harus berbeda |

### Kesimpulan

Tabel kebenaran digunakan untuk melihat hasil dari kombinasi nilai **True (`T`)** dan **False (`F`)** pada setiap operator logika. Dalam studi kasus sistem sekolah, **AND** digunakan ketika semua syarat harus terpenuhi, **OR** digunakan ketika salah satu syarat sudah cukup, sedangkan **XOR** digunakan ketika hanya salah satu dari dua kondisi yang boleh terpenuhi.
