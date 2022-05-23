import numpy as np
import os
from configargparse import ArgParser
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib
np.set_printoptions(precision=4)


def main(datadir,flag_spliting,soil_depth):
    if flag_spliting == "temporal":
        Site_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/Site_temporal_correct/train/"
        ERA5_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/ERA5_temporal/train/"
    elif flag_spliting == "station":
        Site_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/Site_temporal_correct/train/"
        ERA5_file_dir = datadir + f"/{soil_depth}cm" + "/rf_train_test_DATA/ERA5_temporal/train/"

    China_site_files = os.listdir(Site_file_dir)
    conut = 0
    for i in China_site_files:
        train_y_temp = np.load(Site_file_dir + i)  ###########   标签 Y  的部分
        train_x_temp = np.load(ERA5_file_dir + i)  ##########   特征  X  的部分
        if np.isnan(train_y_temp.all()):
            print(i.rstrip('.npy') + "  站点为 nan ")
        else:
            if conut == 0:
                train_y = train_y_temp
                train_x = train_x_temp
                conut += 1
            else:
                train_y = np.concatenate((train_y, train_y_temp), axis=0)
                train_x = np.concatenate((train_x, train_x_temp), axis=0)
                print("%s  站点土壤湿度样本总数是    %d   " % (i.rstrip(".npy"), train_y.shape[0]))
                print("%s  站点土壤湿度样本总数是    %d   " % (i.rstrip(".npy"), train_x.shape[0]))

    print("train_y.shape", train_y.shape)
    print("train_x.shape", train_x.shape)
    yy = train_y.reshape((-1, 1))
    train_YY = yy[~np.any(np.isnan(yy), axis=1)]
    xx_xx = train_x[~np.any(np.isnan(yy), axis=1)]

    feature_x = xx_xx[~np.any(np.isnan(xx_xx), axis=1)]  ####这是处理，特征X中如果有缺失值的情况
    _yy_ = train_YY[~np.any(np.isnan(xx_xx), axis=1)]
    lable_y = np.squeeze(_yy_)

    rfr = RandomForestRegressor(n_estimators=1000, n_jobs=-1, min_samples_leaf=50, random_state=20, oob_score=True,verbose=2)
    grid = {
        'n_estimators': list(range(600, 6000, 200)),
        'min_samples_leaf': list(range(10, 200, 20))
    }
    gscv = GridSearchCV(rfr, param_grid=grid, cv=10, scoring='neg_mean_squared_error', return_train_score=True, verbose=2)
    gscv.fit(feature_x, lable_y)
    result = gscv.cv_results_
    for mean_score, param in zip(result["mean_test_score"], result["params"]):
        print("RMSE:{}     param:{}".format(np.sqrt(-mean_score), param))
    best_param = gscv.best_params_
    print("best param: {}".format(best_param))

    if Flag == "temporal":
        joblib.dump(rfr, r"./Temporal.m")##  save model
    elif Flag == "station":
        joblib.dump(rfr, r"./Station.m")



if __name__ == '__main__':
    p = ArgParser()
    p.add_argument('--datadir', type=str, default='../test_data/', help='Path to data')
    # flag=[temporal,station]
    p.add_argument('--flag_spliting', type=str, default='temporal', help='Way for spliting dataset')
    p.add_argument('--soil_depth', type=int, default=10, help='SM at x soil_depth') # 10 ~ 100cm
    args = p.parse_args()

    main(
        datadir=args.datadir,
        flag_spliting=args.flag_spliting,
        soil_depth=args.soil_depth,
    )

