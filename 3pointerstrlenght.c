#include <stdio.h>
int calculateLength(char *str) {
  int length = 0;
  while (*str != '\0') {
    length++;
    str++;
  }
  return length;
}
int main() {
  char str[20];
  int len;
  printf("Enter a string: ");
  scanf("%s", str);
  len = calculateLength(str);
  printf("The length of the string is %d\n", len);
  return 0;
}

