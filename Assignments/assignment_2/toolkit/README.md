# Toolkit for Assignment 2

Không cần copy/paste từ `solutions`. Sinh ra `expect = str()` vào file `ASTGenSuite.py` trong 1 nốt nhạc

## Prerequisites

+ Cài Node.JS
+ Không chơi Windows
+ `expect = ` hiện tại trong file `ASTGenSuite.py` là inline (chỉ nằm trên 1 dòng, phía dưới phải là dòng `self.assertTrue(TestAST.test...`)

## How to use?

### Bước 1
+ Tải `toolkit.zip` về. Unzip rồi merge `./toolkit/src` vào `src` của assignment hiện tại.
+ Các files trong toolkit:

```bash
../toolkit
└── src
    ├── all.sh
    ├── ast.sh
    ├── clean.sh
    ├── gen.sh
    ├── main
    │   └── mp
    │       └── utils
    │           └── AntiAST.py
    └── scripts
        └── ast_sol2str.js
```


+ Sau khi merge, `src` của assignment thành như vậy:

```bash
├── all.sh
├── ast.sh
├── clean.sh
├── gen.sh
├── main
│   └── mp
│       ├── astgen
│       │   ├── ASTGeneration.py
│       ├── parser
│       │   ├── lexererr.py
│       │   ├── MP.g4
│       └── utils
│           ├── AntiAST.py
│           ├── AST.py
│           ├── Utils.py
│           └── Visitor.py
├── run.py
├── scripts
│   ├── ast_sol2str.js
└── test
    ├── ASTGenSuite.py
    ├── LexerSuite.py
    ├── ParserSuite.py
    ├── solutions
    ├── testcases
    └── TestUtils.py
```


### Bước 2
+ Chạy `./clean.sh` để xóa các files trong `solutions/` và `testcases/`
+ Vào các files `ASTGenSuite.py` và `ASTGeneration.py`, đổi import từ `AST.py` thành `AntiAST.py`, như sau:

```python
# from AST import *
from AntiAST import *
```

+ Chạy `./all.sh` để chạy các test trong `ASTGenSuite.py` và sinh ra các files trong `solutions`
+ Chạy `./ast.sh` để fix lại file `ASTGenSuite.py` thành `expect = str()`.
+ Đổi lại `AntiAST` thành `AST`: vào các files `ASTGenSuite.py` và `ASTGeneration.py`, đổi import từ `AntiAST.py` thành `AST.py`, như sau:

```python
from AST import *
# from AntiAST import *
```

+ Hiện tại, file `ASTGenSuite.py` đã được fix lại `str()`, còn file cũ được backup lại thành file `ASTGenSuite_[timestamp].py`
+ Chạy lại `./all.sh` để chạy lại testcases như bình thường.



```bash
 _____ _                 _     __   __            _
|_   _| |__   __ _ _ __ | | __ \ \ / /__  _   _  | |
  | | | '_ \ / _` | '_ \| |/ /  \ V / _ \| | | | | |
  | | | | | | (_| | | | |   <    | | (_) | |_| | |_|
  |_| |_| |_|\__,_|_| |_|_|\_\   |_|\___/ \__,_| (_)
```