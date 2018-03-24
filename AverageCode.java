public class AverageCode {
    public static int [][] blosum = {
            { 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0},
            {-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3},
            {-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3},
            {-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3},
            { 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1},
            {-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2},
            {-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2},
            { 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3},
            {-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3},
            {-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3},
            {-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1},
            {-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2},
            {-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1},
            {-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1},
            {-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2},
            { 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2},
            { 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0},
            {-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3},
            {-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1},
            { 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4}
    }; // Array with BLOSUM62 Matrix
    public static char [][] input ={
            {'M' , 'R', 'M', 'W'},
            {'M' , 'N', 'L', 'W'},
            {'M' , 'R', 'I', 'W'},
            {'M' , 'N', 'K', 'P'},
    }; //Input matrix --> dynamic reading next
    public static char[] AS = {
            'A','R','N','D', 'C','Q','E','G','H','I','L','K','M','F','P', 'S', 'T', 'W', 'Y', 'V'
    };// Aminoacid array

    public static double [][] MMatrix;
    //output array
    public static void main(String[] args){
        MMatrix = new double[AS.length][input.length];
        createMatrix();
        output();


    }

    public static void createMatrix(){
        int counter = 0;
        for (int j= 0; j<MMatrix.length; j++){
            for(int k = 0;k <MMatrix[j].length; k++){

                for (int i = 0; i<AS.length; i++){
                    counter =  AcidCount(k ,i);
                    MMatrix[j][k] += (counter/4.0)*blosum[i][j]; //(counter/4)*blosum[i][j];
                }
                /*if (MMatrix[j][k] == 0.0){
                    MMatrix[j][k] = 1.0;
                }*/
            }
        }

    }
    public static int AcidCount(int k, int i){
        int count = 0;
        for (int r = 0; r < input.length; r++){
            if(input[r][k] == AS[i]){
                count++;
            }
        }
        return count;
    }
    public static void output(){
        for (int i = 0; i<MMatrix.length; i++){
            for(int j = 0; j <MMatrix[i].length; j++){
              System.out.print(MMatrix[i][j]);
              System.out.print(" ");
            }
            System.out.println();
        }

    }



}
