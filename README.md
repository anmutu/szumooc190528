## szumooc190528项目简介
####  写本项目之目的在于想做一个小型的在线教育平台，将自己学到的东西以视频录制的方式上传到这个平台上。 以便可以在自己写的这个平台上传个师，授个道，解个惑，与此同时，提高自己的一些授课能力以及相关知识。目前想的是针对一些从来没有编程基础的同学出一些特别基础的编程课程，目前是想针对golang出一个相应的课程。
---
## 所需要的安装包
#### 注意：因python使用的是3.7的版本，其对应的mysql的驱动是PyMySQL。
详情可见szumooc.txt。

---
## 如何run起来？
1. 在本机的mysql里创建一个叫mooc的数据库，用户名和密码都是graduation。当然这个用户名或者密码都可以改成你自己设置的，如果改成你自己设置的则需要到settings.py里找到相应的位置改成你所设置的就可以了。
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mooc',
        'USER': 'graduation',
        'PASSWORD': 'graduation',
        'HOST': '127.0.0.1',
    }
}
```
2. 到命令行里执行createsuperuser，按照其步骤创建超级管理员。
```
createsuperuser
```
3. 将所有app里创建的表mapping到数据库里。执行makemigration和migrate命令。
```
makemigration
migrate
```
4. 在IDE里把当前的项目run起来，并在浏览器里输入下边的地址。用第二步创建好的超级管理员登录，输入用户名和密码即可进入后台的管理界面。在这里就可以对课程，章节，视频，或者是用户进行CRUD的操作了。
```
http://127.0.0.1:8000/xadmin/
```
5. 创建好相应的课程，章节，视频后，即可看看前台展示的效果，在浏览器里输入下面的地址即可看到相应的效果了。
```
http://127.0.0.1:8000/course/info/1/
```
---
## 效果展示
#### 管理后台效果图
![](https://github.com/anmutu/szumooc190528/blob/master/static/img_projectdemo/admin.jpg)
#### mooc平台效果图
![](https://github.com/anmutu/szumooc190528/blob/master/static/img_projectdemo/mooc.jpg)






