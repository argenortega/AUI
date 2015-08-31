__author__ = 'Argen'

import networkx as nx
import matplotlib.pyplot as plt

import jpype
from jpype import JClass, shutdownJVM, JavaException
import os.path
import networkx as nx

hid = nx.DiGraph()
evidence = {'joystick_input': ('gui', 'views', 'main_views', 'additional_views'),
            'joystick_direction': ('main_views', 'additional_views'),
            'AV_visible': ('views', 'additional_views'),
            'focus': ('main_views', 'snapshots'),
            'C1': ('main_views', 'additional_views'),
            'C2': ('main_views', 'additional_views'),
            'LM': ('main_views', 'additional_views'),
            'GM': ('main_views', 'additional_views'),
            'PC': ('main_views', 'additional_views'),
            'AS_visible': ('snapshots', 'additional_snapshots'),
            'battery_visible': ('gui', 'robot_state', 'battery'),
            'wifi_visible': ('gui', 'robot_state', 'wifi'),
            'battery_level': ('gui', 'robot_state', 'battery'),
            'wifi_level': ('gui', 'robot_state', 'wifi')}

hid.add_nodes_from([('gui', {
    'evidence': ['joystick_direction', 'battery_level', 'battery_visible', 'wifi_visible', 'wifi_level', 'AV_visible',
                 'AS_visible', 'SA', 'SL', 'CL', 'Context']}),
                    ('views', {'evidence': ['joystick_direction', 'AV_visible', 'C1', 'C2', 'LM', 'PC', 'GM',
                                            'SA', 'SL', 'CL', 'Context']}),
                    ('snapshots', {'evidence': ['AS_visible', 'focus', 'SA', 'SL', 'CL']}),
                    ('robot_state', {'evidence': ['battery_level', 'battery_visible', 'wifi_level', 'wifi_visible',
                                                  'SA', 'SL', 'CL']}),
                    ('nothing', {}),
                    ('main_views', {'evidence': ['joystick_direction', 'PC', 'GM', 'LM', 'C1', 'C2',
                                                 'SA', 'SL', 'CL', 'Context'],
                                    'HSM':['HSM_C1_View', 'HSM_C2_Parent', 'HSM_LM_View', 'HSM_GM_Parent', 'HSM_PC_Parent']}),
                                    #'HSM':['HSM_C1_View', 'HSM_C2_View', 'HSM_LM_View', 'HSM_GM_View', 'HSM_PC_View']}),
                    ('add_C1', {}),
                    ('add_C2', {}),
                    ('add_LM', {}),
                    ('add_GM', {}),
                    ('add_PC', {}),
                    ('remove_C2', {}),
                    ('remove_GM', {}),
                    ('remove_PC', {}),
                    ('additional_views',
                     {'evidence': ['AV_visible', 'joystick_direction', 'focus', 'PC', 'GM', 'LM', 'C1', 'C2',
                                   'SA', 'SL', 'CL', 'Context'],
                      'HSM': ['HSM_AV']}),
                    ('hide_AV', {}),
                    ('show_AV', {}),
                    ('widget_content', {'evidence':['joystick_direction', 'SA', 'SL', 'CL', 'Context'],
                                        'HSM':['HSM_View_Content']}),
                    ('minimum',{}),
                    ('mapping',{}),
                    ('exploring',{}),
                    ('navigation',{}),
                    ('minimum_C2',{}),
                    ('mapping_C2',{}),
                    ('exploring_C2',{}),
                    ('navigation_C2',{}),
                    ('navigation_C1C2',{}),
                    ('main_snapshot', {'evidence': ['focus', 'SA', 'SL', 'CL'],
                                       'HSM': ['HSM_Snapshot']}),
                    ('increase', {}),
                    ('decrease', {}),
                    ('additional_snapshots', {'evidence': ['AS_visible', 'focus', 'SA', 'SL', 'CL'],
                                              'HSM': ['HSM_AS']}),
                    ('hide_AS', {}),
                    ('show_AS', {}),
                    ('battery', {'evidence': ['battery_level', 'battery_visible', 'SA', 'SL', 'CL'],
                                 'HSM':['HSM_Battery']}),
                    ('show_wifi', {}),
                    ('hide_wifi', {}),
                    ('wifi', {'evidence': ['wifi_level', 'wifi_visible', 'SA', 'SL', 'CL'],
                              'HSM': ['HSM_Wifi']}),
                    ('show_battery', {}),
                    ('hide_battery', {})])

hid.add_edges_from([('gui', 'views'), ('gui', 'snapshots'), ('gui', 'robot_state'), ('gui', 'nothing'),
                    ('views', 'main_views'), ('views', 'additional_views'), ('views', 'widget_content'),
                    ('snapshots', 'main_snapshot'), ('snapshots', 'additional_snapshots'),
                    ('robot_state', 'wifi'), ('robot_state', 'battery'),
                    ('main_views', 'add_C1'), ('main_views', 'add_C2'), ('main_views', 'add_LM'),
                    ('main_views', 'add_GM'), ('main_views', 'add_PC'),
                    ('main_views', 'remove_C2'), ('main_views', 'remove_GM'), ('main_views', 'remove_PC'),
                    ('additional_views', 'hide_AV'), ('additional_views', 'show_AV'),
                    ('widget_content', 'minimum'), ('widget_content', 'mapping'), ('widget_content', 'exploring'),
                    ('widget_content', 'navigation'),
                    ('widget_content', 'minimum_C2'), ('widget_content', 'mapping_C2'), ('widget_content', 'exploring_C2'),
                    ('widget_content', 'navigation_C2'), ('widget_content', 'navigation_C1C2'),
                    ('main_snapshot', 'increase'), ('main_snapshot', 'decrease'),
                    ('additional_snapshots', 'hide_AS'), ('additional_snapshots', 'show_AS'),
                    ('battery', 'show_battery'), ('battery', 'hide_battery'),
                    ('wifi', 'show_wifi'), ('wifi', 'hide_wifi')])

nx.write_gpickle(hid, 'networks/hid.gpickle')

#pos = nx.graphviz_layout(hid, prog='dot')
#nx.draw_graphviz(hid, prog='dot')
#nx.draw_networkx(hid, pos=pos)
#plt.show()

#HSM = nx.get_node_attributes(hid, 'HSM')
#print HSM

#node_evidence = nx.get_node_attributes(hid, 'evidence')
#print node_evidence
