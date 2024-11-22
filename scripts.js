// Mendapatkan elemen modal dan gambar
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');
const closeModal = document.querySelector('.modal .close');

// Tambahkan event listener ke setiap item galeri
document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
        const imgSrc = item.querySelector('img').src;
        modal.style.display = 'flex';
        modalImg.src = imgSrc;
    });
});

// Tutup modal
closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Tutup modal saat klik di luar gambar
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
