+++
title = 'Windows中使用hugo和Github Pages搭建个人博客（三）'
date = 2024-04-17T16:51:26+08:00
draft = true

+++

1.修改博客的主题，调整字体。

2.建立自动化脚本，合并多条命令为一条命令。

3.更换设备之后，如果快速给博客增添新的文章。

## 1.修改博客主题，调整字体

本文选取[hugo-PaperMod](https://themes.gohugo.io/themes/hugo-papermod/)作为主题，当然你可以从[hugo-themes](https://themes.gohugo.io/)选取其他主题进行使用。

1. 打开Powershell，进入到博客所在目录下。（以D:/quickstart目录为例）

2. 使用`git submodule`方式安装PaperMod主题。

```shell
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

![image-20240417172242767](./assets/image-20240417172242767.png#center)

3. 在博客所在目录下添加config.yml文件，同时删除hugo.toml文件或者将其重命名为hugo.toml.bak。

```yml
baseURL: "https://examplesite.com/"
title: ExampleSite
paginate: 5
theme: PaperMod

enableRobotsTXT: true
buildDrafts: false
buildFuture: false
buildExpired: false

minify:
  disableXML: true
  minifyOutput: true

params:
  env: production # to enable google analytics, opengraph, twitter-cards and schema.
  title: ExampleSite
  description: "ExampleSite description"
  keywords: [Blog, Portfolio, PaperMod]
  author: Me
  # author: ["Me", "You"] # multiple authors
  images: ["<link or path of image for opengraph, twitter-cards>"]
  DateFormat: "January 2, 2006"
  defaultTheme: auto # dark, light
  disableThemeToggle: false

  ShowReadingTime: true
  ShowShareButtons: true
  ShowPostNavLinks: true
  ShowBreadCrumbs: true
  ShowCodeCopyButtons: false
  ShowWordCount: true
  ShowRssButtonInSectionTermList: true
  UseHugoToc: true
  disableSpecial1stPost: false
  disableScrollToTop: false
  comments: false
  hidemeta: false
  hideSummary: false
  showtoc: false
  tocopen: false

  assets:
    # disableHLJS: true # to disable highlight.js
    # disableFingerprinting: true
    favicon: "<link / abs url>"
    favicon16x16: "<link / abs url>"
    favicon32x32: "<link / abs url>"
    apple_touch_icon: "<link / abs url>"
    safari_pinned_tab: "<link / abs url>"

  label:
    text: "Home"
    icon: /apple-touch-icon.png
    iconHeight: 35

  # profile-mode
  profileMode:
    enabled: false # needs to be explicitly set
    title: ExampleSite
    subtitle: "This is subtitle"
    imageUrl: "<img location>"
    imageWidth: 120
    imageHeight: 120
    imageTitle: my image
    buttons:
      - name: Posts
        url: posts
      - name: Tags
        url: tags

  # home-info mode
  homeInfoParams:
    Title: "Hi there \U0001F44B"
    Content: Welcome to my blog

  socialIcons:
    - name: x
      url: "https://x.com/"
    - name: stackoverflow
      url: "https://stackoverflow.com"
    - name: github
      url: "https://github.com/"

  analytics:
    google:
      SiteVerificationTag: "XYZabc"
    bing:
      SiteVerificationTag: "XYZabc"
    yandex:
      SiteVerificationTag: "XYZabc"

  cover:
    hidden: true # hide everywhere but not in structured data
    hiddenInList: true # hide on list pages and home
    hiddenInSingle: true # hide on single page

  editPost:
    URL: "https://github.com/<path_to_repo>/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link

  # for search
  # https://fusejs.io/api/options.html
  fuseOpts:
    isCaseSensitive: false
    shouldSort: true
    location: 0
    distance: 1000
    threshold: 0.4
    minMatchCharLength: 0
    limit: 10 # refer: https://www.fusejs.io/api/methods.html#search
    keys: ["title", "permalink", "summary", "content"]
menu:
  main:
    - identifier: categories
      name: categories
      url: /categories/
      weight: 10
    - identifier: tags
      name: tags
      url: /tags/
      weight: 20
    - identifier: example
      name: example.org
      url: https://example.org
      weight: 30
# Read: https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs#using-hugos-syntax-highlighter-chroma
pygmentsUseClasses: true
markup:
  highlight:
    noClasses: false
    # anchorLineNos: true
    # codeFences: true
    # guessSyntax: true
    # lineNos: true
    # style: monokai
```

4. 在[Google fonts](https://fonts.google.com/)中找到自己喜欢的字体，下载。这里以[Numito](https://fonts.google.com/specimen/Nunito)为例，点击右上角的get font进行下载。

![image-20240418155614069](D:\quickstart\content\posts\hugo-blog03\assets\image-20240418155614069.png)

5. 将下载的文件夹中的ttf文件解压之后防止在博客根目录下的static/fonts/文件夹下（没有fonts文件夹就自己新建一个），这里以quickstart目录为例，如下图。

![image-20240418155922317](D:\quickstart\content\posts\hugo-blog03\assets\image-20240418155922317.png)

6. 在quickstart/themes/PaperMod/assets/extended目录下新建文件fonts.css，填充以下代码引用字体

```css
@font-face {
	font-family: "Nunito-Italic-VariableFont_wght"; 
	src: url("/fonts/Nunito-Italic-VariableFont_wght") format ("truetype");
}
@font-face {
	font-family: "Nunito-VariableFont_wght";
	src: url("/fonts/Nunito-VariableFont_wght") format ("truetype");
}
```

7.修改quickstart/themes/PaperMod/assets/css/extended目录下的blank.css文件，填充以下代码设置整个网页所使用的字体。

```css
body {
    font-family: Nunito-Italic-VariableFont_wght, Nunito-VariableFont_wght;
} 
```























