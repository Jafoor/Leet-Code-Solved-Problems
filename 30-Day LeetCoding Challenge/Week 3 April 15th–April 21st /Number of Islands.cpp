class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
        int x = grid.size();
        int y = 0;
        if(x>0)
            y = grid[0].size();
        int ans = 0;
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(grid[i][j] == '1')
                {
                    ans += 1;
                    findisland(i,j,grid);
                }
            }
        }
        return ans;
    }
private:
    void findisland(int a, int b, vector<vector<char>>& grid) {
        
        int x = grid.size();
        int y = grid[0].size();
        
        if(a<0 or b<0 or a>=x or b>=y or grid[a][b] != '1')
            return;
        
        int xaxis[] = {-1, 0, 0, 1};
        int yaxis[] = {0, 1, -1, 0};
        
        grid[a][b] = '0';
        
        for(int i=0; i< 4; i++){
            findisland(a+xaxis[i], b+yaxis[i], grid);
        }
        
    }
    
};