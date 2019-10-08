- Objective

> The aim of this work is to follow a person and turn with respect to the movement

- Outline

> Using two separate python files
>
> 1. Establish ROS publisher and constantly sending drive commans to Jackal UGV
>
> 2. Post-process camera frames and send variable changes to publisher for updating Jackal's control

- Post-process

> 1. Enable pipeline streaming on D435 and post-process each frame
>
> 2. Define two float64 variables FowardMessage and TurnMessage
>
> 3. Use pytorch pre-trainer Faster-RCNN model for post-processing
>> a. 'Person' detected - assign linear.x to ForwardMessage for driving Jackal forward
>>> i. Check whether the mid-point of the 'person' bounding box is within the pre-defined range of the frame
>>>
>>>> 1.Left: assign a positive value of angular speed to ControlMessage
>>>>
>>>> 2.Right: assign a negative value of angular speed to ControlMessage
>>>
>>
>> b. No 'Person' detected - assign 0 to ForwardMessage to stop Jackal
>
> 4. Publish and update cmd_vel 
>
> 5. Repeat process


- ROS Publisher
- 
> 1. Initial ROS node for publishing and receiving messages
>
> 2. Publisher
>> a. Topic name: cmd_vel
>>
>> b. ROS publishing rate: 10HZ
>>
>> c. Message type: geology Twist
>>> i. geometry_msgs/Vector3 linear
>>>> float64 x
>>>>
>>>> float64 y
>>>>
>>>> float64 z
>>>>
>>>  
>>
>>> ii. geometry_msgs/Vector3 angular
>>>> float64 x
>>>> 
>>>> float64 y
>>>>
>>>> float64 z
>>>>
>>>
>>
>
> 3. Receive
>> a. Topic name: ForwardMessage
>>
>> b. callbackfunction(): Once received message, change linear.x to FowardMessage
>>
>> c. Topic name: ControlMessage
>>
>> d. callbackfunction(): Once received message, change angular.z to ControlMessage

