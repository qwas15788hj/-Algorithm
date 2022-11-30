package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_2294_동전2 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] coin = new int[n];
		for(int i=0; i<n; i++) {
			coin[i] = Integer.parseInt(br.readLine());
		}
		
		int INF = 1000000;
		int[] money = new int[k+1];
		for(int i=1; i<k+1; i++) {
			int min = INF;
			for(int j=0; j<n; j++) {
				if(i>=coin[j]) min = Math.min(min, money[i-coin[j]]+1);
			}
			money[i] = min;
		}
		
		if(money[k]==INF) {
			System.out.println(-1);
		} else {
			System.out.println(money[k]);
		}
		
	}
	
}
