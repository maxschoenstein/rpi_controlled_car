#include "pwmControl.h"
#include <iostream>
#include <wiringPi.h>
#include <unistd.h>

#include "pwmControl.h"

PWMControl::PWMControl(int pin, int frequency, int max, int min, int neutral, double step)
    : pin(pin), frequency(frequency), neutral(neutral), min(min), max(max), step(step), duty_cycle(neutral) {

    wiringPiSetupGpio();
    pinMode(pin, PWM_OUTPUT);

    pwmSetMode(PWM_MODE_MS);
    pwmSetClock(1920);  // 50Hz
    pwmSetRange(200);

    pwmWrite(pin, neutral);
    usleep(1500000);
    pwmWrite(pin, 0);

    std::cout << "PWMControl initialized\n"
              << "Pin: " << pin << "\n"
              << "PWM Frequency: " << frequency << "\n"
              << "PWM Max: " << max << "\n"
              << "PWM Min: " << min << "\n"
              << "PWM Neutral: " << neutral << "\n"
              << "PWM Step: " << step << "\n";
}

void PWMControl::increaseDutyCycle() {
    if (duty_cycle >= max) {
        return;
    } else {
        duty_cycle += step;
        pwmWrite(pin, duty_cycle);
        usleep(30000);
        pwmWrite(pin, 0);
    }
    std::cout << "increase\n" << duty_cycle << "\n";
}

void PWMControl::decreaseDutyCycle() {
    if (duty_cycle <= min) {
        return;
    } else {
        duty_cycle -= step;
        pwmWrite(pin, duty_cycle);
        usleep(30000);
        pwmWrite(pin, 0);
    }
    std::cout << "decrease\n" << duty_cycle << "\n";
}

void PWMControl::exit() {
    std::cout << "exit\n";

    pwmWrite(pin, neutral);
    usleep(1500000);
    pwmWrite(pin, 0);

    pwmSetMode(PWM_MODE_MS);
    pwmSetClock(1920);  // Reset PWM settings
    pwmSetRange(200);

    pinMode(pin, INPUT);
}

int main() {
    PWMControl steerControl(18, 50, 7, 5, 6, 0.25);

    while (true) {
        int value;
        std::cout << "Type something: ";
        std::cin >> value;
        steerControl.increaseDutyCycle();
    }

    return 0;
}
