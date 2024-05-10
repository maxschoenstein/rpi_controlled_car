#include "image_processor_factory.h"
#include "ImageProcessorImpl.h"

ImageProcessorImpl ImageProcessorFactory::createImageProcessor() {
    // auto config = loadConfig("config.json");
    // ImageProcessorImplementation implementation = config.imageProcessorImplementation;
    // ImageProcessorImplementation implementation = ImageProcessorImplementation::IMG_PROC;
    
    ImageProcessorImpl imageProcessor;

    // if (implementation == ImageProcessorImplementation::IMG_PROC) {
    //     ImageProcessorImpl imageProcessor;
    // } else {
    //     throw std::invalid_argument("Invalid Image Processor Implementation");
    // }

    std::cout << "ImageProcessorFactory - Created ImageProcessor: " << typeid(imageProcessor).name() << std::endl;

    return imageProcessor;
}
