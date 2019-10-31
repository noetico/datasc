# -*- coding: utf-8 -*-
#Spyder Editor

#This is a temporary script file.
import subprocess
import sys
import os
import pip



      
def chkpkg():
    pkgs = ['numpy', 'scipy', 'pandas', 'money', 'xlrd']
    try:
        for pk in pkgs:
            __import__(pk)
            print("Package ready: %s" % pk)
    except ImportError as e:
        #from setuptools.command.easy_install import main as pyl
        for k in pkgs:
            #subprocess.call([sys.executable, "-m", "pip", "ïnstall", k])
            os.system('sudo pip install {0}'.format(k))



chkpkg() 

import numpy as np
import scipy as sc
import pandas as pd
from datetime import datetime as dtm
from scipy import stats as st
import colorama
from colorama import init, Fore, Back, Style
import io
#import os
import xlrd
from money import Money

init()

print(Fore.YELLOW + """ ***A small Python Data Analysis program to help you make simple quick analysis for business data.
Enjoy this little program. Thanks***
""")
print(Style.RESET_ALL)


#init()

def process_ANOVA():
    asktowrite = opts.exttofile
    if(asktowrite == 'y'):
        filewrite = open(opts.extfile, 'a+')
        print(filewrite)
    
    p1 = input("enter 1st file name including extension: >> ")
    

    f01 = os.getcwd() + '\\'  + p1
    if(asktowrite == 'y'):
        filewrite = open(opts.extfile, 'a+')
        filewrite.write("File 1: {0} \n".format(f01 ))
    if f01.endswith(".csv"):
        db1 = pd.read_csv(f01, header=None)

    elif f01.endswith(".xlsx") or f01.endswith(".xls"):
        db1 = pd.read_excel(io.FileIO(f01, 'r+'), header=0)
    
    p2 = input("enter 2nd file name including extension: >> ")
    f02 = os.getcwd() + '\\'  + p2
    if(asktowrite == 'y'):
        filewrite = open(opts.extfile, 'a+')
        filewrite.write("File 2: {0} \n".format(f02) )
    if f02.endswith(".csv"):
        db2 = pd.read_csv(f02, header=None)

    elif f02.endswith(".xlsx") or f02.endswith(".xls"):
        db2 = pd.read_excel(io.FileIO(f02, 'r+'), header=0)
    qry = input("Add another file> y/n")

    if(qry == 'y'):
        p3= input("enter 3rd file name including extension: >> ")
        f03 = os.getcwd() + '\\'  + p3
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("File 3: {0} \n" .format( f03) )
        if f03.endswith(".csv"):
            db3 = pd.read_csv(f03, header=None)

        elif f03.endswith(".xlsx") or f03.endswith(".xls"):
            db3 = pd.read_excel(io.FileIO(f03, 'r+'), header=0)
    try:
        print("Data Preview")
        print(db1[1:3])        
        row1 = input("Select column for ANOVA from file 1 with name: {0} >> " .format(p1))
        r1 = db1.iloc[:, int(row1)]
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("Column from file 1: {0} \n".format(r1) )
    except Exception as exc:
        print(exc)
        print("Choose proper columns for data... try again")

    try:
        print("Data Preview")
        print(db2[1:3])        
        row2 = input("Select column for ANOVA from file 2 with name: {0} >> " .format(p2))
        r2 = db2.iloc[:, int(row2)]
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("Column from file 2: {0} \n" .format(r2) )
    except Exception as exc:
        print(exc)
        print("Choose proper columns for data... try again")
    
    try:
        if(qry == 'y'):
            print("Data Preview")
            print(db3[1:3])        
            row3 = input("Select column for ANOVA from file 3 with name: {0} >> " .format( p3))
            r3 = db3.iloc[:, int(row3)]
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("Column from file 3: {0} \n" .format(r3) )
    except Exception as exc:
        print(exc)
        print("Choose proper columns for data... try again")

    #Process f_oneway with r1,r2,r3

    if(qry == 'y'):
        anva, pvalx = st.f_oneway(r1, r2, r3)
        print(str(st.f_oneway(r1, r2, r3)))
        print(pvalx)
        print(anva)
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("ANOVA Result: \n")
            filewrite.write("P-Value: {0} \n".format(pvalx) )
            filewrite.write("Stat: {0} \n" .format(anva))
        opts()
    else:
        anva, pvalx = st.f_oneway(r1, r2)
        print(str(st.f_oneway(r1, r2)))
        print(pvalx)
        print(anva)
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("ANOVA Result: \n")
            #filewrite.write(str())
            filewrite.write("P-Value: {0} \n".format(pvalx) )
            filewrite.write("Stat: {0} \n" .format(anva))
        opts()
        
