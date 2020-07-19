class Solution {
public:
    int numTrees(int n) {
    
    unsigned long int catalan[n+3]; 
  
    
    catalan[0] = catalan[1] = 1; 
  
    
    for (int i=2; i<=n; i++) 
    { 
        catalan[i] = 0; 
        for (int j=0; j<i; j++) {
            catalan[i] += catalan[j] * catalan[i-j-1]; 
            //cout<<catalan[j]<<' '<<catalan[i-j-1]<<' ';
        }
        //cout<<endl;
    } 
  
    return catalan[n]; 

    }
};