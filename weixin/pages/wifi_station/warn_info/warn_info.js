var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  warn_info: function () {

    //从oneNET请求我们的Wi-Fi气象站的数据

    const requestTask = wx.request({

      url: 'https://api.heclouds.com/devices/503088492/datapoints?datastream_id=Light,Temperature,Humidity&limit=15',

      header: {

        'content-type': 'application/json',

        'api-key': 'aAug=c8Dtwym3XrIOcgg3C2u=fY='

      },

      success: function (res) {

        //console.log(res.data)

        //拿到数据后保存到全局数据

        var app = getApp()

        app.globalData.temperature = res.data.data.datastreams[0]

        app.globalData.light = res.data.data.datastreams[1]

        app.globalData.humidity = res.data.data.datastreams[2]

        
  
        if (res.data.data.datastreams[0]>20)
         {
          wx.showModal({

            title: '提示～',

            content: '温度异常。',

            success: function (res) {

              if (res.confirm) {

                console.log('用户点击确定')

              } else if (res.cancel) {

                console.log('用户点击取消')

              }

            }

          })
         }


        if (res.data.data.datastreams[1] > 400) {
          wx.showModal({

            title: '提示～',

            content: '光照异常。',

            success: function (res) {

              if (res.confirm) {

                console.log('用户点击确定')

              } else if (res.cancel) {

                console.log('用户点击取消')

              }

            }

          })
        }

      
        if (res.data.data.datastreams[2] > 20) {
          wx.showModal({

            title: '提示～',

            content: '湿度异常。',

            success: function (res) {

              if (res.confirm) {

                console.log('用户点击确定')

              } else if (res.cancel) {

                console.log('用户点击取消')

              }

            }

          })
        }




      },


      







  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
  }
})