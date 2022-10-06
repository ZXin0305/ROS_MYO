how to use:
1.connect usb4.0 to your PC or server
2.privide authority for the port: 
     cd /dev
     sudo chmod 777 ttyACM0 (or ttyACM1)
3.build ros pkg in your ros workplace
4.compile: catkin_make 
5.source your workplace && run the ros node: rosrun ....

Note that: this is just for a single MYO device
           if you want to use multi MYO, it's easy to build a ".launch" file to execute it!
