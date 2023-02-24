class Cafe:
    cnt = 0     # 클래스 변수
    
    def __init__(self, cnt, name):
        self.cnt = cnt
        self.name = name

    def show_order(self):
        Cafe.cnt += self.cnt # 클래스 변수도 사용
        return f'{self.name} {self.cnt}개에 대한 주문이 들어왔습니다'

    @classmethod
    def show_total_order_cnt(cls):
        return f'총 주문 개수는 {cls.cnt}개 입니다!^_^'

    @staticmethod
    def show_review(text):
        return f'리뷰 : {text}'

# 인스턴스 변수    
order1 = Cafe(3, '아메리카노')
order2 = Cafe(1, '카페라떼')

# print(Cafe.show_order())    # 클래스는 인스턴스 메서드 호출 불가
print(order1.show_order()) # 아메리카노 3개에 대한 주문이 들어왔습니다
print(order2.show_order()) # 카페라떼 1개에 대한 주문이 들어왔습니다

print()

print(Cafe.show_total_order_cnt()) # 총 주문 개수는 4개 입니다!^_^
print(order1.show_total_order_cnt()) # 총 주문 개수는 4개 입니다!^_^
print(order2.show_total_order_cnt()) # 총 주문 개수는 4개 입니다!^_^

print()

print(Cafe.show_review('맛있어요')) # 리뷰 : 맛있어요
print(order1.show_review('별로네요..')) # 리뷰 : 별로네요..
print(order2.show_review('1000원에 해주세요')) # 리뷰 : 1000원에 해주세요