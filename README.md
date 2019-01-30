# Super-Intelligent-Car
银色飞猪（树莓WIFI智能管家）代码

# Dev 分支
Dev分支下的代码大概发生了以下变化

* 小车啊小车……
* 尝试封装WebSocket作为后端，以满足未来可能需要的双向通信。
* 加入asyncio异步框架。
* 添加了一个小工具，可以实现登录第二层网关。因为第一层网关很难复现，还没写好。这个工具理想下应该可以开机自启连接指定WiFi并完成所有可能存在的登录工作，能够通过蓝牙和手机通信，来在无法联网的情况下快速排除故障。
* 使用crontab来执行周期任务，如上传数据。
* 添加了fake的机械臂控制部分，但是被实际情况卡住了。

2019年1月17日

# 部署方法
并没有准备任何的依赖解决方案，感觉手工够了。
1. 使用 pip 安装 websockets 与 asyncio 包来保证wssocket的运行。
2. end。

# 通信细节
## 网页端WebSocket通信方法
网页端采用了JQuery来负责处理页面的点击事件。在相应的事件中，可以直接
```
data={'handle':'move','direction':'S',};
ws.send(JSON.stringify(data));
```
这样构造一个通信包发送给小车的后端。

## WebSocket的通信格式
WebSocket间的通信使用很简易的(utf-8编码)Json。格式大概是这样
```
{
    'handle':'<unique name>',
	/*other data*/
}
```
例如，控制车前进后退的为
```
{
    'handle':'move',
    'direction':'?',
}
```
后端与前端可以通过bind到不同handle上的操作来处理相应数据。

## 后端
WsSocket（非常简陋的）封装了一个WebSocket服务，其中的hand方法可以把处理某个方法挂载到特定的handle上，并将已经转换好的Json结构体传递给方法。

## 后端通信方法
后端大概有2种通信形式。
1. 被动通信：上端发送命令后被动返回一段信息。请在hind的方法后使用`await`语法调用ws.send()，例如
```
await ws.send(json.dumps({'handle':'test','msg':data['msg']}))
```
2. 主动通信：……因没有需求，不知道。

## 机械臂的（暂定）控制通信格式
因为还不知道机械臂到底是什么情况，暂定为下。
格式为`<id>:<angle>,<id>:<angle>...`的一段运动序列。

`id`为电机的唯一代号，`angle`为电机的**绝对**角度。后端接受后将顺序执行动作。
