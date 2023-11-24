import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
class slip16b
{
static String[] str=new String[5];
static Scanner sc=new Scanner(System.in);
static ArrayList<String>list=new ArrayList<String>();
public static void main(String args[])
{
for(int i=0;i<str.length;i++)
{
System.out.print("please insert employee name of indexof["+i+"] :");
str[i]=sc.next();
list.add(str[i]);
}
Collections.sort(list);
System.out.println(list);
}
}