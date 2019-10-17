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
        "法国的特殊单位是什么？",
        "伊拉克的特殊单位是什么？",
        "天启坦克的造价是多少？",
        "幻影坦克的造价是多少？",
        "冰天雪地地图中有几个位置？",
        "冰天雪地地图中2号位在什么位置？（从以下选择: 左上，右上，左下，右下，小岛）",
        "尤里复仇中盟军开局爆兵压制战术经常用在哪张六人地图中？",
        "尤里复仇世仇地图中哪个盟军阵营国家有针对伊拉克的卖基地暴兵战术？",
        "冰天雪地地图中左下位置经常采用几牛抢中的快攻打法？",
        "拯救行动地图中一共有几个油井？",
        "中间拥有大面积天然辐射的地图是什么？",
        "红色警戒时间线中盟军的核武器被谁破坏？（从以下选择：斯大林，爱因斯坦，尤里，伊拉克，谭雅，美国总统，盟军间谍，警犬）",
        "红色警戒2原版中核弹攻击己方的什么建筑不会造成伤害？",
        "磁暴线圈非充电状态时在原版和尤里复仇版本中冷却时间（射速）的差值绝对值是多少？"
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

            if content.q1 == "巨炮":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q2 == "辐射工兵" or content.q2 == "辐射":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q3 == "1750":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q4 == "1000":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q5 == "8" or content.q5 == "8个" or content.q5 == "八" or content.q5 == "八个":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q6 == "右上":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q7 == "埃及" or content.q7 == "埃及之旅":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q8 == "英国":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if "4" in content.q9 or "四" in content.q9 or "5" in content.q9 or "五" in content.q9 or "6" in content.q9 or "六" in content.q9:
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if "16" in content.q10 or "十六" in content.q10:
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q11 == "污水坑":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q12 == "尤里":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if "核弹" in content.q13:
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

            if content.q14 == "40":
                answer.append("正确")
                score += 10
            else:
                answer.append("错误")

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
        "level": level
    }

    return render(request, "data_predict.html", context);


