#encoding:utf-8
import os,sys
import ConfigParser
import codecs
from src.common import MyExcepiton as M
reload(sys)
sys.setdefaultencoding('utf-8')

# def optionxform(self,optionstr):

class IniHelper(object):
    def __init__(self,file_name,path=''):
        #处理file_name为绝对路径
        data_path=path
        #配置文件名称
        file_name=unicode(file_name)
        if os.path.exists(file_name):
            self.file_name=file_name
        else:
            self.file_name="".join([unicode(data_path),file_name])
            self.read_handle=None
            self.cfg=self.ini_read()
    def _get_read_handle(self):
        cfg=ConfigParser.ConfigParser()
        try:
            with codecs.open(self.file_name,"r","utf-8")as handle:
                cfg.readfp(handle)
                return  cfg
        except UnicodeDecodeError:
            with codecs.open(self.file_name,"r")as handle:
                cfg.readfp(handle)
                return cfg
        except IOError,e:
            print "找不到这个文件{0}".format(self.file_name)
            print e.message
    def get_value(self,section,option):
        #获取配置文件中section组下option的值
        try:
            value=self.cfg.get(unicode(section),unicode(option))
        except M.NoSectionError,e:
            print "".join(["没有找到section名称",section,e.message])
        except M.NoOptionError,e:
            print "".join(["没有找到option名称",option,e.message])
        else:
            return value
