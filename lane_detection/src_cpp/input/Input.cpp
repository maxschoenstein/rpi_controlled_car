#include "Input.h"
#include <iostream>

// Example subclass implementing Input
class ConcreteInput : public Input {
public:
    // Implementing the connect function
    void connect() override {
        std::cout << "Connecting..." << std::endl;
        // Add your connection logic here
    }

    // Implementing the disconnect function
    void disconnect() override {
        std::cout << "Disconnecting..." << std::endl;
        // Add your disconnection logic here
    }
};
