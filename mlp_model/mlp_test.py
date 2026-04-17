from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import csv
import numpy as np

#########################################################################################################################################################################
# SET UP THE TRAIN DATASET

neg_senti = []
neut_senti = []
pos_senti = []
latitude = []
longitude = []

with open("train.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        #neg_senti.append(row[0])
        neut_senti.append(row[1])
        #pos_senti.append(row[2])
        #pos_senti.append(row[3])
        latitude.append(row[4])
        longitude.append(row[5])

#print(len(neg_senti))

#print(longitude)

def make_int(list):
    altered_list = list[1:409]
    revised_list = []
    for value in altered_list:
        new_value = float(value)
        revised_list.append(new_value)
    
    return revised_list

#new_neg_senti = make_int(neg_senti)
new_neut_senti = make_int(neut_senti)
#new_pos_senti = make_int(pos_senti)
new_latitude = make_int(latitude)
new_longitude = make_int(longitude)

senti_tuple_list = []
coord_tuple_list = []

for current_index in range(len(new_neut_senti)):
    senti_tuple_bit = [new_neut_senti[current_index]]
    coord_tuple_bit = [new_latitude[current_index], new_longitude[current_index]]
    
    senti_tuple_list.append(senti_tuple_bit)
    coord_tuple_list.append(coord_tuple_bit)

#########################################################################################################################################################################
# SET UP THE TEST DATASET

#test_neg_senti = []
test_neut_senti = []
#test_pos_senti = []
test_latitude = []
test_longitude = []

with open("train_a2.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        #test_neg_senti.append(row[0])
        test_neut_senti.append(row[1])
        #pos_senti.append(row[2])
        #test_pos_senti.append(row[3])
        test_latitude.append(row[4])
        test_longitude.append(row[5])

def make_float(list):
    altered_list = list[1:19]
    revised_list = []
    for value in altered_list:
        new_value = float(value)
        revised_list.append(new_value)
    
    return revised_list

#test_new_neg_senti = make_float(test_neg_senti)
test_new_neut_senti = make_float(test_neut_senti)
#test_new_pos_senti = make_float(test_pos_senti)
test_new_latitude = make_float(test_latitude)
test_new_longitude = make_float(test_longitude)

test_senti_tuple_list = []
test_coord_tuple_list = []

for current_index in range(len(test_new_neut_senti)):
    senti_tuple_bit = [test_new_neut_senti[current_index]]
    coord_tuple_bit = [test_new_latitude[current_index], test_new_longitude[current_index]]
    
    test_senti_tuple_list.append(senti_tuple_bit)
    test_coord_tuple_list.append(coord_tuple_bit)


#########################################################################################################################################################################
# TRAIN THE MLP

regr = MLPRegressor(random_state=1, max_iter=2000, tol=0.1)
regr.fit(senti_tuple_list, coord_tuple_list)

#########################################################################################################################################################################
# RUN OUR TEST DATASETS

#trial_run_1  = [[0.813052058], [0.565901339], [0.196202248], [0.391033769], [0.080306664], [0.846154392], [0.178978279], [0.749595225], [0.914276659], [0.648621798], [0.799522758], [0.602960169], [0.544353843], [0.1592931], [0.498783052], [0.818654895], [0.486101687], [0.683767855], [0.710969865], [0.760922432]]

#trial_run_2 = [[0.237943053], [0.778347194], [0.555220544], [0.171181217], [0.356986314], [0.062708139], [0.865941405], [0.746815264], [0.925486028], [0.6717816], [0.796003342], [0.552253723], [0.150832638], [0.507652521], [0.868851483], [0.760922432], [0.022640409], [0.042524315], [0.61626929], [0.49299711], [0.811134994]]


#t_neg_senti = []
t_neut_senti = []
#t_pos_senti = []

with open("ablation_2.1_results.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        #t_neg_senti.append(row[1])
        t_neut_senti.append(row[2])
        #t_pos_senti.append(row[3])

#print(len(t_neg_senti))

#neg_lil_list = [float(x) for x in t_neg_senti[1:21]]
neut_lil_list = [float(x) for x in t_neut_senti[1:21]]
#pos_lil_list = [float(x) for x in t_pos_senti[1:21]]

trial_run_1 = []

for ind in range(len(neut_lil_list)):
    #tupp1 = neg_lil_list[ind]
    tupp2 = neut_lil_list[ind]
    #tupp3 = pos_lil_list[ind]

    final_tup_list = [tupp2]
    trial_run_1.append(final_tup_list)


ablation_1_result_list = []

for little_list in trial_run_1:
    result = regr.predict([little_list])
    #print(result)
    ablation_1_result_list.append(result)

#print(ablation_1_result_list)

#result = regr.predict([[0.040706567, 0.813052058, 0.146241307]])
#print(result)

with open("ablation_1_results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    for item in ablation_1_result_list:
        lat = item[0][0]
        lon = item[0][1]

        writer.writerow([lat, lon])
