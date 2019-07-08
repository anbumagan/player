import java.util.*;
public class Main
{
	public static void main(String args[]) {
		Scanner s=new Scanner(System.in);
		int a=s.nextInt();
		int[] a1=new int[a];
		for(int i=0;i<a;i++){
		    a1[i]=s.nextInt();
		}
		s.close();
		for(int i=1;i<a;i++){
		    if(a1[i]%a1[i-1]==0){
		        System.out.print(a1[i]+" ");
		    }
		}
	}
}
