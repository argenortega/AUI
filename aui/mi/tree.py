__author__ = 'Argen'

import networkx as nx
import matplotlib.pyplot as plt

import jpype
from jpype import JClass, shutdownJVM, JavaException
import os.path
import networkx as nx



hid = nx.DiGraph()
evidence = {'joystick_input':('gui','views','main_views','additional_views'),
            'joystick_direction':('main_views','additional_views'),
            'AV_visible':('views','additional_views'),
            'focus':('main_views','snapshots'),
            'C1':('main_views','additional_views'),
            'C2':('main_views', 'additional_views'),
            'LM':('main_views', 'additional_views'),
            'GM':('main_views', 'additional_views'),
            'PC':('main_views', 'additional_views'),
            'AS_visible':('snapshots','additional_snapshots'),
            'battery_visible':('gui','robot_state','battery'),
            'wifi_visible':('gui','robot_state','wifi'),
            'battery_level':('gui','robot_state','battery'),
            'wifi_level':('gui','robot_state','wifi')}

hid.add_nodes_from([('gui', {'evidence':['joystick_direction','battery_level','battery_visible', 'wifi_visible', 'wifi_level']}),
                    ('views',{'evidence':['joystick_direction', 'AV_visible', 'C1', 'C2', 'LM']}),
                    ('snapshots',{'evidence':['AS_visible', 'focus']}),
                    ('robot_state',{'evidence':['battery_level', 'battery_visible', 'wifi_level', 'wifi_visible']}),
                    ('nothing',{}),
                    ('main_views',{'evidence':['focus', 'joystick_direction','PC','GM','LM','C1','C2']}),
                    ('priority',{}),
                    ('content',{}),
                    ('additional_views',{'evidence':['AV_visible','joystick_direction','PC','GM','LM','C1','C2']}),
                    ('hide_AV',{}),
                    ('show_AV',{}),
                    ('main_snapshot',{'evidence':['focus']}),
                    ('increase',{}),
                    ('decrease', {}),
                    ('additional_snapshots',{'evidence':['AS_visible']}),
                    ('hide_AS',{}),
                    ('show_AS',{}),
                    ('battery',{'evidence':['battery_level', 'battery_visible']}),
                    ('show_wifi',{}),
                    ('hide_wifi',{}),
                    ('wifi',{'evidence':['wifi_level', 'wifi_visible']}),
                    ('show_battery',{}),
                    ('hide_battery',{})])

hid.add_edges_from([('gui','views'),('gui','snapshots'),('gui','robot_state'),('gui','nothing'),
                    ('views','main_views'),('views','additional_views'),
                    ('snapshots','main_snapshot'),('snapshots','additional_snapshots'),
                    ('robot_state','wifi'),('robot_state','battery'),
                    ('main_views','priority'),('main_views','content'),
                    ('additional_views', 'hide_AV'),('additional_views','show_AV'),
                    ('main_snapshot','increase'),('main_snapshot','decrease'),
                    ('additional_snapshots','hide_AS'),('additional_snapshots','show_AS'),
                    ('battery','show_battery'),('battery','hide_battery'),
                    ('wifi','show_wifi'),('wifi', 'hide_wifi')])


nx.write_gpickle(hid, 'networks/hid.gpickle')

# pos = nx.graphviz_layout(hid, prog='dot')
# nx.draw_graphviz(hid, prog='dot')
# nx.draw_networkx(hid, pos=pos)
# plt.show()

evidence = {'battery_level': 'Ok', 'wifi_level': 'Ok', 'LM': 'AV', 'focus': 'S', 'PC': 'AV',
            'AS_visible': 'True', 'wifi_visible': 'True', 'battery_visible': 'True',
            'C2': 'AV', 'C1': 'MV', 'AV_visible': 'True', 'GM': 'AV', 'joystick_direction': 'Forward'}

path = nx.shortest_path(hid, 'gui','show_wifi')

for p in path:
    if hid.successors(p):
        observed = hid.node[p]['evidence']
        b = {k:v for k,v in evidence.iteritems() if k in observed}
        print b
