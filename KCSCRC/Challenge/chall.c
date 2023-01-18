#include<stdio.h>
#include<string.h>

int 
get_first_4_bit(unsigned char target){
	return target&0xf;
}

int
get_later_4_bit(unsigned char target){
	return (target>>4)&0xf;
}

void
Flat(unsigned char *input,int len){
	unsigned char first_4_bit,later_4_bit,block,cipher[1024];
	for(int idx=0;idx<len;idx++){
		first_4_bit = get_first_4_bit(input[idx]);
		later_4_bit = get_later_4_bit(input[(idx+1)%len]);
		// merging...
		block = (first_4_bit << 4) + later_4_bit;
		cipher[idx] = input[idx]^block;
	}
	memmove(input,cipher,len);
}

int main(){
	unsigned char input[1024],result[1024];
	printf("[+] FLAG: ");
	scanf("%s",input);
	int len = strlen((const char*)input);
	Flat(input,len);
	Flat(input,len);
	Flat(input,len);
	Flat(input,len);
	Flat(input,len);
	printf("[+] Cipher: ");
	for(int i=0;i<len;i++) 
		printf("0x%02x,",input[i]);
	
	return 1;
}

 
