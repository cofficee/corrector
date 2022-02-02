# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: Run BERT on Masked LM.
"""

import argparse
import sys
from transformers import pipeline

sys.path.append('../..')
from pycorrector import config

MASK_TOKEN = "[MASK]"


def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--bert_model_dir", default=config.bert_model_dir,
                        type=str,
                        help="Bert pre-trained model dir")
    args = parser.parse_args()

    nlp = pipeline('fill-mask',
                   model=args.bert_model_dir,
                   tokenizer=args.bert_model_dir,
                   device=-1,  # gpu device id
                   )
    i = nlp('hi lili, What is the name of the [MASK] ?')
    print(i)

    i = nlp('今天[MASK]情很好')
    print(i)

    i = nlp('少先队员[MASK]该为老人让座')
    print(i)

    i = nlp('[MASK]七学习是人工智能领遇最能体现智能的一个分知')
    print(i)

    i = nlp('机[MASK]学习是人工智能领遇最能体现智能的一个分知')
    print(i)


if __name__ == "__main__":
    main()
