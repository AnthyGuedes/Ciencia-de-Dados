package org.example;

import java.util.ArrayList;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.println("Exemplo ruim\n");
        List<int[]> data = new ArrayList<>();
        data.add(new int[]{4, 10});
        data.add(new int[]{2, 5});
        data.add(new int[]{4, 7});

        Test1 test = new Test1(data);
        List<int[]> result = test.getThem();

        for (int[] arr : result) {
            System.out.println(arr[0] + ", " + arr[1]);
        }

        System.out.println("\nExemplo Bom\n");
        List<int[]> board = new ArrayList<>();
        board.add(new int[]{1, 2});
        board.add(new int[]{-1, 3});
        board.add(new int[]{4, 5});
        board.add(new int[]{6, -1});
        board.add(new int[]{7, 8});

        Flag flag = new Flag(board);
        List<int[]> resulta = flag.getFlaggedCells();

        for (int[] cell : resulta) {
            System.out.println(cell[0] + ", " + cell[1]);
        }
    }
}
