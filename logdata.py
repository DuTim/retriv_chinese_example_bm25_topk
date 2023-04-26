import csv
from typing import Dict
import csv 
 
csv.field_size_limit(500 * 1024 * 1024)
 
def log_tsv_data(file_path: str, delimiter: str = "\t") -> Dict[int, str]: ## note:数据准备  将 id ,句子 : ==> {id:"句子"}

    print(file_path)
    with open(file_path, encoding="utf-8") as f:
        for  idx ,  line in enumerate(csv.reader(f, delimiter=delimiter)) :  ## [pid: text]
            print(line)
            if idx> 100 :
               break

            # id_to_item_dict[int(_id)] = content
datapath ="train.top100.bm25.tsv"
log_tsv_data(datapath,)