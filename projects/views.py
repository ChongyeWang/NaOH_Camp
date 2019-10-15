from django.shortcuts import render

from projects.models import Project

def home(request):

    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]
        
    context = {
        'language': language
    }
    
    return render(request, 'home.html', context)

def setting(request):

    if request.method == 'POST':
        selection = request.POST['selection']
        request.session[request.user.username] = selection

    context = {
        'language': request.session[request.user.username]
    }
    return render(request, 'setting.html', context)

def project_index(request):
    Project.objects.all().delete()
    # p1 = Project(
    #     title='背景资料',
    #     description='斯大林死後，美國扶植洛馬諾夫為傀儡蘇聯部長會議主席（總理）。但是洛馬諾夫趁墨西哥民眾引發暴動時，傾全國之兵攻擊美國。美國總統杜根得知此事後，撥通了洛馬諾夫的專線，卻被他冷嘲熱諷一番。杜根授權卡維利將軍使用戰略核導彈向蘇聯還擊。在導彈已經點火之際，尤里心靈控制了美國導彈控制台的技術人員，阻止了發射井的開啟，致使導彈在井中爆炸。喪失了戰略打擊能力的美國，完全向蘇聯軍隊敞開了大門。龐大的基洛夫飛艇將紐約曼哈頓島籠罩在陰影之中，威昂的無畏級戰艦將導彈射向高聳的摩天大樓，天啟坦克壓碎了「文明駕駛」的路牌，挺進了德州。而美國的象徵——自由女神像，早已被蘇軍的无畏级战舰打掉了頭顱，而整個美國也因此陷入了風雨飄搖之中',
    #     technology="""盟軍劇情\n盟軍劇情由一支以特務譚雅帶領的特種部隊被送到紐約開始，對抗蘇聯入侵。指揮官（玩家）在譚雅的幫助下，順利地消滅在紐約的蘇聯軍隊。譚雅和指揮官然後派遣到科罗拉多斯普林斯解放那裡的美國空軍學院和空軍基地。同時，蘇聯在華盛頓特區部署了一個名為「心靈信標」的設備。心靈信標能控制整個城市人口的心靈，蘇聯設法控制美國總統和華盛頓的主要官員，讓美國向蘇聯投降。然而，一次由指揮官指揮的反擊破壞了心靈信標。美國政府迅速遷移到加拿大，以逃脫蘇聯心靈控制的威脅。遷移政府到加拿大後，盟軍情報發現蘇聯在芝加哥部署了另一個心靈控制設備，「心靈控制增幅器」，它是一個有能力控制整個北美洲的大型設備。盟軍從加拿大動員部隊，橫跨密西根湖，展開渡湖的兩棲攻擊，闖入被蘇聯佔領的芝加哥，解放城市和毀壞心靈控制增幅器。為了報復，蘇聯軍隊的最高司令維拉迪摩將軍，宣稱芝加哥對他已經沒有用，並且對芝加哥發動一次核攻擊，完全摧毀芝加哥。芝加哥的核攻擊驚動了歐洲，法國、德國和英國同意幫助美國，但要求美國軍隊先破壞位於波蘭的兩座蘇聯核彈發射井。美國總統麥可·杜根同意，送由譚雅帶領的一隊特種部隊，進入波蘭與德國的邊界。特種部隊成功摧毀了發射井，并且歐洲加入對抗蘇聯的戰爭。得到額外的士兵和軍備支持，美軍能展開對被蘇聯佔領的華盛頓特區的一次兩棲攻擊和奪回城市。在奪回華盛頓以後，盟軍情報顯露蘇聯計劃奪取夏威夷海島，并且指揮官派遣到珍珠港保衛海島。夏威夷的危機解除，但是美國仍然在一個飄搖的位置。蘇聯在心靈信標幫助下，控制密西西比河南部的聖路易斯，嚴重妨礙美國發動地面作戰的能力。因此盟軍對城市展開攻擊，毀壞心靈信標和解放城市。盟軍也得知蘇聯在墨西哥图卢姆的研究基地企圖複製光棱技術。因此派遣一支海豹部隊摧毀該研究基地設施，蘇聯的企圖失敗。卡維利將軍在一次對指揮官的簡報中，說他們要前往德國。他說盟軍領導會派出部隊到德國黑森林保護愛因斯坦實驗室。愛因斯坦的實驗室有超時空傳送儀的原型，一個能夠運輸部隊到世界上任何地方的設備。在卡維利將軍離開辦公室的時候，瘋狂伊文在等待卡維利並引爆炸彈，暗殺了卡維利將軍。指揮官派遣到黑森林並對付蘇聯軍隊。愛因斯坦實驗室和超時空傳送儀安然無恙，愛因斯坦繼續他的工作。在此以後，愛因斯坦親自感謝指揮官，說他發現了最佳部署超時空傳送儀的地方。它是在一個在佛羅里達礁島群的小島，而且離古巴只有幾公里。盟軍派軍隊到小島駐軍并且在那裡建造基地和超時空傳送儀，然後進入古巴摧毀三座蘇聯核彈發射井。指挥官继任盟军总司令，盟軍使用超時空傳送儀的遠距傳物能力把一隊盟軍突擊隊帶到莫斯科。盟軍其後在克里姆林宮附近，發動突襲摧毀防禦，然後譚雅立刻俘虜了洛馬諾夫主席。蘇聯向盟軍投降。但是作為挑起這場戰爭的幕後黑手的尤里卻不知所蹤……而最後，譚雅會以身穿著禮服邀請指揮官和自己共同參加總統在白宮設下的晚宴...... 
    #     """ + '\n' + 
    #     """蘇軍劇情\n苏联在华盛顿哥伦比亚特区上空大量空投伞兵，部署了基地，利用强大的地面力量，迅速摧毁了五角大楼。初期的胜利加大了苏联的野心，苏军希望摧毁美军位于佛罗里达的海军基地，以为全线登陆做准备。在中途弗拉基米尔声称“用一只橡皮鸭就可以消灭美国海军”，但是自行前行遇到美国海军驱逐舰拦截时却先逃走了。随后一批苏联潜艇前来支援，帮助玩家成功地摧毁了美海军基地。弗拉基米尔先行回国，罗曼诺夫听到捷报后很高兴，并且给弗拉基米尔颁发了斯大林奖章。尤里知道后很生气，对弗拉基米尔心生恨意，但暂时又无可奈何。尤里当时正在研发“心灵信标”，但是他需要盟军科技。苏联红军开进纽约，工程师占领了纽约的作战实验室，心灵信标在纽约被建起，随后当地所有美军全部宣誓加入苏军。美军节节败退，韩国表示願意提供支援，并派兵入侵苏联海参崴。尤里和罗曼诺夫正在讨论派遣哪位指挥官。罗曼诺夫主张派遣弗拉基米尔去，尤里便打开电视，看见弗拉基米尔正在与几个女人泡温泉。玩家被派往前线，同时一种叫“恐怖机器人”的新武器也开始投入实战，这种轻型机器人可以将坦克变成碎片，但是装甲很薄。因为新武器的采用，韩国军队很快被赶回大海。美军在重压之下，向欧洲盟友求援。欧洲盟友承诺出兵，但是这也导致了这些盟友内部防御力量的亏空。苏军这时乘虚而入，用一支小分队侵入巴黎，并且用磁暴步兵磁化了埃菲尔铁塔。巴黎的盟军很快被击溃。苏军节节挺进，但尤里与弗拉基米尔的关系却不断恶化。在苏军全歼韩国海军并且占领夏威夷后，两人彻底闹翻，罗曼诺夫因为“健康问题”又一直不在，尤里成为苏军最高司令，实际上担当苏联部长会议主席（总理）职务。盟军将要用超时空传送仪入侵苏联位于乌拉尔山的实验室，那里正在研发天启坦克。超时空传送仪由爱因斯坦建造，而爱因斯坦对尤里的心灵控制先天免疫。后来天启坦克被生产出来，用车载对空飞弹和双管主炮守住了实验室。尤里声称罗曼诺夫主席被“叛徒”弗拉基米尔将军杀害（实际是尤里所为并嫁祸弗拉基米尔），命令玩家追杀弗拉基米尔。弗拉基米尔逃到蘇佔美国华盛顿，但是被尤里的心灵控制所感应出。玩家率领苏军又一次开进华盛顿，白宫被苏军摧毁，苏军从废墟中找出了弗拉基米尔，但是还没等到弗拉基米尔解释时他便已经被心灵控制并被当场处决。尤里此时发现美国总统杜根已经退到了得克萨斯州圣安东尼奥的阿拉莫。周围由重兵把守，从警犬到海豹部队应有尽有。苏军试图空降部队俘获杜根，但没有成功。尤里想到即使把杜根抓住也不会屈服，不如直接把他心灵控制。于是，蘇聯改而派出「超能力部队」——尤里的复制人，最终成功控制了杜根。接着，尤里发现美军在中美洲的美属维尔京群岛測試天气控制仪，这个由爱因斯坦发明的仪器可以产生强大的闪电风暴。尤里批准玩家使用核弹，苏联工程师占领了那里的作战实验室，取得了天气控制仪的坐标。最终天气控制仪被摧毁，苏联统治全球只是时间问题了。尤里突然请玩家到莫斯科，表示要亲自接见。通讯官佐菲雅此时突然收到一卷录像带，是罗曼诺夫主席生前的一段訊息，罗曼诺夫表示尤里心灵控制了他，并且「杀害」了他。玩家率领苏军进攻莫斯科，叛国的尤里所藏匿的克里姆林宫最终变成废墟，尤里被埋于废墟之下，玩家继任苏军最高司令。索菲亚在整理尤里的档案时发现，尤里留下了一份「离别礼物」：盟军在阿拉斯加的希望之角有一部超时空传送仪，并且有重兵把守。苏军跨海作战，顺利登陆，摧毁了盟军最后一座的超时空传送仪。盟军战败，玩家成为新一任苏联部长会议主席（总理）甚至是“世界总理”，成为世界的统治者。苏军在伦敦、巴黎等全球各地进行盛大阅兵，欢庆「共产主义」的到来，玩家在巴黎凯旋门前香榭丽舍大街的阅兵式上现身。但是，有一个很大的后患，尤里运用复制中心，复制出了无数个自己…… """
    #     ,
    #     image='img/background.png'
    # )
    # p1.save()

    # p2 = Project(
    #     title = "游戏设定",
    #     description = "游戏内的场景地图包括岛屿，山地，平原三种类型。玩家在地图中作战，在平地上可以建造建筑。山地可以当做自然防御的屏障。水域可能会出现海战。在部分地区可能有采矿场，玩家可以指挥采矿车到采矿场。玩家可以战斗开始前对兵种进行编队、规划路线。玩家一开始只有基地内的视野，并且没有小地图，必须要建造雷达或者空指部才能获得包含迷雾的小地图，单位探路和间谍卫星、心灵感应器可以去除迷雾。除了裂缝产生器的效果外，迷雾一旦去除，永久可见。裂缝产生器所产生的迷雾只能通过单位探路去除，如果敌人来侦察，裂缝会在敌人视野中消失，在敌人离开后会重新制造裂缝。",
        # technology = """盟军阵营：\n\n美国大兵：盟军的基本作战单位。可以通过部署来增加射程和对装甲单位的攻击力，但部署会丧失匍匐能力。
        #         工程师：支援单位。可以修缮桥梁、建筑、拆除疯狂伊文的炸弹，或者将敌方建筑占为己有。
        #         警犬：侦察单位与反步兵单位。优秀的德国牧羊犬，能够识别间谍，秒杀步兵。
        #         火箭飞行兵：   火箭飞行兵纯粹只是盟军美国大兵的空中攻擎版本。装备强力武器，身上捆绑一具同样火力十足的喷射包，能盘旋于战场上空。火箭飞行兵是绝佳的防空军种，也是空对地攻击脆弱目标的好选择。
        #         间谍：      间谍并不攻击敌方部队，而是选择锁定敌人之后，改变自己的外观，潜入越过敌军防线，进入敌方建筑物。间谍的功能视其所进入的建筑物而定，不过警犬并不会被间谍的伪装所惑。
        #         海豹部队：    装备了高效能的机关枪，海豹部队在对付敌人步兵单位的时候相当有效，而且在面对交通工具的时候也可以保护自己。就跟谭雅一样，海豹部队使用C4地雷来破坏敌人的建筑物。
        #         超时空军团兵：  超时空军团兵会瞬间移动，瞬移距离会决定他需要多久时间才能进行下一次传送。超时空军团会直接将敌方部队、建筑物自时空中抹消，而不是将之摧毁。敌人的威力愈强大，所需的时间就愈久。
        #         谭雅：      谭雅的行进速度与一般美国大兵相同，但她也具备游泳穿越河川、海洋的能力。擅长宰杀敌方步兵和摧毁建筑。
        #         狙击手：     狙击手是英国的特殊步兵单位，能在远处秒杀步兵，进入多功能步兵车后移动速度和射速都会有所提高。苏联阵营的恐怖机器人是狙击手的克星。
        #         心灵突击队：   特殊单位，需要侵入苏联作战实验室并拥有盟军军营。同时具备尤里的心灵控制能力和海豹部队的C4炸药。
                
        #         超时空突击队：  特殊单位，需要侵入盟军作战实验室并拥有盟军军营。是具有超时空传送能力的海豹部队。
        #         超时空采矿车：  盟军的采矿车，在返回矿场时可以超时空传送回去。
        #         灰熊坦克：    盟军的主战坦克。拥有较高的机动性和较低的造价。
        #         多功能步兵车：  盟军的防空单位。可通过进入步兵来变更武器。
        #         幻影坦克：    幻影坦克是爱因斯坦在德国黑森林中研发的一种坦克，是盟军的王牌之一。虽然它无法隐形，但却可以利用先进的光线偏折原理伪装自己。和光棱坦克配合往往能发挥出更加强大的作用。其弱点为容易被尤里心灵控制。
        #         光棱坦克：    盟军的王牌坦克之一，可以说是一座会移动的光棱塔。适合攻击步兵和建筑物，群攻威力十分强悍。但它的装甲薄，速度慢，对坦克单位效果差，所以不适于攻击坦克单位以及单独作战。在幻影坦克的掩护下行动起来会更加便利。
        #         坦克杀手：    坦克杀手是德国的特色武器，坦克的克星，但是对建筑与步兵效果很不理想，因此大大削弱了它的利用价值。其原型为以色列梅卡瓦主战坦克，但是与“梅卡瓦主战坦克”不同的是它并没有可旋转炮塔。
        #         MCV： 盟军的机动工程车，可以展开为盟军建造厂。
                
        #         夜鹰直升机：   盟军的空中运输单位，拥有一定的自卫能力。
        #         入侵者战机：   盟军的空中轰炸单位，能够有效打击地面单位。
        #         黑鹰战机：    黑鹰战机是韩国特有空军单位，停在空指部。可以有效对敌实行空对地打击。生命力、攻击力大于入侵者战机，速度、造价和入侵者相同。
                
        #         两栖运输艇：   两栖运输单位，没有自卫能力。
        #         驱逐舰： 盟军海军的主要作战单位，搭载155 mm加农炮和“鱼鹰”反潜机。
        #         神盾巡洋舰：   盟军海军的防空单位，具有优秀的防空能力。
        #         海豚：  盟军海军的支援单位，对抗巨型乌贼的利器。
        #         航空母舰：    顾名思义，它是于甲板上停放战机，并用以攻击目标的大型船舰。航空母舰上搭载的战机会降落，重新装载弹药，再继续攻击到完全摧毁选定目标才罢休。更棒的是，航空母舰上所有损失的战机毋须消耗任何资源即可自动补充。
        #         \n
        #         \n
        #         苏军阵营：\n
        #         动员兵： 苏军的基本作战单位，造价低廉易于形成 人海战术。
        #         工程师： 支援单位。可以修缮桥梁、建筑、拆除疯狂伊文的炸弹，或者将敌方建筑占为己有。
        #         警犬：  侦察单位与反步兵单位。优秀的西伯利亚爱斯基摩犬，能够识别间谍，秒杀步兵。
        #         防空步兵：    苏军的防空单位，对抗步兵也十分有效。
        #         磁爆步兵：    又称“杨永信”，这种特殊的步兵部队，以强力的磁能波攻击，这种磁能波是由其身上装备的可携式磁能线圈所产生。磁爆步兵不但不会被坦克辗毙，而且还能替基地的磁能线圈充能，并增强其攻击范围及威力。
        #         辐射工兵：    伊拉克的特殊兵种，以强力的辐射杀死对手的步兵、装甲车辆、生物、海军、以及停靠在地面上的空军单位。可以部署，部署后在四周形成一圈绿色辐射层，能对大部分敌人造成杀伤。缺点是造价高，且容易误伤友军。
        #         疯狂伊文：    疯狂伊文是用来称呼苏联爆破专家的代号，他可以在地图上安置炸药进行攻击。几乎所有东西都可以引爆，从敌方建筑物到个别的士兵，就连闲晃的乳牛也不例外。装置炸药之后，会先倒数计恃再引爆。疯狂伊文也能在桥头维修小屋里装置炸药，摧毁桥梁。
        #         恐怖分子：    古巴特色兵种，通过接近敌方然后自爆来造成伤害。
        #         超能力部队/尤里：    尤里具备心灵控制大部分敌方部队、车辆的能力。敌方车辆或人员一旦遭到心灵控制，就会立刻变成你的战力，可以如同自己建造的部队般下令他移动攻击。假如尤里遇害了，则与这个受控制的部队连系即告中止。
        #         尤里改： 特殊单位，需要侵入苏联作战实验室并拥有苏军军营。仅限造1个（可克隆），拥有超远的心灵控制能力和心灵爆破能力。
        #         超时空伊文：   特殊单位，需要侵入盟军作战实验室并拥有苏军军营。拥有超时空传送能力的疯狂伊文。
        #         菁英战斗兵：   菁英战斗兵对付步兵单位相当有效率。虽然不会用C4炸药破坏建筑物，但是菁英战斗兵可以呼叫米格战斗机轰炸他用雷射指示的建筑物。
                
        #         武装采矿车：   苏军的采矿车，车顶搭载了一个机炮。
        #         犀牛坦克：   苏军的主战坦克，牺牲机动性但拥有较高的装甲。
        #         防空履带车：   苏军的防空单位，同时具备运输步兵的能力。
        #         恐怖机器人：   恐怖机器人是坦克的克星（包括坦克杀手），速度快，攻击力强。攻击方式是跳起，钻入坦克后蓄电摇动坦克以攻击坦克或跳起飞过后秒杀步兵。被寄生的战车只能放入维修站、科技前哨站或被多功能修理车进行维修。缺点是防守差，对建筑物无攻击力。
        #         V3火箭发射车： 苏军的攻城单位，可以从极远的距离发射给予打击。
        #         磁能坦克：    苏俄特有的反装甲坦克，可以越过围墙发动攻击。
        #         自爆卡车：    利比亚特有的自爆载具，通过自爆造成伤害并在一定范围洒下核辐射。
        #         MCV： 苏军的机动工程车，可以展开为苏联建造厂。
        #         天启坦克：    苏联的究极坦克兵种。天启本身是辆大型车辆，能承受大规模攻击，屹立不摇。这种坦克能用来攻击地面及空中目标，擅长攻击坦克和建筑。多辆天启坦克在一起防空能力较强。                          
                
        #         基洛夫空艇：   苏军的空军单位。这款巨型苏联齐柏林飞艇以密集投掷大型炸弹来攻击，攻击力惊人。一架3级飞艇能秒杀地面建筑，并且炸毁各种设施。缺点是只能对地攻击，没有防空力量，且移动速度十分慢。
        #         米格战机：    辅助攻击的一种单位。米格无法建造，只能通过菁英战斗兵召唤。

        #         装甲运兵船：   两栖运输单位，没有自卫能力。
        #         台风级攻击潜艇： 苏联海军的主要作战单位，在没有反潜单位的情况下能够悄无声息地发动攻击。
        #         海蝎：  苏联海军的防空单位，拥有极高的射速。
        #         巨型乌贼：    苏联科学家掳获、并加以训练的巨型乌贼。它具有紧紧抓住敌方船舰，再用威力强大的触手将之撕裂成碎片的能力。巨型乌贼是匿踪部队，不会出现在敌方雷达上。
        #         无畏级战舰：   这种大型战舰在攻击敌方船舰及地面设施上效果卓越。以威力强大的长程飞弹发动攻击，使得敌人难以靠近还击。  
        #         \n\n
    #             """,
        
    #     image='img/a2.jpg'
    # )
    # p2.save()
    

    # p3 = Project(
    #     title='游戏平台下载',
        
    #     description= """战网平台: """ + 'http://www.ra2ol.com/' + '\n' + \
    #                 """CnCNet: """ + 'https://cncnet.org/yuris-revenge\n' + \
    #                 """游戏下载: http://www.uc129.com/xiazai/
    #                 腾讯对战平台: https://dz.qq.com/
    #                 """,
    #     technology='',
    #     image='img/project1.png'
    # )
    # p3.save()

    # p4 = Project(
    #     title='任务战役',
    #     description='',
    #     technology='',
    #     image='img/a5.jpg'
    # )
    # p4.save()

    # p5 = Project(
    #     title='地图池',
    #     description='',
    #     technology='',
    #     image='img/heckfreeze.jpg'
    # )
    # p5.save()

    # p6 = Project(
    #     title='对战教学',
    #     description='',
    #     technology='',
    #     image='img/a1.jpg'
    # )
    # p6.save()

    # p7 = Project(
    #     title='历史资料',
    #     description='',
    #     technology='',
    #     image='img/history.jpg'
    # )
    # p7.save()

    # p8 = Project(
    #     title='MOD介绍',
    #     description='',
    #     technology='',
    #     image='img/mod.jpg'
    # )
    # p8.save()

    # p9 = Project(
    #     title='番外',
    #     description='',
    #     technology='',
    #     image='img/c2.jpg'
    # )
    # p9.save()

    # p3 = Project(
    #     title='My Third Project',
    #     description='A final development project.',
    #     technology='Django',
    #     image='img/project3.png'
    # )
    # p3.save()
    
    #projects = Project.objects.all()

    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]
        
    context = {
        #'projects': projects,
        'language': language
    }
    return render(request, 'project_index.html', context)


def background(request):
    return render(request, 'background.html', {})


def game_setting(request): 
    return render(request, 'game_setting.html', {})


def download(request):
    return render(request, 'download.html')

# def project_detail(request, pk):
#     project = Project.objects.get(pk=pk)
#     language = 'English'
#     if request.user.is_authenticated:
#         if request.session.get(request.user.username, None) == None:
#             request.session[request.user.username] = 'Chinese'
#         language = request.session[request.user.username]
#     context = {
#         'project': project,
#         'language': language
#     }
#     return render(request, 'project_detail.html', context)