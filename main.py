
import numpy as np
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt


st.header("UBC Course Compare")
url = "https://raw.githubusercontent.com/DonneyF/ubc-pair-grade-data/1516765eb6fd962066149b18ec8c6d64ae06046a/tableau-dashboard/UBCV"
url2 = "https://raw.githubusercontent.com/DonneyF/ubc-pair-grade-data/1516765eb6fd962066149b18ec8c6d64ae06046a/tableau-dashboard/UBCV"

course_list = ['AANB','ACAM','ADHE','AFST','AGEC','AMNE','ANAT','ANTH','APBI','APPP','APSC','AQUA','ARBC','ARBM','ARC *','ARCH','ARCL','ARST','ARTC','ARTH','ARTS','ASIA','ASIC','ASL','ASLA *','ASTR','ASTU','ATSC','AUDI','BA','BAAC','BABS','BAEN','BAFI','BAHR','BAIT','BALA','BAMA','BAMS','BAPA','BASC','BASM','BAUL','BEST','BIOC','BIOF','BIOL','BIOT','BMEG','BOTA','BRDG','BUSI','CAPS','CCFI','CCST','CDST','CEEN','CELL','CENS','CHBE','CHEM','CHIL','CHIN','CIVL','CLST *','CNPS','CNTO','COEC','COGS','COHR','COLX','COMM','COMR','CONS','CPEN','CPSC','CRWR','CSIS','CSPW','CTLN *','DANI','DENT','DES','DHYG','DMED','DSCI','ECED','ECON','ECPS','EDCP','EDST','EDUC','EECE','ELEC','ELI','EMBA *','ENDS *','ENGL','ENPH','ENPP *','ENST','ENVE','ENVR','EOSC','EPSE','ETEC','EXCH','EXGR','FACT *','FCOR','FEBC','FIPR','FISH','FIST','FMPR *','FMST','FNEL','FNH','FNIS','FOOD','FOPE','FOPR','FRE','FREN','FRSI *','FRST','FSCT','GEM','GENE','GEOG','GEOS','GERM','GREK','GRS','GRSJ','GSAT','HEBR','HESO *','HGSE','HINU','HIST','HPB','HUNU','IAR','IEST *','IGEN','ILS *','INDO *','INDS','INFO','INLB','ISCI','ITAL','ITST *','IWME','JAPN','JRNL','KIN','KORN','LAIS','LARC','LASO','LAST','LATN','LAW','LFS','LIBE','LIBR','LING','LLED','LWS','MANU','MATH','MDIA *','MDVL','MECH','MEDD','MEDG','MEDI','MES','MGMT *','MICB','MIDW','MINE','MRNE','MTRL','MUSC','NAME','NEPL *','NEST *','NEUR *','NRSC','NSCI','NURS','OBMS *','OBST','OHS *','ONCO','ORNT','ORPA','OSOT','PATH','PCTH','PERS','PHAR','PHIL','PHRM','PHTH','PHYL *','PHYS','PLAN','PLAS *','PLNT','POLI','POLS','PORT','PPGA','PRHC *','PSYC','PSYT','PUNJ','RADI *','RADS *','RELG','RES','RGLA *','RGST','RHSC','RMST','RUSS','SANS','SCAN','SCIE','SEAL','SGES *','SLAV','SOAL *','SOCI','SOIL','SOWK','SPAN','SPE','SPHA','SPPH','STAT','STS','SURG','SWED','TEST','THFL','THTR','TIBT','TRSC','UDES','UFOR','UKRN *','URO *','UROL *','URST','URSY','VANT','VGRD','VISA','VRHC *','VURS','WACH','WOOD','WRDS','WRIT *','ZOOL']

st.sidebar.header("Enter the courses you wish to compare")
st.sidebar.caption('Compare courses from 2014 to 2020')

cc1 = st.sidebar.selectbox(
    "Enter Course Code (for eg: MATH)",
    course_list, 71    )

year1 = st.sidebar.selectbox(
     'Enter year for Course 1',
     (list(range(2014, 2022))), 7)

term1 = st.sidebar.radio(
     "Select Term for Course 1:  Winter (W), Winter (S)",
     ('W', 'S'))
url = url + '/' + str(year1) + str(term1) +"/" 
url = url + "UBCV-" + str(year1) + str(term1) +"-" + cc1 +".csv"
course_num1 = pd.read_csv(url)
course_number_set1 = set(course_num1["Course"])

cn1 = st.sidebar.selectbox(
    "Enter of Course Number (for eg: 221, 121 etc)",
    course_number_set1 
    )

