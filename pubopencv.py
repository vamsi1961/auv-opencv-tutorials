import cv2 
import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def talker():
    DisImg = rospy.Publisher('DisplayingImage', Image, queue_size=1)
    rospy.init_node('SendingImage', anonymous=True)
    

    while 1:
        img = cv2.imread('rod2.png')
        img_re = cv2.resize(img,(600,600))
        blur = cv2.GaussianBlur(img_re,(5,5),cv2.BORDER_DEFAULT)
        msg_image = CvBridge().cv2_to_imgmsg(blur,"bgr8")
        DisImg.publish(msg_image)
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


