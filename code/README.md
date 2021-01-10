# README

- 运行说明：由于连接的是本地数据库，需要修改`main.py`文件中`Library`类传入的`pwd`参数为本机的MySQL数据库密码才能连接上本地数据库。
- 测试运行时，由于初始化的数据库内容为空，无法进行测试。在附带的`t.sql`文件中保存有初始化的数据，先使用`python main.py`运行程序一次，再在终端运行`mysql -u root -p*** bookmanagement < t.sql`导入数据即可初始化预先录入的事例数据，其中***表示本机MySQL数据库密码。

