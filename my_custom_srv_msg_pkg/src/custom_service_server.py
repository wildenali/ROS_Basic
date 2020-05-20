#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    print "Request Data==> duration==>" + str(request.duration)
    my_response = MyCustomServiceMessageResponse()
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    return my_response

rospy.init_node('service_client')
my_service = rospy.Service('/my_service', MyCustomServiceMessage, my_callback)      # membuat service dgn nama my_service dgn mendefinisikan callback 
rospy.spin()    # maintain the service open

'''
Terminal #1
1. catkin_make
2. source devel/setup.bash
3. rossrv list | grep MyCustomServiceMessage    # untuk nge cek apakah srv msg nya udah ada atau belum

Terminal #2
1. rosservice call /my_service [TAB]+[TAB]
2. kemudian ganti durationnya, silahkan masukan sesukanya
'''