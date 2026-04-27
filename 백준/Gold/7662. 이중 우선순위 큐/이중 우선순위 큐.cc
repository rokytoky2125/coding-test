#include <iostream>
#include <set>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        multiset<int> ms;
        int k;
        cin >> k;
        for (int j = 0; j < k; j++)
        {
            char s;
            int n;
            cin >> s >> n;
            if (s == 'I')
            {
                ms.insert(n);
            }
            else if (s == 'D' && n == 1)
            {
                if (ms.empty())
                    continue;
                ms.erase(prev(ms.end())); // 최댓값 삭제
            }
            else if (s == 'D' && n == -1)
            {
                if (ms.empty())
                    continue;
                ms.erase(ms.begin()); // 최솟값 삭제
            }
        }
        if (ms.empty())
            cout << "EMPTY" << endl;
        else
        {
            cout << *prev(ms.end()) << " " << *ms.begin() << endl; //최댓값, 최솟값 출력
        }
    }
}