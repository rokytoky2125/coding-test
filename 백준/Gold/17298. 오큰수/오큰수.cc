#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> ary(n);
    vector<int> result(n, -1); // 기본값: -1

    for (int i = 0; i < n; i++)
    {
        cin >> ary[i];
    }
    
    stack<int> st; // 인덱스 저장

    for (int i = 0; i < n; i++)
    {
        while (!st.empty() && ary[i] > ary[st.top()])
        {
            result[st.top()] = ary[i];
            st.pop();
        }
        st.push(i);
    }

    for (int i = 0; i < n; i++)
        cout << result[i] << " ";
}