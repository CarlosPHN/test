#include <chrono>
using namespace std::chrono;

class Watchtime {
    std::chrono::system_clock::time_point m_start;
    system_clock::duration diff;
public:
    void startTime();
    unsigned getTime();
};

void Watchtime::startTime() {
    m_start = std::chrono::system_clock::now();
}

unsigned Watchtime::getTime() {
    diff = system_clock::now() - m_start;
    return (unsigned)(duration_cast<milliseconds>(diff).count());
}
