// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctxd10 = document.getElementById("myBarChart_10");
var ctxd50 = document.getElementById("myBarChart_50");
var ctxd100 = document.getElementById("myBarChart_100");
var ctxd500 = document.getElementById("myBarChart_500");
var ctxd1000 = document.getElementById("myBarChart_1000");

var bar10 = new Chart(ctxd10, {
  type: 'bar',
  data: {
    labels: ["Naive Bayes", "Naive Bayes - Semantic Approach"],
    datasets: [{
      label: "Sentiment",
      backgroundColor: "rgba(193,76,76,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [60, 80],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

var bar50 = new Chart(ctxd50, {
  type: 'bar',
  data: {
    labels: ["Naive Bayes", "Naive Bayes - Semantic Approach"],
    datasets: [{
      label: "Sentiment",
      backgroundColor: "rgba(220,163,106,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [48, 60],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

var bar100 = new Chart(ctxd100, {
  type: 'bar',
  data: {
    labels: ["Naive Bayes", "Naive Bayes - Semantic Approach"],
    datasets: [{
      label: "Sentiment",
      backgroundColor: "rgba(239,232,46,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [36, 50],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

var bar500 = new Chart(ctxd500, {
  type: 'bar',
  data: {
    labels: ["Naive Bayes", "Naive Bayes - Semantic Approach"],
    datasets: [{
      label: "Sentiment",
      backgroundColor: "rgba(21,116,45,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [51.8, 60],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

var bar1000 = new Chart(ctxd1000, {
  type: 'bar',
  data: {
    labels: ["Naive Bayes", "Naive Bayes - Semantic Approach"],
    datasets: [{
      label: "Sentiment",
      backgroundColor: "rgba(46,149,239,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [50.1, 50],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});