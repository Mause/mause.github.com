---
layout: post
title: "Applying Mathematics - Assessment 2"
tags:
    - python
    - notebook
---
All questions are (number)(letter), so to find question 2a, just do
&lt;Ctrl-F&gt;2a

Some standard library imports

**In [2]:**

{% highlight python %}
from io import StringIO
from functools import wraps
from functools import partial
from operator import itemgetter
from collections import defaultdict
from csv import DictReader, DictWriter
{% endhighlight %}

Imports for web requests, and data manipulation and display

**In [3]:**

{% highlight python %}
# web requests
import requests

# to display and process data
%pylab inline
import pandas
import ipy_table as pyt
import prettyplotlib as ppl
{% endhighlight %}

    Populating the interactive namespace from numpy and matplotlib
    

Pull in the survey data

**In [28]:**

{% highlight python %}
r = requests.get(
    url='https://docs.google.com/spreadsheet/ccc',
    params={
        'key': '0ApTk7F_aw6vqdGE4b0VLZTBkMmwyZk5RNV9lbC1Nb1E',
        'output': 'csv'
    }
)

data = pandas.read_csv(StringIO(r.text))

{% endhighlight %}

Some useful functions

**In [5]:**

{% highlight python %}
def surveys_for(field, value):
    return data[data[field] == value]


surveys_for_catagory = partial(surveys_for, 'Occupation Catagory')
for_gender = partial(surveys_for, 'Gender')


def for_field(field, spec=None):
    return data[field] if spec is None else spec[field]

def ints(seq):
    return list(map(int, seq))

def calc_mus(data):
    data['MUS'] = data.apply(
        lambda row: sum(row[ACTIVITIES]),
        axis=1
    )
    return data

{% endhighlight %}

And some useful constants;

**In [6]:**

{% highlight python %}
ACTIVITIES = ['Recording Data', 'Interpreting Data', 'Using Operations', 'Estimating', 'Using a Calculator', 'Problem Solving']
CATAGORIES = {
    'BU': 'Business',
    'HS': 'Health Sciences',
    'HU': 'Humanities'
}
{% endhighlight %}

Calculate and add the MUS data, sort the genders

**In [7]:**

{% highlight python %}
data = calc_mus(data)

females = for_gender('F')
males = for_gender('M')
{% endhighlight %}

## 2a

**In [10]:**

{% highlight python %}
males_mus = for_field('MUS', males)

print('Male average:', males_mus.mean())
{% endhighlight %}

    Male average: 7.78571428571
    

## 2b

**In [11]:**

{% highlight python %}
females_mus = for_field('MUS', females)

print('Female average:', females_mus.mean())
{% endhighlight %}

    Female average: 8.25
    

## 2c

Judging by these results, I would say that females use math more than males.
Perhaps because they tend towards business roles?

## 3a

**In [12]:**

{% highlight python %}
IMPORTANCE = {
    'V': 2,  # Very important
    'I': 1,  # Important
    'N': 0   # Not important
}
{% endhighlight %}

## 3b

**In [15]:**

{% highlight python %}
def importance(lst):
    return lst['Importance Of Math'].apply(IMPORTANCE.get).mean().round(2)
{% endhighlight %}

**In [16]:**

{% highlight python %}
pyt.make_table([
    ('Average female importantance of math', importance(females)),
    ('Average male importantance of math', importance(males))
])
{% endhighlight %}




<table border="1" cellpadding="3" cellspacing="0"  style="border:1px solid black;border-collapse:collapse;"><tr><td>Average&nbspfemale&nbspimportantance&nbspof&nbspmath</td><td>1.31</td></tr><tr><td>Average&nbspmale&nbspimportantance&nbspof&nbspmath</td><td>1.36</td></tr></table>



It would seem that males rate maths as being more important for their jobs than
females.

## 4a

Perhaps the older they are, the more used to using maths directly they are? As
opposed through an abstraction such as a computer? Might this affect how much
they perceive themselves as relying on math?

Essentially;
> Group all people by age group,
> determine average perceived reliance on mathematics?

## 4b

**In [22]:**

{% highlight python %}
# sort people into their age groups
ages = data.groupby('Age')

# determine averages of each age group, round to 2 decimal places
rating_to_age = {
    age: round(for_field('MUS', people).mean(), 2)
    for age, people in ages
}

# sort by age range
table_rating_to_age = sorted(rating_to_age.items(), key=itemgetter(0))

pyt.make_table([['Age Range', 'Rating']] + table_rating_to_age)
pyt.apply_theme('basic')
{% endhighlight %}




