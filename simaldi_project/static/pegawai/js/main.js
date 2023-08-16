// Mengambil elemen video, gambar, form, dan elemen input nama pegawai
var videoElement = document.getElementById('webcamVideo');
var imagePreview = document.getElementById('previewImage');
var form = document.getElementById('presensiForm');
var namaPegawaiInput = document.getElementById('namaPegawai');

// Memeriksa dukungan webcam pada browser
function hasWebcamSupport() {
  return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
}

// Mengaktifkan webcam
function activateWebcam() {
  if (hasWebcamSupport()) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        videoElement.srcObject = stream;
      })
      .catch(function (error) {
        console.log('Error accessing webcam:', error);
      });
  } else {
    console.log('Webcam not supported');
  }
}

// Mengambil foto dari webcam
function capturePhoto() {
  var canvas = document.createElement('canvas');
  canvas.width = videoElement.videoWidth;
  canvas.height = videoElement.videoHeight;
  var context = canvas.getContext('2d');
  context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
  var dataURL = canvas.toDataURL('image/png');
  imagePreview.src = dataURL;
  imagePreview.style.display = 'block'; // Menampilkan elemen imagePreview
  videoElement.style.display = 'none';
  document.getElementById('captureButton').style.display = 'none';
  document.getElementById('ulangButton').style.display = 'block';
}

// Mengulang proses pengambilan foto
function retakePhoto() {
  imagePreview.style.display = 'none';
  videoElement.style.display = 'block';
  document.getElementById('captureButton').style.display = 'block';
  document.getElementById('ulangButton').style.display = 'none';
}

// Fungsi validasi saat form dikirim
function validateForm(event) {
  var errorMessage = document.getElementById('namaError');
  if (namaPegawaiInput.value.trim() === '') {
    errorMessage.textContent = 'Nama pegawai harus diisi';
    event.preventDefault();
  } else {
    errorMessage.textContent = '';
  }
}

// Mengirim form dengan AJAX
function sendForm(event) {
  event.preventDefault();

  var formData = new FormData(form);
  var dataURL = imagePreview.getAttribute('src');
  var blob = dataURItoBlob(dataURL);
  formData.append('buktiAbsen', blob, 'bukti.png');

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

// Mengubah data URI menjadi Blob
function dataURItoBlob(dataURI) {
  var byteString = atob(dataURI.split(',')[1]);
  var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
  var ab = new ArrayBuffer(byteString.length);
  var ia = new Uint8Array(ab);
  for (var i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  return new Blob([ab], { type: mimeString });
}

// Menambahkan event listener saat halaman dimuat
window.addEventListener('DOMContentLoaded', function () {
  activateWebcam();

  // Mengikat fungsi validasi ke event submit form
  form.addEventListener('submit', validateForm);

  // Mengikat fungsi pengiriman form ke event submit form
  form.addEventListener('submit', sendForm);

  // Mengikat fungsi-fungsi ke elemen tombol
  document.getElementById('captureButton').addEventListener('click', capturePhoto);
  document.getElementById('ulangButton').addEventListener('click', retakePhoto);
});
