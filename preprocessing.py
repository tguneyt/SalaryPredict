import pandas as pd

# from sklearn import preprocessing
import re

def preprocess(df, option):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """
    column_all = ['AssessBenefits1','AssessBenefits2','AssessBenefits3','AssessBenefits4','AssessBenefits5','AssessBenefits6','AssessBenefits7','AssessBenefits8','AssessBenefits9','AssessBenefits10', 'AssessBenefits11',
 'TimeFullyProductive',	 'Dependents',	 'Country_Argentina',	 'Country_Australia',	 'Country_Austria',	 'Country_Bangladesh',	 'Country_Belarus',	 'Country_Belgium',	 'Country_BosniaandHerzegovina',	 'Country_Brazil',	 'Country_Bulgaria',	 'Country_Canada',	 'Country_Chile',	 'Country_China',	 'Country_Colombia',	
 'Country_Croatia',	 'Country_CzechRepublic',	 'Country_Denmark',	 'Country_DominicanRepublic',	 'Country_Egypt',	 'Country_Estonia',	 'Country_Finland',	 'Country_France',	 'Country_Germany',	 'Country_Greece',	 'Country_HongKongSAR',	 'Country_Hungary',	 'Country_India',	 'Country_Indonesia',	 'Country_IranIslamicRepublicof',	 'Country_Ireland',
 'Country_Israel',	 'Country_Italy',	 'Country_Japan',	 'Country_Kazakhstan',	 'Country_Kenya',	 'Country_Latvia',	 'Country_Lithuania',	 'Country_Malaysia',	 'Country_Mexico',	 'Country_Morocco',	 'Country_Nepal',	 'Country_Netherlands',	 'Country_NewZealand',	 'Country_Nigeria',	 'Country_Norway',	
 'Country_Other',	 'Country_Pakistan',	 'Country_Peru',	 'Country_Philippines',	 'Country_Poland',	 'Country_Portugal',	 'Country_Romania',	 'Country_RussianFederation',	 'Country_SaudiArabia',	 'Country_Serbia',	 'Country_Singapore',	 'Country_Slovakia',	 'Country_Slovenia',	 'Country_SouthAfrica',	 'Country_SouthKorea',	
 'Country_Spain',	 'Country_SriLanka',	 'Country_Sweden',	 'Country_Switzerland',	 'Country_Taiwan',	 'Country_Thailand',	 'Country_Turkey',	 'Country_Ukraine',	 'Country_UnitedArabEmirates',	 'Country_UnitedKingdom',	 'Country_UnitedStates',	 'Country_VietNam',	 'Student_No',	 'Student_Yesfulltime',	 'Student_Yesparttime',	
 'Employment_Employedfulltime',	 'Employment_Employedparttime',	 'Employment_Independentcontractorfreelancerorselfemployed',	 'Employment_Notemployedandnotlookingforwork',	 'Employment_Notemployedbutlookingforwork',	 'Employment_Retired',	 'FormalEducation_Associatedegree',	 'FormalEducation_BachelorsdegreeBABSBEngetc',	 'FormalEducation_Inevercompletedanyformaleducation',	 'FormalEducation_MastersdegreeMAMSMEngMBAetc',						
 'FormalEducation_OtherdoctoraldegreePhDEdDetc',	 'FormalEducation_Primaryelementaryschool',	 'FormalEducation_ProfessionaldegreeJDMDetc',	 'FormalEducation_SecondaryschoolegAmericanhighschoolGermanRealschuleorGymnasiumetc',	 'FormalEducation_Somecollegeuniversitystudywithoutearningadegree',	 'UndergradMajor_Abusinessdisciplineexaccountingfinancemarketing',	 'UndergradMajor_Ahealthscienceexnursingpharmacyradiology',	 'UndergradMajor_Ahumanitiesdisciplineexliteraturehistoryphilosophy',	 'UndergradMajor_Anaturalscienceexbiologychemistryphysics',	 'UndergradMajor_Asocialscienceexanthropologypsychologypoliticalscience',						
 'UndergradMajor_Anotherengineeringdisciplineexcivilelectricalmechanical',	 'UndergradMajor_Computersciencecomputerengineeringorsoftwareengineering',	 'UndergradMajor_Fineartsorperformingartsexgraphicdesignmusicstudioart',	 'UndergradMajor_Ineverdeclaredamajor',	 'UndergradMajor_Informationsystemsinformationtechnologyorsystemadministration',	 'UndergradMajor_Mathematicsorstatistics',	 'UndergradMajor_Webdevelopmentorwebdesign',	 'CompanySize_1000to4999employees',	 'CompanySize_10to19employees',							
 'CompanySize_10000ormoreemployees',	 'CompanySize_100to499employees',	 'CompanySize_20to99employees',	 'CompanySize_5000to9999employees',	 'CompanySize_500to999employees',	 'CompanySize_Fewerthan10employees',	 'YearsCoding_02years',	 'YearsCoding_1214years',	 'YearsCoding_1517years',	 'YearsCoding_1820years',	 'YearsCoding_2123years',	 'YearsCoding_2426years',	 'YearsCoding_2729years',			
 'YearsCoding_35years',	 'YearsCoding_30ormoreyears',	 'YearsCoding_68years',	 'YearsCoding_911years',	 'YearsCodingProf_02years',	 'YearsCodingProf_1214years',	 'YearsCodingProf_1517years',	 'YearsCodingProf_1820years',	 'YearsCodingProf_2123years',	 'YearsCodingProf_2426years',	 'YearsCodingProf_2729years',	 'YearsCodingProf_35years',	 'YearsCodingProf_30ormoreyears',	 'YearsCodingProf_68years',	 'YearsCodingProf_911years',	 'JobSatisfaction_Extremelydissatisfied',
 'JobSatisfaction_Extremelysatisfied',	 'JobSatisfaction_Moderatelydissatisfied',	 'JobSatisfaction_Moderatelysatisfied',	 'JobSatisfaction_Neithersatisfiednordissatisfied',	 'JobSatisfaction_Slightlydissatisfied',	 'JobSatisfaction_Slightlysatisfied',	 'CareerSatisfaction_Extremelydissatisfied',	 'CareerSatisfaction_Extremelysatisfied',	 'CareerSatisfaction_Moderatelydissatisfied',	 'CareerSatisfaction_Moderatelysatisfied',	 'CareerSatisfaction_Neithersatisfiednordissatisfied',	 'CareerSatisfaction_Slightlydissatisfied',	 'CareerSatisfaction_Slightlysatisfied',			
 'HopeFiveYears_Doingthesamework',	 'HopeFiveYears_Retirement',	 'HopeFiveYears_Workingasafounderorcofounderofmyowncompany',	 'HopeFiveYears_Workingasaproductmanagerorprojectmanager',	 'HopeFiveYears_Workingasanengineeringmanagerorotherfunctionalmanager',	 'HopeFiveYears_Workinginacareercompletelyunrelatedtosoftwaredevelopment',	 'HopeFiveYears_WorkinginadifferentormorespecializedtechnicalrolethantheoneIminnow',	 'LastNewJob_Between1and2yearsago',	 'LastNewJob_Between2and4yearsago',	 'LastNewJob_Iveneverhadajob',	 'LastNewJob_Lessthanayearago',	 'LastNewJob_Morethan4yearsago',				
 'OperatingSystem_BSDUnix',	 'OperatingSystem_Linuxbased',	 'OperatingSystem_MacOS',	 'OperatingSystem_Windows',	 'NumberMonitors_1',	 'NumberMonitors_2',	 'NumberMonitors_3',	 'NumberMonitors_4',	 'NumberMonitors_Morethan4',	 'EthicsChoice_Dependsonwhatitis',	 'EthicsChoice_No',	 'EthicsChoice_Yes',	 'WakeTime_After1201PM',	 'WakeTime_Before500AM',		
 'WakeTime_Between10011100AM',	 'WakeTime_Between1101AM1200PM',	 'WakeTime_Between500600AM',	 'WakeTime_Between601700AM',	 'WakeTime_Between701800AM',	 'WakeTime_Between801900AM',	 'WakeTime_Between9011000AM',	 'WakeTime_Idonothaveasetschedule',	 'WakeTime_Iworknightshifts',	 'HoursComputer_14hours',	 'HoursComputer_58hours',	 'HoursComputer_912hours',				
 'HoursComputer_Lessthan1hour',	 'HoursComputer_Over12hours',	 'HoursOutside_12hours',	 'HoursOutside_34hours',	 'HoursOutside_3059minutes',	 'HoursOutside_Lessthan30minutes',	 'HoursOutside_Over4hours',	 'Age_024yearsold',	 'Age_2544yearsold',	'Age_45yearsorolder']		
        
    if (option == 'Predict'):
        
  
        df['TimeFullyProductive'] = df['TimeFullyProductive'].map({'More than three months':1,'Less than three months':0})
        df['Dependents'] = df['Dependents'].map({'Yes':1,'No':0})
        
        # One Hot Enc
        cat = df.select_dtypes(include=('object'))
        
        dms = pd.get_dummies(df[cat.columns])
        
        for i in cat.columns:
            df.drop(i,axis=1,inplace=True)
        df = pd.concat([df, dms], axis=1)
        
        df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        
        # for i in df.columns:
        #     if df[i].unique()[0]==1:
        #         f_df[i]=f_df[i].map({0:1})
    
        df = df.reindex(columns=column_all, fill_value=0)
        # f_df=df.copy()
        
        # f_df=f_df.fillna(0)
        
    
    elif (option == 'Batch') :
        
         # d = {}
        # for i in column_all:
        #     d.update({i:0})
        # f_df = pd.DataFrame.from_dict([d])
        df['TimeFullyProductive'] = df['TimeFullyProductive'].map({'More than three months':1,'Less than three months':0})
        df['Dependents'] = df['Dependents'].map({'Yes':1,'No':0})
        
        cat = df.select_dtypes(include=('object'))
        
        dms = pd.get_dummies(df[cat.columns])
        
        for i in cat.columns:
            df.drop(i,axis=1,inplace=True)
        df = pd.concat([df, dms], axis=1)
        
        df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        
        df = df.reindex(columns=column_all, fill_value=0)
        
        
        # for i in range(df.shape[0]):
        #     row_df = df.iloc[i:i+1,:]
        #     row_f = f_df.iloc[i:i+1,:]
            
        #     for i in row_df.columns:
        #         if df[i].unique()[0]==1:
        #             f_df[i]=f_df[i].map({0:1})
        
        
        
       
        
    return df
        
        
        