// kirim.js
// JavaScript untuk mengirim form dengan AJAX

// Menambahkan event listener saat halaman dimuat
window.addEventListener('DOMContentLoaded', function () {
    // Mengambil elemen form
    var form = document.getElementById('presensiForm');
  
    // Mengirim form dengan AJAX
    function sendForm(event) {
      event.preventDefault();
      var formData = new FormData(form);
      var xhr = new XMLHttpRequest();
      xhr.open('POST', form.action, true);
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          // Respon sukses, lakukan sesuatu
          console.log('Form submitted successfully');
        }
      };
      xhr.send(formData);
    }
  
    // Mengikat fungsi pengiriman form ke event submit form
    form.addEventListener('submit', sendForm);
  });
  