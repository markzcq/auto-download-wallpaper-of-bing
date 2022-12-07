# auto-download-wallpaper-of-bing
auto-download-wallpaper of bing

调用IDM自动下载必应每日一图，
没有IDM也可以使用python默认保存文件

可选功能：
# 下载器：
  # python自带文件保存
  # 调用IDM下载（需要修改IDM程序所在位置）
# 图片清晰度：
  # 默认清晰度为超高清
  # 可以设置为必应默认清晰度1920x1080
  
note：
  调用IDM下载器进行下载时，可以更改下载目录
  
 
  使用python文件保存时，默认保存在代码所在文件夹下
  
  
  可以利用电脑任务计划程序设置定时运行，同时将桌面壁纸个性化设置为幻灯片播放模式，选择壁纸文件夹，即可循环更换必应每日一图
  
  
参考：
idm使用命令行调用：https://www.internetdownloadmanager.com/support/command_line.html


''' 


idman /s or idman /d URL [/p local_path] [/f local_file_name] [/q] [/h] [/n] [/a] 

Parameters:
/d URL - downloads a file, eg.
IDMan.exe /d "https://www.internetdownloadmanager.com/path/FileName.zip" 
/s - starts queue in scheduler
/p local_path - defines the local path where to save the file
/f local_file_name - defines the local file name to save the file
/q - IDM will exit after the successful downloading. This parameter works only for the first copy
/h - IDM will hang up your connection after the successful downloading
/n - turns on the silent mode when IDM doesn't ask any questions
/a - add a file, specified with /d, to download queue, but don't start downloading

Parameters /a, /h, /n, /q, /f local_file_name, /p local_path work only
if you specified the file to download with /d URL

Examples:
C:\idman.exe /n /d https://www.tonec.com/download/idman317.exe


'''

