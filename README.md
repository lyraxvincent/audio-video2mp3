# Audio to mp3 converter
This is a script to handle bulk audio to mp3 conversion.  
It uses the [Pydub](https://pypi.org/project/pydub/) python package.

## How to use the script
Place the script in a directory together with the files you wish to convert to mp3.
```python
.
└── [directory]
    ├── convert2mp3.py
    ├── file1
    ├── file2
    └── file3

```  

Alternatively, if the files are in multiple directories, you can also covert them conserving their directory path.  
```python
.
├── convert2mp3.py
├── [subdirectory1]
│   ├── file1
│   ├── file2
│   └── file3
├── [subdirectory2]
│   ├── file1
│   ├── file2
│   └── file3
└── [subdirectory3]
    ├── file1
    ├── file2
    └── file3
```
Execute the script on terminal:
```python
> python3 convert2mp3.py
``` 