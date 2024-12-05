#include <iostream>
#include <limits>

using namespace std;

// Функция для проверки ввода
double inputDouble(const string& prompt) {
    double value;
    while (true) {
        cout << prompt;
        cin >> value;

        if (cin.fail()) {
            cout << "Ошибка ввода! Попробуйте еще раз." << endl;
            cin.clear(); // Сбрасываем состояние потока
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Очищаем ввод
        } else {
            return value;
        }
    }
}

int main() {
    cout << "Программа для проверки принадлежности точки заданной области." << endl;

    // Ввод значений
    double k = inputDouble("Введите коэффициент k для уравнения y = kx + b: ");
    double b = inputDouble("Введите коэффициент b для уравнения y = kx + b: ");
    double a = inputDouble("Введите коэффициент a для уравнения y = a / x: ");

    double x, y;
    while (true) {
        x = inputDouble("Введите координату x точки (x != 0): ");
        if (x != 0) break; // Проверка, чтобы x не был равен 0
        cout << "Ошибка: x не может быть равным 0. Попробуйте еще раз." << endl;
    }

    y = inputDouble("Введите координату y точки: ");

    // Вычисление границ области
    double y1 = a / x;     // y = a / x
    double y2 = k * x + b; // y = kx + b

    // Проверка принадлежности точки области
    if (y >= min(y1, y2) && y <= max(y1, y2)) {
        cout << "Точка (" << x << ", " << y << ") принадлежит заданной области." << endl;
    } else {
        cout << "Точка (" << x << ", " << y << ") не принадлежит заданной области." << endl;
    }

    return 0;
}
