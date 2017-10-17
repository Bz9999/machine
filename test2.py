# coding:utf-8
# 正規方程式

import numpy as np
import re

if __name__ == '__main__':
    file_name = "data1.txt"
    full_text = open(file_name).read()
    full_text_arr = full_text.split('\n')
    table_head = []
    table_data = []


    for i, line in enumerate(full_text.split('\n')):
        data = re.split(r'\t', line.rstrip('\r'))
        for j, d in enumerate(data):
            data[j] = d.replace(" ","0")
        if i == 0 :
            table_head = data
        else:
            table_data.append(data)

    for train_num in range(len(full_text_arr)):
        if train_num < 2:
            continue
        if train_num % 20:
            continue

        table_train_data = []
        table_test_data = []
        for i ,data in enumerate(table_data):
            if i < train_num :
                table_train_data.append(data)
            else:
                table_test_data.append(data)




        ytrain = np.matrix(table_train_data)[:, 0]
        xtrain = np.matrix(table_train_data)
        xtrain = np.delete(xtrain,0,1)
        xtrain = np.insert(xtrain,0,1,axis=1)
        #x_t = np.copy(x)

        x = np.double(xtrain[:])
        y = np.double(ytrain[:])
       # print(y)
        #print(x)
        w = np.linalg.pinv(x.T * x) * x.T * y
        # print (w)

        ###　test




        x_test= np.matrix(table_test_data)

        y_label = x_test[:, 0]
        y_label = np.double(y_label[:])

        x_test = np.delete(x_test, 0, 1)
        x_test = np.insert(x_test, 0, 1, axis=1)
        x_test= np.double(x_test[:])

        y_test = x_test * w

        # print (y_label)
        # print (np.round(y_test))
        # print (y_label == np.round(y_test))

        result = (y_label == np.round(y_test)).T

        success = len(np.where(result ==True)[0])
        rate = int(success * 100 /result.size)

        #print (str(success) + "/" + str(result.size))
        # print ("正解率:" + str(float(success)/(result.size) * 100) + "%")

        print("%4d |" % train_num + rate * "=" + (100 - rate )*" " + "|" + str(rate) + "%")
