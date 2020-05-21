#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")
    move_square.linear.x = 0.2
    move_square.angular.z = 0.2
    my_pub.publish(move_square)
    rate.sleep()
    i = 0
    print(request.repetitions)
    print(request.side)
    
    for i in range(request.repetitions):
        while i < 4:
            move_square.linear.x = 0.2
            move_square.angular.z = 0.0
            my_pub.publish(move_square)
            for x in range(int(request.side)):
                rate.sleep()
                rate.sleep()
                rate.sleep()
            move_square.linear.x = 0.0
            move_square.angular.z = 0.0
            my_pub.publish(move_square)
            rate.sleep()
            rate.sleep()
            move_square.linear.x = 0.0
            move_square.angular.z = 0.25
            my_pub.publish(move_square)
            rate.sleep()
            rate.sleep()
            rate.sleep()
            move_square.linear.x = 0.0
            move_square.angular.z = 0.0
            my_pub.publish(move_square)
            rate.sleep()
            rate.sleep()
            i = i + 1
    
    move_square.linear.x = 0
    move_square.angular.z = 0
    my_pub.publish(move_square)
    rospy.loginfo("Finished service move_bb8_in_square_custom")

    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response     # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_square_custom_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)   # create the Service called move_bb8_in_square with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_square = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
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
    d. rossrv list | grep BB8CustomServiceMessage
        services_quiz/BB8CustomServiceMessage  # kalau muncul ini berarti file srv nya udah jadi

Tahap KEDUA versi 1 (rosrun)
1. Buat file bb8_move_custom_service_server.py
2. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_custom_service_server.py di folder services_quiz/src
    b. roscd; cd .. [ENTER]
    c. rosrun services_quiz bb8_move_custom_service_server.py
3. Terminal #2
    a. rosservice call /move_bb8_in_square_custom "side: 0.0 repetitions: 0"
    b. kemudian isi nilai side dan repitiotions, silahkan masukan angka sesukanya
    c. and the the BB8 robot akan bergerak, excelent

Tahap KEDUA versi 2 (roslaunch)
1. Buat file bb8_move_custom_service_server.py
2. Buat folder launch di dalam project services_quiz
3. Buat file .launch dengan nama start_bb8_move_custom_service_server.launch
4. Terminal #1
    a. Eksekusi perintah chmod +x bb8_move_custom_service_server.py di folder exercise_43/src
    b. roscd; cd .. [ENTER]
    c. roslaunch services_quiz start_bb8_move_custom_service_server.launch
5. Terminal #2
    a. rosservice call /move_bb8_in_square_custom "side: 0.0 repetitions: 0"
    b. kemudian isi nilai side dan repitiotions, silahkan masukan angka sesukanya
    c. and the the BB8 robot akan bergerak, excelent

Tahap KETIGA (membuat service client)
1. Buat file bb8_move_custom_service_client.py di folder services_quiz/src
2. Terminal #1  -> Eksekusi perintah chmod +x bb8_move_custom_service_client.py di folder services_quiz/src
3. Buat file call_bb8_move_custom_service_server.launch di folder services_quiz/launch
4. Terminal #1
    a. roscd; cd .. [ENTER]     # opsional mau di directory mana aja bisa
    b. catkin_make
    c. source devel/setup.bash
    d. roslaunch services_quiz start_bb8_move_custom_service_server.launch
5. Terminal #2
    a. roscd; cd .. [ENTER]     # opsional mau di directory mana aja bisa
    b. source devel/setup.bash
    c. roslaunch services_quiz call_bb8_move_in_square_service_server.launch
6. DONE, yout bb8 moved square
'''




'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import time

def my_callback(request):
    
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")
    
    radius = request.side
    for i in range(request.repetitions):
        rospy.loginfo("Moving forward...")
        move_circle.linear.x = 0.2
        move_circle.angular.z = 0
        my_pub.publish(move_circle)
        time.sleep(radius)
        rospy.loginfo("Rotating...")
        move_circle.linear.x = 0
        move_circle.angular.z = 0.2
        my_pub.publish(move_circle)
        time.sleep(4)
        rospy.loginfo("Moving forward...")
        move_circle.linear.x = 0.2
        move_circle.angular.z = 0
        my_pub.publish(move_circle)
        time.sleep(radius)
        rospy.loginfo("Rotating...")
        move_circle.linear.x = 0
        move_circle.angular.z = 0.2
        my_pub.publish(move_circle)
        time.sleep(4)
        rospy.loginfo("Moving forward...")
        move_circle.linear.x = 0.2
        move_circle.angular.z = 0
        my_pub.publish(move_circle)
        time.sleep(radius)
        rospy.loginfo("Rotating...")
        move_circle.linear.x = 0
        move_circle.angular.z = 0.2
        my_pub.publish(move_circle)
        time.sleep(4)
        rospy.loginfo("Moving forward...")
        move_circle.linear.x = 0.2
        move_circle.angular.z = 0
        my_pub.publish(move_circle)
        time.sleep(radius)
        rospy.loginfo("Rotating...")
        move_circle.linear.x = 0
        move_circle.angular.z = 0.2
        my_pub.publish(move_circle)
        time.sleep(4)
        rospy.loginfo("Stopping...")
        move_circle.linear.x = 0
        move_circle.angular.z = 0
        my_pub.publish(move_circle)
        time.sleep(2)
        
    rospy.loginfo("Finished service move_bb8_in_square_custom")
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_square_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''