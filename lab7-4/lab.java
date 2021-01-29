import java.util.*;
class Pair {
	int key, value;
	Pair(int k, int v) { key = k; value = v; }
}
public class lab {
	static int INF = 1000000;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[][] adjMat = new int[n+1][n+1];

		int k = scan.nextInt();
		for(int i = 0; i < k; i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			int w = scan.nextInt();
			adjMat[a][b] = w;
			adjMat[b][a] = w;
		}

		Queue<Pair> que = new PriorityQueue(n, 
			new Comparator<Pair>() {
				public int compare(Pair x, Pair y) { return x.key - y.key; }
		});
		boolean[] visited = new boolean[n+1];
		int[] values = new int[n+1];
		for(int i = 1; i <= n; i++) values[i] = INF;
		values[1] = 0;
		que.add(new Pair(0, 1));
		int sum = 0;
		while(!que.isEmpty()) {
			Pair r = que.remove();
			if(visited[r.value]) continue;
			sum += values[r.value];
			visited[r.value] = true;
			for(int i = 1; i <= n; i++) {
				if(adjMat[r.value][i] == 0 || visited[i]) continue;
				if(values[i] > adjMat[r.value][i]) {
					values[i] = adjMat[r.value][i];
					que.add(new Pair(values[i], i));
				}
			}
		}
		System.out.println(sum);
	}
}
