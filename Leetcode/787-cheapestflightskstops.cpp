#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <limits.h>

using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        queue< vector<int> > q;
        vector<vector< pair<int,int> >> adj_list;
        vector<int> flight;
        int from;
        pair<int,int> dest;
        
        // Create Adjacency List
        for(int i = 0; i < flights.size(); i++) {
            adj_list.push_back({});
        }
        for(int i = 0; i < flights.size(); i++) {
            flight = flights[i];
            from = flight[0];
            dest.first = flight[1];
            dest.second = flight[2];
            adj_list[from].push_back(dest);
        }
        
        int min_price = INT_MAX;
        vector<int> start = {src, 0, 0};
        vector<int> curr;
        q.push(start);
        int node, dist, price;
        // BFS keeping track of curr node, curr dist, curr price, min price
        while(!q.empty()) {
            curr = q.front();
            q.pop();
            node = curr[0];
            dist = curr[1];
            price = curr[2];

            if(dist > K) {
                continue;
            }
            if(node == dst) {
                min_price = min(min_price, price);
            }

            for(int i=0; i<adj_list[node].size(); i++) {
                dest = adj_list[node][i];
                q.push({dest.first, dist+1, price+dest.second});
            }
        }
        //Return min price to reach dest
        cout << min_price;
        return min_price;

    }
};