#include <stdio.h>

int get_gcd(int x, int y) {
    while(y>0) {
        int z = x;
        x = y;
        y = z % y; 
    }
    return x;
}

int get_lcm(int x, int y) {
    return x*y/get_gcd(x,y);
}

int main() {
    int t, m, n, x, y;
    scanf("%d", &t);

    while(t--) {
        scanf("%d %d %d %d", &m, &n, &x, &y);

        for(int i = 0; i <= 60/m; i++) {
            int l = (m * i) + x;
            int a = x;
            int b = l % n;

            if(a==x && b==y) {
                printf("%d", l);
            }
        }
    }

    return 0;
}