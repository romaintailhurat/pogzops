def save(questionnaire_json, id, save_dir):
    file_path = f"{save_dir}/{id}.pogues.json"
    with open(file_path, "w", encoding="UTF-8") as f:
        f.writelines(questionnaire_json)