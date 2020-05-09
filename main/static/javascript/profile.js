function loadImg(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var dataURL = reader.result;
        var output = document.getElementById('profilePic');
        output.src = dataURL;
    };
    reader.readAsDataURL(input.files[0]);
  };




