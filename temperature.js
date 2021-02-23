function rand() {
    return Math.random();
  }
  
  var layout = {
    title: 'Grafik Pembacaan Temperature',
  }

  Plotly.newPlot('temp', [{
    y: [1].map(rand),
    mode: 'lines',
    line: {color: '#80CAF6'}
  }], layout);
  
  var cnt = 0;
  
  var interval = setInterval(function() {
  
    Plotly.extendTraces('temp', {
      y: [[rand()]]
    }, [0])
  
    if(++cnt === 100) clearInterval(interval);
  }, 1000);