#include<ros/ros.h>
#include<sub_myo/Emg.h>
#include<string>

using namespace std;

void callback(const sub_myo::Emg& emg_data){
    auto sampler_1 = emg_data.sample1;
    auto sampler_2 = emg_data.sample2;

    cout<<emg_data.header.stamp<<endl;
    if((int)sampler_1[0] > 50)
        cout<<"================================================="<<endl; 
    for(int i = 0; i < sampler_1.size(); ++i){
        cout<<(int)sampler_1[i]<<" ";
    }
        
    cout<<endl; 
}


int main(int argc, char** argv){
    ros::init(argc, argv, "sub_info");
    ros::NodeHandle nh;

    ros::Rate rate(60);
    string topic = "/myo1/emg";
    ros::Subscriber sub_ = nh.subscribe(topic, 10, callback);
    
    while(ros::ok()){

        ros::spinOnce();
    }

    return 0;
}