#Perform a T test on a single sample
def ttst_1samp():
     asktowrite = opts.exttofile
     if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            print(filewrite)
     p1 = input("enter 1st file name including extension: >> ")
     f01 = os.getcwd() + '\\'  + p1
     if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("First file: {0} \n\n" .format( (os.getcwd() + '\\'  + p1)))

     if f01.endswith(".csv"):
        db1 = pd.read_csv(f01, header=None)

     elif f01.endswith(".xlsx") or f01.endswith(".xls"):
        db1 = pd.read_excel(io.FileIO(f01, 'r+'), header=0)

     print("Data Preview")
     print(db1[1:3])        
     row1 = input("Select column for T-Test from file 1 with name: {0} >> " .format( p1))
     r1 = db1.iloc[:, int(row1)]
     if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("Selected Row: {0} \n\n".format(r1))  
     kmean = input("Enter desired mean to use for calculation: > ")
     ttst = st.ttest_1samp(r1, (float(kmean)))
     print("TTest: Result: {0} \n".format(ttst))
     if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("TTest: Result: {0} \n".format(ttst))
     opts()


def fileloc():
    p = input("enter file name including extension: >> ")
#    c = os.path.abspath(p)
    c = os.getcwd() + '\\'  + p
    return c




def preview_data(i):
    print(i[1:10])





