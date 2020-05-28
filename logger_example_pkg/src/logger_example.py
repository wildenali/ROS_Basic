#! /usr/bin/env python

import rospy
import random
import time

# Options: DEBUG, INFO, WARN, ERROR, FATAL
rospy.init_node('log_demo', log_level=rospy.DEBUG)  # disini coba ganti2 log_level=rospy.DEBUG, misal jadi log_level=rospy.INFO dan cek apa perbedaannya
rate = rospy.Rate(0.5)

#rospy.loginfo_throttle(120, "DeathStars Minute info: "+str(time.time()))

while not rospy.is_shutdown():
    rospy.logdebug("There is a missing droid")
    rospy.loginfo("The Emperors Capuchino is done")
    rospy.logwarn("The Revels are coming time "+str(time.time()))
    exhaust_number = random.randint(1,100)
    port_number = random.randint(1,100)
    rospy.logerr(" The thermal exhaust port %s, right below the main port %s", exhaust_number, port_number)
    rospy.logfatal("The DeathStar Is EXPLODING")
    rate.sleep()
    rospy.logfatal("END")

    '''
Tahap PERTAMA
1. Buat file logger_example.py di folder src
2. Terminal #1
    a. Eksekusi perintah chmod +x logger_example.py di folder logger_example_pkg/src
    b. roscd; cd .. [ENTER]
3. Buat folder launch
4. Buat file start_logger_example.launc di folder launch
5. launch file tersebut, cek apa yg terjadi, kemudian close
6. disini coba ganti2 log_level=rospy.DEBUG, misal jadi log_level=rospy.INFO
7. launch file tersebut
8. dan cek apa perbedaannya (ulangi no 6, 7 dan 8)
'''