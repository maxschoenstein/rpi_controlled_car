#include <iostream>
#include <wiringPi.h>
#include <unistd.h>
#include <cmath>



DriveControl::DriveControl(int pin, int frequency, double max, double min, double neutral, double step)
    : pin(pin), frequency(frequency), neutral(neutral), min(min), max(max), step(step), dutyCycle(neutral) {

    wiringPiSetupGpio();
    pinMode(pin, PWM_OUTPUT);

    pwmSetMode(PWM_MODE_MS);
    pwmSetClock(1920);  // 50Hz
    pwmSetRange(200);

    pwmWrite(pin, neutral);

    std::cout << "DriveControl initialized\n"
              << "Pin: " << pin << "\n"
              << "PWM Frequency: " << frequency << "\n"
              << "PWM Max: " << max << "\n"
              << "PWM Min: " << min << "\n"
              << "PWM Neutral: " << neutral << "\n"
              << "PWM Step: " << step << "\n";
}

void DriveControl::increaseDutyCycle() {
    if (dutyCycle >= max) {
        return;
    } else {
        dutyCycle += step;
        pwmWrite(pin, dutyCycle);
    }
    std::cout << "increase\n" << dutyCycle << "\n";
}

void DriveControl::decreaseDutyCycle() {
    if (dutyCycle <= min) {
        return;
    } else {
        dutyCycle -= step;
        pwmWrite(pin, dutyCycle);
    }
    std::cout << "decrease\n" << dutyCycle << "\n";
}

void DriveControl::engageReverse() {
    pwmWrite(pin, min);
    usleep(2500000);  // 2.5 seconds
    pwmWrite(pin, neutral);
}

void DriveControl::exit() {
    std::cout << "exit\n";

    pwmWrite(pin, neutral);
    usleep(1500000);  // 1.5 seconds
    pwmStop(pin);
    pinMode(pin, INPUT);
}

void DriveControl::setup() {
    std::cout << "SetUp program started.\n";
    idle();
    std::cout << "Press Enter to continue.\n";
    std::cin.ignore();
    throttle();
    std::cout << "Press Enter to continue.\n";
    std::cin.ignore();
    brake();
    std::cout << "SetUp program finished.\n";
}

void DriveControl::throttle() {
    pwmWrite(pin, max);
}

void DriveControl::idle() {
    pwmWrite(pin, neutral);
}

void DriveControl::brake() {
    pwmWrite(pin, min);
}

int main() {
    DriveControl driveControl(19, 50, 7.4, 6.2, 6.5, 0.1);

    // Your other logic here...

    return 0;
}
