function rand() {
    return Math.random();
  }
  
  var time = new Date();
  
  var trace1 = {
    // x: [],
    y: [1].map(rand),
    name: 'Pitch',
    mode: 'lines',
    line: {color: '#80CAF6'}
  }
  
  var trace2 = {
    // x: [],
    y: [1].map(rand),
    name: 'Yaw',
    xaxis: 'x2',
    yaxis: 'y2',
    mode: 'lines',
    line: {color: '#DF56F1'}
  };

  var trace3 = {
    // x: [],
    y: [1].map(rand),
    xaxis: 'x3',
    yaxis: 'y3',
    name: 'Roll',
    mode: 'lines',
    line: {color: '#1a2a4c'}
  };
  
  var layout = {
    title: 'Grafik Pembacaan Pitch,Yaw,Roll',
    grid: {rows: 3, columns: 1, pattern: 'independent'}
  }
  
  var dataxx = [trace1,trace2,trace3];

  Plotly.newPlot('pyw', dataxx, layout);
  
  var cnt = 0;
  
  var interval = setInterval(function() {
  
    // var time = new Date();
  
    var update = {
      // x: [[time], [time], [time]],
      y: [[rand()], [rand()], [rand()]]
    }
    
    Plotly.extendTraces('pyw', update, [0,1,2])
  
    if(++cnt === 100) clearInterval(interval);
  }, 1000);