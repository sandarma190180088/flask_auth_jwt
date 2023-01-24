# Learn Postgresql

## Fitur-fitur PostgreSQL

- **************Asynchronous Replication************** - Menggandakan database secara asinkron.
- ******************Data Integrity****************** - Mendukung Primary Key, Foreign, dan lain-lain.
- **************Inheritance************** - Mewariskan Karakteristik objek induk ke objek keturunan.
- ********Non-Relational Support******** - Mendukung perintah non-relasional seperti ****Json****
- ****Point-in-time Recovery**** - Melakukan backup server secara terus menerus
- ****************************************Procedural Languages**************************************** - Mendukung bahasa prosedural misalnya Python, Perl, dan lain sebagainya
- ******************************Rule Customization****************************** - Melakukan Kustomisasi terhadap perintah seperti INSERT, UPDATE, atau DELETE
- **********Savepoints********** - Menangani error transaksi kompleks
- **************Tablespaces************** - Menentukan media penyimpanan database,schema,atau tabel.

## **************************Tipe Data pada PostgreSQL**************************

- ********************Boolean —******************** true,false,null
- **************Character —************** CHAR,VARCHAR,TEXT
- ************************Numeric —************************ SMALLINT,INT,SERIAL,float,real,numeric
- **************************Temporal —************************** DATE,TIME,TIMESTAMP,TIMESTAMPTZ,INTERVAL
- ********************Array —******************** Array String, Array integer
- **********JSON —********** JSON,JSONB
- ******************UUID —****************** uuid-ossp,uuid_generate_v1,uuid_generate_v4
- ********Special Data Types —******** box,line,point,lseg,polygon,inet,macaddr

## ********************Perbandingan PostgreSQL dan MySQL********************

| Perbandingan | MySQL | PostgreSQL |
| --- | --- | --- |
| Lisensi | Open source tapi juga menyediakan versi berbayar | Open source dan gratis |
| Standar (kebijakan, spesifikasi, fitur) SQL | Mendukung sebagian standar SQL | Mendukung semua standar SQL |
| Dukungan platform | Solaris, Windows OS, Linux, OS X, FreeBSD OS | Solaris, Windows OS, Linux, OS X, Unix-OS, Hp-UX OS |
| Dukungan bahasa pemrograman | C/C++, Erlang, PHP, Lisp, Go, Perl, dll. | C/C++, Java, .Net, R, Perl, Python, JavaScript, dll. |
| Keamanan | Menawarkan fitur keamanan bawaan | Menawarkan fitur keamanan SSL |
| Replikasi | Mendukung replikasi master ke master | Mendukung replikasi master ke replika |
| Implementasi | Cocok digunakan untuk sistem yang hanya butuh transaksi data, contoh: Sistem Akademik | Cocok digunakan untuk sistem yang butuh eksekusi query kompleks, contoh: GIS |
| Dukungan Komunitas | Fokus pada pemeliharaan fitur yang ada | Fokus pada peningkatan fitur yang ada |
| Perkembangan | Jarang merilis fitur baru | Sering merilis fitur baru |

## Learn Query SQL

[Learn Basic SQL](https://www.notion.so/Learn-Basic-SQL-887cab4f63dd4acb93b6d5a22a33d4b9)

## Learn Basic Syntax PostgreSQL

[https://www.youtube.com/watch?v=qw--VYLpxG4](https://www.youtube.com/watch?v=qw--VYLpxG4)

| Perintah | Fungsi |
| --- | --- |
| sudo su - postgres | masuk kedalam postgres |
| psql -h http://localhost -p 5432 <username> | masuk kedalam psql  |
| psql -U <user> -W | masuk kedalam psql  |
|  |  |

---

[17 Practical psql Commands](https://www.notion.so/17-Practical-psql-Commands-52115e2d46ac47cebf93ff33211458f8)