
# theaterRPG 帮助说明
用于波段（丢骰子）回合制的RPG 语C（类似TRPG跑团），初步功能是实现自动算PK，之后逐步完善成网站模式。


## 虚拟环境+依赖包
也可见requirements.txt文件

主要环境如下：

| Packages              | version | Description               |
| --------------------- | ------- | ------------------------- |
| python                | 3.5     | -                         |
| Django                | 2.0.6   | -                         |
| django-simple-captcha | 0.5.9   | 图片验证码                |
| xlrd                  | 1.1.0   | 支持对excel进行操作的模块 |

## 默认django管理后台
* 接口:`/admin`
* 帐号:admin
* 密码:ABCabc123

## 测试帐号
|帐号名称|角色|权限|密码|
|-|-|-|-|
|王小明|  ||12345678|
|王大锤|  ||12345678|
|铁乐猫|  |所有|12345678|
|高天赐|  ||12345678|
|李小狼|  ||123|
|木之本樱|  ||123|
|张小凡| 游客 |只有公共部份的观看只读权限|123|


## URL

| URL        | 视图                   | 模板          | 说明 |
| ---------- | ---------------------- | ------------- | ---- |
| /index/    | login.views.index()    | index.html    | 主页 |
| /login/    | login.views.login()    | login.html    | 登录 |
| /register/ | login.views.register() | register.html | 注册 |
| /logout/   | login.views.logout()   | 无需          | 注销 |
|            |                        |               |      |
|            |                        |               | -    |
|            |                        |               |      |
|            |                        | -             |      |
|            |                        | -             | -    |
|            |                        | -             | -    |

## ToDoList
* [x] 用户表和角色相关表建立
* [ ] 用户登录认证app建立参



## 测试环境启动

安装依赖：

```
pip install -r requirements.txt
```

启动：

```
python3 manage.py runserver 0.0.0.0:8000
```

访问本机8000端口可看到网站效果。