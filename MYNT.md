# MYNT-EYE & VSLAM

- Model Used:
- 
> * This was done on remote laptop with docker 
> 
> * MYNT-EYE-Depth D1000-50
>
> * IMU six-axis sensor, Multi-platform SDK, Maximum recognition distance: 10 m

- To install MYNT-EYE SDK
- 
  <https://mynt-eye-d-sdk.readthedocs.io/en/latest/sdk/install_ubuntu_src.html>

- To install VINS-MONO/VINS-FUSION dependencies
- 
  <https://mynt-eye-d-sdk.readthedocs.io/en/latest/openproject/contents.html>

- Launch mynt-eye-d wrapper with Vins-Fusion

```shell
$ roslaunch mynteye_wrapper_d vins_fusion.launch stream_mode:=1

To turn off infrared as Vins Fusion uses optical flow
$ roslaunch mynteye_wrapper_d vins_fusion.launch stream_mode:=1 ir_intensity:=10
```

- Launch Vins-Fusion
- 
```shell
$ roslaunch vins mynt-d-stereo-imu.launch
```
