#include "InputImportImage.h"
#include "OpenJpegToBytes.h"
#include "OutputSaveFrame.h"
# include "controler.h"

#include <filesystem>
#include <vector>
#include <iostream>
// #include <opencv/opencv.hpp>

namespace fs = std::filesystem;

namespace {
    fs::path JPEG_DIR = fs::path(__FILE__).parent_path().parent_path().append("data").append("rpi_camera");
}

InputImportImage::InputImportImage(){
    this->jpeg_directory = JPEG_DIR;
}


void InputImportImage::connect(Controler controler, ImageProcessorImpl imageProcessor, OutputSaveFrame output) {
    while (true) {
        // for (const auto& entry : fs::directory_iterator(this->jpeg_directory)) {
            std::vector<unsigned char> frame(100, 0);
            controler.controlLaneDetection(frame, imageProcessor, output);
            }
        // }
    }

void InputImportImage::disconnect() {
    // No action required for disconnecting
    std::cout << "disconnect" << std::endl;
}
