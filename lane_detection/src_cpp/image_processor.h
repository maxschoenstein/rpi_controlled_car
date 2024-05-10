#pragma once
#include <vector>

class ImageProcessor {
public:
    virtual ~ImageProcessor() {}
    virtual std::vector<unsigned char> processImage(const std::vector<unsigned char>& frame) = 0;
};