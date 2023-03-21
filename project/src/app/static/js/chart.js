var data = [30, 61, 74, 46, 52, 41, 89, 61, 62, 45, 36, 79, 84, 57, 44, 45, 41, 49, 36, 79, 62, 81, 74, 34, 62, 37, 82, 58, 58, 57]

var options = {
  series: [{
    name: "Water Consumption (in Kilo Litres)",
    data: [38, 33, 40, 38, 39, 43, 51, 48, 43]
}],
  chart: {
  height: 350,
  type: 'line',
  zoom: {
    enabled: false
  }
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
title: {
  text: 'Monthly Water Consumption Trend',
  align: 'left'
},
grid: {
  row: {
    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
    opacity: 0.5
  },
},
xaxis: {
  categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
}
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();

// chart2

      // Replace Math.random() with a pseudo-random number generator to get reproducible results in e2e tests
      // Based on https://gist.github.com/blixt/f17b47c62508be59987b
      var _seed = 42;
      Math.random = function() {
        _seed = _seed * 16807 % 2147483647;
        return (_seed - 1) / 2147483646;
      };

  /*
    // this function will generate output in this format
    // data = [
        [timestamp, 23],
        [timestamp, 33],
        [timestamp, 12]
        ...
    ]
  */
  function generateDayWiseTimeSeries(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = baseval;
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  
      series.push([x, y]);
      baseval += 86400000;
      i++;
    }
    return series;
  }
  
  var data = generateDayWiseTimeSeries(new Date('11 Jan 2017').getTime(), 185, {
    min: 30,
    max: 90
  })




      
        var options = {
          series: [{
          data: data
        }],
          chart: {
          id: 'chart2',
          type: 'line',
          height: 230,
          toolbar: {
            autoSelected: 'pan',
            show: false
          }
        },
        colors: ['#546E7A'],
        stroke: {
          width: 3
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          opacity: 1,
        },
        markers: {
          size: 0
        },
        xaxis: {
          type: 'datetime'
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart-line2"), options);
        chart.render();
      
        var optionsLine = {
          series: [{
          data: data
        }],
          chart: {
          id: 'chart1',
          height: 130,
          type: 'area',
          brush:{
            target: 'chart2',
            enabled: true
          },
          selection: {
            enabled: true,
            xaxis: {
              min: new Date('19 Jun 2017').getTime(),
              max: new Date('14 Aug 2017').getTime()
            }
          },
        },
        colors: ['#008FFB'],
        fill: {
          type: 'gradient',
          gradient: {
            opacityFrom: 0.91,
            opacityTo: 0.1,
          }
        },
        xaxis: {
          type: 'datetime',
          tooltip: {
            enabled: false
          }
        },
        yaxis: {
          tickAmount: 2
        }
        };

        var chartLine = new ApexCharts(document.querySelector("#chart-line"), optionsLine);
        chartLine.render();
      

        // chart: 3 in 1
        // Replace Math.random() with a pseudo-random number generator to get reproducible results in e2e tests
      // Based on https://gist.github.com/blixt/f17b47c62508be59987b
      
      var _seed = 42;
      Math.random = function() {
        _seed = _seed * 16807 % 2147483647;
        return (_seed - 1) / 2147483646;
      };

      var options = {
        series: [{
          name: "Current Consumption",
          data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
        },
        {
          name: "Ideal Consumption",
          data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
        },
        {
          name: 'Consumption without Phoenix',
          data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
        }
      ],
        chart: {
        height: 350,
        type: 'line',
        zoom: {
          enabled: false
        },
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        width: [5, 7, 5],
        curve: 'straight',
        dashArray: [0, 8, 5]
      },
      title: {
        text: 'Monthly Water Saved with Phoenix',
        align: 'left'
      },
      legend: {
        tooltipHoverFormatter: function(val, opts) {
          return val + ' - <strong>' + opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] + '</strong>'
        }
      },
      markers: {
        size: 0,
        hover: {
          sizeOffset: 6
        }
      },
      xaxis: {
        categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan',
          '10 Jan', '11 Jan', '12 Jan'
        ],
      },
      tooltip: {
        y: [
          {
            title: {
              formatter: function (val) {
                return val + " (mins)"
              }
            }
          },
          {
            title: {
              formatter: function (val) {
                return val + " per session"
              }
            }
          },
          {
            title: {
              formatter: function (val) {
                return val;
              }
            }
          }
        ]
      },
      grid: {
        borderColor: '#f1f1f1',
      }
      };

      var chart = new ApexCharts(document.querySelector("#lols"), options);
      chart.render();

      // chart 3
window.Promise ||
  document.write(
    '<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"><\/script>'
  )
window.Promise ||
  document.write(
    '<script src="https://cdn.jsdelivr.net/npm/eligrey-classlist-js-polyfill@1.2.20171210/classList.min.js"><\/script>'
  )
window.Promise ||
  document.write(
    '<script src="https://cdn.jsdelivr.net/npm/findindex_polyfill_mdn"><\/script>'
  )


      // Replace Math.random() with a pseudo-random number generator to get reproducible results in e2e tests
      // Based on https://gist.github.com/blixt/f17b47c62508be59987b
      var _seed = 42;
      Math.random = function() {
        _seed = _seed * 16807 % 2147483647;
        return (_seed - 1) / 2147483646;
      };

      var options = {
        title: {
          text: 'Actual Vs Projected Hourly Water Usage ',
          align: 'left'
        },
        series: [{
        name: 'actual',
        data: [31, 40, 28, 51, 42, 109, 100]
      }, {
        name: 'projected (ideal)',
        data: [11, 32, 45, 32, 34, 52, 41]
      }],
        chart: {
        height: 350,
        type: 'area'
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth'
      },
      xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
      },
      tooltip: {
        x: {
          format: 'dd/MM/yy HH:mm'
        },
      },
      };

      var chart = new ApexCharts(document.querySelector("#analysis"), options);
      chart.render();

        // real time chart
      // Replace Math.random() with a pseudo-random number generator to get reproducible results in e2e tests
      // Based on https://gist.github.com/blixt/f17b47c62508be59987b
      var _seed = 42;
      Math.random = function() {
        _seed = _seed * 16807 % 2147483647;
        return (_seed - 1) / 2147483646;
      };

  var lastDate = 0;
  var data = []
  var TICKINTERVAL = 86400000
  let XAXISRANGE = 777600000
  function getDayWiseTimeSeries(baseval, count, yrange) {
    var i = 0;
    while (i < count) {
      var x = baseval;
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  
      data.push({
        x, y
      });
      lastDate = baseval
      baseval += TICKINTERVAL;
      i++;
    }
  }
  
  getDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 10, {
    min: 10,
    max: 90
  })
  
  function getNewSeries(baseval, yrange) {
    var newDate = baseval + TICKINTERVAL;
    lastDate = newDate
  
    for(var i = 0; i< data.length - 10; i++) {
      // IMPORTANT
      // we reset the x and y of the data which is out of drawing area
      // to prevent memory leaks
      data[i].x = newDate - XAXISRANGE - TICKINTERVAL
      data[i].y = 0
    }
  
    data.push({
      x: newDate,
      y: Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
    })
  }
  
  function resetData(){
    // Alternatively, you can also reset the data at certain intervals to prevent creating a huge series 
    data = data.slice(data.length - 10, data.length);
  }


        var options = {
          series: [{
          data: data.slice()
        }],
          chart: {
          id: 'realtime',
          height: 350,
          type: 'line',
          animations: {
            enabled: true,
            easing: 'linear',
            dynamicAnimation: {
              speed: 1000
            }
          },
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Phoenix Chip Utilization (%)',
          align: 'left'
        },
        markers: {
          size: 0
        },
        xaxis: {
          labels: {
            show: false
          },
          type: 'datetime',
          range: XAXISRANGE,
        },
        yaxis: {
          max: 100
        },
        legend: {
          show: false
        },
        };

        var chart = new ApexCharts(document.querySelector("#real-time"), options);
        chart.render();
      
      
        window.setInterval(function () {
        getNewSeries(lastDate, {
          min: 10,
          max: 90
        })
      
        chart.updateSeries([{
          data: data
        }])
      }, 1000)
    

