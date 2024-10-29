#include <unordered_map>
using namespace std;
class Logger {
    unordered_map<string, int> times;
public:
    Logger() {
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if ((times.find(message) != times.end()) && (timestamp < times[message] + 10)) {
            return false;
        }

        times[message] = timestamp;
        return true;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */