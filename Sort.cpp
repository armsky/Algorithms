# include <iostream>

using namespace std;

class Sort{
public:
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
        printArray(arr, length);
    }

    void selectionSort(int arr[], int length){
        int i, j, temp, minIndex;
        for (i = 0; i < length - 1; i++){
           minIndex = i;
           for (j = i+1; j < length; j++)
               if (arr[j] < arr[minIndex])
                   minIndex = j;
            if (i != minIndex){
                temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
        printArray(arr, length);
    }

    void printArray(int arr[], int size) {
        for ( int i = 0; i < size; i++ ) {
            cout << arr[i] << ", ";
        }
        cout << endl;
    }
};

int main(){
    Sort s;
    int arr[] = {21, 3, 45, 1, 0, 100, 0};
    s.insertionSort(arr, 7);
    int arr2[] = {21, 3, 45, 1, 0, 100, 0};
    s.selectionSort(arr2, 7);
    return 0;
}
