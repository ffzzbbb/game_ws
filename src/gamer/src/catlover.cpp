#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/u_int32.hpp"
using std::placeholders::_1;

class gamer : public rclcpp::Node
{

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_game;
    rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr give_money;
    void game_callback(const std_msgs::msg::String::SharedPtr games)
    {
        std_msgs::msg::UInt32 money;
        money.data=10;
        give_money->publish(money);
        RCLCPP_INFO(this->get_logger(), "so cute %scat!", games->data.c_str());
    }
public:
    gamer(std::string name) : Node(name)
    {
        RCLCPP_INFO(this->get_logger(), "%s:I love cat!", name.c_str());
          // 创建一个订阅者订阅话题
        sub_game = this->create_subscription<std_msgs::msg::String>("happy_xiaoxiao_cats", 10, std::bind(&gamer::game_callback,this,_1));
        give_money = this->create_publisher<std_msgs::msg::UInt32>("happy_xiaoxiao_cats_money", 10);
    }
    };

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<gamer>("catlover");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}