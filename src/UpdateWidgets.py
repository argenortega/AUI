__author__ = 'Argen'


from PyQt4.uic import compileUi
import glob

path ='../ui/'

for i in glob.glob(path+'*.ui'):
    uiFile = i.replace('.ui','')
    fileName = uiFile.replace('../ui/','')
    print 'Compiling %s'%fileName
    fout = open(fileName+"UI.py", "w")
    compileUi(path+fileName+'.ui',fout)
    fout.close()

'''
compileUi(path+'Camera.ui','CameraUI.py')
compileUi(path+'Extra.ui','ExtraViewUI.py')
compileUi(path+'Joystick.ui','JoystickUI.py')
compileUi(path+'Map.ui','MapUI.py',resource_suffix='_rc')
compileUi(path+'MixedInitiative.ui','MixedInitiativeUI.py')
compileUi(path+'AUIParameters.ui','ParametersUI.py')
compileUi(path+'Pointcloud.ui','PointcloudUI.py')
compileUi(path+'Probabilities.ui','ProbabilitiesUI.py')
compileUi(path+'Screenshot.ui','ScreenshotUI.py')
compileUi(path+'StatusBar.ui','StatusBarUI.py')
compileUi(path+'Utilities.ui','UtilitiesUI.py')
compileUi(path+'Views.ui','ViewsUI.py')
compileUi(path+'Wifi.ui','WifiUI.py')
'''