#include <iostream>
#include <climits>

int* createMatrix(int size){
    //allocate memory
    int* arr = new int[size * size];


    for(int row =0; row<size; row++)
    {
        for(int col = 0; col<size; col++)
        {
            *(arr + row*size+col) = rand() %100;
        }
    }
    return arr;
};

void deleteMatrix(int* arr){
    delete[] arr;
};

int min(int x1, int x2, int x3){

    if (x1 < x2)
        return (x1 < x3) ? x1 : x3;
    else
        return (x2 < x3) ? x2 : x3;
};

int find_min_path(int* arr, int row, int col, int size){
    if (row<0 || col<0)
    {
        return INT_MAX;
    }
    else
        if(row == 0 && col == 0)
        {
            return arr[row*size+col];
        }
        else
        {
            return arr[row*size+col] +
            min(
                find_min_path(arr, row-1, col, size),
                find_min_path(arr, row-1, col-1, size),
                find_min_path(arr, row, col-1, size)
            );
        }
};

void runTest(int size, int row, int col){
    int* arr = createMatrix(size);

    std::cout<<"test started"<<std::endl;
    for(int row =0; row<size; row++)
    {
        for(int col = 0; col<size; col++)
        {
            std::cout<<arr[row*size+col]<<" ";
        }
        std::cout<<std::endl;
    }

    time_t start, end;
    time(&start);
    int minpath = find_min_path(arr, row, col, size);
    time(&end);
    double time_taken = double(end - start);

    std::cout << "Time taken by program is : " << time_taken;
    std::cout << " sec " << std::endl;

    std::cout<< "Min path= " << minpath <<std::endl;

    deleteMatrix(arr);
};

int main() {


    runTest(3, 2,2);

    runTest(15,14,14);

    return 0;
}