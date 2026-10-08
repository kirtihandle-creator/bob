#include <iostream>
#include <random>
#include <sstream>
#include <string>

// Standalone C++17 game. Build: g++ -std=c++17 number_guessing_game.cpp -o guessing_game
int main() {
    std::mt19937 generator(std::random_device{}());
    std::uniform_int_distribution<int> distribution(1, 100);
    const int secret = distribution(generator);
    constexpr int max_attempts = 7;
    int attempts = 0;

    std::cout << "Guess the number between 1 and 100!\n"
              << "You have " << max_attempts << " attempts. Enter q to quit.\n";

    while (attempts < max_attempts) {
        std::cout << "Guess " << attempts + 1 << ": " << std::flush;
        std::string line;
        if (!std::getline(std::cin, line) || line == "q" || line == "Q") {
            std::cout << "Goodbye!\n";
            return 0;
        }

        std::istringstream input(line);
        int guess = 0;
        std::string extra;
        if (!(input >> guess) || (input >> extra) || guess < 1 || guess > 100) {
            std::cout << "Please enter a whole number from 1 to 100.\n";
            continue;
        }

        ++attempts;
        if (guess == secret) {
            std::cout << "Correct! You won in " << attempts << " attempt(s).\n";
            return 0;
        }
        std::cout << (guess < secret ? "Too low!\n" : "Too high!\n");
    }

    std::cout << "Out of attempts! The number was " << secret << ".\n";
    return 0;
}
