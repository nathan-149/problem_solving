#include <iostream> 
#include <vector> 
#include <cmath>
using namespace std;

int DaysInMonth(int month, int year);
// Do not edit above this line. It is only shown so you can see the function signature.
/*
 * Complete the function below.
 */

/*
 * DaysBetween calculates the number of days between two dates
*/
int DaysBetween(int year1, int month1, int day1, int year2, int month2, int day2) {
    int month_start, month_end;
    int month_curr = month1;
    int year_curr = year1;
    int days_between = 0;

    // First compute the days left in the first month
    days_between += DaysInMonth(month_curr, year_curr) - day1;
    month_curr++;

    // Then, traverse through all the months and add days using helper fn DaysinMonth
    while(year_curr <= year2) {
        // Could try to simply add 365 days * (year2 - year1) for the days between the year difference
        // to save time, but this would not account for leap years.

        // We want to traverse through the entire year, unless
        // we're in year1, then we want to start from month1 + 1
        // and/or we're in year1 then we want to end at month2 - 1

        month_start = 1; // Traverse through all 12 months
        month_end = 12;

        if(year_curr == year1) 
            month_start = month1 + 1; // Traverse from month1 + 1 to end of year
        if(year_curr == year2)
            month_end = month2 - 1;

        for(int i=month_start; i<=month_end; i++) {
            days_between += DaysInMonth(i, year_curr); // Add days using helper fn DaysInMonth
        }
        year_curr += 1;
    }
    // Lastly, add the days in the final month
    days_between += day2;

    return days_between;
}

