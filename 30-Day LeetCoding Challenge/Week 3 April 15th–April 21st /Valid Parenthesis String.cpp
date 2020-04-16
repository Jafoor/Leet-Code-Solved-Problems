class Solution {
public:
    bool checkValidString(string s) {
        
        stack<int> opn, ast;
        for (int i=0; i<s.length();i++)
        {
            if (s[i] == ')')
            {
                if(!opn.empty()){
                    opn.pop();
                }
                
                else if(!ast.empty()){
                    ast.pop();
                }
                else
                    return false;
            }
            else if(s[i]=='(')
                opn.push(i);
            else
                ast.push(i);
        }
        
        while( !opn.empty() and !ast.empty()){
            if(opn.top() > ast.top())
                return false;
            opn.pop();
            ast.pop();
        }
        
        return opn.empty();
    }
};