import csv
import os.path
from post import Post

file_path = './data.csv'

# post 객체 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    f = open(file_path,'r',encoding='utf8')
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성
        post_file = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post_file)
else:
    f = open(file_path,'w',encoding='utf8')
    f.close()

# 게시글 쓰기
def write_post():
    print('\n\n -- 게시글 쓰기 --')
    title = input('제목을 입력해주세요 >> ')
    content = input('본문을 입력해주세요 >> ')
    # 글번호
    id = post_list[-1].get_id() + 1
    post = Post(id , title, content, 0)
    post_list.append(post)
    print('# 게시글이 등록되었습니다.\n\n')

# 게시글 목록
def read_post():
    id_list = []
    print('\n-- 게시글 목록 --')
    for list in post_list:
        print(f'번호 : {list.get_id()}')
        print(f'제목 : {list.get_title()}')
        print(f'조회수 : {list.get_view_count()}')
        print('')
        id_list.append(list.get_id())

    while True:
        print('-- 글 번호를 선택해주세요 -- (메인 메뉴로 돌아가려면 -1을 입력하세요)')
        try:
            id = int(input('>>>'))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print('없는 글 번호입니다.')
        except ValueError :
            print('숫자만 입력해주세요')
# 글 상세 페이지
def detail_post(id):
    print('\n-- 게시글 상세 --')
    for post_num in post_list:
        if post_num.get_id() == id:
            post_num.add_view_count()
            print(f'번호 : {post_num.get_id()}')
            print(f'제목 : {post_num.get_title()}')
            print(f'내용 : {post_num.get_content()}')
            print(f'조회수 : {post_num.get_view_count()}')
            target_post = post_num

    while True:
        print('\n수정 : 1, 삭제 : 2 (메뉴로 돌아가려면 -1을 입력하세요)')
        try:
            choice = int(input('>>>'))
            if choice == 1:
                update_post(target_post)
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print('다시 입력해주세요')
        except ValueError:
            print('숫자만 입력해주세요')

# 게시글 수정
def update_post(target_post):
    print('\n -- 게시글 수정 --')
    title = input('제목을 입력해주세요\n >>')
    content = input('본문을 입력해주세요\n >>')
    target_post.set_post(target_post.id,title,content,target_post.view_count)
    print('# 게시글이 수정되었습니다.')

# 게시글 삭제
def delete_post(target_post):
    post_list.remove(target_post)

# 게시글 저장
def save():
    f = open(file_path,'w',encoding='utf8')
    writer = csv.writer(f)
    for post_write in post_list:
        row = [post_write.get_id(),post_write.get_title(),post_write.get_content(),post_write.get_view_count()]
        writer.writerow(row)
    f.close()
    print('# 저장이 완료되었습니다.')
    print('# 프로그램 종료')



# 메뉴 출력하기
while True:
    print('나만의 블로그 만들기\n')
    print('-- 메뉴를 선택해주세요 --')
    print('1. 게시글 쓰기')
    print('2. 게시글 목록')
    print('3. 나가기')
    try:
        choice = int(input('>>>'))
    except ValueError as e:
        print('숫자 1,2,3만 입력해주세요', e)
    else:
        if choice == 1:
            write_post()

        elif choice == 2:
            read_post()
        elif choice == 3:
            save()
            break

