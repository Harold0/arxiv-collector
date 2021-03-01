import subprocess,requests
from tkinter import *
from bs4 import BeautifulSoup
top = Tk()
width = 300
height = 50
screenwidth = top.winfo_screenwidth()
screenheight = top.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
top.geometry(alignstr)


def get_name(_url_):
    print('正在获取文献名！')
    proxies = {
     "http": "fill-your-proxy-here:88888",
     'https': "fill-your-proxy-here:88888"
    }
    res = requests.get(_url_, proxies=proxies)
    title_str = BeautifulSoup(res.text, 'html.parser').find('title').contents[0]
    print('获取成功：', title_str)
    return title_str+'.pdf'

class Manager(object):

   def __init__(self, text_ui):
      self.text_ui = text_ui

   def download_arxiv(self):
      url_pdf = self.text_ui.get()
      if 'abs' in url_pdf:
         url_pdf = url_pdf.replace('abs','pdf')
         url_pdf = url_pdf + '.pdf'

      url_abs = url_pdf.replace('.pdf','').replace('pdf','abs')
      title_str = get_name(_url_=url_abs)\
                        .replace('?','？')\
                        .replace(':','：')\
                        .replace('\"','“')\
                        .replace('\n','')\
                        .replace('  ',' ')\
                        .replace('  ',' ')
      print('输出下载命令：','aria2c -o \"%s\" %s'%(title_str,url_pdf))
      subprocess.call('aria2c --all-proxy=\"fill-your-proxy-here:88888\" -o \"%s\" %s'%(title_str,url_pdf), shell=True) 
      
top.title("下载arxiv文献")
text_ui = Entry(top, highlightcolor='red', highlightthickness=1)
text_ui.pack(fill='x')

manager = Manager(text_ui)
download_ui = Button(top, text ="下载", command = manager.download_arxiv)
download_ui.pack()

top.mainloop()