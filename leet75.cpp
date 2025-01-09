#include<string>
#include<iostream>
#include <numeric>


using namespace std;

string gcdOfStrings(string str1, string str2) {
        int start=0; 
        int len = 1;
        int gcd = std::gcd( str1.length(), str2.length()); 
        
        while(len <=gcd){
            if ( str1.compare(0,len,str2,0,len) == 0)
            {
                len++;
            }
            else{
                break;
            }
        }
        // check the remaining length
        if(len==1)
        {
            return "";
        }

        string prefix = str1.substr(start,len-1);

        int n = str1.length()/(len-1); 
        int m = prefix.length(); 
        for(int i=1; i < str1.length()/(len-1) ; i++)
        {
            if(prefix.compare(0,m, str1, i*m,m) !=0){
                return "";
            }
        }

        for(int i=1; i < str2.length()/(len-1) ; i++)
        {
            if(prefix.compare(0,m, str2, i*m, m) !=0){
                return "";
            }
        }
        return prefix; 
}

int main()
{
    std::cout << gcdOfStrings("ABCABC","ABC") <<std::endl;
    return 0;
}