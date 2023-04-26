## simple use case 
---
### base on the [[retriv framework]](https://github.com/AmenRa/retriv.git) to use the bm25 method to geenerate a topk file about the trian.queries.tsv and dev.queries.tsv   
 1. speed of the frame work detail data  is very quickly !  
 2. the data from the alibaba data  in the [[repo]](https://github.com/Alibaba-NLP/Multi-CPR.git)  [[Paper]](https://arxiv.org/pdf/2203.03367.pdf). /data/video
 3.  In order to better understand the function of the file, I simply changed part of the file name, without affecting the understanding of the premise
 ```
For example:

train.query.txt ==>   train.queries.tsv

qrels.dev.txt ==> dev.qrels.tsv
```

4. the stop words.txt from [there](https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt)


5. environment
```
python==3.8.0
retriv=0.2.0
csv
jieba
tqdm
```
## preject structure
```

 ├─ data
 │  ├─ cn_stopwords.txt
 │  ├─ ecom
 │  │  ├─ bm25.ipynb
 │  │  ├─ corpus.tsv
 │  │  ├─ dev.qrels.tsv
 │  │  ├─ dev.queries.tsv
 │  │  ├─ dev.query.txt
 │  │  ├─ dev.top100.bm25.tsv
 │  │  ├─ logdata.py
 │  │  ├─ retri.ipynb
 │  │  ├─ train.qrels.tsv
 │  │  ├─ train.queries.tsv
 │  │  ├─ train.query.txt
 │  │  └─ train.top100.bm25.tsv

```
## how run to generate topk file  to geenerate dev.top100.bm25.tsv and  train.top100.bm25.tsv (be zip)

```
run the retri.ipynb


```
## If you think it is helpful to you, please give me a star