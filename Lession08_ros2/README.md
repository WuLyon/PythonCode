
## create a interfaces package
`ros2 pkg create my_custom_interfaces --build-type ament_cmake --dependencies std_msgs`

```shell
cd my_custom_interfaces
mkdir msg
mkdir srv
touch msg/CustomMessage.msg
touch srv/CustomService.srv

```CustomMessage.msg
string data
int32 value

```CustomService.srv
# Request part
int32 a
int32 b

---
# Response part
int32 sum
```
Modify the CMakeLists.txt and package.xml

## create a service node and a client node
`ros2 pkg create my_nodes --build-type ament_python --dependencies rclpy my_interfaces
`
`pip install setuptools==58.2.0` can solve the warning: `setup.py install is deprecated.`