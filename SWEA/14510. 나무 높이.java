import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_14510_나무높이 {
	
	static int n, time;
	static int[] tree;
	static ArrayList<Integer> arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<t+1; tc++) {
			n = Integer.parseInt(br.readLine());
			tree = new int[n];
			st = new StringTokenizer(br.readLine());
			int max = 0;
			for(int i=0; i<n; i++) {
				int height = Integer.parseInt(st.nextToken());
				tree[i] = height;
				max = Math.max(max, height);
			}
			
			arr = new ArrayList<>();
			for(int i=0; i<n; i++) {
				if(tree[i] < max) {
					arr.add(max-tree[i]);
				}
			}
			
			time = 0;
			while(true) {
				
				if(arr.size()==0) break;
				time+=1;
				
				if(time%2!=0) { //홀 수 일때
					if(arr.size()==1) { //크기가 1인데
						if(arr.get(0)==2) { //길이가 2면
							continue; //무시
						} else { //길이가 2가 아니면
							arr.set(0, arr.get(0)-1);
							if(arr.get(0)==0) arr.remove(0);
						}
					} else { //크기가 1이 아니면
						boolean check = false; //줄였는지 판단
						for(int i=0; i<arr.size(); i++) {
							if(arr.get(i)%2==1) { //홀수 줄이기
								arr.set(i, arr.get(i)-1);
								if(arr.get(i)==0) arr.remove(i);
								check = true;
								break;
							}
						}
						if(!check) { //못 줄였다면, 홀 수 없음
							arr.set(0, arr.get(0)-1); //아무거나 줄임
							if(arr.get(0)==0) arr.remove(0);
						}
						
					}
					
				} else { //짝수 줄이기
					for(int i=0; i<arr.size(); i++) {
						if(arr.get(i) > 1) {
							arr.set(i, arr.get(i)-2);
							if(arr.get(i)==0) arr.remove(i);
							break;
						}
					}
					
				}
				
			}
			
			sb.append("#"+tc+" "+time).append("\n");
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
}//class
