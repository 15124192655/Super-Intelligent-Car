// start.js



Page({



  /**

   * 页面的初始数据

   */

  data: {

    opacity: 0.4,

    disabled: true,

    threshold: 0,

    // rule: 'up',

    // items: [

    //   { name: 'up', value: '高于门限报警', checked: 'ture' },

    //   { name: 'down', value: '低于门限报警' },

    // ]

  },



  // radioChange: function (e) {

  //   //保存报警规则到当前页面的数据

  //   if (e.detail.value != "") {

  //     this.setData({

  //       rule: e.detail.value

  //     })

  //   }

  //   console.log(this.data.rule)

  // },



  onShow: function () {
    console.log("anything")
    const requestTask = wx.request({

      url: 'https://api.heclouds.com/devices/yourid/datapoints?datastream_id=Light,Temperature,Humidity&limit=1',

      header: {

        'content-type': 'application/json',

        'api-key': 'yours'

      },

      success: function (res) {

        console.log(res.data)

        //拿到数据后保存到全局数据

        var app = getApp()

        app.globalData.temperature = res.data.data.datastreams[0]

        app.globalData.light = res.data.data.datastreams[1]

        app.globalData.humidity = res.data.data.datastreams[2]

        
  
        if (parseInt(app.globalData.temperature.datapoints[0].value)  > 20) {
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

        if (parseInt(app.globalData.light.datapoints[0].value) > 400) {
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


        if (parseInt(app.globalData.humidity.datapoints[0].value > 20) ){
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
  }
  })
  },







  




  /**

   * 生命周期函数--监听页面加载

   */

 



  /**

   * 生命周期函数--监听页面初次渲染完成

   */

  onReady: function () {



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
