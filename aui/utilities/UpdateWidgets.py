__author__ = 'Argen'


from PyQt4.uic import compileUi

import glob
import os


path ='ui/'
def transformUIfile(self,path):
    for i in glob.glob(path+'*.ui'):
        uiFile = i.replace('.ui','')
        fileName = uiFile.replace(path,'')
        print 'Compiling %s'%fileName
        fout = open(fileName+"UI.py", "w")
        compileUi(path+fileName+'.ui',fout,resource_suffix='_rc')
        fout.close()



'''
print ("Compiling UIs")
os.system("pyuic4 main.ui > ui_main.py")
os.system("pyuic4 pref.ui > ui_pref.py")
os.system("pyrcc4 resources.qrc > resources_rc.py -py3")
print ("completed")
'''