load_data1 = course_num1[(course_num1['Course'] == int(cn1))]
load_data1 = load_data1.drop(['Detail'], axis =1)
# ,'<50','50-54','55-59','60-63', '64-67','68-71', '72-75', '76-79', '80-84', '85-89','90-100'
st.write(load_data1.set_index('Campus'))


cc2 = st.sidebar.selectbox(
    "Enter Course name (for eg: COMM)",
    course_list, 75
    )

year2 = st.sidebar.selectbox(
     'Enter year for Course 2',
     (list(range(2014, 2021))),6)

term2 = st.sidebar.radio(
     "Select Term for Course 2:  Summer (S), Winter (W)",
     ('S', 'W'))

url2 = url2 + '/' + str(year2) + str(term2) +"/" 
url2 = url2 + "UBCV-" + str(year2) + str(term2) +"-" + cc2 +".csv"
course_num2 = pd.read_csv(url2)
course_number_set2 = set(course_num2["Course"])

cn2 = st.sidebar.selectbox(
    "Enter Course Number 2 (for eg: 221, 121 etc)",
    course_number_set2
    )
st.write("Comparing " + cc1 + str(cn1) + " with " + cc2  + str(cn2))

load_data2 = course_num2[(course_num2['Course'] == int(cn2))]
load_data2 = load_data2.drop('Detail', axis = 1)
st.write(load_data2.set_index('Campus'))
st.sidebar.caption('Having issues? Contact akshay.exun@gmail.com')

#Summary Stats
# prof_list = load_data1['Professor']
# avg_list = load_data1['Avg']
# summary_stats = pd.DataFrame(prof_list, avg_list)
# st.write(summary_stats)

# Matplotlib graphing grading trend

x =  ['<50','50-54','55-59','60-63', '64-67','68-71', '72-75', '76-79', '80-84', '85-89','90-100']
y = []
i=0

overall1 = load_data1[(load_data1['Section'] == 'OVERALL')]
overall2 = load_data2[(load_data2['Section']== 'OVERALL')]

# for items in x:
#     i=i+1
#     y[i] = overall1[(x[0])]
#     y[i] = dict(y[i])
    


y0 = overall1[(x[0])]
y0= dict(y0)
y1 = overall1[(x[1])]
y1 = dict(y1)
y2 = overall1[x[2]]
y2= dict(y2)
y3 = overall1[(x[3])]
y3 = dict(y3)
y4 = overall1[(x[4])]
y4 = dict(y4)
y5 = overall1[x[5]]
y5= dict(y5)
y6 = overall1[(x[6])]
y6 = dict(y6)
y7 = overall1[(x[7])]
y7 = dict(y7)
y8 = overall1[(x[8])]
y8 = dict(y8)
y9 = overall1[(x[9])]
y9 = dict(y9)
y10 = overall1[(x[10])]
y10 = dict(y10)

y11 = overall2[(x[0])]
y11= dict(y11)
y12 = overall2[(x[1])]
y12 = dict(y12)
y13 = overall2[x[2]]
y13= dict(y13)
y14 = overall2[(x[3])]
y14 = dict(y14)
y15 = overall2[(x[4])]
y15 = dict(y15)
y16 = overall2[x[5]]
y16= dict(y16)
y17 = overall2[(x[6])]
y17 = dict(y17)
y18 = overall2[(x[7])]
y18 = dict(y18)
y19 = overall2[(x[8])]
y19 = dict(y19)
y20 = overall2[(x[9])]
y20 = dict(y20)
y21 = overall2[(x[10])]
y21 = dict(y20)


y_c1 = [y0.values(),y1.values(),y2.values(),y3.values(),y4.values(),y5.values(),y6.values(),y7.values(),y8.values(),y9.values(),y10.values(), y10.values()]
y_c2 = [y11.values(),y12.values(),y13.values(),y14.values(),y15.values(),y16.values(),y17.values(),y18.values(),y19.values(),y20.values(), y21.values()]

chart_data = pd.DataFrame(
 y_c1 [0:(len(y_c1)-1)], x 
#plt.ylabel("Number of Students"),
# plt.title(overall1['Title'])
)

chart_data2 = pd.DataFrame(
    y_c2, x
)
st.subheader("Grade Distribution for " + cc1 + str(cn1) + ":")
st.bar_chart(chart_data)
avg1 = overall1['Avg']
avg1 = dict(y20)
st.subheader("Grade Distribution for " + cc2 + str(cn2) + ":")
st.bar_chart(chart_data2)



st.caption("Made by Akshay Khandelwal")
