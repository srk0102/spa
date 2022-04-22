#include <iostream>
#include "hash.h"
using namespace std;

class Database {
	public:
	HashMapTable hash;
	void Insert(int k, string data[], int len){
		for(int i = 0; i<len; i++){
			hash.Insert(k, data[i]);
		}
	}
	void searchKey(int k){
		hash.SearchKey(k);
	}
	void Remove(int k){
		hash.Remove(k);
	}
	int loadFactor(){
		return hash.loadFactor();
	}
};
