# MemobirdDev_API_Print
## content
[Introduction](#Introduction)\
[How to use](#How%20to%20use)
### Introduction
~~(My English is not very good, I'm a Chinese.)~~\
It can print paper by memobird thermal printer via memobird Development API.\
~~It's --not can be used now-- testing with python version. --I'm (coding?) it.~~
Its python version are available now. I think C++ is difficult to write (OvO) and I will not wirte C++ version until I studies enough thing about it(doge).
### How to use
1.Make sure you registed a Memobird Dev account and bound to your memobird printer.  
2.Create a file `memobird.ini` and fill it like :
  - The first line is your ak (access key).
  - The second line is your user ID.
  - The third line is your device equipment number.  
 example :
```
698d51a19d8a121ce581499d7b701668
5861578
fb93bfff504c020a
```
3.Run ~~complied file (or~~ python file: `python main.py` ~~) ~~ in the same directory of `memobird.ini` and enter what you want to print(add colorful prompt and see help via `python main.py -h`.
