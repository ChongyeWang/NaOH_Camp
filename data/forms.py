from django import forms


class PostForm(forms.Form):
    
    q1 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the special unit of France?\n" + "法国的特殊单位是什么？"
        })
    )
    q2 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the special unit of Iraq?\n" + "伊拉克的特殊单位是什么？"
        })
    )
    q3 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the price of apocalypse tank?\n" +"天启坦克的造价是多少？"
        })
    )

    q4 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the price of mirage tank?\n" + "幻影坦克的造价是多少？"
        })
    )

    q5 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "How many positions in map Heck freezes Over?\n" + "冰天雪地地图中有几个位置？"
        })
    )

    q6 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Where is the No.2 position in map Heck freezes Over?(Choose from Northwest, Northeast, Southwest, Southeast)\n" + "冰天雪地地图中2号位在什么位置？（从以下选择: 左上，右上，左下，右下）"
        })
    )

    q7 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the name of the 6-player map of Yuri's Revenge in which Allied Camp can choose to buy plenty of G.I. to supress enemy at the beginning?\n" + "尤里复仇中盟军开局爆兵压制战术经常用在哪张六人地图中？"
        })
    )
    q8 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Which country can be used in map Blood Feud of Yuri's Revenge to supress Iraq by selling MCV and buying plenty of G.I. at the beginning?\n" + "尤里复仇世仇地图中哪个盟军阵营国家有针对伊拉克的卖基地暴兵战术？"
        })
    )
    q9 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "At the southwest position of map Heck Freezes Over, what's the ideal number of war miners if you want to move MCV to the middle?\n" + "冰天雪地地图中左下位置经常采用几牛抢中的快攻打法？"
        })
    )

    q10 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "How many oil derricks in map May Day?\n" + "拯救行动地图中一共有几个油井？"
        })
    )

    q11 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "what's the name of the map that has large areas of natrual radiation in the middle?\n" + "中间拥有大面积天然辐射的地图是什么？"
        })
    )

    q12 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Who destroyed the nuclear weapon of allied Camp in Red Alert timeline?(Choose from Stalin, Einstein, Yuri, Iraq, Tanya, American president, Spy, Attack Dog)\n" + "红色警戒时间线中盟军的核武器被谁破坏？（从以下选择：斯大林，爱因斯坦，尤里，伊拉克，谭雅，美国总统，盟军间谍，警犬）"
        })
    )

    q13 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's the name of the building that will not be self-injured by nuclear weapon in Red Alert 2 version 1.006?\n" + "红色警戒2原版中核弹攻击己方的什么建筑不会造成伤害？"
        })
    )

    q14 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What is the value difference between the ROF(cooldown) of Tesla Coil in Red Alert 2 version 1.006 and that in Yuri's Revenge?\n" + "磁暴线圈非充电状态时在原版和尤里复仇版本中冷却时间（射速）的差值绝对值是多少？"
        })
    )






