#include <fstream>
#include <filesystem>

#include "OutputSaveFrame.h"

namespace fs = std::filesystem;

namespace {
    fs::path JPEG_OUTPUT_DIR = fs::path(__FILE__).parent_path().parent_path().append("data").append("processed");
}

OutputSaveFrame::OutputSaveFrame() {
    this->m_outputDirectory = JPEG_OUTPUT_DIR;
}

bool OutputSaveFrame::emitFrame(const std::vector<unsigned char>& frame) const {
    std::ofstream file(this->m_outputDirectory / "output.jpg", std::ios::binary);
    
    if (!file) {
        // Failed to open file for writing
        return false;
    }
    
    std::streamsize size = static_cast<std::streamsize>(frame.size());
    file.write(reinterpret_cast<const char*>(frame.data()), size);
    
    if (!file) {
        // Failed to write data to file
        return false;
    }
    
    // File write successful
    return true;
}

