#include <cstdint>
#include <iostream>

#include "controler.h"
#include "ImageProcessorImpl.h"
#include "OutputSaveFrame.h"

Controler::Controler(){}

void Controler::controlLaneDetection(std::vector<unsigned char> frame, ImageProcessorImpl imageProcessor, OutputSaveFrame output) { 
    std::vector<unsigned char> processedFrame = imageProcessor.processImage(frame);
    output.emitFrame(processedFrame);
}