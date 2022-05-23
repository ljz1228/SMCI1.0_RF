import numpy as np
import os
from configargparse import ArgParser
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.metrics import mean_squared_error,mean_squared_error,mean_absolute_error,r2_score

np.set_printoptions(precision=4)

def main(datadir,flag_spliting,soil_depth):
    if flag_spliting == "temporal":
        Site_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/Site_temporal_correct/test/"
        ERA5_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/ERA5_temporal/test/"
        rfr = joblib.load(r"./Temporal.m")
    elif flag_spliting == "station":
        Site_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/Site_temporal_correct/test/"
        ERA5_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/ERA5_temporal/test/"
        rfr = joblib.load(r"./Station.m")

    China_site_files = os.listdir(Site_file_dir)
    conut = 0
    for i in China_site_files:
        temp_y = np.load(Site_file_dir + i)  ###########   标签 Y  的部分
        temp_x = np.load(ERA5_file_dir + i)  ##########   特征  X  的部分
        if conut == 0:
            test_yy = temp_y
            test_xx = temp_x
            conut += 1
        else:
            test_yy = np.concatenate((test_yy, temp_y), axis=0)
            test_xx = np.concatenate((test_xx, temp_x), axis=0)

    print("test_yy.shape", test_yy.shape)
    print("test_xx.shape", test_xx.shape)
    yy = test_yy.reshape((-1, 1))
    yy_test = yy[~np.any(np.isnan(yy), axis=1)]
    xx_test = test_xx[~np.any(np.isnan(yy), axis=1)]

    xxx = xx_test[~np.any(np.isnan(xx_test), axis=1)]
    yyy = yy_test[~np.any(np.isnan(xx_test), axis=1)]
    test_label = np.squeeze(yyy)

    RF_prediction = rfr.predict(xxx)

    EAR5_MSE = mean_squared_error(xxxxxx[:, 0], test_label)
    EAR5_RMSE = mean_squared_error(xxxxxx[:, 0], test_label) ** 0.5
    EAR5_MAE = mean_absolute_error(xxxxxx[:, 0], test_label)
    EAR5_corrcoef = np.corrcoef(test_label, xxxxxx[:, 0])[0, 1]
    EAR5_r2 = r2_score(test_label, xxxxxx[:, 0])

    RF_MSE = mean_squared_error(test_label, RF_prediction)
    RF_RMSE = mean_squared_error(test_label, RF_prediction) ** 0.5
    RF_MAE = mean_absolute_error(test_label, RF_prediction)
    RF_corrcoef = np.corrcoef(test_label, RF_prediction)[0, 1]
    RF_r2 = r2_score(test_label, RF_prediction)

    print('###########            ERA5产品的结果               ###########')
    print('EAR5产品后的MSE是               ', EAR5_MSE)
    print('EAR5产品后的RMSE是              ', EAR5_RMSE)
    print('EAR5产品后的MAE是               ', EAR5_MAE)
    print('EAR5产品后的相关系数是', EAR5_corrcoef)
    print('EAR5产品后的r2_score是           ', EAR5_r2)
    print('########               RF算法后的结果                 #########')
    print('RF产品后的MSE是                  ', RF_MSE)
    print('RF产品后的RMSE是                 ', RF_RMSE)
    print('RF产品后的MAE是                  ', RF_MAE)
    print('RF产品后的相关系数是               ', RF_corrcoef)
    print('RF产品后的r2_score是              ', RF_r2)
    print('test_label的shape是              ', test_label.shape)
    print('RF_prediction的shape是           ', RF_prediction.shape)




if __name__ == '__main__':
    p = ArgParser()
    p.add_argument('--datadir', type=str, default='../test_data/', help='Path to data')
    # flag=[temporal,station]
    p.add_argument('--flag_spliting', type=str, default='temporal', help='Way for spliting dataset')
    p.add_argument('--soil_depth', type=int, default=10, help='SM at x soil_depth')
    args = p.parse_args()

    main(
        datadir=args.datadir,
        flag_spliting=args.flag_spliting,
        soil_depth=args.soil_depth
    )

