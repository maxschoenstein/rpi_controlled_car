#pragma once

#include <vector>
#include <string>
#include <filesystem>

namespace fs = std::filesystem;

class OutputSaveFrameOcv {
public:
    OutputSaveFrameOcv();
    bool emitFrame(const std::vector<unsigned char>& frame) const;

private:
    fs::path m_outputDirectory;
};

