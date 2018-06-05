#include <stdio.h>
#include <math.h>

void hanoi(int n, int begin, int aux, int end) {
    if(n == 1) {
        printf("%d %d\n", begin, end);
        return;
    }

    hanoi(n-1, begin, end, aux);
    hanoi(1, begin, aux, end);
    hanoi(n-1, aux, begin, end);
}


int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);

    printf("%d\n", (int)pow(2, n)-1);

    hanoi(n, 1, 2, 3);

    return 0;
}
