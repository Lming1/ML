import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


# LenearRegession 다중 변수 또는 단일변수 둘다 사용 가능
# 입력값은 x[i]가 통채로 하나씩 들어간다.
# x_data의 shape는  (데이터의 수  , feature의 수)또는 1차원인경우 (입력데이터집합의 개수)
# y_data의 shape는 1차원이 나오고 (예측데이터 집합의 개수 =입력데이터 집합의 개수
# 변수학습 라이브러리 진행중

class New_LenearRegression2:
    W_val = []
    cost_val = []
    X_val = []
    Y_val = []
    list_step = []
    sess = None
    hypothesis = None
    weights = []
    bias = []
    x_data = None
    y_data = None
    optimizer = None
    train = None
    cost = None
    X = None
    Y = None
    layer = 0
    dic = None
    # 생성자 함수로 LenearRegession에서 반드시 필요한 부분 처리
    def __init__(self, x_data, y_data, dic):
        self.sess = tf.Session()
        self.X = tf.placeholder(tf.float32, [None, None])
        self.Y = tf.placeholder(tf.float32, [None, None])
        self.x_data = x_data
        self.y_data = y_data

        self.dic = dic
        self.w1 = tf.Variable(tf.random_uniform([len(dic[0])]))

        for i in range(len(x_data)):
            for j in range(len(x_data[0])):
                x = dic[j].index(x_data[i][j])
                if j == 0:
                    self.x_data[i][j] = self.w1[x]

    def set_cost(self, input_data, input_length):
        self.bias.append(tf.Variable(tf.random_uniform([len(self.y_data[0])], -1.0, 1.0)))
        self.weights.append(tf.Variable(tf.random_uniform([input_length, len(self.y_data[0])], -1.0, 1.0)))
        self.hypothesis = tf.matmul(self.X, self.weights[-1]) + self.bias[-1]
        self.cost = tf.reduce_mean(tf.square(self.hypothesis - self.Y))

        init = tf.initialize_all_variables()
        self.sess.run(init)

    # 학습시키는 함수
    def training(self, learning_rate=0.04, step=2001, show_training_data=True):
        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        self.train = self.optimizer.minimize(self.cost)

        for step in range(step):
            self.sess.run(self.train, feed_dict={self.X: self.sess.run(self.x_data), self.Y: self.y_data})
            self.list_step = range(step + 1)
            self.cost_val.append(
                self.sess.run(self.cost, feed_dict={self.X: self.sess.run(self.x_data), self.Y: self.y_data}))
            if show_training_data == True and step % 20 == 0:
                print(step, 'weght = ',
                      self.sess.run(self.weights[-1], feed_dict={self.X: self.sess.run(self.x_data), self.Y: self.y_data}),
                      'cost =', self.sess.run(self.cost, feed_dict={self.X: self.sess.run(self.x_data), self.Y: self.y_data}))
        plt.plot(self.list_step, self.cost_val, 'ro')
        plt.ylabel('cost')
        plt.xlabel('step')


        # 입력값이 1차원이였을 때 코스트함수를 보여준다.
    def show_cost_graph(self):

        plt.plot(self.list_step, self.cost_val)
        plt.ylabel('cost')
        plt.xlabel('step')
        plt.show()


    # 입력값이 1차원이였을 때 입력값과 라벨을 보여준다.
    def show_singlevariable_graph(self):
        plt.plot(self.sess.run(self.w1), self.y_data,'ro')
        self.w1 = self.sess.run(self.w1)
        xxx =[]
        for i in self.w1:
            xxx.append([i])
        self.hypothesis = tf.matmul(self.X, self.weights[-1]) + self.bias[-1]
        plt.plot(self.w1, self.sess.run(self.hypothesis, feed_dict={self.X : xxx }),label = 'fitted line')
        plt.ylabel('hypothesis')
        plt.xlabel('X')
        plt.legend()
        plt.show()

    # 조건에 맞는 입력 데이타를 받으면 회귀에 따라 예측이되는 출력값을 보낸다
    def predict(self, x_data):
        for i in range(len(x_data)):
            for j in range(len(x_data[0])):
                if j == 0:
                    if x_data[i][j] >= self.dic[j][len(self.dic[j])-1]:
                        x = self.dic[j].index(self.dic[j][len(self.dic[j])-1])
                        x_data[i][j] = self.w1[x] + (self.w1[x]-self.w1[x-1]) * (x_data[i][j] - self.dic[j][len(self.dic[j])-1])/(self.dic[j][len(self.dic[j])-1] - self.dic[j][len(self.dic[j])-2])
                    else:
                        for k in range(len(self.dic[j]) - 1):
                            if self.dic[j][k] <= x_data[i][j] < self.dic[j][k+1]:
                                x = self.dic[j].index(self.dic[j][k])
                                x_data[i][j] = self.w1[x] + (self.w1[x+1]-self.w1[x])*(x_data[i][j] - self.dic[j][k])/(self.dic[j][k +1] - self.dic[j][k])
                                break;
        for i in range(len(self.weights) - 1):
            temp = tf.matmul(x_data, self.weights[i])
        self.hypothesis = tf.matmul(self.X, self.weights[-1]) + self.bias[-1]
        try:
            print(x_data)
            self.result = self.sess.run(self.hypothesis, feed_dict={self.X: self.sess.run(x_data)})
        except:
            print(x_data)
            self.result = self.sess.run(self.hypothesis, feed_dict={self.X: x_data})


    # try:
    # 	plt.plot(self.X_val, self.Y_val, 'ro')
    # 	plt.plot(self.x_data, self.sess.run(self.weights[-1]) * self.x_data + self.sess.run(self.bias[-1]), label='fitted line')
    # 	plt.ylabel('hypothesis')
    # 	plt.xlabel('X')
    # 	plt.legend()
    # 	plt.show()
    # except:
    # 	print('입력값이 1차원이 아닙니다.')


    # 딥하게 갈수 있는 여지는 만들었지만 의미는 없는듯
    def create_layer(self, X, input_length, output_length):
        self.weights.append(tf.Variable(tf.random_uniform([input_length, output_length], -1.0, 1.0)))
        self.bias.append(tf.Variable(tf.random_uniform([output_length], -1.0, 1.0)))
        ret = tf.add(tf.matmul(X, self.weights[-1]), self.bias[-1])
        self.layer += 1
        ret = tf.nn.relu(ret)
        return ret
