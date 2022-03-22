import json

__all_candidates_datas = []


# Получение списка кандидатов из файла
def candidates_json_list(path):
    global __all_candidates_datas
    with open(path, "r", encoding="utf-8") as file:
        __all_candidates_datas = json.load(file)
        # print("Полный список", __all_candidates_datas)
    return __all_candidates_datas


def profile(candidate_id):
    for candidate in __all_candidates_datas:
        if candidate["id"] == candidate_id:
            # print(candidate["name"], candidate["position"], candidate["picture"], candidate["skills"])
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"],
            }
    return {"not_found": "Такого кандидата нет"}


def profile_by_name(candidate_name):
    for candidate in __all_candidates_datas:
        if candidate_name.lower() in candidate["name"].lower():
            return candidate


def candidate_by_skills(skill_name):
    candidates = []
    for candidate in __all_candidates_datas:
        skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates


# Проверка
# candidates_json_list("candidates.json")
# profile(3)
profile_by_name("A")
candidate_by_skills("Go")
