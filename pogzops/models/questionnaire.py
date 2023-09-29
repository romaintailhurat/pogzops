"""
Questionnaire functions.
"""

def get_dups(struct: list[str]) -> list[str]:
    """Get a sorted list of duplicated elements from a list"""
    dups = [element for element in struct if struct.count(element) > 1]
    return sorted(dups)

def get_seqs_and_questions_ids(qjson: dict):
    seqs = qjson["Child"]
    seqs_ids = []
    subseqs_ids = []
    questions_ids = []
    for seq in seqs:
        seqs_ids.append(seq["id"])
        for child1 in seq["Child"]:
            if child1["type"] == "SequenceType":
                # subseq
                subseqs_ids.append(child1["id"])
                for child2 in child1["Child"]:
                    # question
                    questions_ids.append(child2["id"])
            else:
                # question
                questions_ids.append(child1["id"])
    return {
        "seqs_ids": seqs_ids,
        "subseqs_ids": subseqs_ids,
        "questions_ids": questions_ids
    }

def get_seqs_and_questions_names(qjson: dict):
    seqs = qjson["Child"]
    seqs_names = []
    subseqs_names = []
    questions_names = []
    for seq in seqs:
        seqs_names.append(seq["Name"])
        for child1 in seq["Child"]:
            if child1["type"] == "SequenceType":
                # subseq
                subseqs_names.append(child1["Name"])
                for child2 in child1["Child"]:
                    # question
                    questions_names.append(child2["Name"])
            else:
                # question
                questions_names.append(child1["Name"])
    return {
        "seqs_names": seqs_names,
        "subseqs_names": subseqs_names,
        "questions_names": questions_names
    }

def get_ids(qjson: dict):
    filters_ids = [fc["id"] for fc in qjson["FlowControl"]]
    variables_ids = [var["id"] for var in qjson["Variables"]["Variable"]]
    codelists_ids = [cl["id"] for cl in qjson["CodeLists"]["CodeList"]]
    seqs_questions_ids = get_seqs_and_questions_ids(qjson)
    return {
        "filter_ids": filters_ids,
        "variables_ids": variables_ids,
        "codelists_ids": codelists_ids,
        **seqs_questions_ids
    }

def get_names_and_labels(qjson: dict):
    variables_names = [var["Name"] for var in qjson["Variables"]["Variable"]]
    codelists_labels = [cl["Label"] for cl in qjson["CodeLists"]["CodeList"]]
    seqs_questions_names = get_seqs_and_questions_names(qjson)
    return {
        "variables_names": variables_names,
        "codelists_labels": codelists_labels,
        **seqs_questions_names
    }