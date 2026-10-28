from pickledb import PickleDB

db=PickleDB('paper.db')

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
        db.set(f'{paper_name}',svg)
        db.save()
        print(f'成功存储{paper_name},{push_time},{paper_source},{paper_type}')

    # def paper_visit(paper_name):
    #     db.get('paper_name')
    #         # print(f'{i},{paper_load[i]}')


    # def paper_search(name):
    #
    #

    # def paper_delete(paper_i):
    #


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
        keys=db.all()
        print(keys)

    if select == 3:
        print('输入检索的论文名称')
        search_name=input()
        print(db.get(search_name))
    if select == 4:
        print('输入删除的论文名称')
        del_name=input()
        delete=db.remove(del_name)
        print(f'{delete}')
        db.save()
    if select == 5:
        break











