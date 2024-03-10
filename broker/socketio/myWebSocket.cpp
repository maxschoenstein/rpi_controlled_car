#include <iostream>
#include <websocketpp/config/asio_no_tls.hpp>
#include <websocketpp/server.hpp>
#include <websocketpp/common/thread.hpp>
#include <websocketpp/common/memory.hpp>

using namespace std;

// Define the server type
typedef websocketpp::server<websocketpp::config::asio> server;

// Create an instance of the server
server ws_server;

// Function to handle WebSocket connections
void on_message(websocketpp::connection_hdl hdl, server::message_ptr msg) {
    string command = msg->get_payload();
    cout << "Received message: " << command << "\n";

    // Depending on the command, you can perform actions or send responses
    // For simplicity, we'll just print the received message.
    // Modify this function based on your application's needs.
}

int main() {
    // Set up WebSocket server
    ws_server.set_message_handler(bind(&on_message, placeholders::_1, placeholders::_2));
    ws_server.init_asio();

    // Replace 'your_ip_address' and 'your_port' with your desired IP address and port
    string your_ip_address = "0.0.0.0";
    int your_port = 5001;

    // Start WebSocket server in a separate thread
    thread server_thread([&]() {
        ws_server.listen(your_port);
        ws_server.start_accept();
        ws_server.run();
    });

    cout << "WebSocket server listening on http://" << your_ip_address << ":" << your_port << "\n";

    // Wait for the server thread to finish
    server_thread.join();

    return 0;
}
