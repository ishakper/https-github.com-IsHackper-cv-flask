from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Path folder gambar
IMAGE_FOLDER = os.path.join(os.getcwd(), "image")

# Routing untuk menampilkan gambar
@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

HTML = '''
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CV - Ishak Hadi Pernama</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    :root { --accent:#ff7a00; }
    body { background:#f7f9fb; font-family:Inter,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial; }

    /* ANIMASI */
    .fade-in {
      opacity: 0;
      transform: translateY(20px);
      animation: fadeInUp 0.8s ease forwards;
    }
    .fade-in:nth-child(2) { animation-delay: 0.3s; }
    .fade-in:nth-child(3) { animation-delay: 0.6s; }

    @keyframes fadeInUp {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .avatar { width:140px; height:140px; border-radius:50%; object-fit:cover; transition: transform 0.3s ease; }
    .avatar:hover { transform: scale(1.1) rotate(3deg); }

    .left-panel { background:#2b2b2b; color:#fff; padding:2rem; border-radius:14px; transition: transform 0.3s ease; }
    .left-panel:hover { transform: scale(1.02); }
    .left-panel a, .left-panel p { color:#fff; text-decoration:none; }

    .right-panel { background:#fff; border-radius:14px; padding:2rem; box-shadow:0 2px 8px rgba(0,0,0,0.05); transition: box-shadow 0.3s ease; }
    .right-panel:hover { box-shadow:0 8px 20px rgba(0,0,0,0.1); }

    ul li { transition: transform 0.2s ease, color 0.2s ease; }
    ul li:hover { transform: translateX(5px); color: var(--accent); }
  </style>
</head>
<body>
  <div class="container my-5">
    <div class="row g-4">
      <div class="col-lg-4 fade-in">
        <div class="left-panel text-center">
          <!-- FOTO PROFIL -->
          <img src="/image/profil.jpg" class="avatar mb-3" alt="foto">
          <h3 class="fw-bold">ISHAK HADI PERNAMA</h3>
          <p>Mahasiswa</p>
          <hr class="border-light">
          <h5 class="mt-4">CONTACT</h5>
          <p>📞 085733573036</p>
          <p>📧 ishakhadipernama@gmail.com</p>
          <p>📍 Sidoarjo RT 02, RW 02, Kec. Doko, Kab. Blitar</p>
          <h5 class="mt-4">EDUCATION</h5>
          <p><strong>SMK 1 DOKO</strong><br>Jurusan Bisnis dan Informatika<br><small>2018 - 2021</small></p>
          <p><strong>Politeknik Negeri Banyuwangi</strong><br>Jurusan Bisnis dan Informatika<br><small>2021 - Sekarang</small></p>
          <h5 class="mt-4">SKILLS</h5>
          <ul class="list-unstyled">
            <li>📌 Manajemen Organisasi</li>
            <li>📌 Kepemimpinan</li>
            <li>📌 Kerja Tim</li>
            <li>📌 Pemrograman Dasar</li>
            <li>📌 Web Development</li>
          </ul>
          <h5 class="mt-4">LANGUAGE</h5>
          <p>Indonesia (Aktif)<br>English (Pasif)</p>
        </div>
      </div>
      <div class="col-lg-8 fade-in">
        <div class="right-panel">
          <h4 class="fw-bold">PROFILE</h4>
          <p>Mahasiswa Teknologi Rekayasa Perangkat Lunak Politeknik Negeri Banyuwangi angkatan 2023 dengan pengalaman kepemimpinan dan organisasi...</p>
          <h4 class="fw-bold mt-4">EXPERIENCE</h4>
          <div class="mb-3">
            <h6 class="mb-0">Ketua Umum – FORBIMWANGI</h6>
            <small class="text-muted">2023 - 2025</small>
            <ul>
              <li>Memimpin dan mengelola organisasi.</li>
              <li>Menginisiasi program pengembangan anggota.</li>
              <li>Mengawasi dan mengkoordinasi aktivitas organisasi.</li>
            </ul>
          </div>
          <div class="mb-3">
            <h6 class="mb-0">Anggota Departemen PSDM – Himpunan Mahasiswa Bisnis dan Informatika</h6>
            <small class="text-muted">2023 - 2024</small>
            <ul>
              <li>Mengembangkan program peningkatan keterampilan anggota.</li>
              <li>Membantu koordinasi pelaksanaan kegiatan organisasi.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
