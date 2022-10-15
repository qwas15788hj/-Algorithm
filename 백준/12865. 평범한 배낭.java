package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_12865_평범한배낭 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[] w = new int[n+1];
		int[] v = new int[n+1];
		for(int i=1; i<n+1; i++) {
			st = new StringTokenizer(br.readLine());
			w[i] = Integer.parseInt(st.nextToken());
			v[i] = Integer.parseInt(st.nextToken());
		}
		int[][] dp = new int[n+1][k+1];
		
		for(int i=1; i<n+1; i++) {
			int weight = w[i];
			int value = v[i];
			for(int j=1; j<k+1; j++) {
				if(weight > j) { //넣을무게 > 현재무게 => 못넣음
					dp[i][j] = dp[i-1][j];
				} else {
					dp[i][j] = Math.max(value+dp[i-1][j-weight], dp[i-1][j]);
				}
				
			}
		}
		
//		for(int i=0; i<n+1; i++) {
//			System.out.println(Arrays.toString(dp[i]));
//		}
		System.out.println(dp[n][k]);
		
	}
	
}
