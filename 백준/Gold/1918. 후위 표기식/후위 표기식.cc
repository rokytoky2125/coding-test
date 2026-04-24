#include <iostream>
#include <cstring> // strlen, strcpy 사용
#include <cctype> // isupper 함수 사용
using namespace std;

class String
{
public:
    String(const char* str = "Unknown") // 생성자
    {
        len_ = strlen(str);
        str_ = new char[len_ + 1];
        strcpy(str_, str);
    }
    ~String() { delete[] str_; } // 소멸자

    // 입출력 연산자 오버로딩
    friend ostream& operator<<(ostream& out, String& s);
    friend istream& operator>>(istream& in, String& s);

    void Print() { cout << str_ << endl; }

    char operator[](int index) { return str_[index]; }
    int GetLen() { return len_; }

private:
    int len_;
    char* str_;
};

// 입력 연산자 오버로딩
istream& operator>>(istream& in, String& s)
{
    char temp[1000]; // 임시 저장소
    in >> temp; // 문자열 입력 받음

    // 기존 메모리 해제 후 새로 할당
    delete[] s.str_;

    s.len_ = strlen(temp);
    s.str_ = new char[s.len_ + 1];
    strcpy(s.str_, temp);

    return in;
}

// 출력 연산자 오버로딩
ostream& operator<<(ostream& out, String& s)
{
    out << s.str_ << endl; // 문자열 출력
    return out;
}


class Stack
{
public:
    Stack(int n) { size_ = n; data_ = new int[size_]; count_ = 0; } // 생성자
    ~Stack() { delete[] data_; } // 소멸자
    void Push(int n) { data_[count_] = n; count_++; }
    int Pop() { count_--; return data_[count_]; }
    void PrintStack()
    {
        for (int i = 0; i < count_; i++)
        {
            cout << (char)data_[i] << " ";
        }
        cout << endl;
    }

    int Peek() { return data_[count_ - 1]; }
    bool IsEmpty() { if (count_ == 0) return true; else return false; }
    bool IsFull() { if (count_ == size_) return true; else return false; }

private:
    int size_; // 총 개수
    int* data_; // 배열 포인터
    int count_; // 현재 스택 안의 요소 개수
};

// 연산자 우선순위 판별 함수
int GetPriority(char op)
{
    if (op == '*' || op == '/') return 2; // 곱셈, 나눗셈이 1등
    if (op == '+' || op == '-') return 1; // 덧셈, 뺄셈은 2등
    return 0; // 그 외(괄호 등)
}

int main()
{
    String str; // str 객체 생성
    cin >> str;

    Stack s(100);

    for (int i = 0; i < str.GetLen(); i++)
    {
        char ch = str[i];
        
        // 1. 피연산자(알파벳 대문자)인 경우
        if (isupper(ch))
        {
            cout << ch;
        }
        // 2. 연산자(+, -, *, /, (, ))인 경우
        else if (ch == '(')
        {
            s.Push(ch);
        }
        else if (ch == ')') // 닫는 괄호는 여는 괄호를 만날 때까지 모두 Pop
        {
            while (!s.IsEmpty() && s.Peek() != '(')
            {
                cout << (char)s.Pop();
            }
            s.Pop(); // 마지막 남은 '('를 스택에서 제거
        }
        else // 일반 연산자 (+, -, *, /)
        {
            while (!s.IsEmpty() && GetPriority(s.Peek()) >= GetPriority(ch))
            {
                cout << (char)s.Pop(); // 스택에서 꺼내서 출력
            }
            s.Push(ch); // 현재 연산자를 스택에 삽입
        }
    }

    // 마지막에 스택에 남은 연산자들을 모두 꺼냄
    while (!s.IsEmpty())
    {
        cout << (char)s.Pop();
    }
    cout << endl;

    return 0;
}