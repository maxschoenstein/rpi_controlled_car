#pragma once

#include <cstdint>

#include "ImageProcessorImpl.h"
#include "OutputSaveFrame.h"

class Controler {
public:
    Controler();
    void controlLaneDetection(std::vector<unsigned char> frame, ImageProcessorImpl imageProcessor, OutputSaveFrame output);
};