def processmean():
    try:
        
        
        asktowrite = opts.exttofile
        print(asktowrite)
        filewrite = open(opts.extfile, 'a+')
        filewrite.write('Operation: Mean, Max, Min, Percentile etc \n\n')
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            print(filewrite)

        d = fileloc()

        if d.endswith(".csv"):
            db = pd.read_csv(d, header=None)
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write(d+'\n')

        elif d.endswith(".xlsx") or d.endswith(".xls"):
            db = pd.read_excel(io.FileIO(d, 'r+'), header=0)
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write(d+'\n')
#df = pd.DataFrame(db)


        hdr = db[1:5]
        print("Data Preview")
        print(hdr)
        print("""
                |
                |
                |
        """)
        rrows = input("Select column: >> ")
        filewrite = open(opts.extfile, 'a+')
        filewrite.write('Selected Column is: {0} \n\n' .format(rrows))
        #create variable that will hold sample value to test if column contains numbers
        tst = db.iloc[:, int(rrows)]
        #test if value is of type int or float
        if type(int(tst[0])) is int or type(float(tst[0])) is float:
            #create a dataframe to allow us get the max value
            df = pd.DataFrame(db)
            
            perc = input("Enter percentile: ")
            #select entered column number from dataset
            dat = db.iloc[:, int(rrows)]

            print("{0}th Percentile is: {1}" .format(perc, np.percentile(dat, float(perc))))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("{0}th Percentile is: {1} \n\n" .format(perc, np.percentile(dat, float(perc))))

            print("Mean value is: {0}" .format(np.mean(dat)))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("Mean value is: {0} \n\n" .format(np.mean(dat)))

            print("The highest value is: {0}".format(np.max(dat)))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("The highest value is: {0} \n\n" .format(np.max(dat)))

            print("The lowest value is {0}" .format(np.min(dat)))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("The lowest value is {0} \n\n".format(np.min(dat)))

            print("The median value is {0}" .format(np.median(dat)))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                filewrite.write("The median value is {0} \n\n" .format(np.median(dat)))
            
            
            #check if data has header and user wants to add header
            print(df.head(2))
            qry = input("Add header to data for deeper analysis like highest and lowest row. Preview data above? y/n >> ")
            if qry == "y":
                #automatically give numbered headers by creating a list with numbers in the range of the numbe of columns
                ids = list(range(0, (len(df.columns))))
            ##create an empty list which will be used to convert the range to strings and pass as columns header
                heading = []
                for x in ids:
                    heading.append(str(x))
                df.columns = heading
                print("Headers and Data Frame Preview with headers")
                
                print(heading)
                print(df.head(2))
                print("""
                |
                |
                    """)
                print("Row with max value based on selected column")
                print(df.loc[df[rrows] == np.max(dat)])
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("The row with highest value in data set based on selected column is: \n {0} \n\n" .format(df.loc[df[rrows] == np.max(dat)]))
                
                print("Row with min value based on selected column")
                print(df.loc[df[rrows] == np.min(dat)])
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("The row with lowest value in data set based on selected column is: \n {0} \n\n" .format(df.loc[df[rrows] == np.min(dat)]))
                sel = input("Return top n rows. Enter a value 10 to return the top 10 values based on the selected column: >> ")
                sortmax = df.sort_values([rrows], ascending=[False])
                sortmin = df.sort_values([rrows], ascending=[True])
                print("Top {0} rows: {1}" .format(sel, sortmax.head(int(sel))))
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("Top {0} rows: {1} \n\n" .format(sel, sortmax.head(int(sel))))

                print("""
                |
                |
                |
                """)

                print("Bottom {0} rows: {1}".format(sel, sortmin.head(int(sel))))
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("Bottom {0} rows: {1} \n\n" .format(sel, sortmin.head(int(sel))))
                #Find outliers
                std_data = np.std(dat)
                data_mean = np.mean(dat)
                outlier_mark_off = std_data * 3 #multiply standard dev by 3 to cater for outlier
                outlier_lower = data_mean - outlier_mark_off
                outlier_upper = data_mean + outlier_mark_off
                outlier_list_upper = []
                outlier_list_lower = []

                for outlier in dat:
                    if outlier > outlier_upper:
                        outlier_list_upper.append(df.loc[df[selcol] == outlier])
                        
                    
                    if outlier < outlier_lower:
                        outlier_list_lower.append(df.loc[df[selcol] == outlier])
                        
                if(asktowrite == 'y'):
                            filewrite = open(opts.extfile, 'a+')
                            filewrite.write("Outlier Found (High Anomally):  {0} \n\n" .format(outlier_list_upper))
                            filewrite.write("Outlier Found (Low Anomally):  {0} \n\n" .format(outlier_list_lower))

                print("Outlier Found (High Anomally):  {0} \n\n" .format(outlier_list_upper))
                print("Outlier Found (Low Anomally):  {0} \n\n" .format(outlier_list_lower))
               
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("__End output__")

                opts()
            elif qry == "n":



                selcol = input("Enter Column Name for max value calc >> ")

            #select row with highest value in selected operation column using comparator with numpy array
                print("Row with max value in selected column")
                print(df.loc[df[selcol] == np.max(dat)])
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("The row with highest value in selected columns is: \n {0} \n\n" .format(df.loc[df[selcolmax] == np.max(dat)]))
                print("""
                |
                |
                |
        """)
                print("Row with min value in selected column")
            
                
                print(df.loc[df[selcol] == np.min(dat)])
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("The row with highest value in selected columns is: \n {0} \n\n" .format(df.loc[df[selcolmin] == np.min(dat)]))
            
                sel = input("Return top n rows. Enter a value 10 to return the top 10 values based on the selected column: >> ")
                sortmax = df.sort_values([selcol], ascending=[False])
                sortmin = df.sort_values([selcol], ascending=[True])
                print("Top {0} rows: {1}" .format(sel, sortmax.head(int(sel))))
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("Top {0} rows: {1} \n\n" .format(sel, sortmax.head(int(sel))))

                print("""
                |
                |
                |
                """)

                print("Bottom {0} rows: {1}".format(sel, sortmin.head(int(sel))))
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("Bottom {0} rows: {1} \n\n" .format(sel, sortmin.head(int(sel))))

                #Find outliers
                std_data = np.std(dat)
                data_mean = np.mean(dat)
                outlier_mark_off = std_data * 3 #multiply standard dev by 3 to cater for outlier
                outlier_lower = data_mean - outlier_mark_off
                outlier_upper = data_mean + outlier_mark_off
                outlier_list_upper = []
                outlier_list_lower = []

                for outlier in dat:
                    if outlier > outlier_upper:
                        outlier_list_upper.append(df.loc[df[selcol] == outlier])
                        
                    
                    if outlier < outlier_lower:
                        outlier_list_lower.append(df.loc[df[selcol] == outlier])
                        
                if(asktowrite == 'y'):
                            filewrite = open(opts.extfile, 'a+')
                            filewrite.write("Outlier Found (High Anomally):  {0} \n\n" .format(outlier_list_upper))
                            filewrite.write("Outlier Found (Low Anomally):  {0} \n\n" .format(outlier_list_lower))

                print("Outlier Found (High Anomally):  {0} \n\n" .format(outlier_list_upper))
                print("Outlier Found (Low Anomally):  {0} \n\n" .format(outlier_list_lower))
               
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("__End output__")


                opts()

        else: 
            print("Column is not of number type, int or float")
            preview_data(db)
            print("Try again, select columns that are numbers")
            processmean()

    except ValueError as e:
        print(e)
        print("Try again, select columns that are numbers")
        processmean()

