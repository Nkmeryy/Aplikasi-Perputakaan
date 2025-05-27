from flask import Flask, render_template, request, redirect, url_for
from models import db, Buku, Penulis, Penerbit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/perpustakaan'  # Ganti dengan user/password kamu
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Jalankan create_all() hanya jika tabel belum dibuat (bisa dihapus kalau sudah pakai phpMyAdmin)
with app.app_context():
    db.create_all()

# DASHBOARD
@app.route('/')
def dashboard():
    total_buku = Buku.query.count()
    total_penulis = Penulis.query.count()
    total_penerbit = Penerbit.query.count()
    return render_template('dashboard/index.html',
                           total_buku=total_buku,
                           total_penulis=total_penulis,
                           total_penerbit=total_penerbit)

# BUKU
@app.route('/buku')
def list_buku():
    buku = Buku.query.all()
    penulis = Penulis.query.all()
    penerbit = Penerbit.query.all()
    return render_template('buku/index.html',
                           buku=buku,
                           penulis=penulis,
                           penerbit=penerbit)

@app.route('/buku/tambah', methods=['POST'])
def tambah_buku():
    judul = request.form.get('judul')
    id_penulis = request.form.get('id_penulis')
    id_penerbit = request.form.get('id_penerbit')

    if judul and id_penulis and id_penerbit:
        buku = Buku(judul=judul, id_penulis=id_penulis, id_penerbit=id_penerbit)
        db.session.add(buku)
        db.session.commit()
    return redirect(url_for('list_buku'))

# PENULIS
@app.route('/penulis')
def list_penulis():
    penulis = Penulis.query.all()
    return render_template('penulis/index.html', penulis=penulis)

@app.route('/penulis/tambah', methods=['POST'])
def tambah_penulis():
    nama_penulis = request.form.get('nama_penulis')
    bio = request.form.get('bio')
    if nama_penulis and bio:
        db.session.add(Penulis(nama_penulis=nama_penulis,bio=bio))
        db.session.commit()
    return redirect(url_for('list_penulis'))

# PENERBIT
@app.route('/penerbit')
def list_penerbit():
    penerbit = Penerbit.query.all()
    return render_template('penerbit/index.html', penerbit=penerbit)

@app.route('/penerbit/tambah', methods=['POST'])
def tambah_penerbit():
    nama_penerbit = request.form.get('nama_penerbit')
    alamat = request.form.get('alamat')
    kontak = request.form.get('kontak')
    if nama_penerbit and alamat and kontak:
        db.session.add(Penerbit(nama_penerbit=nama_penerbit,alamat=alamat,kontak=kontak))
        db.session.commit()
    return redirect(url_for('list_penerbit'))

# MAIN
if __name__ == '__main__':
    app.run(debug=True)
