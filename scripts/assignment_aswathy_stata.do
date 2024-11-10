** read the data, set the working directory***
cd C:/Users/Sreekumarannair_Aswa/Desktop/assignment_aswathy
pwd
import delimited "C:/Users/Sreekumarannair_Aswa/Desktop/assignment_aswathy/data/clean/wfh_tidy_person.csv",clear

** summary of the data, missing values **
summarize
misstable summarize

** prepare data for analysis filtering , creating new varibale , transforming the data  and saving the file**
preserve
keep if treatment==1

** create new variable avergae performance, saved to new file**
gen avg_performance = (perform10 +perform11)/2
print avg_performance
avg_performance
list avg_performance

save "C:/Users/Sreekumarannair_Aswa/Desktop/assignment_aswathy/data/clean/new_data.dta"
summarize avg_performance


*** viaulaisation of the data, saving the graph in graph folder**

histogram avg_performance, width(1) frequency title("Average Performance Distribution")
graph export "/path/to/average_performance_histogram.png"
graph export "C:/Users/Sreekumarannair_Aswa/Desktop/assignment_aswathy/graphs/average_performance_histogram.png"
graph export "C:/Users/Sreekumarannair_Aswa/Desktop/assignment_aswathy/graphs/average_perf_stata_histogram.png"
