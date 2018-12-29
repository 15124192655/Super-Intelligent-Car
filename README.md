# Super-Intelligent-Car
银色飞猪（树莓WIFI智能管家）代码


# Dev 分支
Dev分支下的代码大概发生了以下变化

* 小车啊小车……
* 尝试封装WebSocket作为后端，以满足未来可能需要的双向通信。
* 彻底取消服务器端提供的控制面板，改为app页面或者是local的网页。
* 加入asyncio异步框架。
* 添加了一个小工具，可以实现登录第二层网关。因为第一层网关很难复现，还没写好。

# WebSocket的通信方法
WebSocket间的通信使用很简易的(utf-8编码)Json。格式大概是这样
```
{
    'handle':'<unique name>',
	/*other data*/
}
```
后端与前端可以通过bind到不同handle上的操作来处理相应数据。

## 后端
WsSocket（非常简陋的）封装了一个WebSocket服务，其中的hand方法可以把处理某个方法挂载到特定的handle上，并将已经转换好的Json结构体传递给方法。