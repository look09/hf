import java.util.Random;
public class Search {
    public static void main(String[] args) {
		int[] nList = new int[]{50,100,150,200,250,300};
		Random rand = new Random();
		for(int j = 0;j<nList.length;j++){
			int N = nList[j];
			System.out.println("Trials for N = " + nList[j]);
			for(int k = 0;k<10;k++){
				double[] dataList = new double[N];
				for(int i = 0;i<N;i++) //load array
					dataList[i] = rand.nextInt(N-1);
				int target = rand.nextInt(N-1);
				int itNum = search(dataList, target);
				if(itNum == -1) itNum = N+1;
				System.out.println("Trial #" + (k+1) + ", target = " + 
					target + ", " + itNum + " iterations");
			}
		}
    }
	public static int search(double[] data, double target){
		int i;
		for(i = 0;i<data.length;i++){
			if(data[i] == target)
				return i;
		}
		return -1;
	}
}
