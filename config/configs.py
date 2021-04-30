import os,nnlog,time
'''
配置路径
'''

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'report/')
SNAPSHOT_PATH = os.path.join(BASE_PATH, 'snapshot/')
TEST_PATH =  os.path.join(BASE_PATH, 'testCase/')
DATA_PATH = os.path.join(BASE_PATH, 'data')

nowtime = time.strftime('%Y%m%d %H%M%S')
RECORDER_PATH = os.path.join(BASE_PATH , 'recorder' + '/'+ nowtime)
logname = os.path.join(LOG_PATH, 'log.txt')

CONFIG_PATH = os.path.join(BASE_PATH, 'config')


log = nnlog.Logger(file_name=logname, level='debug', when='D')

