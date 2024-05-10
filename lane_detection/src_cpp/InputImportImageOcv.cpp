#include "InputImportImageOcv.h"
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

InputImportImageOcv::InputImportImageOcv(){
    this->jpeg_directory = JPEG_DIR;
}


void InputImportImageOcv::connect(Controler controler, ImageProcessorImpl imageProcessor, OutputSaveFrame output) {
    while (true) {
        // for (const auto& entry : fs::directory_iterator(this->jpeg_directory)) {
            // Load JPEG file
            // cv::Mat image = cv::imread(entry);

            // // Check if the image was loaded successfully
            // if (image.empty()) {
            //     std::cerr << "Error: Could not open or find the image" << std::endl;
            //     return -1;
            // }
            std::vector<unsigned char> frame(100, 0);
            controler.controlLaneDetection(frame, imageProcessor, output);

            }
        // }
    }


void InputImportImageOcv::disconnect() {
    // No action required for disconnecting
    std::cout << "disconnect" << std::endl;
}
