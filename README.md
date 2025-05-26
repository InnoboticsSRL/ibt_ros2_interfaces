# IBT ros2 interfaces

## MoveArm
*MoveArm.action* provides the interface to send movements to the arm controller and to retrieve their status. It's defined as follow:
```bash
# Request
std_msgs/Header header  
MoveReq[] instructions  # list of instructions
---
# Result
int32 error_code        # error code
int32 SUCCESSFUL = 0
int32 INVALID_GOAL = -1

string error_str        # error message
---
# Feedback
string status           # status of the move
```

With the *MoveReq.msg* you can command the following type of movements:
- PTP
- LIN
- JOINT
- CIRC

## SetOutput
*SetOutput.srv* allows to enable/disable our ethercat output module

## SetAttrAll - GetAttrAll
- *SetAttrAll* allows to set certain ethernetip addreses 
- *GetAttrAll* allows to get certain ethernetip addreses 