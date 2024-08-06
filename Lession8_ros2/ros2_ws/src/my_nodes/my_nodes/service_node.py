import rclpy
from rclpy.node import Node
from my_interfaces.srv import CustomService

class CustomServiceServer(Node):

    def __init__(self):
        super().__init__('custom_service_server')
        self.srv = self.create_service(CustomService, 'custom_service', self.handle_custom_service)

    def handle_custom_service(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Request: a={request.a}, b={request.b} Response: sum={response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CustomServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
