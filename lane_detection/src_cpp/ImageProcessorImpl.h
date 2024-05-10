#pragma once

#include <vector>

class ImageProcessorImpl {

public:
    ImageProcessorImpl();
    std::vector<unsigned char> processImage(std::vector<unsigned char> frame);

};