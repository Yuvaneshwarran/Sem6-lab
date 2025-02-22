1 #include <stdio.h>
2 #define PI 3.14
3 #define AREA(r) (PI * r * r)
4 
5 int main() {
6     double radius = 5;
7     printf("Area: %f\n", AREA(radius));
8     return 0;
9 }
