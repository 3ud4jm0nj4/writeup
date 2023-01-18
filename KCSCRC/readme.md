# Merger Xor

![challenge](./chall.png)

---
## overview
Đề bài cho 1 file chall.c:
```c
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
```
Đoạn code trên nếu nhập đúng flag sẽ cho ra file stdout.txt:
```
[+] Cipher: 0x98,0x02,0xaa,0x9b,0xfe,0xdc,0x44,0x73,0xef,0x9d,0x40,0xdd,0xd8,0x05,0xc9,0xea,0x51,0xcd,0xab,0x01,0x77,0x14,0x8c,0x62,0x51,0xea,0x41,0xbe,0xae,0x33,0x23,0xd9,0x9d,0xfe,0x22,0x36,0xdb,0x23,0xfa,0x72,0x36,0xfd,0xb9,0xbc,0x11,0x04,0xfc,0xc8,0xdf
```
Trong bài này flag sẽ được mã hóa 5 lần bằng hàm `Flat()`:
```c 
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
```
Hàm này trích xuất 4 bit cuối cùng của kí tự hiện tại và 4 bit đầu tiên của kí tự tiếp theo sau đó hợp nhất lại với nhau để tạo ra một khối mới rồi XOR khối đó với kí tự hiện tại và lưu trữ kết quả vào chuỗi `cipher[]`.Sau khi hoàn thành thì nó sẽ ghi đè chuỗi ban đầu thành chuỗi `cipher`.Điều này được lặp lại 5 lần, cuối cùng nó in ra kết quả giống trong file stdout.txt


