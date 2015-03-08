import java.util.Arrays;

class Sort {
    
    // Insertion Sort
    public void insertionSort(int[] arr){
        int i, j, temp;
        for (i = 1; i < arr.length; i++){
            j = i;
            while (j > 0 && arr[j-1] > arr[j]){
                temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
                j--;
            }
        }
    }

    // Selection Sort
    public void selectionSort(int[] arr){
        int i, j, temp;
        for (i = 0; i < arr.length - 1; i++){
            int minIndex = i;
            for (j = i+1; j < arr.length; j++){
                if (arr[j] < arr[minIndex])
                    minIndex = j;
                if (minIndex != i){
                    temp = arr[i];
                    arr[i] = arr[minIndex];
                    arr[minIndex] = temp;
                }
            }
        }
    }

    // Bubble Sort
    public void bubbleSort(int[] arr){
        int i, temp;
        int j=0;
        boolean swapped = true;
        while (swapped){
            j++;
            swapped = false;
            for (i=0; i < arr.length - j; i++){
                if (arr[i] > arr[i+1]){
                    temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    swapped = true;
                }
            }
        }
    }

    public static void main(String[] args){
        Sort s = new Sort();
        int[] arr = {21, 3, 45, 1, 0, 100, 0};
        int[] arr1 = arr.clone();
        s.insertionSort(arr1);
        System.out.println(Arrays.toString(arr1));
        int[] arr2 = arr.clone();
        s.selectionSort(arr2);
        System.out.println(Arrays.toString(arr2));
        int[] arr3 = arr.clone();
        s.bubbleSort(arr3);
        System.out.println(Arrays.toString(arr3));
    }
}
