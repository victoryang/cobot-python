<div><img src="logo.png" width="64" height="32"></div>

<div style="height:150px"></div>


<center> <h1><b>协作机器人SDK<b></h1> </center>

<div style="height:300px"></div>

<center> <h2>v1.0.0</h2> </center>
<center> <h2>Elite</h2> </center>

<div style="height:150px"></div>

<div class="page"/>


# 目录

## - 1 上下文服务(ContextService)

- 1.1 [创建上下文](#1.1)

&emsp;&emsp;&emsp;[Context()](#1.1)

- 1.2 [销毁上下文](#1.2)

&emsp;&emsp;&emsp;[del](#1.2)

- 1.3 [登陆](#1.3)

&emsp;&emsp;&emsp;[login()](#1.3)

- 1.4 [退出](#1.4)

&emsp;&emsp;&emsp;[logout()](#1.4)

## - 2 伺服服务(ServoService)

- 2.1 [伺服系统上下电](#2.1)

&emsp;&emsp;&emsp;[power()](#2.1)

- 2.2 [启动伺服](#2.2)

&emsp;&emsp;&emsp;[startup()](#2.2)

- 2.3 [关闭伺服](#2.3)

&emsp;&emsp;&emsp;[shutdown()](#2.3)

## - 3 参数服务(ParamService)

- 3.1 [获取机器人状态](#3.1)

&emsp;&emsp;&emsp;[get_robot_state()](#3.1)

- 3.2 [获取机器人模式](#3.2)

&emsp;&emsp;&emsp;[get_robot_mode()](#3.2)

- 3.3 [设置机器人模式](#3.3)

&emsp;&emsp;&emsp;[set_robot_mode()](#3.3)

- 3.4 [获取机器人当前位置信息](#3.4)

&emsp;&emsp;&emsp;[get_robot_pos()](#3.4)

- 3.5 [获取机器人当前位姿信息](#3.5)

&emsp;&emsp;&emsp;[get_robot_pose()](#3.5)

- 3.6 [获取机械臂伺服状态](#3.6)

&emsp;&emsp;&emsp;[get_servo_status()](#3.6)

- 3.7 [获取机械臂上下电状态](#3.7)

&emsp;&emsp;&emsp;[get_motor_status()](#3.7)

- 3.8 [获取机器人运行速度](#3.8)

&emsp;&emsp;&emsp;[get_play_speed()](#3.8)

- 3.9 [设置机器人运行速度](#3.9)

&emsp;&emsp;&emsp;[set_play_speed()](#3.9)

## - 4 运动服务(MovementService)

- 4.1 [关节运动](#5.1)

&emsp;&emsp;&emsp;[joint_move()](#4.1)

- 4.2 [直线运动](#4.2)

&emsp;&emsp;&emsp;[line_move()](#4.2)

- 4.3 [圆弧运动](#4.3)

&emsp;&emsp;&emsp;[arc_move()](#4.3)

- 4.4 [旋转运动](#4.4)

&emsp;&emsp;&emsp;[rotate_move()](#4.4)

- 4.5 [设置路点运动时最大关节速度](#4.5)

&emsp;&emsp;&emsp;[set_waypoint_max_joint_speed()](#4.5)

- 4.6 [设置路点运动时最大直线速度](#4.6)

&emsp;&emsp;&emsp;[set_waypoint_max_line_speed()](#4.6)

- 4.7 [设置路点运动时最大旋转速度](#4.7)

&emsp;&emsp;&emsp;[set_waypoint_max_rotate_speed()](#4.7)

- 4.8 [添加路点信息](#4.8)

&emsp;&emsp;&emsp;[add_waypoint()](#4.8)

- 4.9 [清除路点信息](#4.9)

&emsp;&emsp;&emsp;[clear_waypoint()](#4.9)

- 4.10 [轨迹运动](#4.10)

&emsp;&emsp;&emsp;[track_move()](#4.10)

- 4.11 [停止机器人运行](#5.11)

&emsp;&emsp;&emsp;[stop()](#4.11)

## - 5 运动学服务(KinematicsService)

- 5.1 [逆解函数](#5.1)

&emsp;&emsp;&emsp;[inverse_kinematic()](#5.1)

- 5.2 [正解函数](#5.2)

&emsp;&emsp;&emsp;[positive_kinematic()](#5.2)

- 5.3 [基坐标到用户坐标位姿转化](#5.3)

&emsp;&emsp;&emsp;[base2user()](#5.3)

- 5.4 [用户坐标到基坐标位姿转化](#5.4)

&emsp;&emsp;&emsp;[user2base()](#5.4)

## - 6 IO服务(IOService)

- 6.1 [获取输入IO状态](#6.1)

&emsp;&emsp;&emsp;[get_input()](#6.1)

- 6.2 [获取输出IO状态](#6.2)

&emsp;&emsp;&emsp;[get_ouput()](#6.2)

- 6.3 [设置输出IO状态](#6.3)

&emsp;&emsp;&emsp;[set_output()](#6.3)

- 6.4 [获取虚拟输入IO状态](#6.4)

&emsp;&emsp;&emsp;[get_virtual_input()](#6.4)

- 6.5 [获取虚拟输出IO状态](#6.5)

&emsp;&emsp;&emsp;[get_virtual_output()](#6.5)

- 6.6 [设置虚拟输出IO状态](#6.6)

&emsp;&emsp;&emsp;[set_virtual_output()](#6.6)

- 6.7 [获取IO总线上的IO变量值](#6.7)

&emsp;&emsp;&emsp;[get_var()](#6.7)

- 6.8 [设置IO总线上的IO变量值](#6.8)

&emsp;&emsp;&emsp;[set_var()](#6.8)

## - 7 报警服务(AlarmService)

- 7.1 [复位操作](#7.1)

&emsp;&emsp;&emsp;[reset()](#7.1)

- 7.2 [获取最新的报警信息](#7.2)

&emsp;&emsp;&emsp;[get_latest_alarms()](#7.2)



<br/>
<br/>
<br/>
<br/>

<div class="page"/>

# Examples

&emsp;<b><i>Example 1</i></b>

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cobot_python import context

ctx = context.Context("192.168.1.253", 9000)

for i in xrange(10):
    ret = ctx.login("xxx", "xxx")
    if ret == False:
        print 'login fail at: ' + str(i)
    else:
        print "check health: " + str(ctx.check_health())

    ctx.logout()

del ctx
```

<br/>
<br/>
<br/>
<br/>


<div class="page"/>

&emsp;<b><i>Example 2</i></b>

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cobot_python import alarm
from cobot_python import context
from cobot_python import io
from cobot_python import kinematic
from cobot_python import movement
from cobot_python import param
from cobot_python import servo

ctx = context.Context("192.168.1.253", 9000)

ret = ctx.login("xxx", "xxx")
if ret == False:
    print 'login fail'
    exit(-1)

print "check health: " + str(ctx.check_health())

print "robot state: " + str(param.get_robot_state(ctx))

print "power on: " + str(servo.power(ctx))

print "get input status: " + str(io.get_input(ctx, 0))

print "get latest alarm: " + str(alarm.get_latest_alarms(ctx))

print "inverse kinematic: " + str(kinematic.inverse_kinematic(ctx, [0,90,0,90,0,90]))

ctx.logout()

del ctx
```

<br/>
<br/>
<br/>
<br/>


<div class="page"/>

# 服务接口

## 1 上下文服务(ContextService)

- <h3 id="1.1">1.1 创建上下文</h3>

|||
|--|--|
|函数名称|Context()|
|功能描述|创建上下文|
|参数说明|addr 目标机械臂控制系统的IP地址 <br> port 服务端口号，目前默认9000|
|返回值|Context对象|
|||

```python
        from cobot_python import context

        context.Context(addr, port=9000)
```

- <h3 id="1.2">1.2 销毁上下文</h3>

```python
        from cobot_python import context

        ctx = context.Context("192.168.1.253", 9000)
        del ctx
```

- <h3 id="1.3">1.3 登陆</h3>

|||
|--|--|
|函数名称|login()|
|功能描述|登陆控制器系统|
|参数说明|username 登陆用户名 <br> password 用户密码|
|返回值|成功: True <br> 失败: False|
|||

```python
        from cobot_python import context

        ctx.login(username, password)
```

- <h3 id="1.4">1.4 退出</h3>

|||
|--|--|
|函数名称|logout()|
|功能描述|退出登陆|
|参数说明||
|返回值||
|||

```python
        from cobot_python import context

        ctx.logout()
```

<br/>
<br/>
<div class="page"/>

## 2 伺服服务(ServoService)

- <h3 id="2.1">2.1 伺服系统上下电</h3>

|||
|--|--|
|函数名称|power()|
|功能描述|伺服系统上下电|
|参数说明|ctx 登陆上下文|
|返回值|成功: True <br> 失败: False|
|||

```python
        from cobot_python import servo

        servo.power(ctx)
```

- <h3 id="2.2">2.2 启动伺服</h3>

|||
|--|--|
|函数名称|startup()|
|功能描述|启动伺服|
|参数说明|ctx 登陆上下文|
|返回值|成功: True <br> 失败: False|
|||

```python
        from cobot_python import servo

        servo.startup(ctx)
```

- <h3 id="2.3">2.3 关闭伺服</h3>

|||
|--|--|
|函数名称|shutdown()|
|功能描述|关闭伺服|
|参数说明|ctx 登陆上下文|
|返回值|成功: True <br> 失败: False|
|||

```python
        from cobot_python import servo

        servo.shutdown(ctx)
```

<br/>
<br/>
<div class="page"/>

## 3 参数服务(ParamService)

- <h3 id="3.1">3.1 获取机器人状态</h3>

|||
|--|--|
|函数名称|get_robot_state()|
|功能描述|获取机器人状态|
|参数说明|ctx 登陆上下文|
|返回值|成功: 机器人状态 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_robot_state(ctx)
```

- <h3 id="3.2">3.2 获取机器人模式</h3>

|||
|--|--|
|函数名称|get_robot_mode()|
|功能描述|获取机器人模式|
|参数说明|ctx 登陆上下文|
|返回值|成功: 机器人模式 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_robot_mode(ctx)
```

- <h3 id="3.3">3.3 设置机器人模式</h3>

|||
|--|--|
|函数名称|set_robot_mode()|
|功能描述|设置机器人模式|
|参数说明|ctx 登陆上下文 <br> mode 机器人模式, ["teach", "play", "remote"]|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import param

        param.set_robot_mode(ctx, mode)
```

- <h3 id="3.4">3.4 获取机器人当前位置信息</h3>

|||
|--|--|
|函数名称|get_robot_pos()|
|功能描述|获取机器人当前位置信息|
|参数说明|ctx 登陆上下文|
|返回值|成功: 机器人位置 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_robot_pos(ctx)
```

- <h3 id="3.5">3.5 获取机器人当前位姿信息</h3>

|||
|--|--|
|函数名称|get_robot_pose()|
|功能描述|获取机器人当前位姿信息|
|参数说明|ctx 登陆上下文|
|返回值|成功: 机器人位姿 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_robot_pose(ctx)
```

- <h3 id="3.6">3.6 获取机械臂伺服状态</h3>

|||
|--|--|
|函数名称|get_servo_status()|
|功能描述|获取机械臂伺服状态|
|参数说明|ctx 登陆上下文|
|返回值|成功: 伺服状态 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_servo_status(ctx)
```

- <h3 id="3.7">3.7 获取机械臂上下电状态</h3>

|||
|--|--|
|函数名称|get_motor_status()|
|功能描述|获取机械臂上下电状态|
|参数说明|ctx 登陆上下文|
|返回值|成功: 上下电状态 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_motor_status(ctx)
```

- <h3 id="3.8">3.8 获取机器人运行速度</h3>

|||
|--|--|
|函数名称|get_play_speed()|
|功能描述|获取机器人运行速度|
|参数说明|ctx 登陆上下文|
|返回值|成功: 机器人运行速度 <br> 失败: None
|||

```python
        from cobot_python import param

        param.get_play_speed(ctx)
```

- <h3 id="3.9">3.9 设置机器人运行速度</h3>

|||
|--|--|
|函数名称|set_play_speed()|
|功能描述|设置机器人运行速度|
|参数说明|ctx 登陆上下文|
|返回值| 成功: True <br> 失败: False
|||

```python
        from cobot_python import param

        param.set_play_speed(ctx)
```

<br/>
<br/>
<div class="page"/>

## 4 运动服务(MovementService)

- <h3 id="4.1">4.1 关节运动</h3>

|||
|--|--|
|函数名称|joint_move()|
|功能描述|关节运动|
|参数说明|ctx 登陆上下文 <br> target_pos 目标关节点, [0,90,0,0,0,0,0,0] <br> speed 运行速度百分比，范围:[1~100]，单位：百分比|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.joint_move(ctx, target_pos, speed)
```

- <h3 id="4.2">4.2 直线运动</h3>

|||
|--|--|
|函数名称|line_move()|
|功能描述|直线运动|
|参数说明|ctx 登陆上下文 <br> target_pos 目标点, [0,90,0,0,0,0,0,0] <br> speed 运行速度，范围[1-3000]，单位：毫米/秒|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.line_move(ctx, target_pos, speed)
```

- <h3 id="4.3">4.3 圆弧运动</h3>

|||
|--|--|
|函数名称|arc_move()|
|功能描述|圆弧运动|
|参数说明|ctx 登陆上下文 <br> mid_pos 第二目标点（相对与当前机器人位置） <br> target_pos 目标点, [0,90,0,0,0,0,0,0] <br> speed 运行速度，范围[1-3000]，单位：毫米/秒|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.arc_move(ctx, mid_pos, target_pos, speed)
```

- <h3 id="4.4">4.4 旋转运动</h3>

|||
|--|--|
|函数名称|rotate_move()|
|功能描述|旋转运动|
|参数说明|ctx 登陆上下文 <br> target_pos 目标点, [0,90,0,0,0,0,0,0] <br> speed 运行速度，单位: 度/秒|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.rotate_move(ctx, target_pos, speed)
```

- <h3 id="4.5">4.5 设置路点运动时最大关节速度</h3>

|||
|--|--|
|函数名称|set_waypoint_max_joint_speed()|
|功能描述|设置路点运动时最大关节速度|
|参数说明|ctx 登陆上下文 <br> speed 关节速度，范围:[%1~100%], 单位：百分比|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.set_waypoint_max_joint_speed(ctx, speed)
```

- <h3 id="4.6">4.6 设置路点运动时最大直线速度</h3>

|||
|--|--|
|函数名称|set_waypoint_max_line_speed()|
|功能描述|设置路点运动时最大直线速度|
|参数说明|ctx 登陆上下文 <br> speed 直线速度，范围:[1~3000], 单位：毫米/秒|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.set_waypoint_max_line_speed(ctx, speed)
```

- <h3 id="4.7">4.7 设置路点运动时最大旋转速度</h3>

|||
|--|--|
|函数名称|set_waypoint_max_rotate_speed()|
|功能描述|设置路点运动时最大旋转速度|
|参数说明|ctx 登陆上下文 <br> speed 关节速度， 单位：度/秒|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.set_waypoint_max_rotate_speed(ctx, speed)
```

- <h3 id="4.8">4.8 添加路点信息</h3>

|||
|--|--|
|函数名称|add_waypoint()|
|功能描述|添加路点信息|
|参数说明|ctx 登陆上下文 <br> target_pos 目标位置（关节角）|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.add_waypoint(ctx, target_pos)
```

- <h3 id="4.9">4.9 清除路点信息</h3>

|||
|--|--|
|函数名称|clear_waypoint()|
|功能描述|清除路点信息|
|参数说明|ctx 登陆上下文|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.clear_waypoint(ctx)
```

- <h3 id="4.10">4.10 轨迹运动</h3>

|||
|--|--|
|函数名称|track_move()|
|功能描述|轨迹运动|
|参数说明|ctx 登陆上下文 <br> target_pos 目标点，与addWaypoint最后一次调用的目标点相同 <br> move_type 运动类型（关节、直线、旋转、圆弧） <br> pl 平滑度等级，范围[0~7]|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.track_move(ctx, target_pos, move_type, pl)
```

- <h3 id="4.11">4.11 停止机器人运行</h3>

|||
|--|--|
|函数名称|stop()|
|功能描述|停止机器人运行|
|参数说明|ctx 登陆上下文|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import movement

        movement.stop(ctx)
```

<br/>
<br/>
<div class="page"/>

## 5 运动学服务(KinematicsService)

- <h3 id="5.1">5.1 逆解函数</h3>

|||
|--|--|
|函数名称|inverse_kinematic()|
|功能描述|逆解函数|
|参数说明|ctx 登陆上下文 <br> pos 位姿信息, [0,90,0,90,0,90]|
|返回值|成功: 关节角信息, [0,90,0,90,0,90,0,90] <br> 失败: None
|||

```python
        from cobot_python import kinematic

        kinematic.inverse_kinematic(ctx, pos)
```

- <h3 id="5.2">5.2 正解函数</h3>

|||
|--|--|
|函数名称|positive_kinematic()|
|功能描述|正解函数|
|参数说明|ctx 登陆上下文 <br> pos 关节角信息, [0,90,0,90,0,90,0,90]|
|返回值|成功: 位姿信息, [0,90,0,90,0,90] <br> 失败: None
|||

```python
        from cobot_python import kinematic

        kinematic.positive_kinematic(ctx, pos)
```

- <h3 id="5.3">5.3 基坐标到用户坐标位姿转化</h3>

|||
|--|--|
|函数名称|base2user()|
|功能描述|基坐标到用户坐标位姿转化|
|参数说明|ctx 登陆上下文 <br> pose 基坐标系下的位姿信息, [0,90,0,90,0,90] <br> user_no (optinal) 用户坐标号，指向用户坐标系|
|返回值|成功: 用户坐标系下的位姿信息, [0,90,0,90,0,90] <br> 失败: None
|||

```python
        from cobot_python import kinematic

        kinematic.base2user(ctx, pose, user_no=-1)
```

- <h3 id="5.4">5.4 用户坐标到基坐标位姿转化</h3>

|||
|--|--|
|函数名称|user2base()|
|功能描述|用户坐标到基坐标位姿转化|
|参数说明|ctx 登陆上下文 <br> pose 用户坐标系下的位姿信息, [0,90,0,90,0,90] <br> user_no (optinal) 用户坐标号，指向用户坐标系|
|返回值|成功: 基坐标系下的位姿信息, [0,90,0,90,0,90] <br> 失败: None
|||

```python
        from cobot_python import kinematic

        kinematic.user2base(ctx, pose, user_no=-1)
```

<br/>
<br/>
<div class="page"/>

## 6 IO服务(IOService)

- <h3 id="6.1">6.1 获取输入IO状态</h3>

|||
|--|--|
|函数名称|get_input()|
|功能描述|获取输入IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输入IO地址|
|返回值|成功: IO状态 <br> 失败: None
|||

```python
        from cobot_python import io

        io.get_input(ctx, addr)
```

- <h3 id="6.2">6.2 获取输出IO状态</h3>

|||
|--|--|
|函数名称|get_ouput()|
|功能描述|获取输出IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输出IO地址|
|返回值|成功: IO状态 <br> 失败: None
|||

```python
        from cobot_python import io

        io.get_ouput(ctx, addr)
```

- <h3 id="6.3">6.3 设置输出IO状态</h3>

|||
|--|--|
|函数名称|set_output()|
|功能描述|设置输出IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输出IO地址 <br> status IO状态|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import io

        io.set_output(ctx, addr, status)
```

- <h3 id="6.4">6.4 获取虚拟输入IO状态</h3>

|||
|--|--|
|函数名称|get_virtual_input()|
|功能描述|获取虚拟输入IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输入IO地址|
|返回值|成功: IO状态 <br> 失败: None
|||

```python
        from cobot_python import io

        io.get_virtual_input(ctx, addr)
```

- <h3 id="6.5">6.5 获取虚拟输出IO状态</h3>

|||
|--|--|
|函数名称|get_virtual_output()|
|功能描述|获取虚拟输出IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输入IO地址|
|返回值|成功: IO状态 <br> 失败: None
|||

```python
        from cobot_python import io

        io.get_virtual_output(ctx, addr)
```

- <h3 id="6.6">6.6 设置虚拟输出IO状态</h3>

|||
|--|--|
|函数名称|set_virtual_output()|
|功能描述|设置输出IO状态|
|参数说明|ctx 登陆上下文 <br> addr 输出IO地址 <br> status IO状态|
|返回值|成功: True <br> 失败: False
|||

```python
        from cobot_python import io

        io.set_virtual_output(ctx, addr, status)
```

- <h3 id="6.7">6.7 获取IO总线上的IO变量值</h3>

|||
|--|--|
|函数名称|get_var()|
|功能描述|获取IO总线上的IO变量值|
|参数说明|ctx 登陆上下文 <br> var_name 变量名|
|返回值|成功: 变量值 <br> 失败: None
|||

```python
        from cobot_python import io

        io.get_var(ctx, var_name)
```

- <h3 id="6.8">6.8 设置IO总线上的IO变量值</h3>

|||
|--|--|
|函数名称|set_var()|
|功能描述|设置IO总线上的IO变量值|
|参数说明|ctx 登陆上下文 <br> var_name 变量名 <br> value 变量值|
|返回值| 成功: True <br> 失败: False
|||

```python
        from cobot_python import io

        io.set_var(ctx, var_name, value)
```

<br/>
<br/>
<div class="page"/>

## 7 报警服务(AlarmService)

- <h3 id="7.1">7.1 复位操作</h3>

|||
|--|--|
|函数名称|reset()|
|功能描述|复位操作|
|参数说明|ctx 登陆上下文|
|返回值| 成功: True <br> 失败: False
|||

```python
        from cobot_python import alarm

        alarm.reset()
```

- <h3 id="7.2">7.2 获取最新的报警信息</h3>

|||
|--|--|
|函数名称|get_latest_alarms()|
|功能描述|复位操作|
|参数说明|ctx 登陆上下文|
|返回值| 成功: 报警信息列表 [{"time": 1551255491,"errLevel": 0,"errNo": 10001,"subErrNo": 0, "message": "get arc weld data error"}] <br> 失败: None
|||

```python
        from cobot_python import alarm

        alarm.get_latest_alarms()
```