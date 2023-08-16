// webcam.js
// JavaScript untuk mengendalikan fitur webcam

// Memeriksa dukungan webcam pada browser
function hasWebcamSupport() {
  return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
}

// Mengambil elemen video dan gambar dari DOM
var video = document.getElementById('webcamVideo');
var imagePreview = document.getElementById('previewImage');

// Mengaktifkan webcam
function activateWebcam() {
  if (hasWebcamSupport()) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;
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
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  var context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  var dataURL = canvas.toDataURL('image/png');
  imagePreview.src = dataURL;
  imagePreview.style.display = 'block'; // Menampilkan elemen imagePreview
  video.style.display = 'none';
  document.getElementById('captureButton').style.display = 'none';
  document.getElementById('ulangButton').style.display = 'block';
}

// Mengulang proses pengambilan foto
function retakePhoto() {
  imagePreview.style.display = 'none';
  video.style.display = 'block';
  document.getElementById('captureButton').style.display = 'block';
  document.getElementById('ulangButton').style.display = 'none';
}

// Mengaktifkan webcam saat halaman dimuat
window.addEventListener('DOMContentLoaded', function () {
  activateWebcam();
});

// Mengikat fungsi-fungsi ke elemen tombol
document.getElementById('captureButton').addEventListener('click', capturePhoto);
document.getElementById('ulangButton').addEventListener('click', retakePhoto);
