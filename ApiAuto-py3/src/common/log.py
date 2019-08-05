# coding:utf-8
import os,time
import logging
class WriteLog(object):
    def __init__(self,logger_name=''):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'logs')
        self.logger_name=logger_name
        if not os.path.exists(log_path):
            #有空查阅mkdir的区别
            os.makedirs(log_path)
        self.runtime_path="".join([log_path,"Runtime.log"])
        self.error_path="".join([log_path,"Error.log"])
    def add_logger(self):
        logger=logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            fh=logging.FileHandler(self.runtime_path)
            fh.setLevel(logging.INFO)
            fh1=logging.FileHandler(self.error_path)
            fh1.setLevel(logging.ERROR)
            fmt="%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s"
            datefmt=time.strptime("%Y.%m.%d-%H:%M:%S",time.localtime(time.time()))
            formatter=logging.Formatter(fmt,datefmt)
            fh.setFormatter(formatter)
            fh1.setFormatter(formatter)
            logger.addHandler(fh)
            logger.addHandler(fh1)
        return logger
    def get_logger(logger_name=""):
        return WriteLog(logger_name).add_logger()

if __name__ == "__main__":
    logger=WriteLog().add_logger()
    logger.info("********我是运行时日志********")
    logger.info("********我是错误日志********")