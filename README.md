# ツール・ライブラリの名前

1.   primary_number1.py
1.   primary_number2.py
1.   primary_number3.py
1.   頻度解析.py
1.   sort.py
1.   sortの解読.py

---

## primary_number1.py
### 説明
このスクリプトは、素因数分解です。関数として「search」を定義しており、while文でループを回して、与えられた数が割り切れたらprimary_listリストに追加します。反対に割り切れないならば、1を足してループを続けます。

### 画像
![primary_numer1](https://user-images.githubusercontent.com/85320766/120753688-85e9b280-c546-11eb-8a4d-d8e38a6abed0.png)

---

## primary_number2.py
### 説明
このスクリプトは、エラトステネスの篩を利用した素因数分解です。関数として「search2」を定義しております。divideリストで2から$\sqrt{num}$までの自然数のリストを用意し、divideの最小値であるdivide[0]で割れたらprimary_listリストにそれを追加し、num変数にnumとdivide[0]を割り算した結果を代入します。divide_copyリストにはdivideから要素を1つずつ取り出し、divideの要素の訳数を削除して、divideにdivide_copy[:]で深いコピーを行います。それでもしdivideの要素数が0、あるいはnumが1になったら終了します。

### 画像
![primary_numer2](https://user-images.githubusercontent.com/85320766/120755616-29d45d80-c549-11eb-9dbd-57b38b606537.png)

---

## primary_number3.py
### 説明
このスクリプトは、先ほどと同様エラトステネスの篩を利用した素因数分解です。ただし単純なリストではなく、numpyを利用して処理の高速化を図りました。

### 画像
![primary_numer3](https://user-images.githubusercontent.com/85320766/120756145-d9113480-c549-11eb-9bf9-7c09a8a467d9.png)

---
## 頻度解析.py
### 説明
このスクリプトは、アルファベットと各種の記号類の頻度を数え上げるスクリプトです。処理の大部分はライブラリのcollectionsのCounterに依存しています。アルファベットの文字列はabcリストで、記号と数字のリストはcharリストにあります。2つのfor文でアルファベットと記号類を出力しています。

### 画像
![頻度解析](https://user-images.githubusercontent.com/85320766/120760405-0b716080-c54f-11eb-84c8-14846ef6f347.png)

---
## sort.py
### 説明
このスクリプトは、[シーザー暗号](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%BC%E3%82%B6%E3%83%BC%E6%9A%97%E5%8F%B7)を実現するためのスクリプトです。zyxリストでずらす文字列であるkey変数分、文字列"abc...z"をずらしてつなげています。その次にfor文で平文の文字数分回して、平文のアルファベットを1つずつ取得します。ある文字が大文字か、小文字化をif文で判断し、それがアルファベットの何番目の文字かをindex_num変数で取得します。zyxから対応するindex_num文ずらされた文字列を得、code_listリストに挿入します。なおこのとき、数字や記号などアルファベットでない文字は暗号化せずにそのままcode_listに挿入しています。

### 画像
![sort](https://user-images.githubusercontent.com/85320766/120763354-17125680-c552-11eb-89fa-c51299c058a5.png)

---
## sortの解読.py
### 説明
このスクリプトは、[シーザー暗号](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%BC%E3%82%B6%E3%83%BC%E6%9A%97%E5%8F%B7)を解読するスクリプトです。このコードの基本的な考え方は、アルファベットには登場する文字に頻度にバラツキがあり、一般的な文章の最頻出文字と暗号文の最頻出文字は一致する可能性が高い、というものです。

optionリストには、一般的な文章におけるアルファベットの頻出順に並んで格納されています。またcountリストには、暗号文のアルファベットの出現回数がインデックスの順番に収納されています。while文でループを回しております。key変数では、暗号文の最頻出文字のインデックスとoptionの文字のインデックスの差の絶対値を求め、それをずらす文字数の候補としています。その次のfor文ではsort.pyと同じように暗号文をずらして、平文の候補を演算しています。その次に、利用者に意味のある文章かを問いかけ、意味があるのなら終了し、違っていたらoptionのその次の最頻出文字と暗号文の最頻出文字が一致すると仮定し変数sを1だけ増分し、次のループに移行します。

### 画像
![sortの解読](https://user-images.githubusercontent.com/85320766/120874610-7455e880-c5e2-11eb-8831-d5890fb2d2a5.png)

---
