#encoding:utf-8
import os
#处理文件路径的全局变量
base_dir=os.path.split(os.path.realpath(__file__))[0]
cfg_dir=''.join([base_dir,'/../../config/'])