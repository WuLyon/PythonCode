import sys
import rclpy
from rclpy.node import Node
from my_interfaces.srv import CustomService

class CustomServiceClient(Node):

    def __init__(self):
        super().__init__('custom_service_client')
        self.cli = self.create_client(CustomService, 'custom_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = CustomService.Request()

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    node = CustomServiceClient()
    node.send_request()

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info(f'Service call failed: {e}')
            else:
                node.get_logger().info(f'Result: {response.sum}')
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
