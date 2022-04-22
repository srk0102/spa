#include "database.h"
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
   Database DataBase;
   int k;
//   string v;
   int c;
   string userData[4];
   vector<int> insertArr;
   while (1) {
      cout<<"1.Insert element into the table"<<endl;
      cout<<"2.Search element from the key"<<endl;
      cout<<"3.Delete element at a key"<<endl;
      cout<<"4.Print HashTable"<<endl;
      cout<<"5.print LoadFactor"<<endl;
      cout<<"6.Exit"<<endl;
      cout<<"Enter your choice: ";
      cin>>c;
      switch(c) {
         case 1:
            cout<<"Enter Frist Name: ";
            cin>>userData[0];
            cout<<"Enter Last Name: ";
            cin>>userData[1];
            cout<<"Enter uuid: ";
            cin>>userData[2];
            cout<<"Enter year: ";
            cin>>userData[3];
            cout <<"Enter the key you need to save the data: ";
            cin>>k;
            if(count(insertArr.begin(), insertArr.end(), k)){
            	cout << "You can only insert data which is not used" << "\n" << "used Ids: ";
            	for(int i = 0; i < insertArr.size(); i++){
    				cout << insertArr[i] << ' ';
    			}
			}else{
				insertArr.insert(insertArr.begin(), k);
				DataBase.Insert(k, userData, 4);
			}
         break;
         case 2:
            cout<<"Enter key of the element to be searched: ";
            cin>>k;
            DataBase.searchKey(k);
         break;
         case 3:
            cout<<"Enter key of the element to be deleted: ";
            cin>>k;
            DataBase.Remove(k);
         break;
         case 4:
         	for(int i = 0; i < insertArr.size(); i++){
    				DataBase.searchKey(insertArr[i]);
    			}
    		break;
    	 case 5:
    	 	cout<< "Load Factor: " <<DataBase.loadFactor()*0.75 << "\n";
         case 6:
            exit(1);
         default:
            cout<<"\nEnter correct option\n";
      }
   }
   return 0;
}
