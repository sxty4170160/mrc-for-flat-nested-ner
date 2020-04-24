# A Unified MRC Framework for Named Entity Recognition 
The repository contains the code of the recent research advances in [Shannon.AI](http://www.shannonai.com). 

**A Unified MRC Framework for Named Entity Recognition** <br>
Xiaoya Li\*, Jingrong Feng\*, Yuxian Meng, Qinghong Han, Fei Wu, Jiwei Li<br>
Preprint. [arXiv](https://arxiv.org/abs/1910.11476)<br>
If you find this repo helpful, please cite the following:
```latex
@article{li2019unified,
  title={A Unified MRC Framework for Named Entity Recognition},
  author={Li, Xiaoya and Feng, Jingrong and Meng, Yuxian and Han, Qinghong and Wu, Fei and Li, Jiwei},
  journal={arXiv preprint arXiv:1910.11476},
  year={2019}
}
```
For any question, please feel free to contact xiaoya_li@shannonai.com or post Github issue.<br>

## Contents
1. [Overview](#overview)
2. [Experimental Results on Flat/Nested NER Datasets](#experimental-results-on-flat/nested-ner-datasets)
3. [Data Preparation](#data-preparation)
4. [Dependencies](#dependencies)
5. [Usage](#usage)
6. [FAQ](#faq)

## Overview 

The task of NER is normally divided into **nested** NER and **flat** NER depending on whether named entities are nested or not. Instead of treating the task of NER as a sequence labeling problem, we propose to formulate it as a SQuAD-style machine reading comprehension (MRC) task. <br>

For example, the task of assigning the [PER] label to *"[Washington] was born into slavery on the farm of James Burroughs"* is formalized as answering the question *"Which person is mentioned in the text?"*. <br>

By unifying flat and nested NER under an MRC framework, we're able to gain a huge improvement on both flat and nested NER datasets, which achives SOTA results.

![docs/overview.png](./docs/overview.png)

We use `MRC-NER` to denote the proposed framework. <br>
Here are some of the **highlights**:

#### 1. *MRC-NER* works better than BERT-Tagger with less training data. 
#### 2. *MRC-NER* is capable of handling both flat and nested NER tasks under a unified framework.  
#### 3. *MRC-NER* has a better zero-shot learning ability which can predicts labels unseen from the training set.  
#### 4. The query encodes prior information about the entity category to extract and has the potential to disambiguate similar classes. 





## Experimental Results on Flat/Nested NER Datasets
Experiments are conducted on both *Flat* and *Nested* NER datasets. The proposed method achieves vast amount of performance boost over current SOTA models. <br>
We only list comparisons between our proposed method and previous SOTA in terms of span-level micro-averaged F1-score here. 
For more comparisons and span-level micro Precision/Recall scores, please check out our [paper](https://arxiv.org/abs/1910.11476.pdf). <br> 
### Flat NER Datasets
Evaluations are conducted on the widely-used bechmarks: `CoNLL2003`, `OntoNotes 5.0` for English; `MSRA`, `OntoNotes 4.0` for Chinese. We achieve new SOTA results on `OntoNotes 5.0`, `MSRA` and  `OntoNotes 4.0`, and comparable results on `CoNLL2003`.

| Dataset |  Eng-OntoNotes5.0 | Zh-MSRA | Zh-OntoNotes4.0 | 
|---|---|---|---|
| Previous SOTA | 89.16 | 95.54  | 80.62 | 
| Our method |  **91.11** | **95.75** | **82.11** | 
|  |  **(+1.95)** | **(+0.21)** | **(+1.49)** | 


### Nested NER Datasets
Evaluations are conducted on the widely-used `ACE 2004`, `ACE 2005`, `GENIA`, `KBP-2017` English datasets.

| Dataset | ACE 2004 | ACE 2005 | GENIA | KBP-2017 | 
|---|---|---|---|---|
| Previous SOTA | 84.7 | 84.33 | 78.31  | 74.60 | 
| Our method | **85.98** | **86.88** | **83.75** | **80.97** | 
|  | **(+1.28)** | **(+2.55)** | **(+5.44)** | **(+6.37)** | 

Previous SOTA:
 
* [DYGIE](https://www.aclweb.org/anthology/N19-1308/) for ACE 2004.
* [Seq2Seq-BERT](https://www.aclweb.org/anthology/P19-1527/) for ACE 2005 and GENIA.
* [ARN](https://www.aclweb.org/anthology/P19-1511/) for KBP2017. 

## Data Preparation

We release preprocessed and source data files for both flat and nested NER benchmarks. <br>

You can download the preprocessed datasets and source data files from [Google Drive](./docs/data_release.md). <br>

NER datasets in the CoNLL-2003 format with BMESO scheme can not be directly used in our project. 
Code for transforming datasets with BMESO labels to query-answer pairs is at [data/data_generate/preprocess_data.py](./data/data_generate/preprocess_data.py). Queries could be found at [data/data_generate/query_map.py](./data/data_generate/query_map.py). 
The code assumes that each dataset after preprocessing lives in a folder containing `query_ner.train`, `query_ner.dev`, `query_ner.test` files under MRC framework.



## Dependencies 
* Packages dependencies:
```bash
python >= 3.6
PyTorch == 1.1.0 
pytorch-pretrained-bert == 0.6.1 
```
* Download and unzip `BERT-Large, Cased English` and `BERT-Base, Chinese` pretrained checkpoints. Then follow the [guideline](https://huggingface.co/transformers/v2.5.0/converting_tensorflow_models.html) from huggingface to convert TF checkpoints to PyTorch. 


## Usage 
You can directly use the following commands to train and evaluate your model with some minor changes.<br>
As an example, the following command trains (and evaluates, automatically done after training) the `BERT-MRC` on English `OntoNotes5.0` and Chinese `Resume`:

```bash
data_dir=/data/work/english_ontonotes
base_path=/home/work/mrc-for-flat-nested-ner
config_path=/home/work/mrc-for-flat-nested-ner/configs/eng_large_case_bert.json
bert_model=/data/BERT_BASE_DIR/cased_L-24_H-1024_A-16

seed=3306
task_name=ner
max_seq_length=150
num_train_epochs=4
warmup_proportion=-1
data_sign=en_onto
checkpoint=28000

gradient_accumulation_steps=4
learning_rate=6e-6
train_batch_size=36
dev_batch_size=72
test_batch_size=72
export_model=/data/export_folder/${train_batch_size}_lr${learning_rate}
output_dir=${export_model}


CUDA_VISIBLE_DEVICES=2 python3 ${base_path}/run/run_query_ner.py \
--config_path ${config_path} \
--data_dir ${data_dir} \
--bert_model ${bert_model} \
--max_seq_length ${max_seq_length} \
--train_batch_size ${train_batch_size} \
--dev_batch_size ${dev_batch_size} \
--test_batch_size ${test_batch_size} \
--checkpoint ${checkpoint} \
--learning_rate ${learning_rate} \
--num_train_epochs ${num_train_epochs} \
--warmup_proportion ${warmup_proportion} \
--export_model ${export_model} \
--output_dir ${output_dir} \
--data_sign ${data_sign} \
--gradient_accumulation_steps ${gradient_accumulation_steps} 
```

```bash
data_dir=/data/work/nl_resume_ner
base_path=/home/work/mrc-for-flat-nested-ner
config_path=/home/work/mrc-for-flat-nested-ner/configs/zh_bert.json
bert_model=/data/nfsdata/nlp/BERT_BASE_DIR/chinese_L-12_H-768_A-12

seed=3306
task_name=ner
max_seq_length=512
num_train_epochs=3
warmup_proportion=-1
data_sign=resume 
checkpoint=200

gradient_accumulation_steps=4
learning_rate=6e-5
train_batch_size=16
dev_batch_size=72
test_batch_size=72
export_model=/data/export_folder/${train_batch_size}_lr${learning_rate}
output_dir=${export_model}


CUDA_VISIBLE_DEVICES=0 python3 ${base_path}/run/run_query_ner.py \
--config_path ${config_path} \
--data_dir ${data_dir} \
--bert_model ${bert_model} \
--max_seq_length ${max_seq_length} \
--train_batch_size ${train_batch_size} \
--dev_batch_size ${dev_batch_size} \
--test_batch_size ${test_batch_size} \
--checkpoint ${checkpoint} \
--learning_rate ${learning_rate} \
--num_train_epochs ${num_train_epochs} \
--warmup_proportion ${warmup_proportion} \
--export_model ${export_model} \
--output_dir ${output_dir} \
--data_sign ${data_sign} \
--gradient_accumulation_steps ${gradient_accumulation_steps} 
```


## FAQ

