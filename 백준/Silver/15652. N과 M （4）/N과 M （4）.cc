#include <iostream>
using namespace std;

int n, m;
int ary[10];

void dfs(int depth, int start)
{
    if (depth == m)
    {
        for (int i = 0; i < m; i++)
            cout << ary[i] << " ";
        cout << endl;
        return;
    }

    for (int i = start; i <= n; i++)
    {
        ary[depth] = i;
        dfs(depth + 1, i);
    }
}

int main()
{
    cin >> n >> m;
    dfs(0, 1);
}