class Solution {
public:
    string longestPalindrome(string s) {
        bool isPalin[1000][1000];
        // Initialize memory array
        for(int i=0; i<s.length(); i++)
            for(int j=0; j<s.length(); j++)
                isPalin[i][j] = false;

        // Fill up with relevant values
        string maxpalin; 
        int b, e;
        for(int k=1; k<=s.length(); k++) {
            for(int i=0; i+k-1 < s.length(); i++) {
                int j = i+k-1;
                if(k==1 || 
                   (k==2 && s[i]==s[j]) ||
                   (k>2 && s[i]==s[j] && isPalin[i+1][j-1])) {
                    isPalin[i][j] = true;
                    if (k > maxpalin.length()) {
                        maxpalin = s.substr(i, k);
                    }
                }
            }
        }
        return maxpalin;
    }
};