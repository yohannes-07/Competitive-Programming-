#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> graph;
    
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.push_back({u, v, w});
    }
    
    vector<int> distances(n + 1, 30000); 
    
    distances[1] = 0;
    
    for (int i = 0; i < n - 1; ++i) {
        for (const auto& edge : graph) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            
            if (distances[u] != 30000 && distances[u] + w < distances[v]) {
                distances[v] = distances[u] + w;
            }
        }
    }
    
    for (int i = 1; i <= n; ++i) {
        cout << distances[i];
        if (i < n) {
            cout << " ";
        }
    }
    
    cout << endl;
    
    return 0;
}
