#include <stdio.h>
#include <vector>
#include <stack>

#define MAX 100001

int n, m;
int ans[MAX];
std::vector<int> adj[MAX];

int dfs(int v)
{
    bool visited[MAX] = {false};
    int cnt = 0;

    std::stack<int> stack;
    stack.push(v);

    while (!stack.empty())
    {
        int v = stack.top();
        stack.pop();
        visited[v] = true;
        cnt += 1;

        for (int nv : adj[v])
        {
            if (!visited[nv])
            {
                stack.push(nv);
            }
        }
    }

    return cnt;
}

int main()
{
    scanf("%d %d", &n, &m);

    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[b].push_back(a);
    }

    int maxCnt = 0;
    for (int i = 1; i <= n; i++)
    {
        ans[i] = dfs(i);
        maxCnt = ans[i] > maxCnt ? ans[i] : maxCnt;
    }

    for (int i = 1; i <= n; i++)
    {
        if (ans[i] == maxCnt)
        {
            printf("%d ", i);
        }
    }
}