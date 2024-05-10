
#pragma once

# include "controler.h"
# include "ImageProcessorImpl.h"
# include "OutputSaveFrame.h"
#include <filesystem>

class InputImportImage {
public:
    InputImportImage();
    void connect(Controler controler, ImageProcessorImpl imageProcessor, OutputSaveFrame output);
    void disconnect();

private:
    std::filesystem::path jpeg_directory;
};

