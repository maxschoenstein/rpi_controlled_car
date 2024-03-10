#ifndef DRIVE_CONROL_H
#define DRIVE_CONROL_H

class DriveControl {
public:
    DriveControl(int pin, int frequency, double max, double min, double neutral, double step);
    void increaseDutyCycle();
    void decreaseDutyCycle();
    void engageReverse();
    void exit();
    void setup();

private:
    int pin;
    int frequency;
    double neutral;
    double min;
    double max;
    double step;
    double dutyCycle;

    void throttle();
    void idle();
    void brake();
};