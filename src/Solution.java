
import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        scan.nextLine();
        for(int i = 0; i<T; i++){
            String N = scan.nextLine();
            StringBuilder sbB = new StringBuilder();
            StringBuilder sbA = new StringBuilder();
            for(int j = 0; j<N.length(); j++){
                char dN = N.charAt(j);
                if(dN == '4'){
                    sbB.append('1');
                    sbA.append('3');
                }
                else{
                    sbB.append('0');
                    sbA.append(N.charAt(j));
                }

            }


            String resA = sbA.toString();
            String resB = sbB.toString();
            boolean zeros = true;
            for (int k = resB.length()-1; k>=0; k--){
                char c = resB.charAt(k);
                if(c=='0' && zeros && resB.length()>1){
                    resB = resB.substring(1,resB.length());
                }else{
                    zeros = true;
                }
            }
            System.out.println("Case #" + (i+1) +":"+ resA + " " + resB);


        }
    }
}
