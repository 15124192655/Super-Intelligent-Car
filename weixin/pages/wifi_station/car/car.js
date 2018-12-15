
// pages/control/control.js

const app = getApp()



Page({


  
  /**

   * 页面的初始数据

   */

  data: {

    // Car control images

    "forwardBtn": "/res/forward.png",

    "leftBtn": "/res/left.png",

    "rightBtn": "/res/right.png",

    "backLeftBtn": "/res/back-left.png",

    "backRightBtn": "/res/back-right.png",

    "backBtn": "/res/backward.png",



    // Camera control images

    // "upBtn": "/res/forward.png",

    // "camLeftBtn": "/res/camLeft.png",

    // "camRightBtn": "/res/camRight.png",

    // "downBtn": "/res/backward.png",

    // "resetBtn": "/res/reset.png"

  },



  carMove: function (event) {

    wx.request({

      url: 'http://192.168.50.122:9090',
      data: event.currentTarget.dataset.direction,

      method: "POST",

      success: function (res) {
        console.log(res)
      },
      fail: function (res) {

      }

    })

  },



  carStop: function (event) {

    wx.request({

      url: 'http://192.168.50.122:9090',

      data: "S",

      method: "POST",

      success: function (res) {
        console.log(res)
      },

      fail: function (res) {



      }

    })

  },



 

   



  /**

   * 生命周期函数--监听页面加载

   */

  onLoad: function (options) {

    //this.data.cameraURL = app.globalData.cameraURL

    this.setData({

      cameraURL: app.globalData.cameraURL,

      postURL: app.globalData.postURL

    })

    console.log(this.data.cameraURL)

    console.log("post url in control page: " + app.globalData.postURL)

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

    //console.log(wx.getSystemInfoSync().windowWidth)

    //console.log(wx.getSystemInfoSync().windowHeight)

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
