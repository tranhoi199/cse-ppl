#include <iostream>
#include <cstdio>

using namespace std;

int *p1;
int *p2 = new int;
int *p3 = new int[10];

int *q1 = p1;
int *q2 = p2;
int *q3 = p3;

int r1;
int r2 = 5;

int h1 = 5;
int h2 = 5;

int foo(int x) {
    int a1;
    int a2 = 5;

    int *e1;
    int *e2 = new int;
    int *e3 = new int[10];

    int *f1 = e1;
    int *f2 = e2;
    int *f3 = e3;

    static int u1;
    static int u2 = 5;

    static int *y1;
    static int *y2 = new int;
    static int *y3 = new int[10];

    int h1 = 10;
    static int h2 = 10;

    // return x; // 5, trả về giá trị của biến x, sau foo(), x bị xóa
    // return a1; // OK, trả về giá trị bất kì từ a1
    // return a2; // 5, giống x
    // return *e1; // Error, con trỏ ko có giá trị tham chiếu tới 
    // return *e2; // 0, trả về vùng nhớ được tạo ra trong heap, biến con trỏ e2 bị xóa sau foo
    // return *e3; // 0, giống trên
    // return *f1; // giống e1, vì 2 con trỏ treo, ko có vùng nhớ để trỏ tới
    // return *f2; // 0, giống e2, sau foo(), biến e2, f2 đều bị xóa, nhưng vùng nhớ được tạo từ heap vẫn còn
    // return *f3; // 0, giống trên
    // return *y1; // lỗi, giống e1
    // return *y2; // 0, giống e2
    // return *y3; // 0, giống e3
    // return h1; // 10, giống a2
    return h2; // 10, giống trên, nhưng ko đổi giá trị h2 global
}

int *bar(int x) {
    int a1;
    int a2 = 5;

    int *e1;
    int *e2 = new int;
    int *e3 = new int[10];

    int *f1 = e1;
    int *f2 = e2;
    int *f3 = e3;

    static int u1;
    static int u2 = 5;

    static int *y1;
    static int *y2 = new int;
    static int *y3 = new int[10];

    int h1 = 15;
    static int h2 = 15;

    // return &x; // Error, lỗi tham khảo treo, biến x cục bộ bị xóa sau bar(), con trỏ treo
    // return &a1; // Error, giống trên
    // return &a2; // giống trên
    // return e1; // Error, con trỏ ko có giá trị tham chiếu tới
    // return e2; // 0, trả về 1 con trỏ khác trỏ tới vùng nhớ được tạo ra trong heap từ con trỏ e2, biến con trỏ e2 bị xóa sau bar
    // return e3; // 0, giống trên
    // return f1; // giống e1, vì 2 con trỏ treo, ko có vùng nhớ để trỏ tới
    // return f2; // 0, giống e2, trả về con trỏ trỏ tới vùng nhớ của f2,e2; sau bar(), biến e2, f2 đều bị xóa, nhưng vùng nhớ được tạo từ heap vẫn còn
    // return f3; // 0, giống trên
    // return y1; // lỗi, giống e1
    // return y2; // 0, giống e2
    // return y3; // 0, giống e3
    // return &h1; // lỗi giống a2
    return &h2; // 15, do là static, nên lúc trả về con trỏ có vùng nhớ h2 ở static, ko ghi đè giá trị h2 global
}


int main() {

    cout << foo(5) << endl;
    cout << *bar(5) << endl;

    cout << h1 << endl; // 5
    cout << h2 << endl; // 5

    return 0;
}