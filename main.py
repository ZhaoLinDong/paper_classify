
store=[]

class Paper:

    def __init__(self,paper_name,push_time,paper_source,paper_type):
        '''
        论文名称 paper_name
        发表时间 push_time
        发表来源 paper_source
        论文种类 paper_type
        '''
        self.paper_name=paper_name
        self.push_time=push_time
        self.paper_source=paper_source
        self.paper_type=paper_type

    def paper_input(paper_name,push_time,paper_source,paper_type):
        svg=[paper_name,push_time,paper_source,paper_type]
        store.append(svg)
        print(f'成功存储 {paper_name},{push_time},{paper_source},{paper_type}')

    def paper_visit(paper_load=[]):
        length= len(paper_load)
        for i in range(length):
            print(paper_load[i])





var = 1
while var == 1:
    print('菜单'
          '1.添加文献'
          '2.查看当前文献库'
          '3.检索文献'
          '4.删除文献'
          '5.退出')

    select = int(input())
    if select == 1:
        print(f'输入论文名称，发表时间，论文来源，论文类型')
        paper_name = input()
        push_time = input()
        paper_source = input()
        paper_type = input()
        Paper.paper_input(paper_name, push_time, paper_source, paper_type)
    if select == 2:
        Paper.paper_visit(store)


    if select == 5:
        break











