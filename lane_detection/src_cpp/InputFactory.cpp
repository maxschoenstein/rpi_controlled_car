
#include "InputEnum.h"
#include "InputImportImage.h"
#include "InputFactory.h"

#include <iostream>

InputFactory::InputFactory() {};

InputImportImage InputFactory::createInput() {
    InputImplementation inputImplementation = InputImplementation::MOCK;
    InputImportImage input;

    switch (inputImplementation) {
        case InputImplementation::MQTT:
            // input = new InputMqtt(CONFIG.messangerIp, CONFIG.messangerPort, controler, imageProcessor, output);
            break;
        case InputImplementation::SOCKETIO:
            // input = new InputSocketIo(CONFIG.messangerIp, CONFIG.messangerPort, controler, imageProcessor, output);
            break;
        case InputImplementation::MOCK:
            input = InputImportImage(); 
            break;
        default:
            throw std::invalid_argument("Invalid inputImplementation");
    }

    std::cout << "InputFactoryFactory - Created InputFactory: " << typeid(input).name() << std::endl;

    return input;
}
