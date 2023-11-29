"""
High-level operations on Pogues questionnaires.

Combines low-level functions of the remote package.
"""
from models.envs import PoguesEnv
from remote.get import get_questionnaire
from remote.update import update_questionnaire
from remote.create import create_questionnaire
from models.status import Status, Success, Failure
from models.questionnaire import get_ids, get_names_and_labels, get_dups


# --- Updating questionnaires
def change_stamp(id: str, stamp: str, env: PoguesEnv) -> Status:
    """
    Update the stamp for a given questionnaire id in the same environment.
    """
    status = get_questionnaire(id, env)
    qjson = status.payload

    if type(status) is Success:
        qjson["owner"] = stamp

    return update_questionnaire(qjson, id, env)


def create_or_update(questionnaire_json: dict, id: str, env: PoguesEnv) -> Status:
    """
    TODO update then create OR create then update ?
    TODO in some cases, update a non existing questionnaire yield a 500 not the expected 404
    """
    update_status: Status = update_questionnaire(questionnaire_json, id, env)

    if type(update_status) is Failure:
        create_status: Status = create_questionnaire(questionnaire_json, id, env)
        return create_status
    else:
        return update_status


# --- From one env to the other
def copy(
    id: str, source_env: PoguesEnv, target_env: PoguesEnv, stamp: str = None
) -> Status:
    """
    Copy a questionnaire from one env to the other.
    The source questionnaire is not deleted.
    """
    get_status = get_questionnaire(id, source_env)
    if type(get_status) is Success:
        qjson = get_status.payload
        if stamp is not None:
            qjson["owner"] = stamp
        ping = get_questionnaire(id, target_env)  # check if questionnaire exists
        if type(ping) is Success:
            print("Questionnnaire exists, updating it.")
            update_status = update_questionnaire(qjson, id, target_env)
            return update_status
        else:
            print("Questionnaire doesn't exist, copying it.")
            create_status = create_questionnaire(qjson, id, target_env)
            return create_status
    else:
        return get_status


def move(id: str, source_env: PoguesEnv, target_env: PoguesEnv) -> Status:
    """
    Move a questionnaire from one env to the other.
    The source questionnaire is deleted.
    """
    pass


def check_duplicates_from_api(ids: list[str], env: PoguesEnv):
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

    for id in ids:
        result = get_questionnaire(id, env)
        if type(result) is Success:
            json = result.payload
            questionnaire_ids = get_ids(json)
            questionnaire_names = get_names_and_labels(json)
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
            all_questions_names = (
                all_questions_names + questionnaire_names["questions_names"]
            )

    duplicates = {}

    duplicates["filter_ids"] = get_dups(all_filter_ids)
    duplicates["variables_ids"] = get_dups(all_var_ids)
    duplicates["codelists_ids"] = get_dups(all_cls_ids)
    duplicates["sequences_ids"] = get_dups(all_seqs_ids)
    duplicates["subsequences_ids"] = get_dups(all_subseqs_ids)
    duplicates["questions_ids"] = get_dups(all_questions_ids)

    duplicates["variables_names"] = get_dups(all_var_names)
    duplicates["labels_names"] = get_dups(all_cls_labels)
    duplicates["sequences_names"] = get_dups(all_seqs_names)
    duplicates["subsequences_names"] = get_dups(all_subseqs_names)
    duplicates["questions_names"] = get_dups(all_questions_names)

    return duplicates
