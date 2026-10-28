
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
        print(f'成功存储{paper_name},{push_time},{paper_source},{paper_type}')

    def paper_visit(paper_load=[]):
        length= len(paper_load)
        for i in range(length):
            print(f'{i},{paper_load[i]}')

    def paper_search(name):
        length = len(store)
        for i in range(length):
            if name == store[i][0]:
                print(store[i])

    def paper_delete(paper_i):
        store.pop(paper_i)


var = 1
while var == 1:
    print('菜单\n'
          '1.添加文献\n'
          '2.查看当前文献库\n'
          '3.根据论文名称检索文献\n'
          '4.删除文献\n'
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
    if select == 3:
        print('输入检索的论文名称')
        search_name=input()
        Paper.paper_search(search_name)
    if select == 4:
        paper_i=int(input())
        Paper.paper_delete(paper_i)
    if select == 5:
        break











