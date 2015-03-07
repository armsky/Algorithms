void insertionSort(int arr[], int length){
    int i, j, curValue;
    for (i = 1; i < length; i++){
        j = i;
        curValue = arr[j];
        while (j > 0 && curValue < arr[j-1]){
            arr[j] = arr[j-1];
            j--;
        }
        arr[j] = curValue;
    }
}

