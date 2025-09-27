package org.example;

import java.util.ArrayList;
import java.util.List;

public class Test1 {

    private List<int[]> theList;

    public Test1(List<int[]> theList){
        this.theList = theList;
    }

    public List<int[]> getThem(){
        List<int[]> list1 = new ArrayList<int[]>();
        for(int[] x : theList){
            if(x[0] == 4) {
                list1.add(x);

            }
        }
        return list1;
    }

}
