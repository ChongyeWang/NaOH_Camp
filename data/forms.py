from django import forms


class PostForm(forms.Form):
    
    q1 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "法国的特殊单位是什么？"
        })
    )
    q2 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "伊拉克的特殊单位是什么？"
        })
    )
    q3 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "天启坦克的造价是多少？"
        })
    )

    q4 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "幻影坦克的造价是多少？"
        })
    )

    q5 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "冰天雪地地图中有几个位置？"
        })
    )

    q6 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "冰天雪地地图中2号位在什么位置？（从以下选择: 左上，右上，左下，右下，小岛）"
        })
    )

    q7 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "尤里复仇中盟军开局爆兵压制战术经常用在哪张六人地图中？"
        })
    )
    q8 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "尤里复仇世仇地图中哪个盟军阵营国家有针对伊拉克的卖基地暴兵战术？"
        })
    )
    q9 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "冰天雪地地图中左下位置经常采用几牛抢中的快攻打法？"
        })
    )

    q10 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "拯救行动地图中一共有几个油井？"
        })
    )

    q11 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "中间拥有大面积天然辐射的地图是什么？"
        })
    )

    q12 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "红色警戒时间线中盟军的核武器被谁破坏？（从以下选择：斯大林，爱因斯坦，尤里，伊拉克，谭雅，美国总统，盟军间谍，警犬）"
        })
    )

    q13 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "红色警戒2原版中核弹攻击己方的什么建筑不会造成伤害？"
        })
    )

    q14 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "磁暴线圈非充电状态时在原版和尤里复仇版本中冷却时间（射速）的差值绝对值是多少？"
        })
    )






