import logging,time,os
import config

log_path = config.rootPath +"\\log\\logger.doc"
class Log:
    def __init__(self):
        #文件命名
        self.logname = os.path.join(log_path,"%s.log"%time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s]-%(leveInname)s:%(message)s')

        #创建一个FileHandler,用于写到本地
        def __console(self,level,message):
            fh = logging.FileHandler(self.logname,'a',encoding = "utf-8")
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)

        #创建一个StreamHandler,用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(self.formatter)
            self.logger.addHandler(ch)
            if level == 'debug':
                self.logger.debug(message)
            if level == 'info':
                self.logger.debug(message)
            if level == 'warning':
                self.logger.debug(message)
            if level == 'error':
                self.logger.debug(message)

            #避免日志重复
            self.logger.removeHandler(ch)
            self.logger.removeHandler(fh)

            #关闭打开的文件
            fh.close()
            def debug(self,message):
                self.__console('debug',message)

            def info(self, message):
                self.__console('info', message)

            def warning(self, message):
                self.__console('warning', message)

            def error(self, message):
                self.__console('error', message)