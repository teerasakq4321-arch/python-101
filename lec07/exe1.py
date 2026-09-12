survey_results = [
    ["Python", "JavaScript", "C++"],              # Participant 1
    ["Python", "JavaScript", "C#"],               # Participant 2
    ["Python", "Java"],                           # Participant 3
    ["Python", "C++", "JavaScript"],              # Participant 4
    ["Python", "JavaScript", "C++", "Java"]       # Participant 5
]

paticipant_set = [set(result) for result in survey_results]

chose_by_all = set.intersection(*paticipant_set)

all_languages = set.union(*paticipant_set)

survey_count = {}
for result in paticipant_set:
    for language in result:
        survey_count[language] = survey_count.get(language, 0) + 1
uniqe_language = {
    language
    for language, count in survey_count.items()
    if count == 1
}

num_uniqe_language = len(all_languages)

chose_by_two = {
    language
        for language, count in survey_count.items()
        if count == 2
}

print(chose_by_all)
print(uniqe_language)
print(num_uniqe_language)
print(chose_by_two)



