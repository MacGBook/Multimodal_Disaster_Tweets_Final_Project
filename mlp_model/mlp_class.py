from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import csv

#########################################################################################################################################################################
# CSV Reader

train_neg_senti_list = []
train_pos_senti_list = []
train_neu_senti_list = []
train_country_list = []
train_continent_list = []

with open('train_new.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        train_neg_senti_list.append(row[0])
        train_pos_senti_list.append(row[2])
        train_neu_senti_list.append(row[1])
        train_country_list.append(row[4])
        train_continent_list.append(row[3])

#print(train_neg_senti_list)

#test_list_international_pos = []
#test_list_international_neu = []
#test_list_international_neg = []


#with open('int_test.csv', 'r') as file: 
 #   reader = csv.reader(file)
    
  #  for row in reader:
   #     test_list_international_pos.append(row[2])
    #    test_list_international_neu.append(row[1])
     #   test_list_international_neg.append(row[0])

test_list_country_neg = []
test_list_country_neu = []
test_list_country_pos = []

with open('only_english_test.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        test_list_country_neg.append(row[0])
        test_list_country_neu.append(row[1])
        test_list_country_pos.append(row[2])

#########################################################################################################################################################################
# GET FLOAT FUNCTION

def get_float(list):
    last_index = len(list) - 1
    grab_the_numbers = list[1:last_index]

    float_list = []

    for value in grab_the_numbers:
        float_value = float(value)
        float_list.append(float_value)
    
    return float_list

#########################################################################################################################################################################
# RECONFIGURE THE LISTS

# TRAINING
final_train_neg_senti_list = get_float(train_neg_senti_list)
final_train_pos_senti_list = get_float(train_pos_senti_list)
final_train_neu_senti_list = get_float(train_neu_senti_list)
final_train_country_list = get_float(train_country_list)
final_train_continent_list = get_float(train_continent_list)

# TEST INTERNATIONAL
#final_test_list_international_pos = get_float(test_list_international_pos)
#final_test_list_international_neu = get_float(test_list_international_neu)
#final_test_list_international_neg = get_float(test_list_international_neg)

# TEST COUNTRY
final_test_list_country_neg = get_float(test_list_country_neg)
final_test_list_country_neu = get_float(test_list_country_neu)
final_test_list_country_pos = get_float(test_list_country_pos)

#########################################################################################################################################################################

# neg, neu, pos training format
input_train_list = []

# country, then continent
result_input_train_list = []

for index in range(len(final_train_neg_senti_list)):
    input_list = [final_train_neg_senti_list[index], final_train_neu_senti_list[index], final_train_pos_senti_list[index]]
    input_train_list.append(input_list)

    result_input_list = [final_train_country_list[index], final_train_continent_list[index]]
    result_input_train_list.append(result_input_list)


clf_country = MLPClassifier(random_state=1, max_iter=1000)
clf_country.fit(input_train_list, final_train_country_list)

clf_continent = MLPClassifier(random_state=1, max_iter=1000)
clf_continent.fit(input_train_list, final_train_continent_list)

###############################################################################################################
# TEST International

#test_international_list = []

#for value in range(len(final_test_list_international_pos)):
 #   test_input_list = [final_test_list_international_neg[value], final_test_list_international_neu[value], final_test_list_international_pos[value]]
  #  test_international_list.append(test_input_list)

#international_results_country = []
#international_results_continent = []

#for val in test_international_list:
 #   country_result = clf_country.predict([val])
  #  continent_result = clf_continent.predict([val])

   # international_results_country.append(country_result)
    #international_results_continent.append(continent_result)

#print(international_results_country)
#print(international_results_continent)

#with open('int_test.csv', 'a', newline='') as file:
 #   writer = csv.writer(file)
    
  #  for value in international_results_country:
   #     row = [''] * (5 + 1)
    #    row[5] = value
     #   writer.writerow(row)
    
    #for value in international_results_continent:
     #   row = [''] * (6 + 1)
      #  row[6] = value
       # writer.writerow(row)

###############################################################################################################
# TEST English Only

test_country_list = []

for value in range(len(final_test_list_country_neg)):
    test_input_list = [final_test_list_country_neg[value], final_test_list_country_neu[value], final_test_list_country_pos[value]]
    test_country_list.append(test_input_list)

country_results_country = []
country_results_continent = []

for val in test_country_list:
    country_result = clf_country.predict([val])
    continent_result = clf_continent.predict([val])

    country_results_country.append(country_result)
    country_results_continent.append(continent_result)

with open('only_english_test.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    
    for value in country_results_country:
        row = [''] * (5 + 1)
        row[5] = value
        writer.writerow(row)
    
    for value in country_results_continent:
        row = [''] * (6 + 1)
        row[6] = value
        writer.writerow(row)

#print(country_results_country)
#print(country_results_continent)
