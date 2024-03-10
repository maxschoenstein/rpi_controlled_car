#ifndef PWM_CONTROL_H
#define PWM_CONTROL_H

class PWMControl {
public:
    PWMControl(int pin, int frequency, int max, int min, int neutral, double step);
    void increaseDutyCycle();
    void decreaseDutyCycle();
    void exit();

private:
    int pin;
    int frequency;
    int neutral;
    int min;
    int max;
    double step;
    int duty_cycle;
};

#endif // PWM_CONTROL_H
