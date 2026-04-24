#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void)
{
    stack<int> st;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "push")
        {
            int s;
            cin >> s;
            st.push(s);
        }
        else if (cmd == "pop")
        {
            if (st.empty())
                cout << "-1" << endl;
            else
            {
                cout << st.top() << endl; 
                st.pop();
            }     
        }
        else if (cmd == "size")
        {
            cout << st.size() << endl;
        }
        else if (cmd == "empty")
        {
            if (st.empty())
                cout << "1" << endl;
            else
                cout << "0" << endl;
        }
        else if (cmd == "top")
        {
            if (st.empty())
                cout << "-1" << endl;
            else
                cout << st.top() << endl;
        }
    }
}