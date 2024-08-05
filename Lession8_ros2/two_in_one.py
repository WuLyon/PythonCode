import rclpy
import rclpy.executors
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    
    def __init__(self):
        super().__init__('log_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Publishing num: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publish: "{msg.data}"')
        self.i += 1

class Subscriber(Node):
    
    def __init__(self):
        super().__init__('log_subscriber')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Listen: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    subscriber = Subscriber()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(publisher)
    executor.add_node(subscriber)

    try:
        executor.spin()
    finally:
        subscriber.destroy_node()
        publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()