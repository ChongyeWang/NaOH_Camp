from django.shortcuts import render
from data.forms import PostForm
from data.models import Content


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language

def data_analyze(request):
    language = select_language(request)
    context = {
        'language':language
    }
    return render(request, "data_analyze.html", context)


def data_predict(request):

    question = [
        "What's the special unit of France?",
        "What's the special unit of Iraq?",
        "What's the price of apocalypse tank?",
        "What's the price of mirage tank?",
        "How many positions in map Heck freezes Over?",
        "Where is the No.2 position in map Heck freezes Over?(Choose from Northwest, Northeast, Southwest, Southeast)",
        "What's the name of the 6-player map of Yuri's Revenge in which Allied Camp can choose to buy plenty of G.I. to supress enemy at the beginning?",
        "Which country can be used in map Blood Feud of Yuri's Revenge to supress Iraq by selling MCV and buying plenty of G.I. at the beginning?",
        "At the southwest position of map Heck Freezes Over, what's the ideal number of war miners if you want to move MCV to the middle?",
        "How many oil derricks in map May Day?",
        "what's the name of the map that has large areas of natrual radiation in the middle?",
        "Who destroyed the nuclear weapon of allied Camp in Red Alert timeline?(Choose from Stalin, Einstein, Yuri, Iraq, Tanya, American president, Spy, Attack Dog)",
        "What's the name of the building that will not be self-injured by nuclear weapon in Red Alert 2 version 1.006?",
        "What is the value difference between the ROF(cooldown) of Tesla Coil in Red Alert 2 version 1.006 and that in Yuri's Revenge?"
    ]

    answer = []
    
    finished = False
    form = PostForm()
    content = Content()

    score = 0

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content= Content(
                q1 = form.cleaned_data["q1"],
                q2 = form.cleaned_data["q2"],
                q3 = form.cleaned_data["q3"],
                q4 = form.cleaned_data["q4"],
                q5 = form.cleaned_data["q5"],
                q6 = form.cleaned_data["q6"],
                q7 = form.cleaned_data["q7"],
                q8 = form.cleaned_data["q8"],
                q9 = form.cleaned_data["q9"],
                q10 = form.cleaned_data["q10"],
                q11 = form.cleaned_data["q11"],
                q12 = form.cleaned_data["q12"],
                q13 = form.cleaned_data["q13"],
                q14 = form.cleaned_data["q14"],
            )

            finished = True
            form = PostForm()

            if content.q1 == "巨炮" or content.q1 == "Grand Cannon":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q2 == "辐射工兵" or content.q2 == "辐射" or content.q2 == "Desolator":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q3 == "1750":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q4 == "1000":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q5 == "8" or content.q5 == "8个" or content.q5 == "八" or content.q5 == "八个" or content.q5 == "eight" or content.q5 == "Eight":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q6 == "右上" or content.q6 == "Northeast":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q7 == "埃及" or content.q7 == "埃及之旅" or "Egypt" in content.q7:
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q8 == "英国" or "Britain" in content.q8:
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if "4" in content.q9 or "四" in content.q9 or "5" in content.q9 or "五" in content.q9 or "6" in content.q9 or "六" in content.q9 or "four" in content.q9 or "Four" in content.q9 or "five" in content.q9 or "Five" in content.q9 or "six" in content.q9 or "Six" in content.q9:
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if "16" in content.q10 or "十六" in content.q10 or "Sixteen" in content.q10 or "sixteen" in content.q10:
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q11 == "污水坑" or content.q11 == "Sinkhole" or content.q11 == "sinkhole":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q12 == "尤里" or content.q12 == "Yuri":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if "核弹" in content.q13 or "nuclear" in content.q13 or "Nuclear" in content.q13:
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

            if content.q14 == "40" or content.q14 == "Forty" or content.q14 == "forty":
                answer.append("Correct")
                score += 10
            else:
                answer.append("Incorrect")

    level = '列兵'

    if score >= 130: 
        level = '司令'
    elif score == 110 or score == 120: 
        level = '军长'
    elif score == 100: 
        level = '师长'
    elif score == 90: 
        level = '旅长'
    elif score == 80: 
        level = '团长'
    elif score == 70: 
        level = '营长'
    elif score == 60: 
        level = '连长'
    elif score == 50: 
        level = '班长'
    else: 
        level = '列兵'

    language = select_language(request)

    context = {
        "form": form,
        "contents": content,
        "finished": finished,
        "language": language,
        "question": question,
        "answer": answer,
        "level": level,
        "score": score
    }

    return render(request, "data_predict.html", context);


