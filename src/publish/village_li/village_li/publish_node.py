import rclpy
from rclpy.node import Node
from std_msgs.msg import String, UInt32

class PublishNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info(f"Node {name} is running!")

       
        self.game_list = []
        self.game_count = 0

        self.sub_game = self.create_subscription(
            String, "happy_xiaoxiao_cats", self.game_callback, 10
        )

        self.pub_statistics = self.create_publisher(UInt32, "happy_xiaoxiao_cats_statistics", 10)

    def game_callback(self, msg):
        self.game_list.append(msg.data)
        self.game_count += 1

        self.get_logger().info(f"Received game: {msg.data}")

        if self.game_count % 5 == 0:
            statistics_msg = UInt32()
            statistics_msg.data = self.game_count  
            self.pub_statistics.publish(statistics_msg)

            self.get_logger().info(f"Published statistics: {self.game_count} games collected!")

def main(args=None):
    rclpy.init(args=args)  
    node = PublishNode("publish")  
    rclpy.spin(node)  
    rclpy.shutdown()  

if __name__ == "__main__":
    main()