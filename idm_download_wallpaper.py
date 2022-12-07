from requests import get
from re import search
#用于调用CMD命令行
from subprocess import call 

base = 'https://cn.bing.com'
base1 = 'https://s.cn.bing.net'

#Bing Wallpaper API
r = get('https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1')
xml = r.text

#获得默认大小图片地址1920x1080
img_url = base + search(r'<url>(.*)</url>', xml).groups()[0]

#获得超高清图片地址(原图)
HDimg_url= base + search(r'<urlBase>(.*)</urlBase>',xml).groups()[0] + '_UHD.jpg'

#获取图片时间以及版权信息
data_text = search(r'<startdate>(.*)</startdate>',xml).groups()[0]
copyright_text = search(r'<copyright>(.*)</copyright>', xml).groups()[0]
copyright_url = base + search(r'<copyrightlink>(.*)</copyrightlink>', xml).groups()[0]

#下载图片以及版权信息
#保存图片版权信息到txt文件中，可以注释掉
with open(f'copyright{data_text}.txt', 'w', encoding='utf-8') as f: f.write(copyright_text + '\n详情: ' + copyright_url)  
  
#使用命令保存图片（没有IDM可以使用该命令，取消注释即可）默认为超高清图片，可以将HDimg_url变量设置为img_url,则为1920x1080
#with open(f'Bing-wallpaper{data_text}.jpg', 'wb') as f: f.write(get(HDimg_url).content)

# 启动idm下载（修改IDM执行文件所在目录）
IDM = r"D:\Tools\InternetDownloadManager\IDM\Bin\IDMan.exe"
# 下载路径（修改下载目录）
down_path = 'E:/Wallpaper'
# 下载文件名称（自定义文件名称）
output_filename = 'Bing-wallpaper'+ data_text +'.jpg'
#下载链接，默认为超高清图片，可以将HDimg_url变量设置为img_url,则为1920x1080
down_url = HDimg_url
#只加入队列不下载
#call([IDM, '/d',down_url, '/p',down_path, '/f', output_filename, '/n', '/a'])
#直接进行下载
call([IDM, '/d',down_url, '/p',down_path, '/f', output_filename,'/n', '/q'])
#开始队列中的任务
call([IDM, '/s'])
