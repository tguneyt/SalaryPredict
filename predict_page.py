
import streamlit as st
import pandas as pd
from preprocessing import preprocess



def show_predict_page(model):
   
   st.title("Software Developer Salary Prediction")

   st.write("""# We need some information""")

   countries = ('Argentina',
   'Australia',
   'Austria',
   'Bangladesh',
   'Belarus',
   'Belgium',
   'Bosnia and Herzegovina',
   'Brazil',
   'Bulgaria',
   'Canada',
   'Chile',
   'China',
   'Colombia',
   'Croatia',
   'Czech Republic',
   'Denmark',
   'Dominican Republic',
   'Egypt',
   'Estonia',
   'Finland',
   'France',
   'Germany',
   'Greece',
   'Hong Kong (S.A.R.)',
   'Hungary',
   'India',
   'Indonesia',
   'Iran, Islamic Republic of...',
   'Ireland',
   'Israel',
   'Italy',
   'Japan',
   'Kazakhstan',
   'Kenya',
   'Latvia',
   'Lithuania',
   'Malaysia',
   'Mexico',
   'Morocco',
   'Nepal',
   'Netherlands',
   'New Zealand',
   'Nigeria',
   'Norway',
   'Pakistan',
   'Peru',
   'Philippines',
   'Poland',
   'Portugal',
   'Romania',
   'Russian Federation',
   'Saudi Arabia',
   'Serbia',
   'Singapore',
   'Slovakia',
   'Slovenia',
   'South Africa',
   'South Korea',
   'Spain',
   'Sri Lanka',
   'Sweden',
   'Switzerland',
   'Taiwan',
   'Thailand',
   'Turkey',
   'Ukraine',
   'United Arab Emirates',
   'United Kingdom',
   'United States',
   'Viet Nam',
   'Other'
   )

   ages = ('0 - 24 years old', '25 - 44 years old', '45 years or older')

   students=(
      'No', 'Yes, part-time', 'Yes, full-time'
   )

   formaleducations = (
      'Bachelor’s degree (BA, BS, B.Eng., etc.)',
   'Some college/university study without earning a degree',
   'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
   'Master’s degree (MA, MS, M.Eng., MBA, etc.)',
   'Associate degree',
   'Professional degree (JD, MD, etc.)',
   'Primary/elementary school',
   'Other doctoral degree (Ph.D, Ed.D., etc.)',
   'I never completed any formal education'
   )

   undergradmajors = (
      'A natural science (ex. biology, chemistry, physics)',
   'Computer science, computer engineering, or software engineering',
   'A business discipline (ex. accounting, finance, marketing)',
   'Another engineering discipline (ex. civil, electrical, mechanical)',
   'Web development or web design',
   'Information systems, information technology, or system administration',
   'A humanities discipline (ex. literature, history, philosophy)',
   'Mathematics or statistics',
   'A social science (ex. anthropology, psychology, political science)',
   'Fine arts or performing arts (ex. graphic design, music, studio art)',
   'A health science (ex. nursing, pharmacy, radiology)',
   'I never declared a major'
   )



   employments = (
      'Employed full-time',
   'Employed part-time',
   'Independent contractor, freelancer, or self-employed',
   'Not employed, and not looking for work',
   'Not employed, but looking for work',
   'Retired'
   )


   jobsatisfactions = ('Moderately dissatisfied',
   'Slightly satisfied',
   'Moderately satisfied',
   'Neither satisfied nor dissatisfied',
   'Slightly dissatisfied',
   'Extremely dissatisfied',
   'Extremely satisfied')


   companysizes =(
      '10,000 or more employees',
   '10 to 19 employees',
   '20 to 99 employees',
   '1,000 to 4,999 employees',
   '100 to 499 employees',
   '500 to 999 employees',
   '5,000 to 9,999 employees',
   'Fewer than 10 employees'
   )

   careersatisfactions = ('Neither satisfied nor dissatisfied',
   'Moderately satisfied',
   'Slightly satisfied',
   'Moderately dissatisfied',
   'Slightly dissatisfied',
   'Extremely satisfied',
   'Extremely dissatisfied')

   lastnewjobs = ('More than 4 years ago',
   'Between 1 and 2 years ago',
   'Between 2 and 4 years ago',
   'Less than a year ago',
   "I've never had a job")


   hopefiveyears = ("Working in a different or more specialized technical role than the one I'm in now",
   'Working as a founder or co-founder of my own company',
   'Working in a career completely unrelated to software development',
   'Working as a product manager or project manager',
   'Doing the same work',
   'Working as an engineering manager or other functional manager',
   'Retirement')


   yearscodings = (
      '30 or more years',
   '6-8 years',
   '9-11 years',
   '0-2 years',
   '15-17 years',
   '18-20 years',
   '3-5 years',
   '12-14 years',
   '24-26 years',
   '21-23 years',
   '27-29 years'
   )

   yearscodingprofs = (
      '18-20 years',
   '0-2 years',
   '3-5 years',
   '12-14 years',
   '6-8 years',
   '9-11 years',
   '24-26 years',
   '15-17 years',
   '30 or more years',
   '21-23 years',
   '27-29 years'
   )

   operatingsystems = ('Linux-based', 'Windows', 'MacOS', 'BSD/Unix')

   timeFullyProductives = ('Less than three months', 'More than three months')

   ethicschooses = ('Depends on what it is', 'No', 'Yes')

   dependents = ('Yes', 'No')

   numberofmonitors = ('2', '1', '3', 'More than 4', '4')

   waketimes = ('Between 6:01 - 7:00 AM',
   'Before 5:00 AM',
   'Between 7:01 - 8:00 AM',
   'Between 9:01 - 10:00 AM',
   'Between 5:00 - 6:00 AM',
   'Between 8:01 - 9:00 AM',
   'I do not have a set schedule',
   'Between 10:01 - 11:00 AM',
   'Between 11:01 AM - 12:00 PM',
   'After 12:01 PM',
   'I work night shifts')

   hourscomputers = ('5 - 8 hours',
   'Over 12 hours',
   '9 - 12 hours',
   '1 - 4 hours',
   'Less than 1 hour')

   hoursoutsides = ('30 - 59 minutes',
   '1 - 2 hours',
   'Less than 30 minutes',
   '3 - 4 hours',
   'Over 4 hours')






   country = st.selectbox('1-In which country do you currently reside?',countries)
   age = st.selectbox('2-What is your age?',ages)
   student = st.selectbox('3-Are you currently enrolled in a formal, degree-granting college or university program?',students)
   formaleducation = st.selectbox('4-Which of the following best describes the highest level of formal education that you have completed?',formaleducations)
   undergradmajor = st.selectbox('5-Which of the following best describes your main field of study?',undergradmajors)
   employment = st.selectbox('6-Which of the following best describes your current employment status?',employments)
   jobsatisfaction = st.selectbox('7-How satisfied are you with your current job? If you work more than one job, please answer regarding the one you spend the most hours on.',jobsatisfactions)
   companysize = st.selectbox('8-Approximately how many people are employed by the company or organization you work for?',companysizes)
   careersatisfaction = st.selectbox('9-Overall, how satisfied are you with your career thus far?',careersatisfactions)
   lastnewjob = st.selectbox('10-When was the last time that you took a job with a new employer?',lastnewjobs)
   hopefiveyear = st.selectbox('11-Which of the following best describes what you hope to be doing in five years?',hopefiveyears)
   yearscoding = st.selectbox('12-Including any education, for how many years have you been coding?',yearscodings)
   yearscodingprof = st.selectbox('13-For how many years have you coded professionally (as a part of your work)?',yearscodingprofs)
   operatingsystem = st.selectbox('14-What is the primary operating system in which you work?',operatingsystems)
   timeFullyProductive = st.selectbox("15-Suppose a new developer with four years of experience, including direct experience working with your company's main technical stack, joined your team tomorrow. All other things being equal, how long would you expect it to take before they were fully productive and contributing at a typical level to your main code base",timeFullyProductives)
   ethicschoose = st.selectbox("16-Imagine that you were asked to write code for a purpose or product that you consider extremely unethical. Do you write the code anyway?",ethicschooses)
   dependent = st.selectbox("17-Do you have any children or other dependents that you care for?",dependents)
   numberofmonitor = st.selectbox("18-How many monitors are set up at your workstation?",numberofmonitors)
   waketime = st.selectbox("19-On days when you work, what time do you typically wake up?",waketimes)
   hourscomputer = st.selectbox("20-On a typical day, how much time do you spend on a desktop or laptop computer?",hourscomputers)
   hoursoutside = st.selectbox("21-On a typical day, how much time do you spend outside?",hoursoutsides)




   ##################################################################################################

   st.write("22-Now imagine evaluating a job's benefits package. Please rank the following aspects of a job benefits package from 1 to 11 from most important to least important to you.")

   order_list = (0,1,2,3,4,5,6,7,8,9,10,11)
   # std_list = [1,2,3,4,5,6,7,8,9,10,11]
   # z_waiting_list=[]
   # z_waiting_list.append(a1)
   a1 = st.selectbox("22.1-Salary and/or bonuses",order_list)
   a2 = st.selectbox("22.2-Stock options or shares",order_list)
   a3 = st.selectbox("22.3-Health insurance",order_list)
   a4 = st.selectbox("22.4-Parental leave",order_list)
   a5 = st.selectbox("22.5-Fitness or wellness benefit (ex. gym membership, nutritionist)",order_list)
   a6 = st.selectbox("22.6-Retirement or pension savings matching",order_list)
   a7 = st.selectbox("22.7-Company-provided meals or snacks",order_list)
   a8 = st.selectbox("22.8-Computer/office equipment allowance",order_list)
   a9 = st.selectbox("22.9-Childcare benefit",order_list)
   a10 = st.selectbox("22.10-Transportation benefit (ex. company-provided transportation, public transit allowance)",order_list)
   a11 = st.selectbox("22.11-Conference or education budget",order_list)

   
      
   ##################################################################################################

   data ={
      'Country': country,
      'Student': student,
      'Employment': employment,
      'FormalEducation': formaleducation,
      'UndergradMajor': undergradmajor,
      'CompanySize': companysize,
      'YearsCoding': yearscoding,
      'YearsCodingProf': yearscodingprof,
      'JobSatisfaction': jobsatisfaction,
      'CareerSatisfaction': careersatisfaction,
      'HopeFiveYears': hopefiveyear,
      'LastNewJob': lastnewjob,
      'AssessBenefits1':a1,
      'AssessBenefits2':a2,
      'AssessBenefits3':a3,
      'AssessBenefits4':a4,
      'AssessBenefits5':a5,
      'AssessBenefits6':a6,
      'AssessBenefits7':a7,
      'AssessBenefits8':a8,
      'AssessBenefits9':a9,
      'AssessBenefits10':a10,
      'AssessBenefits11':a11,
      'TimeFullyProductive': timeFullyProductive,
      'OperatingSystem': operatingsystem,
      'NumberMonitors': numberofmonitor,
      'EthicsChoice':ethicschoose,
      'WakeTime': waketime,
      'HoursComputer': hourscomputer,
      'HoursOutside': hoursoutside,
      'Age': age,
      'Dependents':dependent
   }
   
   features_df = pd.DataFrame.from_dict([data])
   st.markdown("<h3></h3>", unsafe_allow_html=True)
   st.write('Overview of input is shown below')
   st.markdown("<h3></h3>", unsafe_allow_html=True)
   st.dataframe(features_df)

   preprocess_df = preprocess(features_df, 'Predict')
   prediction = model.predict(preprocess_df)
   salary = round(prediction[0],2)
   btn_predict = st.button('Calculate Salary')
   # xs=23545.6564
   
   check_a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
   
   # a1 != a2 and a2 != a3 and a3!= a4 and a4!= a5 and a5!= a6 and a6!= a7 and a7!= a8 and a8!= a9 and a9!= a10 and a10!= a11
   count_a=0
   
   for i in check_a:
      if check_a.count(i)!=1 :
         count_a+=1
         
   if btn_predict:
      if count_a==0 :
         # if (a1 != a2 != a3!= a4 != a5 != a6!= a7 != a8 != a9!= a10 != a11 !=0 ) : 
         
         if  (0 in check_a) or (check_a.count(0)==11):
            st.subheader('ERROR ! ')

            st.subheader("Please rank Question-22 from 1 to 11 from most important to least important to you. Or leave all 0")
         # elif if c.count(0)==11:  
      
         st.subheader(f"The estimated salary is $ {salary}")
      elif check_a.count(0)==11 :
         st.subheader(f"The estimated salary is $ {salary}")
         
      else:
         st.subheader('ERROR ! ')

         st.subheader("Please rank Question-22 from 1 to 11 from most important to least important to you. Or leave all 0")
         # st.subheader("Please rank the aspects of a job benefits package from 1 to 11 from most important to least important to you. Or leave all 0")
         
      
      
      
      
# elif selection == 'Batch':
   
#    st.subheader("Dataset upload")
#    uploaded_file = st.file_uploader("Choose a file")
   
#    if uploaded_file is not None:
#       data = pd.read_csv(uploaded_file,encoding= 'utf-8')
#       #Get overview of data
#       st.write(data.head())
#       st.markdown("<h3></h3>", unsafe_allow_html=True)
#       #Preprocess inputs
#       preprocess_df = preprocess(data, "Batch")
#       btn_predict = st.button('Calculate Salary')
      
#       if btn_predict:
#          #Get batch prediction
#          prediction = model.predict(preprocess_df)
#          prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
#          # prediction_df = prediction_df.replace({1:'Yes, the passenger survive.', 0:'No, the passenger died'})

#          st.markdown("<h3></h3>", unsafe_allow_html=True)
#          st.subheader('Prediction')
#          st.write(prediction_df)


   
   
   

# show_predict_page()




   
   
   
   
   
   
   
   
   
   
   
   