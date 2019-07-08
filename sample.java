import java.util.*;
public class sample {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		HashMap<Integer, Integer> map=new HashMap<>();
		int a1=scn.nextInt();
		int[] a =new int[a1];
		int[] b=new int[a1];
		for(int i=0;i<a1;i++){
		  a[i]=scn.nextInt(); 
		}
		for(int j=0;j<a1;j++) {
			b[j]=scn.nextInt();
		}
		for(int i=0;i<a1;i++) {
			map.put(b[i],a[i]);
		}
		TreeMap<Integer, Integer> tree =new TreeMap<>(map);
		for(Map.Entry m:tree.entrySet()) {
			System.out.print(m.getValue()+" ");
		}

	}

}
