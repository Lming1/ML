from pylib.Softmax import Softmax

x_data = [[5.,4.,2.,1.,4.],[4.,3.,3.,4.,5.],[3.,2.,5.,3.,1.],[0.,1.,2.,4.,1.]]
#x[][0]은 성격의 활발한 정도
#x[][1]은 어느정도 부유한지
#x[][2]은 시간적 여유
#x[][3]은 책읽기를 좋아하는 정도
#x[][4]은 영화보기를 좋아하는 정도
y_data = [[0.,1.,1.,0.,1.,1.,0.],[0.,1.,1.,0.,1.,1.,1.],[1.,1.,0.,1.,1.,0.,0.],[0.,0.,0.,0.,0.,0.,1.]]
#y[][0] 집에서 혼자 영화보기
#y[][1] 영화관에서 영화 보기
#y[][2] 영화 시사회에 가기
#y[][3] 영화배우 팬 싸인회 가기
#y[][4] 영화의 원작 책 읽기

#y[][5] 책을 사서 읽는다.
#y[][6] 책을 빌려서 읽는다.

NN = Softmax(x_data,y_data)

NN.training(0.05,2001,True)
# test.show_cost_graph()
# test.show_singlevariable_graph()
print('------------------------------------------------------------------------------------------------')
NN.predict([[0.,1.,2.,3.,4.],[0.,0.,3.,4.,0.],[5.,5.,5.,0.,5.]])
