from os import listdir
from os.path import isfile, join
from json import load
from models.questionnaire import get_ids, get_names_and_labels, get_dups


# TODO a check_duplicates that takes a list of questionnaire dicts
# TODO the "_from_dir" read from disk and calls check_duplicates
# TODO a "_from_api" to be created (in remote)
def check_duplicates_from_dir(target_dir: str):    
    """Read JSON files in target_dir and list duplicates in questionnaires.
    Currently only list some id duplicates."""
    only_files = [f for f in listdir(target_dir) if isfile(join(target_dir, f))]
    only_json_files = [f for f in only_files if f.endswith(".json")] # only keep JSON files

    # IDs
    all_filter_ids = []
    all_var_ids = []
    all_cls_ids = []
    all_seqs_ids = []
    all_subseqs_ids = []
    all_questions_ids = []
    # Names & Labels
    all_var_names = []
    all_cls_labels = []
    all_seqs_names = []
    all_subseqs_names = []
    all_questions_names = []

    for fichier in only_json_files:
        with open(join(target_dir, fichier)) as f:
            print(f"Reading {fichier}")
            data = load(f)
            questionnaire_ids = get_ids(data)
            questionnaire_names = get_names_and_labels(data)
            # IDs
            all_filter_ids = all_filter_ids + questionnaire_ids["filter_ids"]
            all_var_ids = all_var_ids + questionnaire_ids["variables_ids"]
            all_cls_ids = all_cls_ids + questionnaire_ids["codelists_ids"]
            all_seqs_ids = all_seqs_ids + questionnaire_ids["seqs_ids"]
            all_subseqs_ids = all_subseqs_ids + questionnaire_ids["subseqs_ids"]
            all_questions_ids = all_questions_ids + questionnaire_ids["questions_ids"]
            # Names
            all_var_names = all_var_names + questionnaire_names["variables_names"]
            all_cls_labels = all_cls_labels + questionnaire_names["codelists_labels"]
            all_seqs_names = all_seqs_names + questionnaire_names["seqs_names"]
            all_subseqs_names = all_subseqs_names + questionnaire_names["subseqs_names"]            
            all_questions_names = all_questions_names + questionnaire_names["questions_names"]            

    fdups = get_dups(all_filter_ids)
    vdups = get_dups(all_var_ids)
    cdups = get_dups(all_cls_ids)
    sdups = get_dups(all_seqs_ids)
    ssdups = get_dups(all_subseqs_ids)
    qdups = get_dups(all_questions_ids)

    var_names_dups = get_dups(all_var_names)
    cls_labels_dups = get_dups(all_cls_labels)
    seqs_names_dups = get_dups(all_seqs_names)
    subseqs_names_dups = get_dups(all_subseqs_names)
    questions_names_dups = get_dups(all_questions_names)

    # TODO a write / save / report function
    with open(target_dir + "/doublons.md", "w", encoding="UTF-8") as df:
        df.writelines([
            f"Fichiers : {' - '.join(only_json_files)}\n\n",
            "# Doublons IDs \n\n",            
            "## Filtres\n\n",
            f"{', '.join(set(fdups))}\n\n",
            "## Variables\n\n",
            f"{', '.join(set(vdups))}\n\n",
            "## Listes de codes\n\n",
            f"{', '.join(set(cdups))}\n\n",
            "## Séquences\n\n",
            f"{', '.join(set(sdups))}\n\n",
            "## Sous séquences\n\n",
            f"{', '.join(set(ssdups))}\n\n",
            "## Questions\n\n",
            f"{', '.join(set(qdups))}\n\n",
            "# Doublons names & labels\n\n",
            "## Variables\n\n",
            f"{', '.join(set(var_names_dups))}\n\n",
            "## Codelists labels\n\n",
            f"{', '.join(set(cls_labels_dups))}\n\n",
            "## Séquences names\n\n",
            f"{', '.join(set(seqs_names_dups))}\n\n",
            "## Sous Sequences names\n\n",
            f"{', '.join(set(subseqs_names_dups))}\n\n",
            "## Questions names\n\n",
            f"{', '.join(set(questions_names_dups))}\n\n",
        ])


def check_for_orphan_filters(qjson: dict) -> list[str]:
    members = qjson["ComponentGroup"][0]["MemberReference"]
    orphans = []
    for filter in qjson["FlowControl"]:
        m1, m2 = filter["IfTrue"].split("-")
        if m1 not in members or m2 not in members:
            orphans.append(filter["id"])
    return orphans