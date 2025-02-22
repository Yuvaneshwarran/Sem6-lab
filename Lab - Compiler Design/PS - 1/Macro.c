#include <stdio.h>
#define PI 3.14
#define AREA(r) (PI * r * r)

int main() {
    double radius = 5;
    printf("Area: %f\n", AREA(radius));
    return 0;
}
