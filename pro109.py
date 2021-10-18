import plotly.figure_factory as pf
import statistics
import csv
import pandas as pe 
data_frame=pe.read_csv("projects\pro 109\StudentsPerformance.csv")
mathlist = data_frame["math score"].to_list()
readinglist = data_frame["reading score"].to_list()
writinglist = data_frame["writing score"].to_list()

mathmean = statistics.mean(mathlist)
writingmean = statistics.mean(writinglist)
readingmean = statistics.mean(readinglist)

mathmedian = statistics.median(mathlist)
writingmedian = statistics.median(writinglist) 
readingmedian = statistics.median(readinglist) 

mathmode = statistics.mode(mathlist)
writingmode = statistics.mode(writinglist)
readingmode = statistics.mode(readinglist)

mathstdDev = statistics.stdev(mathlist)
writingstdDev = statistics.stdev(writinglist)
readingstdDev = statistics.stdev(readinglist)

mean_data=[mathmean,writingmean,readingmean]
mean_all=statistics.mean(mean_data)
print("Mean: ", mean_all)

mode_data=[mathmode,writingmode,readingmode]
mode_all=statistics.mean(mode_data)
print("Mode: ", mode_all)

median_data=[mathmedian,writingmedian,readingmedian]
median_all=statistics.mean(median_data)
print("Median: ", median_all)

math1stdDevStart, math1stdDevEnd = mathmean - mathstdDev, mathmean + mathstdDev
math2stdDevStart, math2stdDevEnd = mathmean - (2*mathstdDev), mathmean + (2*mathstdDev)
math3stdDevStart, math3stdDevEnd = mathmean - (3*mathstdDev), mathmean + (3*mathstdDev)

writing1stdDevStart, writing1stdDevEnd = writingmean - writingstdDev, writingmean + writingstdDev
writing2stdDevStart, writing2stdDevEnd = writingmean - (2*writingstdDev), writingmean + (2*writingstdDev)
writing3stdDevStart, writing3stdDevEnd = writingmean - (3*writingstdDev), writingmean + (3*writingstdDev)

reading1stdDevStart, reading1stdDevEnd = readingmean - readingstdDev, readingmean + readingstdDev
reading2stdDevStart, reading2stdDevEnd = readingmean - (2*readingstdDev), readingmean + (2*readingstdDev)
reading3stdDevStart, reading3stdDevEnd = readingmean - (3*readingstdDev), readingmean + (3*readingstdDev)

mathDataWithin1std = [result for result in mathlist if result > math1stdDevStart and result < math1stdDevEnd]
mathDataWithin2std = [result for result in mathlist if result > math2stdDevStart and result < math2stdDevEnd]
mathDataWithin3std = [result for result in mathlist if result > math3stdDevStart and result < math3stdDevEnd]

writingDataWithin1std = [result for result in writinglist if result > writing1stdDevStart and writing1stdDevEnd]
writingDataWithin2std = [result for result in writinglist if result > writing2stdDevStart and writing2stdDevEnd]
writingDataWithin3std = [result for result in writinglist if result > writing3stdDevStart and writing3stdDevEnd]

readingDataWithin1std = [result for result in readinglist if result > reading1stdDevStart and reading1stdDevEnd]
readingDataWithin2std = [result for result in readinglist if result > reading2stdDevStart and reading2stdDevEnd]
readingDataWithin3std = [result for result in readinglist if result > reading3stdDevStart and reading3stdDevEnd]

print("Maths Score for 1sd",len(mathDataWithin1std)*100/len(mathlist))
print("Maths Score for 2sd",len(mathDataWithin2std)*100/len(mathlist))
print("Maths Score for 3sd",len(mathDataWithin3std)*100/len(mathlist))

print("Writing Score for 1sd",len(writingDataWithin1std)*100/len(writinglist))
print("Writing Score for 2sd",len(writingDataWithin2std)*100/len(writinglist))
print("Writing Score for 3sd",len(writingDataWithin3std)*100/len(writinglist))

print("reading Score for 1sd",len(readingDataWithin1std)*100/len(readinglist))
print("reading Score for 2sd",len(readingDataWithin2std)*100/len(readinglist))
print("reading Score for 3sd",len(readingDataWithin3std)*100/len(readinglist))

