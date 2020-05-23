#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from move_bb8 import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(request.duration)
    rospy.loginfo("Finished service move_bb8_in_circle")
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_circle_server') 
my_service = rospy.Service('/move_bb8_in_circle', MyCustomServiceMessage , my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()

'''
Tahap PERTAMA (rosrun)
1. Buat file bb8_move_circle_service_server.py
2. Buat folder launch di dalam project exercise_p1
4. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_circle_service_server.py di folder exercise_p1/src
    b. roscd; cd .. [ENTER]
    c. rosrun exercise_p1 bb8_move_circle_service_server.py
5. Terminal #2
    a. rosservice call /move_bb8_in_circle [TAB]+[TAB]
    b. isi duration nya jadi berapa aj
    c. ENTER and the the BB8 robot will move, excelent
'''