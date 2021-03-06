#include <string.h>
#include <stdio.h>
#include <stdlib.h>
char * longestPalindrome(char * s)
{
    if(!s) return 0;
    int res[1000][1000] = {{0}};
    int len = strlen(s);
    int res_i = 0, res_j = 0;
    int i, j;
    char *palindrome = NULL;
    /*Str of len 1 is palindrome*/
    for(i = 0; i < len; i++)
       res[i][i] = 1; 

    /*Find if string of len 2 is palindrome*/
    for(i = 0; i < len-1; i++) {
        if(s[i] == s[i+1]) {
            res[i][i+1] = 2;
            res_j = i+1;
            res_i = i;
        }
    }
    
    /*Find if string of len > 2 is palindrome*/
    for(i = 0; i < len-2; i++){
        for(j = i+2; j < len; j++) {
            if((res[i+1][j-1] > 0) && s[i] == s[j]) {
                res[i][j] = j-i+1;
                if((res_j-res_i+1) < (j-i+1)) {
                    res_i = i; res_j = j;
                }
            }
        } 
    }

    for(i = 0; i < len; i++) {
        for(j = 0; j < len; j++) {
            printf("%d ", res[i][j]);
        }
        printf("\n");
    }
    palindrome = calloc(1, res_j-res_i+1);
    strncpy(palindrome, s+res_i, res_j-res_i+1);
    return palindrome;
}

int main()
{
    char *res = NULL;
    char *s = NULL;
    printf("Longest palindrome: %s\n", longestPalindrome(s));
    return 0;
}
