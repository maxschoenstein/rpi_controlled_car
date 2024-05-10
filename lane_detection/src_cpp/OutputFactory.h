#pragma once

#include <filesystem>
#include "OutputSaveFrame.h"

class OutputFactory {
public:
    OutputFactory();
    OutputSaveFrame createOutput();
};