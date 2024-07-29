from typing import List
import spacy 
from training_examples import training_data, dev_data, numerical_training_data, numerical_dev_data, location_training_data, location_dev_data
from spacy import displacy
from spacy.tokens import DocBin
from spacy.util import filter_spans

nlp = spacy.load('en_core_web_lg')

def opt_data(dis_train_data: dict, dis_dev_data: dict, num_train_data: dict, num_dev_data: dict, loc_train_data: dict, loc_dev_data: dict) -> List[list]:
    """
    Optimizes raw disease, numerical, and location training and testing data by creating the correct data format to be used for SpaCy model training
    and fine-tuning. Returns two lists representing the optimized training data and the optimized testing data respectively. For more information, read
    the SpaCy documentation on correct data formats. 
    """
    opt_train_data = [] 
    opt_dev_data = []

    for ind, dataset in enumerate([dis_train_data, dis_dev_data]):
        for key in dataset:
            for sentence in dataset[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    if ind == 0: 
                        opt_train_data.append((sentence, {'entities':[(start, end, 'DISEASE')]}))
                    if ind == 1:
                        opt_dev_data.append((sentence, {'entities':[(start, end, 'DISEASE')]}))

    for ind, dataset in enumerate([num_train_data, num_dev_data]):                    
        for key in dataset:
            for sentence in dataset[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    if ind == 0:
                        opt_train_data.append((sentence, {'entities':[(start, end, 'NUMERICAL')]}))
                    if ind == 1:
                        opt_dev_data.append((sentence, {'entities':[(start, end, 'NUMERICAL')]}))

    for ind, dataset in enumerate([loc_train_data, loc_dev_data]):                                    
        for key in dataset:
            for sentence in dataset[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    if ind == 0:
                        opt_train_data.append((sentence, {'entities':[(start, end, 'LOCATION')]}))
                    if ind == 1:
                        opt_dev_data.append((sentence, {'entities':[(start, end, 'LOCATION')]}))

    return opt_train_data, opt_dev_data

def toDocBin(opt_data: list) -> DocBin: 
    """
    Creates a DocBin instance and stores annotation in it, returning that DocBin instance in the end. Read more
    about DocBin format in the SpaCy documentation to learn more. 
    """
    doc_bin = DocBin()
    for sentence, annot in opt_data: 
        doc = nlp(sentence)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label, alignment_mode="expand")
            if span is None: 
                print("Skipping entity")
            else:
                ents.append(span)
                
        filtered_ents = filter_spans(ents)
        doc.ents = filtered_ents
        doc_bin.add(doc)

    return doc_bin

def dataToDisk(training_data: dict, dev_data: dict, numerical_training_data: dict, numerical_dev_data: dict, location_training_data: dict, location_dev_data: dict) -> None:
    """
    Transfers all training data and testing data to the disk.
    """
    opt_train_data, opt_dev_data = opt_data(training_data, dev_data, numerical_training_data, numerical_dev_data, location_training_data, location_dev_data)

    doc_bin_train_instance = toDocBin(opt_train_data)
    doc_bin_dev_instance = toDocBin(opt_dev_data)

    doc_bin_train_instance.to_disk("train.spacy")
    doc_bin_dev_instance.to_disk("dev.spacy")

dataToDisk(training_data, dev_data, numerical_training_data, numerical_dev_data, location_training_data, location_dev_data)

#  python -m spacy train config.cfg --output ./output


