#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time

distanceFront = 0.0
distanceRight = 0.0
distanceLeft  = 0.0

def callback(msg):
    global distanceFront, distanceRight, distanceLeft
    distanceFront = msg.ranges[360]
    distanceRight = msg.ranges[0]
    distanceLeft  = msg.ranges[719]
    
def main():
    rospy.init_node("topics_quiz_node")
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    twist = Twist()
    
    while distanceFront == 0.0:
        print(distanceFront)

    while not rospy.is_shutdown():
        print("%.2f %.2f %.2f" %( distanceLeft, distanceFront, distanceRight))
        
        if(distanceFront < 1):
            twist.linear.x = 0.0
            pub.publish(twist)
            time.sleep(1)
            twist.angular.z = 0.2
            pub.publish(twist)
            time.sleep(3)

        elif(distanceRight < 1):
            twist.linear.x = 0.0
            pub.publish(twist)
            time.sleep(1)
            twist.angular.z = 0.2
            pub.publish(twist)
            time.sleep(3)        

        elif(distanceLeft < 1):
            twist.linear.x = 0.0
            pub.publish(twist)
            time.sleep(1)
            twist.angular.z = -0.2
            pub.publish(twist)
            time.sleep(3)

        else:
            twist.linear.x = 0.2
            twist.angular.z = 0.0
            pub.publish(twist)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
