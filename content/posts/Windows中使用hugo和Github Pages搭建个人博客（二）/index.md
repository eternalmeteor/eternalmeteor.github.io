+++
title = 'Windows中使用hugo和Github Pages搭建个人博客（二）'
date = 2024-04-15T20:48:20+08:00
draft = false

+++

## 1.建立GitHub远程仓库

1. 登录至自己的GitHub账号，建立GitHub Page仓库。

**注意：这里的GitHub page的命名格式必须为`username.github.io`,其中username为GitHub的用户名，即就是Repository name前面的Owner名。**

2. 勾选public，将仓库设置为公开仓库。
3. 勾选`Add a README file`，设置main分支为仓库的默认主分支。

![image-20240416152858695](./assets/image-20240416152858695.png#center)

## 2.将本地仓库和远程仓库相关联

1. 在菜单栏中搜索`git bash`并打开。

![image-20240417164216492](./assets/image-20240417164216492.png#center)

2. 进入至本地仓库目录下，例如我的本地仓库目录为：`d:/quickstart`

![image-20240416160706999](./assets/image-20240416160706999.png#center#center)

3. 在quickStart目录下运行`git init`命令，初始化本地仓库为git仓库

```shell
git init
```

4. 将本地仓库和远程仓库（自己创建的.github.io仓库）相关联。

```shell
git remote add origin url (url代表远程仓库的url)
```

![image-20240416161312921](./assets/image-20240416161312921.png#center)

5. 将本地仓库中的内容推送至远程仓库。

**注意1：本文档采用同一个远程仓库的两个分支进行hugo仓库的自动部署。设置远程仓库中的source分支为本地仓库的内容，main分支代表要发布的静态网页。**

**注意2：`git add .`之后在Windows平台会出现`warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory`，查阅资料之后发现是不同平台下空格表示方式不同，可以不用管。**

**注意3：`git push`时需要本地分支名，本地分支名会显示在git bash界面中当前目录的后面，注意看自己的分支名。**

![image-20240416163302671](./assets/image-20240416163302671.png#center)

```shell
git add . #将本地修改添加至暂存区
git commit -m '注释' #将本地修改从暂存区移动到本地分支
git push -u origin master:source #-u选项代表将所推送的远程分支设置本地分支的上游，后续可以无须指定，相当于缓存了一簇推送设置，master代表本地分支名，source代表远程分支名。 
```

![image-20240416163657579](./assets/image-20240416163657579.png#center)

## 3.使用Github Action实现自动部署

1. 点击Settings-->Developer Settings，进入到Developer Settings页面。

![image-20240416165350755](./assets/image-20240416165350755.png#center)

2. 点击Personal access tokens --> Token(classic) --> Generate new token --> Generate new token(classic)，进入New personal access token(classic) 页面。

![image-20240416165909820](./assets/image-20240416165909820.png#center)

3. 在Note中输入Token名（自己可以随便起，例如hugo-blog），勾选repo和workflow.

![image-20240416170305054](./assets/image-20240416170305054.png#center)

4. 点击页面底部的Generate token产生Token，**敲重点：记录以ghp开头的一串代码，后续步骤需要使用。**

![image-20240416170321329](./assets/image-20240416170321329.png#center)

![image-20240416170602214](./assets/image-20240416170602214.png#center)

5. 打开远程仓库中的Setting页面，点击Sercrets and variables-->Actions-->New reposiroty secert.

![image-20240417103621284](./assets/image-20240417103621284.png#center)

6. 在New repository secret页面中添加步骤4中的Token, 并设置相应的Name（后续需要使用）, 点击Add secret.

![image-20240417104234587](./assets/image-20240417104234587.png#center)

7. 在本地仓库quickstart目录下新建.github/workflows/main.yml文件（.github和workflows均为目录）。

![image-20240417105504777](./assets/image-20240417105504777.png#center)

8. 按照个人信息修改如下所示的main.yml文件（主要修改branches和personal_token），并填充至自己新建的main.yml文件中。

```yaml
name: Hugo Deploy GitHub Pages

on:
  push:
    branches:
      - source  # 设置为自己远程仓库的分支名

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          submodules: true
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.124.1'  # 使用你的Hugo版本号
          extended: true # 如果你使用的不是extended版本的hugo，将true改为false

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.HUGO_BLOG }}  # 使用你步骤6设置的Name(大写)
          publish_dir: ./public
          publish_branch: main  # 添加这一行, 可以将推送分支改为main
          user_name: 'github-actions[bot]'
          user_email: 'github-actions[bot]@users.noreply.github.com'
          commit_message: ${{ github.event.head_commit.message }}
          # cname: yourdomain.com  # 如果你有自定义域名, 替换为你的域名
```

9. 退回至quickstart目录下，使用如下命令推送至远程仓库进行测试。

```shell
git add .
git commit -m "test auto deploy"
git push origin master:source
```

10. 打开域名`https://username.github.io`(username更换为自己的username) 进行查看。

![image-20240417113022906](./assets/image-20240417113022906.png#center)
