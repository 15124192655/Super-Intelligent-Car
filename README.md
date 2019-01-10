# Super-Intelligent-Car
银色飞猪（树莓WIFI智能管家）代码

# Dev 分支
Dev分支下的代码大概发生了以下变化

* 小车啊小车……
* 尝试封装WebSocket作为后端，以满足未来可能需要的双向通信。
* 加入asyncio异步框架。
* 添加了一个小工具，可以实现登录第二层网关。因为第一层网关很难复现，还没写好。这个工具理想下应该可以开机自启连接指定WiFi并完成所有可能存在的登录工作，能够通过蓝牙和手机通信，来在无法联网的情况下快速排除故障。

2019年1月10日

# 部署方法
并没有准备任何的依赖解决方案，感觉手工够了。
1. 使用 pip 安装 websockets 与 asyncio 包来保证wssocket的运行。
2. end。

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