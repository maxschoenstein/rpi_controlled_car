#ifndef INPUT_H
#define INPUT_H

// Abstract base class Input
class Input {
public:
    // Pure virtual function for connect
    virtual void connect() = 0;

    // Pure virtual function for disconnect
    virtual void disconnect() = 0;

    // Virtual destructor (recommended for polymorphic base classes)
    virtual ~Input() {}
};

#endif /* INPUT_H */