def fileCompare():
    try:
        fileext = [".csv", ".cs", ".php", ".html", ".css", ".js", ".xml", ".xhtml", ".htm", ".txt", ".jpg", ".png", ".bmp"]
        asktowrite = opts.exttofile
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            print(filewrite)

        p1 = input("enter 1st file name including extension: >> ")
    

        f01 = os.getcwd() + '\\'  + p1
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("File 1: {0} \n".format(f01 ))
        for x in fileext:
            if f01.endswith(x):

                file1 = open(f01, 'r')
                f01_stat = os.stat(f01)
                f01_size = f01_stat.st_size
        f01_lines = file1.readlines()
        print(f01_lines[0])
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("First Line: " + f01_lines[0] + '\n')
            
                   

        
        p2 = input("enter 2nd file name including extension: >> ")
    

        f02 = os.getcwd() + '\\'  + p2
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("File 2: {0} \n".format(f02))
        for x in fileext:
            if f02.endswith(x):
                file2 = open(f02, 'r')
                f02_stat = os.stat(f02)
                f02_size = f02_stat.st_size
        f02_lines = file2.readlines()
        print(f02_lines[0])
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("First Line: " + f02_lines[0] + '\n')

        if len(f01_lines) != len(f02_lines):
            print("File Length; number of lines not the same, file may be modified or different")
            print("File1 length: >  "+str(len(f01_lines)))
            print("File2 length: > " + str(len(f02_lines)))
            if(asktowrite == 'y'):
                filewrite = open(opts.extfile, 'a+')
                print("File 1 size: {0} bytes, File 2 size: {1} bytes". format(f01_size, f02_size))
                filewrite.write("File Length; number of lines not the same, file may be modified or different \n")
                if(f01_size != f02_size):
                    print("Files are of different sizes; file may have been modified")
                    filewrite.write("Files are of different sizes; file may have been modified \n")
                    filewrite.write("File 1 size: {0} bytes, File 2 size: {1} bytes \n". format(f01_size, f02_size))
                filewrite.write("File1 length: > {0} \n" .format(str(len(f01_lines))))
                filewrite.write("File2 length: > {0} \n" .format(str(len(f02_lines))))

        
          
        fact2 = f01_lines == f02_lines
        print("Do files have equal number of lines? : {0} \n" .format(str(fact2)))
        if(asktowrite == 'y'):
            filewrite = open(opts.extfile, 'a+')
            filewrite.write("Do files have equal number of lines?:  {0} \n" .format(str(fact2)))
        x = 0  
        yd = 0          
        while x < len(f01_lines) and yd < len(f02_lines) and ((not (x > len(f01_lines))) or ( not (yd > len(f02_lines))) or (not (x > len(f02_lines))) or (not (yd > len(f01_lines)))):
            if((f01_lines[x]) not in (f02_lines[yd])):
                print("Line {0}; containing: {1} --is different. \n" .format(str(x), f01_lines[x]) )
                if(asktowrite == 'y'):
                    filewrite = open(opts.extfile, 'a+')
                    filewrite.write("Line {0}; containing: {1} --is different. \n" .format(str(x), f01_lines[x]) )
            
            x += 1
            yd += 1
          
                
            
            

       
            
        opts()

                    

    except FileExistsError as e:
        print("Check selected files are of supported types")

        
        
