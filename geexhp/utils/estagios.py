import numpy as np

def terra_moderna(dicionario):
    """
    Calcula parâmetros atmosféricos para uma Terra moderna.

    Parâmetros:
    -----------
    dicionario : dict
        Dicionário para armazenar os parâmetros atmosféricos calculados.

    Retorno:
    --------
    None

    Notas:
    ------
    Esta função calcula os parâmetros atmosféricos de uma Terra moderna,
    incluindo a pressão, a temperatura e a abundância de diversos gases em diferentes camadas atmosféricas.

    As camadas atmosféricas são modeladas com base em valores fixos de pressão e temperatura,
    enquanto a abundância dos gases varia em cada camada.

    A abundância dos gases é fornecida como uma fração em relação ao total da mistura em cada camada.
    """

    camadas = 60

    # Valores fixos iguais da Terra
    pressao_fixa = np.array([1.013e+00, 8.988e-01, 7.950e-01, 7.012e-01, 6.166e-01, 5.405e-01,
                        4.722e-01, 4.111e-01, 3.565e-01, 3.080e-01, 2.650e-01, 2.270e-01,
                        1.940e-01, 1.658e-01, 1.417e-01, 1.211e-01, 1.035e-01, 8.850e-02,
                        7.565e-02, 6.467e-02, 5.529e-02, 4.729e-02, 4.047e-02, 3.467e-02,
                        2.972e-02, 2.549e-02, 1.743e-02, 1.197e-02, 8.258e-03, 5.746e-03,
                        4.041e-03, 2.871e-03, 2.060e-03, 1.491e-03, 1.090e-03, 7.978e-04,
                        4.250e-04, 2.190e-04, 1.090e-04, 5.220e-05, 2.400e-05, 1.050e-05,
                        4.460e-06, 1.840e-06, 7.600e-07, 3.200e-07, 1.450e-07, 7.100e-08,
                        4.010e-08, 2.540e-08, 6.023e-09, 2.614e-09, 1.337e-09, 7.427e-10,
                        4.386e-10, 2.681e-10, 1.693e-10, 1.097e-10, 7.234e-11, 4.900e-11])
    temperatura_fixa = np.array([ 288.2,  281.7,  275.2,  268.7,  262.2,  255.7,  249.2,  242.7,
                                236.2,  229.7,  223.3,  216.8,  216.7,  216.7,  216.7,  216.7,
                                216.7,  216.7,  216.7,  216.7,  216.7,  217.6,  218.6,  219.6,
                                220.6,  221.6,  224. ,  226.5,  229.6,  236.5,  243.4,  250.4,
                                257.3,  264.2,  270.6,  270.7,  260.8,  247. ,  233.3,  219.6,
                                208.4,  198.6,  188.9,  186.9,  188.4,  195.1,  208.8,  240. ,
                                300. ,  360. ,  610. ,  759. ,  853. ,  911. ,  949. ,  973. ,
                                988. ,  998. , 1000. , 1010. ])
    
    # Razões de abundância para várias moléculas
    CO2 = np.full(camadas, 3.795e-04)
    N2 = np.full(camadas, 0.781)
    O2 = np.full(camadas, 0.209)
    H2O = np.array([7.745e-03, 6.071e-03, 4.631e-03, 3.182e-03, 2.158e-03, 1.397e-03,
                    9.254e-04, 5.720e-04, 3.667e-04, 1.583e-04, 6.996e-05, 3.613e-05,
                    1.906e-05, 1.085e-05, 5.927e-06, 5.000e-06, 3.950e-06, 3.850e-06,
                    3.825e-06, 3.850e-06, 3.900e-06, 3.975e-06, 4.065e-06, 4.200e-06,
                    4.300e-06, 4.425e-06, 4.575e-06, 4.725e-06, 4.825e-06, 4.900e-06,
                    4.950e-06, 5.025e-06, 5.150e-06, 5.225e-06, 5.250e-06, 5.225e-06,
                    5.100e-06, 4.750e-06, 4.200e-06, 3.500e-06, 2.825e-06, 2.050e-06,
                    1.330e-06, 8.500e-07, 5.400e-07, 4.000e-07, 3.400e-07, 2.800e-07,
                    2.400e-07, 2.000e-07, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00,
                    0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00])
    CO = np.array([1.500e-07, 1.450e-07, 1.399e-07, 1.349e-07, 1.312e-07, 1.303e-07,
                    1.288e-07, 1.247e-07, 1.185e-07, 1.094e-07, 9.962e-08, 8.964e-08,
                    7.814e-08, 6.374e-08, 5.025e-08, 3.941e-08, 3.069e-08, 2.489e-08,
                    1.966e-08, 1.549e-08, 1.331e-08, 1.232e-08, 1.232e-08, 1.307e-08,
                    1.400e-08, 1.498e-08, 1.598e-08, 1.710e-08, 1.850e-08, 2.009e-08,
                    2.220e-08, 2.497e-08, 2.824e-08, 3.241e-08, 3.717e-08, 4.597e-08,
                    6.639e-08, 1.073e-07, 1.862e-07, 3.059e-07, 6.375e-07, 1.497e-06,
                    3.239e-06, 5.843e-06, 1.013e-05, 1.692e-05, 2.467e-05, 3.356e-05,
                    4.148e-05, 5.000e-05, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00,
                    0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00])
    C2H6 = np.array([2.00e-09, 2.00e-09, 2.00e-09, 2.00e-09, 1.98e-09, 1.95e-09,
                    1.90e-09, 1.85e-09, 1.79e-09, 1.72e-09, 1.58e-09, 1.30e-09,
                    9.86e-10, 7.22e-10, 4.96e-10, 3.35e-10, 2.14e-10, 1.49e-10,
                    1.05e-10, 7.96e-11, 6.01e-11, 4.57e-11, 3.40e-11, 2.60e-11,
                    1.89e-11, 1.22e-11, 5.74e-12, 2.14e-12, 8.49e-13, 3.42e-13,
                    1.34e-13, 5.39e-14, 2.25e-14, 1.04e-14, 6.57e-15, 4.74e-15,
                    3.79e-15, 3.28e-15, 2.98e-15, 2.79e-15, 2.66e-15, 2.56e-15,
                    2.49e-15, 2.43e-15, 2.37e-15, 2.33e-15, 2.29e-15, 2.25e-15,
                    2.22e-15, 2.19e-15, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
                    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00])
    HCN = np.array([1.70e-10, 1.65e-10, 1.63e-10, 1.61e-10, 1.60e-10, 1.60e-10,
                    1.60e-10, 1.60e-10, 1.60e-10, 1.60e-10, 1.60e-10, 1.60e-10,
                    1.60e-10, 1.59e-10, 1.57e-10, 1.55e-10, 1.52e-10, 1.49e-10,
                    1.45e-10, 1.41e-10, 1.37e-10, 1.34e-10, 1.30e-10, 1.25e-10,
                    1.19e-10, 1.13e-10, 1.05e-10, 9.73e-11, 9.04e-11, 8.46e-11,
                    8.02e-11, 7.63e-11, 7.30e-11, 7.00e-11, 6.70e-11, 6.43e-11,
                    6.21e-11, 6.02e-11, 5.88e-11, 5.75e-11, 5.62e-11, 5.50e-11,
                    5.37e-11, 5.25e-11, 5.12e-11, 5.00e-11, 4.87e-11, 4.75e-11,
                    4.62e-11, 4.50e-11, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
                    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00])
    SO2 = np.array([3.00e-10, 2.74e-10, 2.36e-10, 1.90e-10, 1.46e-10, 1.18e-10,
                    9.71e-11, 8.30e-11, 7.21e-11, 6.56e-11, 6.08e-11, 5.79e-11,
                    5.60e-11, 5.59e-11, 5.64e-11, 5.75e-11, 5.75e-11, 5.37e-11,
                    4.78e-11, 3.97e-11, 3.19e-11, 2.67e-11, 2.28e-11, 2.07e-11,
                    1.90e-11, 1.75e-11, 1.54e-11, 1.34e-11, 1.21e-11, 1.16e-11,
                    1.21e-11, 1.36e-11, 1.65e-11, 2.10e-11, 2.77e-11, 3.56e-11,
                    4.59e-11, 5.15e-11, 5.11e-11, 4.32e-11, 2.83e-11, 1.33e-11,
                    5.56e-12, 2.24e-12, 8.96e-13, 3.58e-13, 1.43e-13, 5.73e-14,
                    2.29e-14, 9.17e-15, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
                    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00]) 
    O3 = np.array([2.660e-08, 2.931e-08, 3.237e-08, 3.318e-08, 3.387e-08, 3.768e-08,
                    4.112e-08, 5.009e-08, 5.966e-08, 9.168e-08, 1.313e-07, 2.149e-07,
                    3.095e-07, 3.846e-07, 5.030e-07, 6.505e-07, 8.701e-07, 1.187e-06,
                    1.587e-06, 2.030e-06, 2.579e-06, 3.028e-06, 3.647e-06, 4.168e-06,
                    4.627e-06, 5.118e-06, 5.803e-06, 6.553e-06, 7.373e-06, 7.837e-06,
                    7.800e-06, 7.300e-06, 6.200e-06, 5.250e-06, 4.100e-06, 3.100e-06,
                    1.800e-06, 1.100e-06, 7.000e-07, 3.000e-07, 2.500e-07, 3.000e-07,
                    5.000e-07, 7.000e-07, 7.000e-07, 4.000e-07, 2.000e-07, 5.000e-08,
                    5.000e-09, 5.000e-10, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00,
                    0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00])
    CH4 = np.full(camadas, 1.700e-06)
    N2O = np.full(camadas, 3.200e-07)
    NH3 = np.array([5.00e-10, 5.00e-10, 4.63e-10, 3.80e-10, 2.88e-10, 2.04e-10,
                    1.46e-10, 9.88e-11, 6.48e-11, 3.77e-11, 2.03e-11, 1.09e-11,
                    6.30e-12, 3.12e-12, 1.11e-12, 4.47e-13, 2.11e-13, 1.10e-13,
                    6.70e-14, 3.97e-14, 2.41e-14, 1.92e-14, 1.72e-14, 1.59e-14,
                    1.44e-14, 1.23e-14, 9.37e-15, 6.35e-15, 3.68e-15, 1.82e-15,
                    9.26e-16, 2.94e-16, 8.72e-17, 2.98e-17, 1.30e-17, 7.13e-18,
                    4.80e-18, 3.66e-18, 3.00e-18, 2.57e-18, 2.27e-18, 2.04e-18,
                    1.85e-18, 1.71e-18, 1.59e-18, 1.48e-18, 1.40e-18, 1.32e-18,
                    1.25e-18, 1.19e-18, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
                    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00]) 
    CH3Cl = np.array([7.00e-10, 6.70e-10, 6.43e-10, 6.22e-10, 6.07e-10, 6.02e-10,
                    6.00e-10, 6.00e-10, 5.98e-10, 5.94e-10, 5.88e-10, 5.79e-10,
                    5.66e-10, 5.48e-10, 5.28e-10, 5.03e-10, 4.77e-10, 4.49e-10,
                    4.21e-10, 3.95e-10, 3.69e-10, 3.43e-10, 3.17e-10, 2.86e-10,
                    2.48e-10, 1.91e-10, 1.10e-10, 4.72e-11, 1.79e-11, 7.35e-12,
                    3.03e-12, 1.32e-12, 8.69e-13, 6.68e-13, 5.60e-13, 4.94e-13,
                    4.56e-13, 4.32e-13, 4.17e-13, 4.05e-13, 3.96e-13, 3.89e-13,
                    3.83e-13, 3.78e-13, 3.73e-13, 3.69e-13, 3.66e-13, 3.62e-13,
                    3.59e-13, 3.56e-13, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00,
                    0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00, 0.00e+00])                 

    # Moléculas adicionais com abundância fixa (2%)
    H2 = np.full(camadas, 0.02)
    H2S = np.full(camadas, 0.02)

    # Informação sobre as moléculas (https://pt.webqc.org/mmcalc.php)
    moleculas = ["CO2" , "N2" , "O2" , "H2O", "CO", "H2" , "C2H6" , "HCN", 
                 "H2S", "SO2" , "O3" , "CH4" , "N2O", "NH3" , "CH3Cl"]
    peso_molecular = [44.0095, 28.01340, 31.99880, 18.01528, 28.0101, 2.01588, 
                      30.0690, 27.0253, 34.0809, 64.0638, 47.99820, 16.0425, 44.01280, 
                      17.03052, 50.4875]
    
    # Preenchendo o dicionário com dados atmosféricos
    for i in range(camadas):
        total_abundancia_camada = np.sum([
            CO2[i], N2[i], O2[i], H2O[i], CO[i], H2[i], C2H6[i], HCN[i], H2S[i], SO2[i],
            O3[i], CH4[i], N2O[i], NH3[i], CH3Cl[i]
        ])
        
        dicionario[f'ATMOSPHERE-LAYER-{i + 1}'] = ','.join([
            str(pressao_fixa[i]), str(temperatura_fixa[i]),
            *[str(abundancia / total_abundancia_camada) for abundancia in [
                CO2[i], N2[i], O2[i], H2O[i], CO[i], H2[i], C2H6[i], HCN[i], H2S[i], SO2[i],
                O3[i], CH4[i], N2O[i], NH3[i], CH3Cl[i]
            ]]
        ])
    
    # Pegando a abundância média apenas da primeira camada (isso é uma aproximação!)
    molweights = np.array(peso_molecular)
    abuns = np.array([CO2[0], N2[0], O2[0], H2O[0], CO[0], H2[0], C2H6[0], HCN[0], H2S[0], SO2[0], O3[0], CH4[0], 
                        N2O[0], NH3[0], CH3Cl[0]])
    peso_molecular_medio = np.sum(molweights * abuns)
    
    # Dicionário de mapeamento de moléculas para índices de banco de dados HITRAN
    # https://hitran.org/lbl/
    HITDICT = {"CO2": "HIT[2]", "N2" : "HIT[22]", "O2" : "HIT[7]", 
                "H2O": "HIT[1]", "CO": "HIT[5]", "H2": "HIT[45]", "C2H6": "HIT[27]",
                "HCN": "HIT[23]", "H2S": "HIT[31]", "SO2": "HIT[9]", "O3":"HIT[3]", 
                "CH4" :"HIT[6]", "N2O": "HIT[4]", "NH3" : "HIT[11]", "CH3Cl": "HIT[24]"}
    
    dicionario['ATMOSPHERE-WEIGHT'] = peso_molecular_medio
    dicionario['ATMOSPHERE-NGAS'] = len(moleculas)
    dicionario['ATMOSPHERE-GAS'] = ",".join(moleculas)
    dicionario['ATMOSPHERE-TYPE'] = ",".join([HITDICT[i] for i in moleculas]) 
    dicionario['ATMOSPHERE-ABUN'] = "1,"*(len(moleculas)-1)+ '1'
    dicionario['ATMOSPHERE-UNIT'] = "scl,"*(len(moleculas)-1)+ 'scl' 
    dicionario['ATMOSPHERE-LAYERS-MOLECULES'] = ','.join(moleculas)