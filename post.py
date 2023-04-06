# CRUD 게시판 파이썬 콘솔로 만들기 프로젝트
class Post:
    '''
        게시물 클래스
        param id: 글번호
        param title: 글제목
        param content: 글내용
        param view_count: 조회수
    '''

    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count


if __name__ == '__main__':
    post = Post(1, 'test', 'test입니다.', 0)
    post.add_view_count();
    # post.set_post(1, 'test2', 'test2입니다.', 0)
    print(f'{post.get_id()},{post.get_title()},{post.get_content()},{post.get_view_count()}')
