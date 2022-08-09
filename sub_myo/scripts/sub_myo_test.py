import rospy
import sys
sys.path.append('/home/xuchengjun/zx_ws/src')
from sub_myo.msg import Emg
from time import time

st = time()
emg_list = []

def callback(msg):
    global st
    rospy.loginfo_once('have connected ..')
    sample1 = list(msg.sample1)
    emg_list.append(sample1)
    if len(emg_list) >= 100:
        et = time()
        print(f'time: {et-st}')
        del emg_list[0:20]
        st = time()
    # print('working ..')


if __name__ == "__main__":
    rospy.init_node("sub_myo_", anonymous=True)
    myo_topic = "/myo1/emg"
    suber = rospy.Subscriber(myo_topic, Emg, callback, queue_size=5)
    rospy.loginfo_once('ready ..')
    rospy.spin()
