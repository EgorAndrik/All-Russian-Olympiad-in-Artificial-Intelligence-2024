#include <iostream>
#include <string>
#include <vector>
#include <cmath>


using namespace std;


int main()
{
    string text;
    cin >> text;
    int n = text.size();
    
    int mx_len_sub_str = 1;
    
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if (text[i] == text[j])
                mx_len_sub_str = max(mx_len_sub_str, j - i + 1);
            if (mx_len_sub_str == n - i) break;
        }
        if (mx_len_sub_str == n - i) break;
    }
    
    cout << mx_len_sub_str;
}