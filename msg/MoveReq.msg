# Move request message for a robotic ARM

int32 move_type # Possible type of movement
int32 PTP=0
int32 LIN=1
int32 JOINT=2
int32 CIRC=3

Waypoint[] waypoints # List of waypoints to move through

float64 angle
float64 velocity
float64 acceleration
float64 rotational_velocity
float64 rotational_acceleration