<table border="1" cellpadding="3" cellspacing="0"  style="border:1px solid black;border-collapse:collapse;"><tr><td  style="background-color:LightGray;"><b>Age&nbspRange</b></td><td  style="background-color:LightGray;"><b>Rating</b></td></tr><tr><td  style="background-color:Ivory;">15-19</td><td  style="background-color:Ivory;">11.0</td></tr><tr><td  style="background-color:AliceBlue;">20-29</td><td  style="background-color:AliceBlue;">7.4</td></tr><tr><td  style="background-color:Ivory;">30-39</td><td  style="background-color:Ivory;">9.43</td></tr><tr><td  style="background-color:AliceBlue;">40-49</td><td  style="background-color:AliceBlue;">7.7</td></tr><tr><td  style="background-color:Ivory;">50-59</td><td  style="background-color:Ivory;">6.5</td></tr></table>



**In [23]:**

{% highlight python %}
# grab the names and values in the appropriate order
rating_to_age_names = list(rating_to_age.keys())
rating_to_age_names = sorted(rating_to_age_names)
rating_to_age_values = list(map(rating_to_age.get, rating_to_age_names))

index = np.arange(len(rating_to_age))
bar_width = 0.35

ppl.bar(index, rating_to_age_values, bar_width)
plt.title('Age range to average rating')
plt.xticks(index + bar_width, rating_to_age_names)
plt.ylabel('Rating')
None
{% endhighlight %}


![png](data:image/png;base64,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)


## 5a

**In [27]:**

{% highlight python %}
mus = for_field('MUS', data)

ppl.hist(mus)
plt.title('Mathematical Usage Scores')
plt.ylabel('Freq')
plt.xlabel('Score ranges')
None
{% endhighlight %}


![png](data:image/png;base64,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)


## 5b

The histogram shows a large clumping of people perceiving their jobs as
requiring mathematics in high quantity, with another clump showing people who do
not perceive it as being as important.

We can conclude that people in Business, the Humanities, and the Health Sciences
perceive their jobs as requiring maths in quantity.

## 6a

**In [25]:**

{% highlight python %}
# calculate the sums of the different catagories
activities_to_use = {
    field: for_field(field).sum()
    for field in ACTIVITIES
}

# sort em by sum
activities_to_use = sorted(activities_to_use.items(), key=itemgetter(1), reverse=True)

pyt.make_table([['Activity', 'Sum']] + activities_to_use)
pyt.apply_theme('basic')
{% endhighlight %}




<table border="1" cellpadding="3" cellspacing="0"  style="border:1px solid black;border-collapse:collapse;"><tr><td  style="background-color:LightGray;"><b>Activity</b></td><td  style="background-color:LightGray;"><b>Sum</b></td></tr><tr><td  style="background-color:Ivory;">Recording&nbspData</td><td  style="background-color:Ivory;">51</td></tr><tr><td  style="background-color:AliceBlue;">Interpreting&nbspData</td><td  style="background-color:AliceBlue;">44</td></tr><tr><td  style="background-color:Ivory;">Estimating</td><td  style="background-color:Ivory;">38</td></tr><tr><td  style="background-color:AliceBlue;">Problem&nbspSolving</td><td  style="background-color:AliceBlue;">37</td></tr><tr><td  style="background-color:Ivory;">Using&nbspOperations</td><td  style="background-color:Ivory;">37</td></tr><tr><td  style="background-color:AliceBlue;">Using&nbspa&nbspCalculator</td><td  style="background-color:AliceBlue;">34</td></tr></table>



## 6b

Unsurprisingly, the recording of data is the most prevalent form of mathematics
in the real world, as the simple act of recording data is perfomed everywhere,
whilst using a calculator seems surprising uncommon.

## 7

**In [26]:**

{% highlight python %}
# calculate the average MUS values for the different profesions
categories = {}
for code in CATAGORIES:
    surveys = surveys_for('Occupation Catagory', code)
    mus_values = for_field('MUS', surveys)

    # get the appropriate name for the catagory
    cat_name = CATAGORIES.get(code)
    categories[cat_name] = round(mus_values.mean(), 2)

# sort by MUS average
categories = sorted(categories.items(), key=lambda r: r[1], reverse=True)
    
pyt.make_table([['Category', 'Rating']] + categories)
pyt.apply_theme('basic')
{% endhighlight %}




<table border="1" cellpadding="3" cellspacing="0"  style="border:1px solid black;border-collapse:collapse;"><tr><td  style="background-color:LightGray;"><b>Category</b></td><td  style="background-color:LightGray;"><b>Rating</b></td></tr><tr><td  style="background-color:Ivory;">Humanities</td><td  style="background-color:Ivory;">9.44</td></tr><tr><td  style="background-color:AliceBlue;">Business</td><td  style="background-color:AliceBlue;">8.43</td></tr><tr><td  style="background-color:Ivory;">Health&nbspSciences</td><td  style="background-color:Ivory;">5.8</td></tr></table>



It would seem that the humanities use the most math.

## Postscript

This code generates a final `.csv` with the MUS included for all the records.

**In [37]:**

{% highlight python %}
data.to_csv('output.csv')

{% endhighlight %}
