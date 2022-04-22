#include <iostream>
const int T_S = 200;
using namespace std;
struct HashTableEntry {
   int k;
   string v;
   HashTableEntry *n;
   HashTableEntry *p;
   HashTableEntry(int k, string v) {
      this->k = k;
      this->v = v;
      this->n = NULL;
   }
};
class HashMapTable {
   public:
      HashTableEntry **ht, **top;
      HashMapTable() {
         ht = new HashTableEntry*[T_S];
         for (int i = 0; i < T_S; i++)
            ht[i] = NULL;
      }
      int HashFunc(int key) {
         return key % T_S;
      }
      void SearchKey(int k) {
         int hash_v = HashFunc(k);
         bool flag = false;
         HashTableEntry* en = ht[hash_v];
         if (en != NULL) {
            while (en != NULL) {
               if (en->k == k) {
                  flag = true;
               }
               if (flag) {
                  cout<<"Element found at key "<<k<<": ";
                  cout<<en->v<<endl;
               }
               en = en->n;
            }
         }
         if (!flag)
            cout<<"No Element found at key "<<k<<endl;
      }
      void Insert(int k, string v) {
         int hash_v = HashFunc(k);
         HashTableEntry* p = NULL;
         HashTableEntry* en = ht[hash_v];
         while (en!= NULL) {
            p = en;
            en = en->n;
         }
         if (en == NULL) {
            en = new HashTableEntry(k, v);
            if (p == NULL) {
               ht[hash_v] = en;
            } else {
               p->n = en;
            }
         } else {
            en->v = v;
         }
      }
      void Remove(int k) {
         int hash_v = HashFunc(k);
         HashTableEntry* en = ht[hash_v];
         HashTableEntry* p = NULL;
         if (en == NULL || en->k != k) {
            cout<<"No Element found at key "<<k<<endl;
            return;
         }
         while (en->n != NULL) {
            p = en;
            en = en->n;
         }
         if (p != NULL) {
            p->n = en->n;
         }
         delete en;
         cout<<"Element Deleted"<<endl;
      }
      int loadFactor(){
      	return T_S;
	  }
      ~HashMapTable() {
         delete [] ht;
      }
};
