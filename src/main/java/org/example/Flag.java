package org.example;

import java.util.ArrayList;
import java.util.List;

public class Flag {

    private List<int[]> gameBoard;

    public Flag(List<int[]> gameBoard) {
        this.gameBoard = gameBoard;
    }

    public List<int[]> getFlaggedCells() {
        List<int[]> flaggedCells = new ArrayList<int[]>();

        for (int[] cell : gameBoard) {
            if (cell[0] != -1 && cell[1] != -1) { // cell[STATUS_VALUE] == FLAGGED
                flaggedCells.add(cell);
            }
        }
        return flaggedCells;
    }
}
