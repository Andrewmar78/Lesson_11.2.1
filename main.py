from utils import candidates_json_list, profile, profile_by_name, candidate_by_skills
from configure import path_all_candidates_datas
from flask import Flask, render_template

app = Flask(__name__)

data = candidates_json_list(path_all_candidates_datas)


# Страничка всех кандидатов
@app.route("/")
def main_page():
    return render_template("list.html", candidates=data)


# Страничка данных выбранного по id кандидата, если он есть
@app.route("/candidates/<int:candidate_id>")
def candidate_page(candidate_id):
    candidate = profile(candidate_id)
    return render_template("single.html", candidate=candidate)


# Страничка данных выбранного по имени кандидата, если он есть
@app.route("/search/<name>")
def candidate_page_by_name(name):
    candidates = profile_by_name(name)
    print(candidates)
    return render_template("search.html", candidates=candidates, candidates_length=len(candidates))


# Страничка списка кандидатов по выбранному навыку, если такой навык есть
@app.route("/skills/<skill>")
def candidate_by_skills(skill):
    candidates = candidate_by_skills(skill)
    return render_template("skills.html", candidates=candidates, candidates_length=len(candidates), skill=skill)


# Запуск сервера
app.run()
