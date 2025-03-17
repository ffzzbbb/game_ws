import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32


class WriterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("hallo, I'm a game creator %s." % name)
        self.pub_game = self.create_publisher(String,"happy_xiaoxiao_cats",10)
        
        self.version = 1
        self.timer_period = 5
        self.timer = self.create_timer(self.timer_period,self.timer_callback)

        self.account = 1000
        self.sub_money = self.create_subscription(UInt32,"happy_xiaoxiao_cats_money",self.recv_money_callback,10)

    

    def timer_callback(self):
        msg = String()
        msg.data = "bad cats version %d" % (self.version)
        self.pub_game.publish(msg)
        self.get_logger().info("A new version of the game was released: %s" % msg.data)
        self.version += 1
        


    def recv_money_callback(self,money):
        self.account += money.data
        self.get_logger().info("receive %d , now i have %d yuan" % (money.data,self.account))

def main(args=None):
    rclpy.init(args=args)
    xiaowang_node = WriterNode("xiaowang")
    rclpy.spin(xiaowang_node)
    rclpy.shutdown()