def opts():
    opt = input(Fore.YELLOW + """ Please select an operation to perform amongst the options (Just hit the number for your desired option, followed by the enter key):
1. Mean, Highest, Lowest Values
2. 1-Way ANOVA test
3. T-Test with one sample
4. T-test with 2 samples
5. Audit: Compare 2 files
11. Backup this file (Use this if you want to play with the code so you have a clean backup)
12. Exit

""")
    print(Style.RESET_ALL)

    if opt == '2':
        tofile = input("Write output to file in /DataScProjects folder? y/n: >> ")
        opts.exttofile = tofile
        if(tofile == 'y'):
            cur = dtm.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            currdate = cur.replace(':', '_')
            fname = '\\' + 'DataScProjects' + '\\' +'ANOVA_' + currdate
            opts.fname = '\\' + 'DataScProjects' + '\\' + 'ANOVA_' + currdate
            os.mkdir(os.getcwd() + fname )
            filestr = os.getcwd() +  fname + '\\' + 'ANOVA_'+currdate + '.txt'
                #Create attribute to access file outsdie this def 
            opts.extfile = filestr
            f = open(filestr, 'w+')
        process_ANOVA()

    if opt == '3':
        tofile = input("Write output to file in /DataScProjects folder? y/n: >> ")
        opts.exttofile = tofile
        if(tofile == 'y'):
            cur = dtm.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            currdate = cur.replace(':', '_')
            fname = '\\' + 'DataScProjects' + '\\' +'TTest1Samp_' + currdate
            os.mkdir(os.getcwd() +  fname )
            filestr = os.getcwd() +  fname + '\\' + 'TTest_'+currdate + '.txt'
            opts.extfile = filestr
            f = open(filestr, 'w+')
        ttst_1samp()
    if opt=='1':
        tofile = input("Write output to file in /DataScProjects folder? y/n: >> ")
        opts.exttofile = tofile
        if(tofile == 'y'):
            cur = dtm.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            currdate = cur.replace(':', '_')
            fname = '\\' + 'DataScProjects' + '\\' + 'Mean_Perc_' + currdate
            os.mkdir(os.getcwd() + fname )
            filestr = os.getcwd() +  fname + '\\' + 'Mean_Perc_'+currdate + '.txt'
            opts.extfile = filestr
            f = open(filestr, 'w+')
        processmean()

    if opt == '5':
        tofile = input("Write output to file in /DataScProjects folder? y/n: >> ")
        opts.exttofile = tofile
        if(tofile == 'y'):
            cur = dtm.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            currdate = cur.replace(':', '_')
            fname = '\\' + 'DataScProjects' + '\\' + 'FileCompare_' + currdate
            os.mkdir(os.getcwd() + fname )
            filestr = os.getcwd() +  fname + '\\' + 'FileCompare_'+currdate + '.txt'
            opts.extfile = filestr
            f = open(filestr, 'w+')
        fileCompare()

    if opt == '11':
        from shutil import copyfile, copy2
        cur = dtm.now().strftime("%d-%b-%Y %H:%M:%S.%f")
        currdate = cur.replace(':', '_')
        copy2(os.getcwd() + ('\\datasc.py'), os.getcwd()+('\\datasc_{0}.py'.format(currdate)))
        
        print("File backed up successfully. To restore, just rename backup to datasc.py")
        opts()

    if opt == '12':
        print('GRRRR! It\'s just a file...We\'ll go away now or you could Close the terminal or command window')


    
opts()

        
        

#check if row is of number type



    






    








    

