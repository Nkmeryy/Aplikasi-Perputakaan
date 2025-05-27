from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Penulis(db.Model):
    __tablename__ = 'penulis'
    id_penulis = db.Column(db.Integer, primary_key=True)
    nama_penulis = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)

    buku = db.relationship('Buku', backref='penulis', lazy=True)


class Penerbit(db.Model):
    __tablename__ = 'penerbit'
    id_penerbit = db.Column(db.Integer, primary_key=True)
    nama_penerbit = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.Text)
    kontak = db.Column(db.String(50))

    buku = db.relationship('Buku', backref='penerbit', lazy=True)


class Buku(db.Model):
    __tablename__ = 'buku'
    id_buku = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(150), nullable=False)
    tahun_terbit = db.Column(db.Integer)
    id_penulis = db.Column(db.Integer, db.ForeignKey('penulis.id_penulis'), nullable=True)
    id_penerbit = db.Column(db.Integer, db.ForeignKey('penerbit.id_penerbit'), nullable=True)
    isbn = db.Column(db.String(20))
    jumlah_halaman = db.Column(db.Integer)
    sinopsis = db.Column(db.Text)
