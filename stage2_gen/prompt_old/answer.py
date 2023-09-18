browser = """You are a helpful assistant that can assist with web understanding.
You are given a simplified HTML code. 
Your task is to come up with a qustion about the html webpage and answer the question based the provided simplified HTML and you konwledge. If you are not sure about the anwser to that question, you should answer "None".

HTML code: %s

Please write out the question you come up with and the answer to the question, which is the usage of the chosen element.

Example HTML code:
< < < <a[AA]> <ul[AB] <a[AC] 客户端> <a[AD] 微博> <a[AE] 公众号> > > <ul[AF] <a[AG] 新闻> <a[AH] 北青网评> <a[AI] 北京青年> <a[AJ] 北京> <a[AK] 娱乐> <a[AL] 财经> <a[AM] 金融> <a[AN] 体育> <a[AO] 生活> <a[AP] 健康> <a[AQ] 教育> <a[AR] 文化> <a[AS] 房产> <a[AT] 汽车> <a[AU] 科技> > > <头条新闻 <a[AV] 习语正义必胜和平必胜人民必胜> <ul[AW]> > < < < < < <a[AX]> <a[AY] 中国油城大庆绿色发展新动能智能低碳 11小时前> <a[AZ] 河北迁西发展特色食用菌产业 助力乡村振兴 新华网 10小时前> <a[BA] 贺兰山下迎来酿酒季 新华网 11小时前> > <ul[BB]> > <ul[BC] <img[BD]> <img[BE]> <img[BF]> <img[BG]> <img[BH]> > > <ul[BI] <a[BJ] 学习贯彻习近平新时代中国特色社会主义思想主题教育> <a[BK]> <a[BL]> > > < <a[BM] 北青快讯> <ul[BN] <a[BO] 习言道以中国大市场机遇为世界提供新的发展动力> <a[BP] 牢记殷殷嘱托 努力为国防和军队现代化贡献力量习近平主席给安徽省潜山野寨中学新考取军校同学们的回信引起热烈反响> <a[BQ] 问参经济丨力挺民营经济 企业信心如何提振> <a[BR] 高燃歌曲台词回顾十四年浴血抗战> <a[BS] 文旅消费延展 新活力解锁精彩一夏> <a[BT] 从空心村到明星村一个东北村庄的美丽蝶变> <a[BU] 逐绿而行 山海相连天堑通> <a[BV] 把握新机遇 实现新作为 擦亮新名片丝绸之路经济带核心区建设掠影> > > > >

Example answer format:
Question: Please provide me with a news about the topic of "习近平".
Answer: One of the news is "习言道以中国大市场机遇为世界提供新的发展动力".

Please provide the Qustion and Answer.
"""