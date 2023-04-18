

var socket = io();

socket.on('connect', function () {
    console.log('conectados');
    socket.on('event', (res) => {
        console.log(res);
    });    
});

socket.on('processed_buscar_faces',  (res) =>{
    console.log('respuesta de camara server:', res);
    // res = atob(res);
    // Obtener la etiqueta de imagen
    let img = document.getElementById("imagen");

// Asignar el valor del atributo src
    img.src = "data:image/jpg;base64," + res;
    // console.log(decodedString);

});

// socket.on('processed_stream', function(processed_data) {
//   var video = document.getElementById('processed_video');
//   video.src = 'data:image/jpeg;base64,' + processed_data;
// });

navigator.mediaDevices.getUserMedia({video: true})
  .then(stream => {
    var video = document.getElementById("video");
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    
    video.srcObject = stream;
    video.addEventListener("loadedmetadata", () => {
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
    });
    
    setInterval(() => {
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      var imageData = canvas.toDataURL("image/png");
      socket.emit('buscarFaces', imageData);
    // }, 1000/2); // envía 30 frames por segundo
    }, 600); // envía 1 frames por segundo
  })
  .catch(error => {
    console.log("Error accessing camera: " + error.message);
  });
// navigator.mediaDevices.getUserMedia({video: true})
//   .then(stream => {
//     var video = document.getElementById("video");
//     video.srcObject = stream;
//     // console.log(stream)
//     socket.emit('stream', stream);
//     // var streamId = socket.id;
//   })
//   .catch(error => {
//     console.log("Error accessing camera: " + error.message);
//   });