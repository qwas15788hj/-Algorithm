import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_5643_키순서 {
	
	static int n, m;
	static ArrayList<Integer>[] arr;
	static ArrayList<Integer>[] arr_reverse;
	static boolean[] visited;
	static int count, answer;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<t+1; tc++) {
			n = Integer.parseInt(br.readLine());
			arr = new ArrayList[n+1];
			arr_reverse = new ArrayList[n+1];
			for(int i=0; i<n+1; i++) {
				arr[i] = new ArrayList<>();
				arr_reverse[i] = new ArrayList<>();
			}
			
			m = Integer.parseInt(br.readLine());
			for(int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				arr[a].add(b);
				arr_reverse[b].add(a);
			}
			
			answer = 0;
			for(int i=1; i<n+1; i++) {
				count = 0;
				visited = new boolean[n+1];
				bfs(i);
				bfs_reverse(i);
				if(count==n-1) answer+=1;
			}
			
			sb.append("#"+tc+" "+answer).append("\n");
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
	public static void bfs(int x) {
		Queue<Integer> queue = new LinkedList<Integer>();
		visited[x] = true;
		queue.offer(x);
		while(!queue.isEmpty()) {
			int nx = queue.poll();
			int size = arr[nx].size();
			for(int i=0; i<size; i++) {
				if(!visited[arr[nx].get(i)]) {
					queue.offer(arr[nx].get(i));
					visited[arr[nx].get(i)] = true;
					count += 1;
				}
			}
		}
		
	}
	
	public static void bfs_reverse(int x) {
		Queue<Integer> queue = new LinkedList<Integer>();
		visited[x] = true;
		queue.offer(x);
		while(!queue.isEmpty()) {
			int nx = queue.poll();
			int size = arr_reverse[nx].size();
			for(int i=0; i<size; i++) {
				if(!visited[arr_reverse[nx].get(i)]) {
					queue.offer(arr_reverse[nx].get(i));
					visited[arr_reverse[nx].get(i)] = true;
					count += 1;
				}
			}
		}
		
	}
	
}//class
