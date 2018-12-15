var myCharts = require("../../../utils/wxcharts.js")//引入一个绘图的插件

var lineChart_hum = null

var lineChart_light = null

var lineChart_tempe = null
// var lineChart_fog = null

var app = getApp()



Page({

  data: {

  },

  onPullDownRefresh: function () {

    console.log('onPullDownRefresh', new Date())

  },
  getDataFromOneNet: function (cb) {
    var that = this;

    //从oneNET请求我们的Wi-Fi气象站的数据

    const requestTask = wx.request({

      url: 'https://api.heclouds.com/devices/yourid/datapoints?datastream_id=Light,Temperature,Humidity&limit=15',

      header: {

        'content-type': 'application/json',

        'api-key': 'yours'

      },

      success: function (res) {

        //console.log(res.data)

        //拿到数据后保存到全局数据

        var app = getApp()

        app.globalData.temperature = res.data.data.datastreams[0]

        app.globalData.light = res.data.data.datastreams[1]

        app.globalData.humidity = res.data.data.datastreams[2]

        cb(that)
      },



      fail: function (res) {

        console.log("fail!!!")

      },



      complete: function (res) {

        console.log("end")

      }

    })

  },




  //把拿到的数据转换成绘图插件需要的输入格式

  convert: function () {

    var categories = [];

    var humidity = [];

    var light = [];

    var tempe = [];
    // var fog =[];



    var length = app.globalData.light.datapoints.length

    for (var i = 0; i < length; i++) {

      categories.push(app.globalData.humidity.datapoints[i].at.slice(11, 19));

      humidity.push(app.globalData.humidity.datapoints[i].value);

      light.push(app.globalData.light.datapoints[i].value);

      tempe.push(app.globalData.temperature.datapoints[i].value);
      // fog.push(app.globalData.fog.datapoints[i].value);

    }

    return {

      categories: categories,

      humidity: humidity,

      light: light,

      tempe: tempe,
      // fog:  fog

    }

  },






  onLoad: function () {
    this.getDataFromOneNet(createChart)
  }


})

function createChart(that) {

    var wheatherData = that.convert();



    //得到屏幕宽度

    var windowWidth = 320;

    try {

      var res = wx.getSystemInfoSync();

      windowWidth = res.windowWidth;

    } catch (e) {

      console.error('getSystemInfoSync failed!');

    }



    var wheatherData = that.convert();



    //新建湿度图表

    lineChart_hum = new myCharts({

      canvasId: 'humidity',

      type: 'line',

      categories: wheatherData.categories,

      animation: true,

      background: '#232323',

      series: [{

        name: 'humidity',

        data: wheatherData.humidity,

        format: function (val, name) {

          return val.toFixed(2);

        }

      }],

      xAxis: {

        disableGrid: true

      },

      yAxis: {

        title: 'humidity (%)',

        format: function (val) {

          return val.toFixed(2);

        },

        min: 55

      },

      width: windowWidth,

      height: 150,

      dataLabel: false,

      dataPointShape: true,

      extra: {

        lineStyle: 'curve'

      }

    });
    //新建烟雾图表
    // lineChart_fog = new myCharts({

    //   canvasId: 'fog',

    //   type: 'line',

    //   categories: wheatherData.categories,

    //   animation: true,

    //   background: '#f5f5f5',

    //   series: [{

    //     name: 'fog',

    //     data: wheatherData.fog,

    //     format: function (val, name) {

    //       return val.toFixed(2);

    //     }

    //   }],

    //   xAxis: {

    //     disableGrid: true

    //   },

    //   yAxis: {

    //     title: 'fog (浓度)',

    //     format: function (val) {

    //       return val.toFixed(2);

    //     },

    //     min: 55

    //   },

    //   width: windowWidth,

    //   height: 150,

    //   dataLabel: false,

    //   dataPointShape: true,

    //   extra: {

    //     lineStyle: 'curve'

    //   }

    // });

    //新建光照强度图表

    lineChart_light = new myCharts({

      canvasId: 'light',

      type: 'line',

      categories: wheatherData.categories,

      animation: true,

      background: '#f5f5f5',

      series: [{

        name: 'light',

        data: wheatherData.light,

        format: function (val, name) {

          return val.toFixed(2);

        }

      }],

      xAxis: {

        disableGrid: true

      },

      yAxis: {

        title: 'light (lux)',

        format: function (val) {

          return val.toFixed(2);

        },

        min: 190

      },

      width: windowWidth,

      height: 150,

      dataLabel: false,

      dataPointShape: true,

      extra: {

        lineStyle: 'curve'

      }

    });



    //新建温度图表

    lineChart_tempe = new myCharts({

      canvasId: 'tempe',

      type: 'line',

      categories: wheatherData.categories,

      animation: true,

      background: '#f5f5f5',

      series: [{

        name: 'temperature',

        data: wheatherData.tempe,

        format: function (val, name) {

          return val.toFixed(2);

        }

      }],

      xAxis: {

        disableGrid: true

      },

      yAxis: {

        title: 'temperature (摄氏度)',

        format: function (val) {

          return val.toFixed(2);

        },

        min: 24

      },

      width: windowWidth,

      height: 150,

      dataLabel: false,

      dataPointShape: true,

      extra: {

        lineStyle: 'curve'

      }

    });

}