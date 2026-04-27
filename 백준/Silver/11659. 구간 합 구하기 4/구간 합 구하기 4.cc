#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> ary(n + 1);
    vector<int> prefix(n + 1, 0);

    for (int i = 1; i <= n; i++)
    {
        cin >> ary[i];
        prefix[i] = prefix[i - 1] + ary[i];
    }

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;

        cout << prefix[b] - prefix[a - 1] << '\n';
    }
}