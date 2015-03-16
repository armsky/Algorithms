#include <iostream>
#include <vector>

using namespace std;

class BinaryTreeSort{
    public:
        
        // Merge sort, use array
        void mergeSort(int a[], int l, int r){
            // If l == r, do nothing
            if (l < r){
                int mid = (l+r) / 2; // Or use mid = l + (r-l)/2 for avoiding overflow
                mergeSort(a, l, mid);
                mergeSort(a, mid+1, r);
                merge(a, l, mid, r);
            }
        }
        // merge a[l, mid] and a[mid, r] of a[]
        void merge(int a[], int l, int mid, int r){
            int i, j, k;
            int n1 = mid - l + 1; // remember + 1 here
            int n2 = r - mid;
            // Create temp arrays
            int left[n1], right[n2];
            // Copy data to temp
            for (i=0; i < n1; i++)
                left[i] = a[l + i];
            for (j=0; j < n2; j++)
                right[j] = a[mid+1 + j];
            //Merge
            i = 0;
            j = 0;
            k = l; // Not 0 !!!
            while (i < n1 && j < n2){
                if (left[i] <= right[j]){
                    a[k] = left[i];
                    i++;
                }else{
                    a[k] = right[j];
                    j++;
                }
                k++;
            }
            // Copy the remaining if any
            while (i < n1){
                a[k] = left[i];
                k++;
                i++;
            }
            while (j < n2){
                a[k] = right[j];
                j++;
                k++;
            }
        }

        void printArray(int a[], int sz) { 
            for (int i = 0; i < sz; i++)
                cout << a[i] << " "; 
            cout << endl; 
        }
};

int main(){
    BinaryTreeSort bts;
    int a[] = {21, 2, 45, 103, 0, 64, 0};
    int sz = sizeof(a)/sizeof(a[0]);
    
    bts.printArray(a, sz);
    bts.mergeSort(a, 0, sz-1);
    bts.printArray(a, sz);
    return 0;
}

