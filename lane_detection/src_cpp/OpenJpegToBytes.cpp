#include <iostream>
#include <fstream>
#include <vector>

std::vector<unsigned char> openJpegToBytes(const std::string& file_path) {
    std::ifstream file(file_path, std::ios::binary);
    
    if (!file) {
        std::cerr << "Error: Could not open file " << file_path << std::endl;
        return std::vector<unsigned char>(); // Return an empty vector
    }
    
    // Determine the file size
    file.seekg(0, std::ios::end);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    // Read the file into a vector
    std::vector<unsigned char>::size_type buffer_size = static_cast<std::vector<unsigned char>::size_type>(size);
    std::vector<unsigned char> buffer(buffer_size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        std::cerr << "Error: Could not read file " << file_path << std::endl;
        return std::vector<unsigned char>(); // Return an empty vector
    }
    
    return buffer;
}
