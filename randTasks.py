################################################################################
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
"""
                      File    :   "randTasks.py"
                      Author  :   James Michael Brown
                      Updated :   March 2, 2020
"""
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
import random, pickle
import pandas as pd
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
N = 45; # 45 subjects
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
sizeRanking = [0]*(int(N/3));
glossMatching = [1]*(int(N/3));
shineMapping = [2]*(int(N/3));
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# random.seed(99999)
# rand_seed = random.randrange(1,10000000);
# print(rand_seed)
# > 2021495
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
random.seed(2021495);
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
subject_order = sizeRanking + glossMatching + shineMapping;
random.shuffle(subject_order)
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
rand_sample = random.sample(subject_order, N)
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# pickle.dump(rand_sample, open("rand_sample.p", "wb"))
# subject_order = pickle.load(open("rand_sample.p", "rb"))
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
task = [];
for i in rand_sample:
    if i == 0:
        j = 'sizeRanking';
        task.append(j)
    if i == 1:
        j = 'glossMatching';
        task.append(j)
    if i == 2:
        j = 'shineMapping';
        task.append(j)
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
subject_number = ["%03d" % x for x in range(N)]
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
empt1 = empt2 = empt3 = empt4 =['']*len(task);
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
cols = ['subject #', 'task', 'ID', 'first name', 'last name', 'email'];
df = pd.DataFrame(list(zip(subject_number, task, empt1, empt2, empt3, empt4)), columns = cols);
df.to_excel("sizeGloss_exp1_SampleFrame.xlsx");
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
################################################################################