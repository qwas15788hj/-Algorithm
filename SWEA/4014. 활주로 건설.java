import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_4014_활주로건설 {
	
	static int n, x;
	static int map[][], map2[][];
	static int answer;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<t+1; tc++) {
			
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			x = Integer.parseInt(st.nextToken());
			map = new int[n][n];
			map2 = new int[n][n];
			
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map2[j][i] = map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			sb.append("#"+tc+" "+process()).append("\n");
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
	public static int process() {
		int count = 0;
		for(int i=0; i<n; i++) {
			if(makeRoad(map[i])) count++; //수평 활주로 건설 체크
			if(makeRoad(map2[i])) count++; //수직 활주로 건설 체크
		}
		return count;
	}
	
	//해당 지형 정보로 활주로 건설이 가능하면 true, 불가능하면 false 리턴
	public static boolean makeRoad(int[] road) {
		
		int beforeHeight = road[0], size = 0;
		int j = 0;
		
		while(j<n) {
			
			if(beforeHeight == road[j]) { //동일 높이
				size++;
				j++;
			} else if(beforeHeight+1 == road[j]) { //이전높이보다 1높음: 오르막 경사로 설치 체크
				if(size < x) return false; //X길이 미만이면 활주로 건설 불가
				
				beforeHeight++;
				size = 1;
				j++;
			} else if(beforeHeight-1 == road[j]) { //이전 높이보다 1 작음
				int count = 0;
				for(int k=j; k<n; k++) {
					if(road[k] != beforeHeight-1) return false;
					
					if(++count == x) break;
				}
				
				if(count < x) return false;
				
				beforeHeight--;
				j += x;
				size = 0;
				
			} else { //높이가 2이상 차이
				return false;
			}
			
		}
		
		return true;
	}
	
}//class
