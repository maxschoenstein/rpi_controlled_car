#include <fstream>
#include <filesystem>
#include <iostream>
// #include <opencv2/opencv.hpp>

#include "OutputSaveFrameOcv.h"

namespace fs = std::filesystem;

namespace {
    fs::path JPEG_OUTPUT_DIR = fs::path(__FILE__).parent_path().append("data").append("processed");
}

OutputSaveFrameOcv::OutputSaveFrameOcv() {
    this->m_outputDirectory = JPEG_OUTPUT_DIR;
}

bool OutputSaveFrameOcv::emitFrame(const std::vector<unsigned char>& frame) const {
    std::cout << "Frame content: ";
    for (const auto& pixel : frame) {
        std::cout << static_cast<int>(pixel) << " ";
    }
    std::cout << std::endl;

    // Return a boolean indicating success/failure
    return true;
}

