package leaky;

import java.util.Scanner;


public class leaky {
    
    
    public static void main(String[] args) {

           Scanner sc = new Scanner(System.in);
           int bcktsize, iter, rate, line, total = 0,temp;
            int[] pkt = new int[25];
            System.out.print("Enter the bucket size and output rate(both in MB):");
            bcktsize = sc.nextInt();
            rate = sc.nextInt();
            System.out.println("Enter the number of input lines");
            line = sc.nextInt();
            System.out.println("Enter input packet rate of " + line + " lines");
            for(int i = 0; i < line; i++) {
                pkt[i] = sc.nextInt();
            }
            System.out.println("Enter the number of iterations");
            iter = sc.nextInt();
            
            
            
            
            for(int i = 0; i < iter; i++) {
                System.out.println("\nIteration " + (i + 1));
                
                
                
                for(int j = 0; j < line; j++) {
                    total += pkt[j];
                    
                    System.out.println("\nInput from line " + (j + 1) + " with rate "+ pkt[j] + " is added to the bucket\nCurrent bucket size(Mb) is " + total);
               
                    if(total >= bcktsize) {
                    temp =total- bcktsize;
                    total = total-temp;
                    
                    System.out.println("\n"+ temp + " is removed from the bucket\nCurrent bucket size(Mb) is " + total);
                }
                
                
                
             
                
                                                }
                      
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                if(total <= rate) {
                            System.out.print("packet sent to outputline at rate " + total);
                            total = 0;
                            System.out.print("current bucket size is " + total);
                                            } else {
                                                    total -= rate;
                                                       System.out.println("\n---------------------------------");
                                                       System.out.println("\npacket sent to output line at rate " + rate + " \n Current bucket size(Mb)is " + total);
                                                    }
                                            }
                                            } 
 }
