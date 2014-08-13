# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# <codecell>

school_data = pd.read_csv("/Users/larakattan/Desktop/Data Camp 2012/Data merged and ready for investigation.csv")
school_data

# <codecell>

school_data.head()

# <codecell>

school_data.bTreated.sum(0)

# <codecell>

plt.scatter(school_data[school_data['bTreated']==1].Pretest,school_data[school_data['bTreated']==1].Posttest1)
plt.title('Treatment group only: Pretest v. Posttest1')

# <codecell>

school_data['testImprovement'] = school_data.Posttest1 - school_data.Pretest
school_data.head()

# <codecell>

school_data['Posttest1'].min()

# <codecell>

plt.scatter(school_data[school_data['bTreated']==1].Pretest,school_data[school_data['bTreated']==1].testImprovement)
plt.title('Treatment group only: Pretest v. Treatment 1 effect')

# <codecell>

print 'Total of test improvements for treatment group =', school_data[school_data['bTreated']==1].testImprovement.sum(0) 
print 'Number of students in treatment group = ', school_data.bTreated.sum(0)
averageTreamentScoreImprovement = school_data[school_data['bTreated']==1].testImprovement.sum(0)/ school_data.bTreated.sum(0)
print 'Average test improvement for treatment group = ', averageTreamentScoreImprovement

# <codecell>

school_data.AssignedSchNum.unique()

# <codecell>

school_data.SchName.unique()

# <codecell>

school_data.SchType.unique()

