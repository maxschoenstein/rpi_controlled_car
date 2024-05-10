#include <iostream>
#include <cstdint>

# include "controler.h"
#include "InputFactory.h"
#include "image_processor_factory.h"
#include "ImageProcessorImpl.h"
#include "OutputFactory.h"
#include "OutputSaveFrame.h"

int main() {

    Controler controler;

    ImageProcessorFactory imageProcessorFactory;
    ImageProcessorImpl imageProcessorImpl = imageProcessorFactory.createImageProcessor();

    OutputFactory outputSaveFrameFactory;
    OutputSaveFrame output = outputSaveFrameFactory.createOutput();

    InputFactory inputFactory;
    InputImportImage input = inputFactory.createInput();
    input.connect(controler, imageProcessorImpl, output);
    return 0;
}
