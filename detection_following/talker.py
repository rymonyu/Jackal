import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

message = Float64()
move_cmd = Twist()
move_cmd.linear.x = 0.0
move_cmd.linear.y = 0.0
move_cmd.linear.z = 0.0
move_cmd.angular.x = 0.0
move_cmd.angular.y = 0.0
move_cmd.angular.z = 0.0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard z = %s", data.data)
    move_cmd.angular.z = data.data

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard x = %s", data.data)
    move_cmd.linear.x = data.data

def listener():
    print("running listener")
    rospy.init_node('listener',anonymous=True)
    message = rospy.Subscriber("ControlMessage",Float64, callback)
    #print(message)
    angular = message
    #move_cmd.angular.z = angular
    rospy.spin()

def talker():
    print("running talker")
    rospy.init_node('talker', anonymous = False)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("ForwardMessage",Float64, callback2)
    rospy.Subscriber("ControlMessage",Float64, callback)

    #print(type(message))
    #print(type(move_cmd.angular.z))
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        print("x1:",move_cmd.linear.x)
        print("z2:",move_cmd.angular.z)
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    talker()
    listener()
