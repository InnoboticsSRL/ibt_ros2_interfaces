# IBT ROS2 INTERFACES

## move arm interface

This interface declare the action type that the move_arm_action_server accept.
 - The Goal is composed by a std_msg header and a vector of Instructions of MoveReq type.

 - The Result is an error code and an error string
 
 - The Feedback is composed by as status string, a move_index instruction and a move_type

the message "MoveReq" defines the structure of the instruction to be executed
the "PoseRPY" defines the Eulerian format to describe the pose.