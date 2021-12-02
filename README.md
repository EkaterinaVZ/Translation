# Translation
Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Resources
Solutions
Pricing
Log In
Language Technology Research Group at the University of Helsinki's picture
Helsinki-NLP
/
opus-mt-en-ru Copied
like
1
Translation
PyTorch
Rust
Transformers
en
ru
apache-2.0
marian
seq2seq
text2text-generation
AutoNLP Compatible
Model card
Files and versions
opus-mt-en-ru
/
README.md
julien-c's picture
julien-c
HF STAFF
metadata: add license
b4544f7
3 months ago
raw
history
blame
1.1 kB
---
tags:
- translation
license: apache-2.0
---
### opus-mt-en-ru
* source languages: en
* target languages: ru
*  OPUS readme: [en-ru](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ru/README.md)
*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-02-11.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ru/opus-2020-02-11.zip)
* test set translations: [opus-2020-02-11.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ru/opus-2020-02-11.test.txt)
* test set scores: [opus-2020-02-11.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ru/opus-2020-02-11.eval.txt)
## Benchmarks
| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012.en.ru 	| 31.1 	| 0.581 |
| newstest2013.en.ru 	| 23.5 	| 0.513 |
| newstest2015-enru.en.ru 	| 27.5 	| 0.564 |
| newstest2016-enru.en.ru 	| 26.4 	| 0.548 |
| newstest2017-enru.en.ru 	| 29.1 	| 0.572 |
| newstest2018-enru.en.ru 	| 25.4 	| 0.554 |
| newstest2019-enru.en.ru 	| 27.1 	| 0.533 |
| Tatoeba.en.ru 	| 48.4 	| 0.669 |
