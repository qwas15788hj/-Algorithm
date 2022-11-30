import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.StringTokenizer;

public class Main_15961_회전초밥 {
	
	static int n, d, k, c;
	static Map<Integer, Integer> select;
	static int[] sushi;
	static int answer;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		select = new HashMap<>();
		sushi = new int[n+k-1];
		answer = 0;
		for(int i=0; i<n; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}
		
		for(int i=n; i<n+k-1; i++) { //앞 스시 추가
			sushi[i] = sushi[i-n];
		}
		
		//초밥 시작
		int count = 0;
		for(int i=0; i<k; i++) { //시작 뽑기
			if(select.containsKey(sushi[i])) {
				select.put(sushi[i], select.get(sushi[i])+1);
			} else {
				select.put(sushi[i], 1);
			}
		}
		count = select.size();
		if(!select.containsKey(c)) {
			count += 1;
		}
		answer = count;
		
		
		int left = 0;
		int right = left+k;
		while(right<sushi.length) {
			count = 0;
			if(select.get(sushi[left])==1) {
				select.remove(sushi[left]);
			} else {
				select.put(sushi[left], select.get(sushi[left])-1);
			}
			
			if(select.containsKey(sushi[right])) {
				select.put(sushi[right], select.get(sushi[right])+1);
			} else {
				select.put(sushi[right], 1);
			}
			
			count = select.size();
			if(!select.containsKey(c)) {
				count += 1;
			}
			
			answer = Math.max(answer, count);
			left++;
			right++;
		}
		
		
		System.out.println(answer);
		
	}//main
	
}//class
