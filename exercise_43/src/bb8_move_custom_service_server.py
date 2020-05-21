#! /usr/bin/env python

import rospy
from exercise_43.srv import exercise_43_ServiceMessage, exercise_43_ServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom has been called")
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2
    i = 0
    while i <= request.duration:
        my_pub.publish(move_circle)
        rate.sleep()
        i = i + 1
    
    move_circle.linear.x = 0
    move_circle.angular.z = 0
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_circle_custom")

    response = exercise_43_ServiceMessageResponse()
    response.success = True
    return response     # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_circle_custom_server')
my_service = rospy.Service('/move_bb8_in_circle_custom', exercise_43_ServiceMessage, my_callback)   # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()    # mainain the service open


'''
Tahap PERTAMA (membuat service server)
1. Buat file .srv di folder srv
2. Setting configuration di CMakeList.txt
3. Setting configuration di package.xml
4. Terminal #1
    a. roscd; cd .. [ENTER]
    b. catkin_make
    c. source devel/setup.bash
    d. rossrv list | grep exercise_43_ServiceMessage
        exercise_43/exercise_43_ServiceMessage  # kalau muncul ini berarti file srv nya udah jadi

Tahap KEDUA versi 1 (rosrun)
1. Buat file bb8_move_custom_service_server.py
2. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_custom_service_server.py di folder exercise_43/src
    b. roscd; cd .. [ENTER]
    c. rosrun exercise_43 bb8_move_custom_service_server.py
3. Terminal #2
    a. rosservice call /move_bb8_in_circle_custom [TAB]+[TAB]
    b. kemudian ganti durationnya, silahkan masukan angka sesukanya
    c. and the the BB8 robot berputaaaar, excelent

Tahap KEDUA versi 1 (roslaunch)
1. Buat file bb8_move_custom_service_server.py
2. Buat folder launch di dalam project exercise_43
3. Buat file .launch dengan nama start_bb8_move_custom_service_server.launch
4. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_custom_service_server.py di folder exercise_43/src
    b. roscd; cd .. [ENTER]
    c. roslaunch exercise_43 start_bb8_move_custom_service_server.launch
5. Terminal #2
    a. rosservice call /move_bb8_in_circle_custom [TAB]+[TAB]
    b. kemudian ganti durationnya, silahkan masukan angka sesukanya
    c. and the the BB8 robot berputaaaar, excelent

Tahap KETIGA (membuat service client)
1. Buat file bb8_move_custom_service_client.py di folder exercise_43/src
2. Terminal #1  -> Eksekusi perintah chmod +x bb8_move_custom_service_client.py di folder exercise_43/src
3. Buat file call_bb8_move_custom_service_server.launch di folder exercise_43/launch
4. Terminal #1
    a. roscd; cd .. [ENTER]     # opsional mau di directory mana aja bisa
    b. catkin_make
    c. roslaunch exercise_43 start_bb8_move_custom_service_server.launch
5. Terminal #2
    a. roscd; cd .. [ENTER]     # opsional mau di directory mana aja bisa
    b. roslaunch exercise_43 call_bb8_move_in_circle_service_server.launch
6. DONE, yout bb8 moved circle
'''