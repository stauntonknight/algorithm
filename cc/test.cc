#include <iostream>
#include <thread>

using namespace std;

void thread_function() {
	std::cout << "Thread function\n";
}
int main() {
	std::thread t(&thread_function);
	cout << std::thread::hardware_concurrency() << endl;
	t.join();
}
