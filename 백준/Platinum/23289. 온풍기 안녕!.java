import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int r, c, k, w;
	static int[][] arr;
	static ArrayList<int[]> air; //온풍기 저장
	static ArrayList<int[]> wall; //벽
	static ArrayList<int[]> check; //체크해야하는 칸 저장
	static int choco;
	static int[] dx = {0, 0, 0, -1, 1};
	static int[] dy = {0, 1, -1, 0, 0}; //벽과 같은 방향 => 오, 왼, 위, 아래
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[r][c];
		air = new ArrayList<>();
		wall = new ArrayList<>();
		check = new ArrayList<>();
		for(int i=0; i<r; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<c; j++) {
				int hot = Integer.parseInt(st.nextToken());
				if(hot==1) air.add(new int[] {i, j, 1});
				else if(hot==2) air.add(new int[] {i, j, 2});
				else if(hot==3) air.add(new int[] {i, j, 3});
				else if(hot==4) air.add(new int[] {i, j, 4});
				else if(hot==5) check.add(new int[] {i, j});
			}
		}
		w = Integer.parseInt(br.readLine());
		for(int i=0; i<w; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken())-1;
			int y = Integer.parseInt(st.nextToken())-1;
			int t = Integer.parseInt(st.nextToken());
			if(t==0) {
				wall.add(new int[] {x, y, 3});
				wall.add(new int[] {x-1, y, 4});
			} else if(t==1) {
				wall.add(new int[] {x, y, 1});
				wall.add(new int[] {x, y+1, 2});
			}
		}
		
		choco = 0;
		
		
		for(int tc=0; tc<101; tc++) {
		
			//1. 집에 있는 모든 온풍기 가동
			for(int i=0; i<air.size(); i++) {
				if(air.get(i)[2]==1) act_right(air.get(i)[0], air.get(i)[1]);
				else if(air.get(i)[2]==2) act_left(air.get(i)[0], air.get(i)[1]);
				else if(air.get(i)[2]==3) act_up(air.get(i)[0], air.get(i)[1]);
				else if(air.get(i)[2]==4) act_down(air.get(i)[0], air.get(i)[1]);
			}
			
			//2. 온도 조절
			spread();
			
			//3. 온도 1이상인 바깥 1씩 감소
			for(int i=1; i<r-1; i++) { //가운데 +1
				for(int j=1; j<c-1; j++) {
					arr[i][j] += 1;
				}
			}
			
			for(int i=0; i<r; i++) { //전부 -1
				for(int j=0; j<c; j++) {
					if(arr[i][j]>0) {
						arr[i][j] -= 1;
					}
				}
			}
			
			
			//4. 초콜릿 먹는다
			choco += 1;
			
			//5. 조사하는 칸 온도k이상 판별
			boolean hit_check = true;
			for(int i=0; i<check.size(); i++) {
				if(arr[check.get(i)[0]][check.get(i)[1]] < k) {
					hit_check = false;
				}
			}
			
			if(hit_check) break;
			
		}
		
		System.out.println(choco);
		
	}//main
	
	
	//온도 조절 퍼트리기
	public static void spread() {
		int[][] SubArr = new int[r][c];
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				int x = i;
				int y = j;
				int nx = 0;
				int ny = 0;
				for(int k=1; k<5; k++) {
					nx = x+dx[k];
					ny = y+dy[k];
					boolean flag = true;
					//그 방향에 벽이 있다면 무시
					for(int z=0; z<wall.size(); z++) {
						if(wall.get(z)[0]==x && wall.get(z)[1]==y && wall.get(z)[2]==k) {
							flag = false;
						}
					}
					
					if(flag && nx>=0 && nx<r && ny>=0 && ny<c && arr[x][y] > arr[nx][ny]) { //범위 안에 있고, 온도도 낮은 온도 찾으면
						int diff = (arr[x][y]-arr[nx][ny])/4;
						SubArr[x][y] -= diff;
						SubArr[nx][ny] += diff;
					}
				}
			}
		}
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j] += SubArr[i][j];
			}
		}
		
		
	}//spread
	
	
	//오른쪽으로 가는 온풍기 확인
	public static void act_right(int x, int y) {
		int[][] SubArr = new int[r][c];
		
		Queue<int[]> queue = new LinkedList<>();
		boolean flag = true;
		for(int i=0; i<wall.size(); i++) { //벽 돌면서
			if(wall.get(i)[0]==x && wall.get(i)[1]==y && wall.get(i)[2]==1) { //온풍기 위치와 같고 오른쪽으로 벽이면
				flag = false;
			}
		}
		
		if(!flag) return;
		
		queue.add(new int[] {x, y+1});
		SubArr[x][y+1] = 5;
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll();
			int nx = temp[0];
			int ny = temp[1];
			int mx = 0;
			int my = 0;
			if(SubArr[nx][ny]==1) break;
			
			//오른쪽 위 확인
			mx = nx-1;
			my = ny+1;
			boolean checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //오른쪽 위 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==3) { //벽중에 위로 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx-1 && wall.get(i)[1]==ny && wall.get(i)[2]==1) { //벽중에 오른쪽으로 막히고 x-1, y면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//오른쪽 확인
			mx = nx;
			my = ny+1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //오른쪽 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==1) { //벽중에 오른쪽 막히고 같은 곳이면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//오른쪽 아래 확인
			mx = nx+1;
			my = ny+1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //오른쪽 아래 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==4) { //벽중에 아래 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx+1 && wall.get(i)[1]==ny && wall.get(i)[2]==1) { //벽중에 오른쪽으로 막히고 x+1, y면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			
		}//while(queue)
		
