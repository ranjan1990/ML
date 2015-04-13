#include<iostream>
#include<vector>
using namespace std;
template<class T> class genetic
{
	private:
		int N;	//population size	
		int M;	//string size 
		vector<T> S;	//actual string
		vector<float> fitness[N];	//fitness value of each string of N;
	public:
		genetic(int N,int M);	//constructor
		void crossover(int s1_id,int s2_id); //	cross over two string  s1_id and s2_id
		void fitness(int str_id);		//returns the fitness if the string id str_id
	
};
template<class T> genetic<T>::genetic(int n,int m)
{
	N=n;
	M=m;
}

main()
{
	 genetic<char> g1(2,3);


}





