***maybe Discarded***

# Super-Intelligent-Car
银色飞猪（树莓WIFI智能管家）代码

# Dev 分支
3/20/2019 Dev分支下的代码大概发生了以下变化

* 小车啊小车……
* 尝试封装WebSocket作为后端，以满足可能需要的双向通信。(非常抱歉的口误,这里使用了python的内置模块,并非*完全*自行编写)
* 添加了一个小工具，可以实现登录第二层网关。因为第一层网关很难复现，还没写好。
* 使用crontab来执行周期任务，如上传数据。
* 添加了用于调试的机械臂控制部分。
* 添加了摄像头云台控制部分.

2019年2月4日 新年快乐

# 部署方法
并没有准备任何的依赖解决方案，感觉手工够了。
1. 使用 pip 安装 websockets 与 asyncio 包来保证wssocket的运行。
2. 确保crontab已安装，修改`humtem.py`中的APIKEY与上传数据的格式，并执行`crontab crontabtask`来部署环境湿度和温度的上传。
3. 配置`server.py`中服务器的端口号。
3. 安装screen（一个能够保证服务在后台运行的小程序），运行`carStart.sh`来启动小车的其他服务。
4. end。

## 关于分支
一般情况下，master分支下的代码为能够稳定运行的代码。
dev为在master代码基础上做出修改/改进的代码，在确保没有问题的情况下，再并入master。


# 通信细节
目前
* “小车->云<->手机”：小车以http形式上传数据到云，手机以http从云获取消息。
* “小车<->手机”：以websocket互通消息。

## 手机端WebSocket通信方法
网页端采用了JQuery来负责处理页面的点击事件。在相应的事件中，可以直接
```
data={'handle':'move','direction':'S',};
ws.send(JSON.stringify(data));
```
这样构造一个包发送给小车的后端。

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
后端与前端可以通过bind上不同handler来处理相应数据。

### JSON
JSON是一种简洁的数据交换语言，其大概表示为`键:值`对。键和值可以为多种数据格式，在这这里目前只涉及到字符串。

基本结构与c系语言的大括号类似，可嵌套。例子在上面有。

## 后端
WsSocket（非常简陋的）封装了一个WebSocket服务，其中的hand方法可以把处理某个方法挂载到特定的handle上，并将已经转换好的Json结构体传递给方法。

## 后端通信方法
后端大概有2种通信形式。
### 被动通信：
上端发送命令后被动返回一段信息。请在hind的方法后使用`await`语法调用ws.send()，例如
```
await ws.send(json.dumps({'handle':'test','msg':data['msg']}))
```
具体可以看代码中`heartbeat`部分的实现。

### 主动通信：
……因没有需求，不知道。

## 机械臂的（暂定）控制通信格式
因为还不知道机械臂到底是什么情况，暂定为下。
格式为`<id>:<angle>,<id>:<angle>...`的一段运动序列。

`id`为电机的唯一代号，`angle`为电机的**绝对**角度。后端接受后将顺序执行动作。**注意目前小车的动作执行为阻塞式**。

## 摄像头云台控制通信格式
```javascript
{
    'handle':'cammove',
    'axis':'<axis>',
    'angle':<angle>
}
```
* axis:云台的两个轴,分别为p1,p2
* angle:云台旋转绝对角
* * p1: 2-15
* * p2: 1-9

每条指令的运行延时为1秒(可改).

# crontab的配置

## 准备
* 一个只运行单次，并上传信息到云平台的脚本(humtem.py)
* crontab

## 步骤
### 准备脚本
将脚本放置在一个合适的位置，并记录它的路径，如"/home/kanari/upload.py"

### 创建一个任务描述文件
创建一个文件，如叫"kanaricron"。并写入`*/5 * * * * * python3 /home/kanari/upload.py`。

### 提交任务
在kanaricron所在目录下执行指令`crontab kanaricron`。理想状况下，crontab将每隔5分钟启动一次上传脚本。

## 任务描述文件的格式
如例子，任务描述文件的格式为`* * * * * * <要执行的命令>`。6个星号分别为分、时、天、月、周、年。

对于每个星号，其格式为
* <星号> ，表示每个周期都运行一次
* <数字> ，表示在此周期运行一次
* <*/数字> ，表示每隔几个周期运行一次
* <数字,数字,...> ，表示在指定的多个周期运行
* 其他请参照crontab的官方文档