//		for(int i=0; i<r; i++) {
//			System.out.println(Arrays.toString(SubArr[i]));
//		}
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j] += SubArr[i][j];
			}
		}
		
	}//act_right
	
	
	//아래로가는 온풍기 확인
	public static void act_left(int x, int y) {
		int[][] SubArr = new int[r][c];
		
		Queue<int[]> queue = new LinkedList<>();
		boolean flag = true;
		for(int i=0; i<wall.size(); i++) { //벽 돌면서
			if(wall.get(i)[0]==x && wall.get(i)[1]==y && wall.get(i)[2]==2) { //온풍기 위치와 같고 왼쪽으로 벽이면
				flag = false;
			}
		}
		
		if(!flag) return;
		
		queue.add(new int[] {x, y-1});
		SubArr[x][y-1] = 5;
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll();
			int nx = temp[0];
			int ny = temp[1];
			int mx = 0;
			int my = 0;
			if(SubArr[nx][ny]==1) break;
			
			//왼쪽 위 확인
			mx = nx-1;
			my = ny-1;
			boolean checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //왼쪽 위 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==3) { //벽중에 위로 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx-1 && wall.get(i)[1]==ny && wall.get(i)[2]==2) { //벽중에 왼쪽으로 막히고 x-1, y면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//왼쪽 확인
			mx = nx;
			my = ny-1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //왼쪽 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==2) { //벽중에 왼쪽 막히고 같은 곳이면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//왼쪽 아래 확인
			mx = nx+1;
			my = ny-1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //왼쪽 아래 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==4) { //벽중에 아래 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx+1 && wall.get(i)[1]==ny && wall.get(i)[2]==2) { //벽중에 왼쪽으로 막히고 x+1, y면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			
		}//while(queue)
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j] += SubArr[i][j];
			}
		}
		
	}
	
	
	//위로가는 온풍기 확인
	public static void act_up(int x, int y) {
		int[][] SubArr = new int[r][c];
		
		Queue<int[]> queue = new LinkedList<>();
		boolean flag = true;
		for(int i=0; i<wall.size(); i++) { //벽 돌면서
			if(wall.get(i)[0]==x && wall.get(i)[1]==y && wall.get(i)[2]==3) { //온풍기 위치와 같고 위쪽으로 벽이면
				flag = false;
			}
		}
		
		if(!flag) return;
		
		queue.add(new int[] {x-1, y});
		SubArr[x-1][y] = 5;
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll();
			int nx = temp[0];
			int ny = temp[1];
			int mx = 0;
			int my = 0;
			if(SubArr[nx][ny]==1) break;
			
			//왼쪽 위 확인
			mx = nx-1;
			my = ny-1;
			boolean checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //왼쪽 위 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==2) { //벽중에 왼쪽으로 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny-1 && wall.get(i)[2]==3) { //벽중에 위쪽으로 막히고 x, y-1면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//위쪽 확인
			mx = nx-1;
			my = ny;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //위쪽 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==3) { //벽중에 위쪽 막히고 같은 곳이면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//오른쪽 위 확인
			mx = nx-1;
			my = ny+1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //오른쪽 위 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==1) { //벽중에 오른쪽 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny+1 && wall.get(i)[2]==3) { //벽중에 위쪽으로 막히고 x, y+1면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			
		}//while(queue)
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j] += SubArr[i][j];
			}
		}
		
	}
	
	//아래로 가는 온풍기 확인
	public static void act_down(int x, int y) {
		int[][] SubArr = new int[r][c];
		
		Queue<int[]> queue = new LinkedList<>();
		boolean flag = true;
		for(int i=0; i<wall.size(); i++) { //벽 돌면서
			if(wall.get(i)[0]==x && wall.get(i)[1]==y && wall.get(i)[2]==4) { //온풍기 위치와 같고 아래쪽으로 벽이면
				flag = false;
			}
		}
		
		if(!flag) return;
		
		queue.add(new int[] {x+1, y});
		SubArr[x+1][y] = 5;
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll();
			int nx = temp[0];
			int ny = temp[1];
			int mx = 0;
			int my = 0;
			if(SubArr[nx][ny]==1) break;
			
			//왼쪽 아래 확인
			mx = nx+1;
			my = ny-1;
			boolean checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //왼쪽 아래 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==2) { //벽중에 왼쪽으로 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny-1 && wall.get(i)[2]==4) { //벽중에 아래쪽으로 막히고 x, y-1면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//아래쪽 확인
			mx = nx+1;
			my = ny;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //아래쪽 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==4) { //벽중에 아래쪽 막히고 같은 곳이면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			//오른쪽 아래 확인
			mx = nx+1;
			my = ny+1;
			checked = true;
			if(mx<0 || mx>=r || my<0 || my>=c) checked = false;
			if(mx>=0 && mx<r && my>=0 && my<c && SubArr[mx][my]==0) { //오른쪽 아래 확인
				for(int i=0; i<wall.size(); i++) {
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny && wall.get(i)[2]==1) { //벽중에 오른쪽 막히고 같은 곳이면
						checked = false;
					}
					if(wall.get(i)[0]==nx && wall.get(i)[1]==ny+1 && wall.get(i)[2]==4) { //벽중에 아래쪽으로 막히고 x, y+1면
						checked = false;
					}
				}
			}
			
			if(checked) {
				SubArr[mx][my] = SubArr[nx][ny]-1;
				queue.offer(new int[] {mx, my});
			}
			
			
		}//while(queue)
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j] += SubArr[i][j];
			}
		}
		
	}
	
}//class
