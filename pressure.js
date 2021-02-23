function rand() {
    return Math.random();
  }
  
  var layout = {
    title: 'Grafik Pembacaan Tekanan',
  }

  Plotly.newPlot('press', [{
    y: [1].map(rand),
    mode: 'lines',
    line: {color: '#80CAF6'}
  }], layout);
  
  var cnt = 0;
  
  var interval = setInterval(function() {
  
    Plotly.extendTraces('press', {
      y: [[rand()]]
    }, [0])
  
    if(++cnt === 100) clearInterval(interval);
  }, 1000);