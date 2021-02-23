var myVar = setInterval(myTimer, 1000);
now = Date.now();

function myTimer() {
  var hasil = document.getElementById("time")
  elapsedMil = Date.now() - now;
  menit = Math.floor(elapsedMil/60000) % 60
  detik = Math.floor(elapsedMil/1000) % 60;

  function padTime(num) {
    if(num<10) {
      num = "0" + num;
    }
    return num;
  }

  min = padTime(menit);
  sec = padTime(detik);

  hasil.innerHTML = "Waktu : " + min + ":" + sec;
}