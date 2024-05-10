#include <cstdint>

enum class InputImplementation : std::int8_t {
    MQTT = 0,
    SOCKETIO = 1,
    MOCK = 2
};
