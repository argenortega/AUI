__author__ = 'Argen'


from PyQt4.uic import compileUi

import glob

path ='ui/'
def transformUIfile(self,path):
    for i in glob.glob(path+'*.ui'):
        uiFile = i.replace('.ui','')
        fileName = uiFile.replace('ui/','')
        print 'Compiling %s'%fileName
        fout = open(fileName+"UI.py", "w")
        compileUi(path+fileName+'.ui',fout,resource_suffix='_rc')
        fout.close()

transformUIfile('GUI/*/*.ui')
transformUIfile('GUI/*/*/*.ui')
transformUIfile('MI/*.ui')