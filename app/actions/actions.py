# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
import datetime as date
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class ActionShowtime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{date.datetime.now()}")

        return []


class ActionInfo(Action):

    def name(self) -> Text:
        return "action_help_desk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_help_desk")

        return []

class ActionCareerAdvisor(Action):

    def name(self) -> Text:
        return "action_career_advisor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_career_advisor")

        return []

class ActionCareerAdvisorScince(Action):

    def name(self) -> Text:
        return "action_career_advisor_science"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_career_advisor_science")

        return []

class ActionCareerAdvisorManagement(Action):

    def name(self) -> Text:
        return "action_career_advisor_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_career_advisor_management")

        return []

class ActionCareerAdvisorArtHuman(Action):

    def name(self) -> Text:
        return "action_career_advisor_Art_Human"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_career_advisor_Art_Human")

        return []

class DisplayUpcomingHolidaysYear(Action):

    def name(self) -> Text:
        return "action_holiday_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = f"{date.datetime.today()}"
        print("Today's date:", today)
        year,this_month,day=today.split('-')
        df2 = pd.read_excel('2021_calendar.xlsx')
        df2['Date'] = pd.to_datetime(df2['Date'])
        current_year_df = df2[df2['Date'].dt.year == int(year)]
        content = 'Total of Holidays ' + str(current_year_df.shape[0]) + ' this year\n\n'
        for i in range(current_year_df.shape[0]):
            content = content + str(current_year_df['Date'].values[i])[:10] + '  -  ' + str(
                current_year_df['Holiday Description'].values[i]) + '\n'

        dispatcher.utter_message(text=content)

        return []

class Actiontermdate(Action):

    def name(self) -> Text:
        return "action_termdates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df2 = pd.read_excel('termdates.xlsx')
        content = 'Kindly see the term dates Information below:\n' + str(df2.shape[0])+ ' Term Dates\n\n' ' Week -  Date  -  Event \n\n'
        for i in range(df2.shape[0]):
            content = content + '\n Week '+ str(df2['Week'].values[i]) + '  :\n' + str(
                df2['Standard Date'].values[i]) + ' - ' + str(df2['Event'].values[i]) 

        dispatcher.utter_message(text=content)

        return []

class DisplayUpcomingHolidaysMonth(Action):

    def name(self) -> Text:
        return "action_holiday_month"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = f"{date.datetime.today()}"
        print("Today's date:", today)
        year,this_month,day=today.split('-')
        df2 = pd.read_excel('2021_calendar.xlsx')
        df2['Date'] = pd.to_datetime(df2['Date'])
        current_month_df = df2[df2['Date'].dt.month == int(this_month)]
        if (current_month_df.shape[0]==1):   
            for i in range(current_month_df.shape[0]):
                content = 'Total of Holidays ' + str(current_month_df.shape[0]) +' this month\n\n'
                content = content + str(current_month_df['Date'].values[i])[:10] + '  -  ' + str(
                    current_month_df['Holiday Description'].values[i]) + '\n'
        else:
            content = "Sorry there is no Holidays this month"
        dispatcher.utter_message(text=content)

        return []

class DisplayUpcomingHolidays(Action):

    def name(self) -> Text:
        return "action_display_upcoming_holidays"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_display_upcoming_holidays")

        return []

class ActionHelpDeskContactUs(Action):

    def name(self) -> Text:
        return "action_help_desk_contactus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_help_desk_contactus")

        return []


class ActionHelpDeskIT(Action):

    def name(self) -> Text:
        return "action_IT_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_IT_support")

        return []


class ActionHelpDeskContactUsAdmission(Action):

    def name(self) -> Text:
        return "action_help_desk_contactus_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_help_desk_contactus_admission")

        return []

class ActionHelpDeskContactUsStaff(Action):

    def name(self) -> Text:
        return "action_help_desk_contactus_staff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_print = pd.read_excel('staff_Info_basic.xlsx')
        content = 'You can speak to your department by Staff Information below:\n' + str(info_print.shape[0])+ ' Head Instructors of all colleges\n\n' ' Staff Name -  College  -  Email -  Phone Number\n\n'
        for i in range(info_print.shape[0]):
            content = content + str(info_print['satffName'].values[i])[:10] + '  -  ' + str(
                info_print['college'].values[i]) [:10] + '  -  ' + str(info_print['email'].values[i]) [:10] + '  -  ' + str(info_print['number'].values[i])+'\n'

        dispatcher.utter_message(text=content)

        return []

class ActionHelpDeskStudentAcc(Action):

    def name(self) -> Text:
        return "action_help_desk_student_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(template="utter_help_desk_student_account")
        
        return []

class ActionHelpDeskCovid19(Action):

    def name(self) -> Text:
        return "action_help_desk_covid19"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(template="utter_help_desk_covid19")
        
        return []

class ActionHelpDeskStudentAccFA(Action):

    def name(self) -> Text:
        return "action_help_desk_student_account_FA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(template="utter_help_desk_student_account_FA")
        
        return []

class ActionCampusGuide(Action):

    def name(self) -> Text:
        return "action_campus_guide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #configure api
        # gmaps.configure(api_key="AIzaSyByQAmJiVd7AOPRUq8k3YCy-mAE3PczMxE")
        # now = date.datetime.today()
        # directions_result = gmaps.directions("Sydney Town Hall",
        #                              "Parramatta, NSW",
        #                              mode="transit")
        
        dispatcher.utter_message(template ="utter_campus_guide")
        
        return []
        
class ActionCampusGuideMain(Action):

    def name(self) -> Text:
        return "action_campus_guide_main"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_campus_guide_main")
        
        return []

