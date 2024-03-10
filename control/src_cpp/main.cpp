#include <iostream>
#include <thread>
#include <websocketpp/config/asio_no_tls.hpp>
#include <websocketpp/server.hpp>
#include <websocketpp/common/thread.hpp>
#include <websocketpp/common/memory.hpp>

#include "drive_control.h"  // Assume you have a DriveControl class
#include "pwm_control.h"    // Assume you have a PWMControl class

using namespace std;

// Define the server type
typedef websocketpp::server<websocketpp::config::asio> server;

// Create an instance of the server
server ws_server;

// Global instances of DriveControl and PWMControl
PWMControl steerControl(18, 50, 9.5, 4, 6.5, 0.25);
DriveControl driveControl(19, 50, 7.4, 6.2, 6.5, 0.1);

// Function to handle WebSocket connections
void on_message(websocketpp::connection_hdl hdl, server::message_ptr msg) {
    string command = msg->get_payload();
    if (command == "ArrowUp") {
        cout << "ArrowUp\n";
        driveControl.increaseDutyCycle();
    } else if (command == "ArrowDown") {
        cout << "ArrowDown\n";
        driveControl.decreaseDutyCycle();
    } else if (command == "ArrowRight") {
        cout << "ArrowRight\n";
        steerControl.decreaseDutyCycle();
    } else if (command == "ArrowLeft") {
        cout << "ArrowLeft\n";
        steerControl.increaseDutyCycle();
    } else if (command == "Escape") {
        steerControl.exit();
        driveControl.exit();
        cout << "Exiting...\n";
        ws_server.stop();
    }
}

int main() {
    // Set up WebSocket server
    ws_server.set_message_handler(bind(&on_message, placeholders::_1, placeholders::_2));
    ws_server.init_asio();

    // Start WebSocket server in a separate thread
    thread server_thread([&]() {
        ws_server.listen(9002);
        ws_server.start_accept();
        ws_server.run();
    });

    // Start your PWM and Drive controls here...

    // Wait for the server thread to finish
    server_thread.join();

    return 0;
}
