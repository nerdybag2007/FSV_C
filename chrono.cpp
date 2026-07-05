#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <thread>
#include <chrono>

using namespace std;

const int WIDTH = 80;
const int HEIGHT = 25;

int main() {
    srand(time(0));

    vector<int> drops(WIDTH);

    for (int i = 0; i < WIDTH; i++)
        drops[i] = rand() % HEIGHT;

    while (true) {
        system("cls");

        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) {
                if (y == drops[x])
                    cout << char(33 + rand() % 94);
                else
                    cout << " ";
            }
            cout << '\n';
        }

        for (int i = 0; i < WIDTH; i++) {
            drops[i]++;
            if (drops[i] > HEIGHT)
                drops[i] = 0;
        }

        this_thread::sleep_for(chrono::milliseconds(50));
    }

    return 0;
}