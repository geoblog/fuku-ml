#encoding=utf8

import os
import FukuML.Utility as utility
import FukuML.SupportVectorMachine as svm

input_train_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'FukuML/dataset/emotion.dat')

cross_validator = utility.CrossValidator()

svm_mc = svm.MultiClassifier()
svm_mc.load_train_data(input_train_data_file)
svm_mc.set_param(svm_kernel='soft_gaussian_kernel', gamma=1, C=1)
cross_validator.add_model(svm_mc)
avg_errors = cross_validator.excute()
print(avg_errors)

svm_mc = svm.MultiClassifier()
svm_mc.load_train_data(input_train_data_file)
svm_mc.set_param(svm_kernel='soft_gaussian_kernel', gamma=1, C=1)
svm_mc.init_W()
svm_mc.train()

print("W 平均錯誤值（Ein）：")
print(svm_mc.calculate_avg_error_all_class(svm_mc.train_X, svm_mc.train_Y, svm_mc.W))
#print("W 平均錯誤值（Eout）：")
#print(svm_mc.calculate_avg_error_all_class(svm_mc.test_X, svm_mc.test_Y, svm_mc.W))

test_data = '0.0367848876657 0.0190718294012 3.1080664818 0.107384504694 0.159547520669 0.233803296411 0.00612485689099 0.0536239374707 -26.6089320976 2.33606400969 -0.333769664462 0.0138045281512 -0.0148494084419 0.0303536729859 -0.196376361559 -0.108319780026 -0.0346169232897 -0.00912045616777 0.119780266762 0.0992009407408 0.168255441735 0.0210987728989 0.00348026916885 0.0240132187857 0.00329874531212 0.00949610436714 0.0561737300036 0.00114399644645 0.00760031271892 0.0283300390908 0.00474578198455 0.0449264354733 0.0047452251764 0.0319005586135 0.0207527952575 0.00892970652891 0.105377654109 0.0347985383722 0.0368829275208 0.17776580867 0.00532295802658 0.0345238704408 1.06728650676 0.489469000324 0.39347824289 0.385838353895 0.314195995826 0.300734036373 0.281028939469 0.290078829198 0.288662919896 0.283121885923 0.294621147579 0.268105935005 0.230082628273 0.0138399915509 0.00325823909501 0.0154321579472 0.0032780885893 0.00861436438584 0.0314409681689 0.00131887135862 0.00708399141365 0.0193360224672 0.00396162787958 0.0256776984692 0.00465701532994 0.00723195973305 1'
prediction = svm_mc.prediction(test_data)
print(prediction)