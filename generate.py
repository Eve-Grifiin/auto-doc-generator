def generate_doc():
    # 获取用户输入
    user_input = os.environ['ISSUE_BODY']
    
    # 调用AI生成内容
    time = ask_ai("生成观察时间")
    location = ask_ai("生成观察地点")
    observer = ask_ai("生成观察者姓名")
    target = ask_ai("生成观察对象")
    background = ask_ai(f"生成观察背景，主题：{user_input}")
    record = ask_ai(f"生成观察记录，主题：{user_input}")
    analysis = ask_ai(f"生成分析评价，主题：{user_input}")
    strategy = ask_ai(f"生成支持策略，主题：{user_input}")
    reflection = ask_ai(f"生成我的反思，主题：{user_input}")
    
    # 处理文档
    doc = Document('一对一倾听表模板.docx')
    for para in doc.paragraphs:
        if '{{时间}}' in para.text: para.text = time
        if '{{地点}}' in para.text: para.text = location
        if '{{观察者}}' in para.text: para.text = observer
        if '{{观察对象}}' in para.text: para.text = target
        if '{{观察背景}}' in para.text: para.text = background
        if '{{记录}}' in para.text: para.text = record
        if '{{分析评价}}' in para.text: para.text = analysis
        if '{{支持策略}}' in para.text: para.text = strategy
        if '{{我的反思}}' in para.text: para.text = reflection
    doc.save('output.docx')
