#include <filesystem>

#include "OutputFactory.h"
#include "OutputSaveFrame.h"


OutputFactory::OutputFactory() {}

OutputSaveFrame OutputFactory::createOutput() {
    OutputSaveFrame output;
    return output;
}