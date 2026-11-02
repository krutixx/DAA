#include <iostream>
#include <algorithm>
using namespace std;
//define struct
struct item{
    int value;
    int weight;
};

//sorting function

bool compare(item a, item b){
    return (double) a.value / a.weight >
            (double) b.value /b.weight;
}

int main(){
    int n;
    int capacity;
   
    cout<<"Enter number of items: ";
    cin>>n;

    cout<<"Enter capacity: ";
    cin>> capacity;
    item items[n];
    for(int i=0;i<n;i++){
     cout<<"Enter value and weight: ";
     cin>>items[i].value >>items[i].weight; 
    }
    
    sort(items, items+n, compare);

    double total_value=0;

    for(int i=0;i<n;i++){
        if(items[i].weight<capacity){
            capacity-=items[i].weight;
            total_value +=items[i].value;
        }
        else{
            total_value += items[i].value * (double) capacity/items[i].weight;
            break;
        }
    }
    cout<<"Total value: "<< total_value;
    return 0;
    
}
