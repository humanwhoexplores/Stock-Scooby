def kalman_filtertemp(df, sentiMatrix):
    #creating a kalman filter object,,

    #hey problem ,, df dimension not equal to sentiMatrix as twitter sentiment analysis daily,, but
    #stock market does not open everyday, so we need to do something,,



    obs_mat = np.vstack([df['2014-05-13']['SENSEX'], sentiMatrix[0:1]]).T[:, np.newaxis]
    #obs_mat = np.vstack([df['SENSEX'], sentiMatrix]).T[:, np.newaxis]
    #obs_mat = np.vstack([df['SENSEX'], sentiMatrix]).T[:, np.newaxis]

    #obs_mat = np.vstack([sentiMatrix, np.ones(1)]).T[:, np.newaxis]


    delta = 1e-5
    trans_cov = delta / (1 - delta) * np.eye(2)

    kf = pk.KalmanFilter(n_dim_obs=1, n_dim_state=2,
                  initial_state_mean=np.zeros(2),
                  initial_state_covariance=np.ones((2, 2)),
                  transition_matrices=np.eye(2),
                  observation_matrices=obs_mat,
                  observation_covariance=1.0,
                  transition_covariance=trans_cov)


    state_means, state_covs = kf.filter([df['2014-05-13']['SENSEX']])

    value1 = df['2014-05-14']['SENSEX']
    print "the price on day " , value1

    myvalue = df['2014-05-13']['SENSEX']
    value2 = myvalue*state_means[0][0]
    print "the price on day 2014-05-14 as predicted by noise and price of " , value2
     #print "state_covs is ", state_covs