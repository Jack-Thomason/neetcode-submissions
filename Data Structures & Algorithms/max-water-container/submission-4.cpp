class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximum = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (l < r){
            int length = r - l;
            int area = length * min(heights[l], heights[r]);

            if (area > maximum){
                maximum = area;
            }

            if (heights[l] < heights[r]){
                l++;
            } else{
                r--;
            }
        }
        return maximum;
    }
};
