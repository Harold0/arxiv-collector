import subprocess
from tkinter import *
top = Tk()

def get_name(_url_):
    from lxml import html
    doc = html.parse(_url_)
    title = doc.findtext('.//title')
    return title+'.pdf'

class Manager(object):

   def __init__(self, text_ui):
      self.text_ui = text_ui

   def download_arxiv(self):
      url = self.text_ui.get()
      url = url.replace('arxiv.org','xxx.itp.ac.cn')
      url = url.replace('https','http')
      abstract_url = url.replace('.pdf','').replace('pdf','abs')
      title_str = get_name(_url_=abstract_url)\
                        .replace('?','？')\
                        .replace(':','：')\
                        .replace('\"','“')\
                        .replace('\n','')\
                        .replace('  ',' ')\
                        .replace('  ',' ')
      print('输出下载命令：','aria2c -o \"%s\" %s'%(title_str,url))
      subprocess.call('aria2c -o \"%s\" %s'%(title_str,url), shell=True) # --all-proxy="http://127.0.0.1:11084"
      

text_ui = Entry(top)
text_ui.pack(side = LEFT)

manager = Manager(text_ui)
download_ui = Button(top, text ="下载", command = manager.download_arxiv)
download_ui.pack(side = RIGHT)

top.mainloop()