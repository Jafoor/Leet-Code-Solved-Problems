'''
Sorting O(nlogn) time, space O(1)

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        if(n == 1)return nums[0];
        sort(nums.begin(), nums.end());
        
        //edge case: when the single no is at one of any end of the cluster
        if(nums[0] != nums[1])return nums[0];
        if(nums[n-1] != nums[n-2])return nums[n-1];
        
        // when the single no is in the middle of the cluster
        int i = 1;
        while(i < n){
            if(nums[i] != nums[i-1]){
                return nums[i-1];
            }
            i += 3;
        }
        return -1;
    }
};
2. Hashtable O(n) space and time

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int>m;
        for(int num: nums)m[num]++;
        for(auto i: m){
            if(i.second == 1)return i.first;
        }
        return -1;
    }
};
3. Taking the count at each bit position, time O(n) space O(1)

Approach: Just take the sum of each ofthe 32 bit position and keep adding the sum%3 in the result. If the sum is divisible is 3, then the ith bit in the single no is 0, else 1.

Example : Let us consider the example array {5, 5, 5, 8}. The 101, 101, 101, 1000

Sum of first bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of second bits%3 = (0 + 0 + 0 + 0)%0 = 0;
Sum of third bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of fourth bits%3 = (1)%3 = 1;
Hence number which appears once is 1000

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < 32; ++i){
            int bitCount = 0;
            for(int num: nums){
                bitCount += ((num >> i)&1); // for first bit, right shift num by 0 and for 2nd bit, right shift num by 1 and so on...
            }
            if(bitCount%3){
                result |= (1<<i); // left shift 1 by i bit starting from 0
            }
        }
        return result;
    }
};

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for i in range(32):
            bitcount = 0
            for num in nums:
                bitcount += ((num >> i)&1)
           
            if i == 31 and bitcount%3:
                result -= (1<<i)
            elif bitcount%3 != 0:
                result |= (1<<i) 
                
        return result

'''
4. Smart bit manipulation time O(n) space O(1)
Approach : ones will contain the no appearing once, and twos will contain the no appearing twice.
Example : 2, 2, 5, 2

2: ones = 2, twos = 0 (ones will get 2, and twos won't get 2 since ones had 2 already)
2: ones = 0, twos = 2 (ones will get 2 but ones = 2^2 = 0, hence twos will get 2)
5: ones = 5, twos = 2 (ones will get 5 and twos will not get 5 since ones had 5 already)
2: ones = 5, twos = 0 (ones won't get 2, since twos already had 2. And twos will get 2 but it had already 2. Hence twos = 2^2 = 0)
Hence the no which appears thrice is not in any of the two. ones will have the final answer. And twos will be 0 finally. Since all the no either appears thrice or once.

class Solution {
public:    
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
         for(int num: nums){
             ones = (ones ^ num) & (~twos);
             twos = (twos ^ num) & (~ones);
         }
        return ones;
    }
};
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Let the numbers be x,y,z,.....
        # require sum should be 3x+3y+3z
        # original sum = 3x+3y+z
        # Sub req sum from original sum
        # (3x+3y+3z) - (3x+3y-z) = 2z
        # div the ans by 2 = 2z/2 = z--> our ans

        return (3 * sum(set(nums)) - sum(nums)) // 2

#Another Solution

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count = Counter(nums)
        for c in count:
            if count[c] == 1:
                return c