class ActionCampusGuideColleges(Action):

    def name(self) -> Text:
        return "action_colleges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_colleges")
        
        return []

class ActionCampusACC(Action):

    def name(self) -> Text:
        return "action_campus_guide_accommodation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_campus_guide_accommodation")
        
        return []


class ActionCampusLibraries(Action):

    def name(self) -> Text:
        return "action_campus_guide_libraries"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_campus_guide_libraries")
        
        return []

class ActionCourses(Action):

    def name(self) -> Text:
        return "action_course_enroll"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_course_enroll")
        
        return []

class ActionCourseEnrollAccount(Action):

    def name(self) -> Text:
        return "action_course_enroll_my_Acc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_course_enroll_my_Acc")
        
        return []

class ActionGeneralCourses(Action):

    def name(self) -> Text:
        return "action_course_enroll_general"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template ="utter_course_enroll_general")
        
        return []


class ActionAskUsn(Action):

    def name(self) -> Text:
        return "action_ask_un"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ask_un")

        return []

class ActionAskPassword(Action):

    def name(self) -> Text:
        return "action_ask_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        
        dispatcher.utter_message(template="utter_ask_password")

        return []

class ValidateCredentialsAndDisplayMarks(Action):

    def name(self) -> Text:
        return "action_validate_credentials_and_display_marks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)

        reg_no = messages[-2]
        password = str((tracker.latest_message)['text'])
        conn = sqlite3.connect('University.db')
        query = "select * from Student_details where regno = '{0}' and password = '{1}'".format(reg_no,password)
        print("Final query : ",query)
        df = pd.read_sql(query, conn)
        if df.shape[0] == 1:
            values = list(df.values)[0]
            name = values[0]
            subjects_col = ['sub1', 'sub2', 'sub3', 'sub4', 'lab1', 'lab2']
            marks_df = df[subjects_col]
            val_dict = (marks_df.to_dict('r'))[0]
            failed_subjects = 'failed'
            total_marks = sum(list(val_dict.values()))/len(subjects_col)
            content = "Kindly find your details below " + name + "\n\n\n"

            for k, v in val_dict.items():
                if v < 25:
                    failed_subjects = failed_subjects + k + ', '
                content = content + k + " : " + str(v) + "\n"

            content = content + "Total Average: "  + str(total_marks) + "\n"
        else:
            content = "Sorry your credentials are incorrect. Please enter valid credentials next time"
        dispatcher.utter_message(text=content)
        return []


class ValidateCredentialsAndDisplayAttendance(Action):

    def name(self) -> Text:
        return "action_validate_credentials_and_display_attendance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        password = str((tracker.latest_message)['text'])
        conn = sqlite3.connect('University.db')
        query = "select * from Student_details where regno = '{0}' and password = '{1}'".format(reg_no,password)
        print("Final query : ",query)
        df = pd.read_sql(query, conn)
        if df.shape[0] == 1:
            values = list(df.values)[0]
            name = values[0]
            #marks = values[2:8]
            days_col = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7',
                        'Day8', 'Day9', 'Day10', 'Day11', 'Day12', 'Day13', 'Day14', 'Day15',
                        'Day16', 'Day17', 'Day18', 'Day19', 'Day20', 'Day21', 'Day22', 'Day23',
                        'Day24', 'Day25', 'Day26', 'Day27', 'Day28', 'Day29', 'Day30']

            attendance_df = df[days_col]
            attendance_data = list(list(attendance_df.values)[0])
            present_no_of_days = attendance_data.count(1)
            absent_no_of_days = attendance_data.count(0)

            content =  name + ' Kindly find your Attendence details below: ' + "\n\n\n" + 'No of days present : ' + str(present_no_of_days) + '\nNo of days absent  : ' + str(
                absent_no_of_days)

        else:
            content = "Sorry your credentials are incorrect. Please enter valid credentials next time"
        dispatcher.utter_message(text=content)
        return []

class ValidateCredentialsAndDisplayTimetable(Action):

    def name(self) -> Text:
        return "action_course_enroll_my_Acc_timetable"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)

        reg_no = messages[-2]
        password = str((tracker.latest_message)['text'])
        conn = sqlite3.connect('University.db')
        query = "select * from Student_details where regno = '{0}' and password = '{1}'".format(reg_no,password)
        print("Final query : ",query)
        df = pd.read_sql(query, conn)
        if df.shape[0] == 1:
            values = list(df.values)[0]
            name = values[0]
            subjects_col = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            time_df = df[subjects_col]
            val_dict = (time_df.to_dict('r'))[0]
            content = "Kindly find your details below " + name + "\n\n\n"

            for k, v in val_dict.items():
                content = content + k + " : " + "\n" + str(v) + "\n\n"
        else:
            content = "Sorry your credentials are incorrect. Please enter valid credentials next time"
        dispatcher.utter_message(text=content)
        return []

class ActionFinancialAid(Action):

    def name(self) -> Text:
        return "action_Financial_aid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_Financial_aid")

        return []

class ActionFinancialAidTFees(Action):

    def name(self) -> Text:
        return "action_Financial_aid_tuitionFees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_Financial_aid_tuitionFees")

        return []
        

class ActionFinancialAidPayFees(Action):

    def name(self) -> Text:
        return "action_Financial_aid_pay_fees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_Financial_aid_pay_fees")

        return []

class ActionScholarships(Action):

    def name(self) -> Text:
        return "action_Scholarships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_Scholarships")

        return []

class ActionFunding(Action):

    def name(self) -> Text:
        return "action_Financial_aid_funding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_Financial_aid_funding")

        return []

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_default")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]