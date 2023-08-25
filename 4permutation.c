#include <stdio.h>
void permute(char *str, int l, int r) {
  if (l == r) {
    printf("%s\n", str);
  } else {
    for (int i = l; i <= r; i++) {
      swap(&str[l], &str[i]);
      permute(str, l + 1, r);
      swap(&str[l], &str[i]);
    }
  }
}
void swap(char *a, char *b) {
  char temp = *a;
  *a = *b;
  *b = temp;
}
int main() {
  char str[] = "abcd";
  int n;
  printf("The permutations of string are:\n");
  n = strlen(str);
  permute(str, 0, n - 1);
  return 0;
}
