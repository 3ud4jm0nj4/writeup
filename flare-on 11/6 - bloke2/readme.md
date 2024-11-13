![](./Asset/1.png)

We were provided with some Verilog files, specifically test benches and modules for the implementation of BLAKE2 hash calculations.

After compiling the test bench files and examining their output, I am now mainly focusing on two files:

- `bloke2s.v`

- `bloke2b.v`

The test benches for these modules hash some test messages:

  ![](./Asset/2.png)
    
Output is the hash result, with different lengths for each type: Blake2b optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes, while Blake2s optimized for 8- to 32-bit platforms and produces digests of any size between 1 and 32 bytes:

-   BLOKE2S:
 
  ![](./Asset/3.png)

- BLOKE2B:
 
  ![](./Asset/4.png)

Based on the description, our goal is a message that can be extracted from the test bench. To do this, i decided to trace back from the first file that prints out the hashes. Ignoring the test bench for the `bloke2s` module, we went directly into `bloke2s.v`. Initially, this one invokes `bloke2` module, pass parameters into it, indicating that `bloke2s.v` serves as a wrapper of actual hashing module:

  ![](./Asset/5.png)

Moving on to `bloke2.v`, it invokes the `f_unit` and `data_mgr` modules:

  ![](./Asset/6.png)

  ![](./Asset/7.png)

`f_unit` module then invokes all the remaining modules, setting up some BLAKE2 constants for the subsequent hashing process, as shown below:

  ![](./Asset/8.png)

Therefore, it’s better to ignore this part and not delve too deeply into the hashing process, as our target is the hidden message.

When examining `data_mgr.v`, we can observe a suspicious value there:

  ![](./Asset/9.png)

To confirm my assumption this is our hidden message, i changed `TEST_VAL` to different value, then ran `bloke2s_tb.v` again. Since it didnt affects the hashing result, i proceeded to analyze further how this variable is used in the code.

It is going to be used to XOR with `h_in`:

  ![](./Asset/10.png)

`h_in` here refers to `h_out`:

  ![](./Asset/11.png)

Compare to an [implement of blake2](https://github.com/buggywhip/blake2_py/blob/master/blake2.py). `h_out` should be hash result:

  ![](./Asset/12.png)

We can confirm that by printing out the `h_in`, you will see `h_in` is our hash value but in reverse order:

  ![](./Asset/13.png)

Next, we can simply xor reversed hash with `TEST_LOCAL`, where one of them is flag:

  ![](./Asset/14.png)

Flag: `please_send_help_i_am_trapped_in_a_ctf_flag_factory@flare-on.com`
