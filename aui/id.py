__author__ = 'Argen'

import jpype
from jpype import JClass, shutdownJVM, JavaException
import os.path

jvmPath = jpype.getDefaultJVMPath()
jarpath = os.path.join(os.path.abspath('.'), '/Library/Java/Extensions/')
#jvmArg = " -Xint "
#jarpath = os.path.join(os.path.abspath('.'), '-Djava.library.path=/Users/Argen/Documents/MAS/R\&D/Code/smile/jsmile_src/java/:-Djava.library.path=/Users/Argen/Documents/MAS/R\&D/Code/smile/jsmile_src/java/smile.jar')
#classpath = './smile/jsmile_src/java/smile/'
#librarypath= '/Users/Argen/Documents/MAS/R\&D/Code/smile/jsmile_src/java/'
#print classpath
#jarArg = " -Djava.class.path=%s"%jarpath
jpype.startJVM(jvmPath, "-Djava.class.path=/Library/Java/Extensions/smile.jar")


print 'started JVM'
jpype.java.lang.System.out.println("hello!")

#Trying to create a network
net = JClass("smile.Network")
n = net()
#print net
#n.addNode(18,'Success')
n.readFile('networks/gui.xdsl')
n.updateBeliefs()
v1 = n.getNode('U')

decision = n.getNode('decision')

print 'Expected Values'
print '--'*10
expectedUtility = n.getNodeValue('U')
outCount = n.getOutcomeCount(decision)
print outCount
print len(expectedUtility)

for i in xrange(0, outCount):
    parentOutId = n.getOutcomeId(decision,i)
    expectedUtility = n.getNodeValue('U')[i]
    print n.getNodeName('U'), '(', parentOutId, '): '
    print 'Expected Utility = ', expectedUtility


# getAllNodes()
# getAllNodesIds()
'''
aValueIndexingParents = n.getValueIndexingParents('V1')
nodeDecision = aValueIndexingParents[0]
decisionName = n.getNodeName(nodeDecision)

print 'Expected values'
for i in xrange(0, n.getOutcomeCount(nodeDecision)):
    parentOutcomeId = n.getOutcomeId(nodeDecision, i)
    expectedUtility = n.getNodeValue('V1')[i]
    print '-', decisionName, '=', parentOutcomeId, ': '
    print 'Expected Utility = ', expectedUtility

print 'Success!'
'''
shutdownJVM()