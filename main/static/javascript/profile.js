function loadImg() {
    var url = document.getElementById('url_input');
    console.log(url.value)
    var output = document.getElementById('profilePic');
    output.src = url.value;
  };




