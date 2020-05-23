#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from bb8_move_circle_class import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8()
    rospy.loginfo("Finished service move_bb8_in_circle")
    return EmptyResponse()

rospy.init_node('service_move_bb8_in_circle_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()    # maintain the service open

'''
Tahap PERTAMA (roslaunch)
1. Buat file bb8_move_circle_service_server.py
2. Buat folder launch di dalam project my_python_class
3. Buat file .launch dengan nama bb8_move_circle_service_server.launch
4. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_circle_service_server.py di folder my_python_class/src
    b. roscd; cd .. [ENTER]
    c. roslaunch my_python_class bb8_move_circle_service_server.launch
5. Terminal #2
    a. rosservice call /bb8_move_circle_service_server [TAB]+[TAB]
    b. ENTER and the the BB8 robot berputaaaar, excelent
'''