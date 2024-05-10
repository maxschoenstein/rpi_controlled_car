#pragma once

#include <stdexcept>
#include <iostream>
#include <memory>
#include "ImageProcessorImpl.h"
#include "ImageProcessorEnum.h"
#include "image_processor.h"
// #include "loadConfig.h"

class ImageProcessorFactory {
public:
    ImageProcessorImpl createImageProcessor();
};