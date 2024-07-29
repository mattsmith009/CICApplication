import spacy 
from training_examples import training_data, dev_data, numerical_training_data, numerical_dev_data, location_training_data, location_dev_data
from spacy import displacy
from spacy.tokens import DocBin
from spacy.util import filter_spans

nlp = spacy.load('en_core_web_lg')

def opt_disease_data(training_data: dict) -> list:
    optimized_data = [] # each entry has a key ID that is mapped to a list of lists containing the sentence, and a three-key dictionary containing the start index, end index, and the label (always DISEASE).
    for key in training_data:
        if len(training_data[key]) > 0:
            for sentence in training_data[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    optimized_data.append((sentence, {'entities':[(start, end, 'DISEASE')]}))

    return optimized_data

def opt_numerical_data(training_data: dict) -> list:
    optimized_numerical_data = []
    for key in training_data: 
        if len(training_data[key]) > 0:
            for sentence in training_data[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    optimized_numerical_data.append((sentence, {'entities':[(start, end, 'NUMERICAL')]}))

    return optimized_numerical_data

def opt_location_data(training_data: dict) -> list:
    optimized_location_data = []
    for key in training_data: 
        if len(training_data[key]) > 0:
            for sentence in training_data[key][0]: 
                start = sentence.lower().find(key.lower())
                if start != -1:
                    end = start + len(key)
                    optimized_location_data.append((sentence, {'entities':[(start, end, 'LOCATION')]}))

    return optimized_location_data

def toDocBin(opt_data: dict, numerical_opt_data: dict, location_opt_data: dict): 
    doc_bin = DocBin()
    for data in [opt_data, numerical_opt_data, location_opt_data]:
        for sentence, annot in data: 
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

opt_train_data = opt_disease_data(training_data)
opt_dev_data = opt_disease_data(dev_data)

opt_num_train_data = opt_numerical_data(numerical_training_data)
opt_num_dev_data = opt_numerical_data(numerical_dev_data)

opt_loc_train_data = opt_location_data(location_training_data)
opt_loc_dev_data = opt_location_data(location_dev_data)

doc_bin_train_instance = toDocBin(opt_train_data, opt_num_train_data, opt_loc_train_data)
doc_bin_dev_instance = toDocBin(opt_dev_data, opt_num_dev_data, opt_loc_dev_data)

doc_bin_train_instance.to_disk("train.spacy")
doc_bin_dev_instance.to_disk("dev.spacy")

#  python -m spacy train config.cfg --output ./output

# nlp = spacy.load("output/model-best")
# test_sentences = [ "alphavirus has created 25 infections in the past two years in Alabama."]

# doc = nlp("".join(test_sentences))

# for ent in doc.ents: 
#     print(ent.text, ent.label_)
