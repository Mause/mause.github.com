function calc_age(year,month,day){
    "use strict";
    var cur_date = new Date();
    var seconds_in_year = 31535973734.399998;

    var birth_date = new Date(year, (month-1), day);
    var date_difference = (cur_date-birth_date);
    var years_difference = Math.floor(date_difference/seconds_in_year);

    var my_age = toWords(years_difference);
    if(my_age[my_age.length-1] === ' ')
        my_age = my_age.substring(0, my_age.length-1);
    return my_age;
}
document.getElementById('age').innerHTML = calc_age(1996,8,7);
