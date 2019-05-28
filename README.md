## 项目简介
####  写本项目之目的在于想做一个小型的在线教育平台，将自己学到的东西以视频录制的方式上传到这个平台上。 以便可以在自己写的这个平台上传个师，授个道，解个惑，与此同时，提高自己的一些授课能力以及相关知识。目前想的是针对一些从来没有编程基础的同学出一些特别基础的编程课程，目前是想针对golang出一个相应的课程。
---
## 所需要的安装包
#### 注意：因python使用的是3.7的版本，其对应的mysql的驱动是PyMySQL。
1. backports.csv          1.0.7
2. captcha                0.3
3. certifi                2019.3.9
4. chardet                3.0.4
5. defusedxml             0.5.0
6. diff-match-patch       20181111
7. Django                 2.1.7
8. django-crispy-forms    1.7.2
9. django-formtools       2.1
10. django-import-export   1.2.0
11. django-pure-pagination 0.3.0
12. django-ranged-response 0.2.0
13. django-reversion       3.0.3
14. django-simple-captcha  0.5.11
15. et-xmlfile             1.0.1
16. future                 0.17.1
17. httplib2               0.9.2
18. idna                   2.8
19. jdcal                  1.4
20. odfpy                  1.4.0
21. openpyxl               2.6.2
22. Pillow                 5.4.1
23. pip                    19.0.3
24. PyMySQL                0.9.3
25. pytz                   2018.9
26. PyYAML                 5.1
27. requests               2.21.0
28. setuptools             40.8.0
29. six                    1.12.0
30. tablib                 0.13.0
31. urllib3                1.24.2
32. wheel                  0.33.1
33. xadmin                 2.0.1
34. xlrd                   1.2.0
35. xlwt                   1.3.0
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
5.创建好相应的课程，章节，视频后，即可看看前台展示的效果，在浏览器里输入下面的地址即可看到相应的效果了。
```
http://127.0.0.1:8000/course/info/1/
```





