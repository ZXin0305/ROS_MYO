import rospy
import sys
sys.path.append('/home/xuchengjun/zx_ws/src')
from sub_myo.msg import Emg
from time import time
import message_filters

class MultiModalSub(object):
    def __init__(self):
        self.emg_sample1 = None

        self.emg_topic = '/myo1/emg'
        self.emg_sub = message_filters.Subscriber(self.emg_topic, Emg)

        self.syc = message_filters.ApproximateTimeSynchronizer([self.emg_sub], queue_size=10, slop=1, allow_headerless=True)   # 近似同步
        self.syc.registerCallback(self.callback)
        
        print('setting done ..')

    def callback(self, msg_emg):
        rospy.loginfo('Image has received...')

        self.emg_sample1 = list(msg_emg.sample1)
    
    def __iter__(self):
        return self

    def __next__(self):

        if self.emg_sample1 is None: 
            raise StopIteration

        return self.emg_sample1
    
if __name__ == "__main__":
    rospy.init_node("sub_myo_", anonymous=True)
    provider = MultiModalSub()

    while not rospy.is_shutdown():
        for data in provider:
            print(data)