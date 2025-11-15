#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;

    cout << "Welcome to Adithi's Chatbot!" << endl;
    cout << "Type something (or 'exit' to quit):" << endl;

    while (true) {
        cout << "\nYou: ";
        getline(cin, input);

        if (input == "hello") {
            cout << "Bot: Hi there! How can I assist you today?" << endl;
        } else if (input == "how are you?") {
            cout << "Bot: I'm just a bunch of C++ code, but I'm running smoothly!" << endl;
        } else if (input == "what's your name?") {
            cout << "Bot: I'm a rule-based chatbot created by Adithi." << endl;
        } else if (input == "bye!") {
            cout << "Bot: Goodbye! Have a great day." << endl;
            break;
        } else if (input == "thank you") {
            cout << "Bot: You're welcome!" << endl;
        } else if (input == "") {
            cout << "Bot: Hmm, you didn’t type anything." << endl;
        } else {
            cout << "Bot: I'm not sure how to respond to that." << endl;
        }
    }

    return 0;
}
