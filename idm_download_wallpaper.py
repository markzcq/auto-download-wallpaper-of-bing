from requests import get
from re import search
# # 用于调用CMD命令行
from subprocess import call 


# def IDMdownload(DownUrl, DownPath, FileName):
# 	IDM = r"D:\Tools\InternetDownloadManager\IDM\Bin\IDMan.exe"
#     os.chdir(IDMPath)
#     IDM = "IDMan.exe"
#     command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q'])
#     print(command)
#     os.system(command)

base = 'https://cn.bing.com'
base1 = 'https://s.cn.bing.net'

#Bing Wallpaper API
r = get('https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1')
xml = r.text

#获得默认大小图片地址
img_url = base + search(r'<url>(.*)</url>', xml).groups()[0]

#获得高清图片地址
HDimg_url= base + search(r'<urlBase>(.*)</urlBase>',xml).groups()[0] + '_UHD.jpg'

#获取图片时间以及版权信息
data_text = search(r'<startdate>(.*)</startdate>',xml).groups()[0]
copyright_text = search(r'<copyright>(.*)</copyright>', xml).groups()[0]
copyright_url = base + search(r'<copyrightlink>(.*)</copyrightlink>', xml).groups()[0]

#下载图片以及版权信息
with open(f'copyright{data_text}.txt', 'w', encoding='utf-8') as f: f.write(copyright_text + '\n详情: ' + copyright_url)   
# 启动idm下载
IDM = r"D:\Tools\InternetDownloadManager\IDM\Bin\IDMan.exe"
# 下载路径
down_path = 'E:/Wallpaper'
# 下载文件名称
output_filename = 'Bing-wallpaper'+ data_text +'.jpg'
# 下载文件链接（注意是这个列表）
down_url = HDimg_url
#只加入队列不下载
#call([IDM, '/d',down_url, '/p',down_path, '/f', output_filename, '/n', '/a'])
#直接进行下载
call([IDM, '/d',down_url, '/p',down_path, '/f', output_filename,'/n', '/q'])
call([IDM, '/s'])
