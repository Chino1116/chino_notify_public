**简体中文** | [English](README_en.md) | [日本語](README_ja.md)

## 客户端下载

- [Android APK](client/ChinoNotify_android.apk)
- [iOS IPA](client/ChinoNotify_ios.ipa)
- [Windows x64 ZIP](client/ChinoNotify_windows_x64.zip)
- ### [全端 123 云盘下载](https://www.123865.com/s/Cbj7Vv-RPxuA)

# 声明

0. 本项目禁止商业使用。<br>
1. 客户端已打包但不做开源，仅提供下载使用。<br>
2. 服务端开源，可自行部署。<br>
3. 软件内可以配置任意服务端地址。<br>
4. 软件完全免费，若您喜欢可以给个 STAR。<br>
5. 本项目由 AI 开发，若您处于任何原因不喜欢本项目请离开。
6. iOS 端安装需要自行对 IPA 进行签名，否则无法使用。
7. iOS 端后台推送依赖苹果官方 APNs 服务，需要苹果开发者当然是开通不起啦。
8. 您也可以根据这个及其简易的服务端开发自己的客户端。

[![image](https://img.cdn1.vip/i/691d8b2dbfdd8_1763543853.webp)](https://github.com/Chino1116/chino_blog)

# <font color="#4671bb">ChinoNotify</font>

ChinoNotify 是一个跨平台的通知软件，支持 Android、iOS 和 Windows 客户端。您可以自行部署服务端，并配置客户端连接到任意服务端。

## 客户端能力

1. 批量删除通知。
2. 通知详情查看。
3. 全文搜索通知，并可对搜索内容全选删除。
4. 支持多选调整消息状态（已读/未读）。
5. 全平台通知删除/阅读状态伪实时同步。
6. 当配置保存后或许需要点击刷新按钮才能生效（这好像不是能力，更多是因为我懒）。

## 应用截图

<center class="half">
<img src="screenshot_1.png" width="300"/>
<img src="screenshot_2.png" width="300"/>
</center>
<center class="half">
<img src="screenshot_3.png" width="300"/>
<img src="screenshot_4.png" width="300"/>
</center>

## 下面或许是废话

> Q: <font color="#4671bb">为什么想要做这个东西？</font><br>A: 因为大部分 Webhook 推送软件都需要一定费用或者是有推送量限制，又或者是有平台限制，为了满足我个人需求所以诞生了这个 ChinoNotify。<br><br>
> Q: <font color="#4671bb">技术栈</font><br>A: 服务端采用 Python Flask + SQLite。客户端采用 Flutter 进行全平台的快速开发。（没有 Mac 使用 Github Action 对 iOS 端反复打包调试了一万年才搞定）

# <font color="#4671bb">部署教程</font>

## 服务端部署

### 前置条件

已安装 Python 3.x。

### 1. 安装依赖

进入 server 文件夹，运行下面命令安装 Python 依赖库。

```bash
pip install -r requirements.txt
```

### 2. 运行服务端

进入 server 文件夹，运行下面命令，后端将运行在 <font color="#4671bb">localhost:5000</font> 上。

```bash
python run.py
```

### 3. 配置客户端

在客户端软件中配置服务端地址为您的部署地址。

### 至此服务端部署结束

## 都看到这里了想必你一定对本项目有兴趣，请点个免费的 Star 吧！

### Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=Chino1116/chino_notify_public&type=date&legend=top-left)](https://www.star-history.com/#Chino1116/chino_notify_public&type=date&legend=top-left)
