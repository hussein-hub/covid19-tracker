import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import INSERT, messagebox
from tkinter import *
import json
import datetime
from tkcalendar import Calendar
import matplotlib.pyplot as plt

LARGEFONT = ("Courier", 35)
MEDIUMFONT = ("Courier", 20)
SMALLFONT = ("Courier", 15)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('800x550')
        self.title('Covid19')
        self.configure(bg='#accdf5')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, countryPage, IndiaPage, stateCityPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#accdf5')
        def initialize():
            label = tk.Label(self, text="COVID19 TRACKER", font=LARGEFONT, bg='#accdf5')
            label.grid(row=0, column=2, padx=150, pady=10, rowspan=2)

            WORLD_URL = "https://www.worldometers.info/coronavirus/"
            total_request = requests.get(WORLD_URL)
            soup = BeautifulSoup(total_request.content, 'html.parser')
            total_deaths_recevored = soup.findAll('div', attrs={'class': 'maincounter-number'})
            data = []
            for d in total_deaths_recevored:
                data.append(d.span.text)

            T1 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
            T2 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
            T3 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
            # total cases
            total_cases = tk.Label(self, text="Total Cases", bg='#accdf5', font=LARGEFONT)
            total_cases.config(font=("Courier", 14))
            total_cases.place(x=80, y=100)
            total = f'   {data[0]}'
            T1.insert(INSERT, total)
            T1.place(x=40, y=125, height=35, width=200)

            # total deaths
            total_deaths = tk.Label(self, text="Total Deaths", bg='#accdf5', font=LARGEFONT)
            total_deaths.config(font=("Courier", 14))
            total_deaths.place(x=320, y=100)
            deaths = f'   {data[1]}'
            T2.insert(INSERT, deaths)
            T2.place(x=280, y=125, height=35, width=200)

            # total recovered
            total_recovered = tk.Label(self, text="Total Recovered", bg='#accdf5', font=LARGEFONT)
            total_recovered.config(font=("Courier", 14))
            total_recovered.place(x=535, y=100)
            recovered = f'   {data[2]}'
            T3.insert(INSERT, recovered)
            T3.place(x=520, y=125, height=35, width=200)

            # row 2 active cases data
            T4 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
            T5 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
            T6 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)

            WORLD_URL = "https://www.worldometers.info/coronavirus/"
            total_request = requests.get(WORLD_URL)
            soup = BeautifulSoup(total_request.content, 'html.parser')
            curr = soup.find('div', attrs={'class': 'number-table-main'})
            mild_serious_fetch = soup.findAll('span', attrs={'class': 'number-table'})
            mild_serious = []
            for i in mild_serious_fetch:
                mild_serious.append(i.text)

            current = tk.Label(self, text="Active Cases", bg='#accdf5', font=LARGEFONT)
            current.config(font=("Courier", 14))
            current.place(x=80, y=175)
            cur = f'   {curr.text}'
            T4.insert(INSERT, cur)
            T4.place(x=40, y=200, height=35, width=200)

            mild = tk.Label(self, text="Mild Condition", bg='#accdf5', font=LARGEFONT)
            mild.config(font=("Courier", 14))
            mild.place(x=300, y=175)
            m = f'   {mild_serious[0]}'
            T5.insert(INSERT, m)
            T5.place(x=280, y=200, height=35, width=200)

            critical = tk.Label(self, text="Critical Condition", bg='#accdf5', font=LARGEFONT)
            critical.config(font=("Courier", 14))
            critical.place(x=520, y=175)
            cri = f'   {mild_serious[1]}'
            T6.insert(INSERT, cri)
            T6.place(x=520, y=200, height=35, width=200)

            countryinfo = tk.Button(self, text='Country Info', command=lambda: controller.show_frame(countryPage),
                                    bg='#4e74fc',
                                    font=MEDIUMFONT)
            Indiainfo = tk.Button(self, text='India Info', command=lambda: controller.show_frame(IndiaPage),
                                  bg='#4e74fc',
                                  font=MEDIUMFONT)

            countryinfo.place(x=50, y=300)
            countryinfo.config(font=("Courier", 13))
            Indiainfo.place(x=250, y=300)
            Indiainfo.config(font=("Courier", 13))

        refresh = tk.Button(self, text='Refresh', command=initialize, bg='#4e74fc', font=("Courier", 10))
        refresh.place(x=30, y=30)
        initialize()

        # markAttendance.place(x=560, y=200)
class IndiaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#accdf5')

        # label of frame Layout 2
        label = tk.Label(self, text="COVID INDIA", font=LARGEFONT, bg='#accdf5')
        label.place(x=210, y=10)

        back = tk.Button(self, text='back', command=lambda: controller.show_frame(StartPage), bg='#4e74fc',
                         font=("Courier", 10))
        back.place(x=30, y=30)

        cal = Calendar(self, selectmode='day',
                       year=2020, month=5,
                       day=22)

        cal.place(x=70, y=75)

        date_time_obj = datetime.datetime.strptime('01/01/21', '%m/%d/%y')

        def getSingleData(date, dailyConfirmed, dailyDeath):
            url = "https://api.covid19india.org/data.json"
            page = requests.get(url)
            data = json.loads(page.text)
            # cases.append(int(data["cases_time_series"][i]["dailydeceased"]))
            for i in range(len(data["cases_time_series"])):
                if data["cases_time_series"][i]["dateymd"] == str(date):
                    dailyConfirmed.delete("1.0", "end")
                    dailyConfirmed.insert(INSERT, data["cases_time_series"][i]["dailyconfirmed"])
                    dailyDeath.delete("1.0", "end")
                    dailyDeath.insert(INSERT, data["cases_time_series"][i]["dailydeceased"])

        def grad_date(dailyConfirmed, dailyDeath):
            date_time_str = cal.get_date()
            date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%y')

            print('Date:', date_time_obj.date())
            text = "Selected Date is: " + str(date_time_obj.date())
            dateDATA.delete(0, END)
            dateDATA.insert(0, text)
            getSingleData(date_time_obj.date(), dailyConfirmed, dailyDeath)

        # Add Button and Label
        getDate = tk.Button(self, text='Get Date', command=lambda: grad_date(dailyConfirmed, dailyDeath),
                                bg='#4e74fc',
                                font=MEDIUMFONT)
        getDate.place(x=35, y=370)
        getDate.config(font=("Courier", 13))

        dateDATA = tk.Entry(self, width=29, borderwidth=2)
        dateDATA.config(font=("Courier", 14))
        dateDATA.place(x=185, y=375, height=35)
        dateDATA.focus()

        state_city = tk.Button(self, text='State and City', command=lambda: controller.show_frame(stateCityPage),
                            bg='#4e74fc',
                            font=MEDIUMFONT)
        state_city.place(x=575, y=370)
        state_city.config(font=("Courier", 13))

        cases_label = tk.Label(self, text="Cases: ", bg='#accdf5')
        cases_label.config(font=("Courier", 14))
        cases_label.place(x=450, y=100)
        dailyConfirmed = tk.Text(self, height=4, width=52, bg='#accdf5', font=("Courier", 13))
        dailyConfirmed.place(x=525, y=100, height=30, width=125)

        death_label = tk.Label(self, text="Deaths: ", bg='#accdf5')
        death_label.config(font=("Courier", 14))
        death_label.place(x=430, y=150)
        dailyDeath = tk.Text(self, height=4, width=52, bg='#accdf5', font=("Courier", 13))
        dailyDeath.place(x=525, y=150, height=30, width=125)

        def giveGraph(n, type):
            if n.isdigit():
                dates = []
                cases = []
                n = abs(int(n))

                url = "https://api.covid19india.org/data.json"
                page = requests.get(url)
                data = json.loads(page.text)
                for i in range(-1, (-1) * (n + 1), -1):
                    dates.append(data["cases_time_series"][i]["date"][:-4])
                    # cases.append(int(data["cases_time_series"][i]["dailydeceased"]))
                    cases.append(int(data["cases_time_series"][i][type]))

                dates.reverse()
                cases.reverse()
                # print(dates)
                # print(cases)
                plt.figure(figsize=(8, 8))
                plt.plot(dates, cases, marker='o')
                plt.xlabel('Date')
                plt.xticks(rotation=35)
                plt.ylabel('Number of Cases')
                plt.show()
            else:
                tk.messagebox.showwarning('Wrong Input', 'Enter a number not a string!!!')


        days = tk.Entry(self, width=10, borderwidth=2)
        days.config(font=("Courier", 14))
        days.place(x=215, y=300, height=35)
        days.focus()

        countryinfo = tk.Button(self, text='Cases stats', command=lambda: giveGraph((days.get()), "dailyconfirmed"),
                                bg='#4e74fc',
                                font=MEDIUMFONT)
        countryinfo.place(x=35, y=300)
        countryinfo.config(font=("Courier", 13))

        deathStat = tk.Button(self, text='Death stats', command=lambda: giveGraph((days.get()), "dailydeceased"),
                                bg='#4e74fc',
                                font=MEDIUMFONT)
        deathStat.place(x=370, y=300)
        deathStat.config(font=("Courier", 13))


        '''year = tk.Label(self, text="Year", font=("Courier", 16), bg='#accdf5')
        year.place(x=250, y=100)

        yearInput = tk.Entry(self, width=12, borderwidth=6, font=("Courier", 14))
        yearInput.place(x=385, y=100)
        yearInput.focus()

        subject = tk.Label(self, text="Subject", font=("Courier", 16), bg='#accdf5')
        subject.place(x=240, y=175)

        subjectInput = tk.Entry(self, width=12, borderwidth=6, font=("Courier", 14))
        subjectInput.place(x=385, y=170)

        back = tk.Button(self, text='back', font=("Courier", 15), command=lambda: controller.show_frame(StartPage),
                         bg='#4e74fc')
        back.place(x=210, y=280)

        create = tk.Button(self, text='Create', font=("Courier", 15), bg='#4e74fc')
        create.place(x=520, y=280)

        send = tk.Button(self, text='Send Attendance', font=("Courier", 15), bg='#4e74fc')
        send.grid(row=5, column=1, pady=10)
        send.place(x=305, y=280)'''
class stateCityPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#accdf5')
        label = tk.Label(self, text="STATE AND CITY INFO", font=LARGEFONT, bg='#accdf5')
        label.place(x=100, y=10)

        back = tk.Button(self, text='Back', command=lambda: controller.show_frame(IndiaPage), bg='#4e74fc',
                         font=("Courier", 10))
        back.place(x=30, y=30)

        T1 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T2 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T3 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        stateName = tk.Text(self, height=5, width=52, bg='#accdf5', font=MEDIUMFONT)
        districtName = tk.Text(self, height=5, width=52, bg='#accdf5', font=MEDIUMFONT)

        def getStateData(state, T1, T2, T3, stateName):
            flag = True
            url = "https://api.covid19india.org/data.json"
            page = requests.get(url)
            data = json.loads(page.text)
            stateName.delete("1.0", "end")
            stateName.insert(INSERT, state)
            for i in range(len(data["statewise"])):
                if data["statewise"][i]["state"] == state:
                    flag = False
                    T1.delete("1.0", "end")
                    T1.insert(INSERT, data["statewise"][i]["active"])
                    T2.delete("1.0", "end")
                    T2.insert(INSERT, data["statewise"][i]["confirmed"])
                    T3.delete("1.0", "end")
                    T3.insert(INSERT, data["statewise"][i]["deaths"])
            if flag:
                tk.messagebox.showwarning('Input Error', f'instead of "{state}" try "{state.capitalize()}" or trying entering state name correctly!!')

        def getDistrictData(district, T4, T5, T6, districtName):
            flag = True
            url = "https://api.covid19india.org/district_wise.json"
            page = requests.get(url)
            data = json.loads(page.text)
            districtName.delete("1.0", "end")
            districtName.insert(INSERT, district)
            print(district)
            for i in range(len(data["districts"])):
                if data["districts"][i]["district"] == district:
                    flag = False
                    T4.delete("1.0", "end")
                    T4.insert(INSERT, data["districts"][i]["active"])
                    T5.delete("1.0", "end")
                    T5.insert(INSERT, data["districts"][i]["confirmed"])
                    T6.delete("1.0", "end")
                    T6.insert(INSERT, data["districts"][i]["deceased"])
            if flag:
                tk.messagebox.showwarning('Input Error', f'instead of "{district}" try "{district.capitalize()}" or trying entering district name correctly!!')

        data = [0, 0, 0]
        mild_serious = [0, 0]

        stateName.place(x=40, y=80, height=35, width=200)

        activeCases = tk.Label(self, text="Active Cases", bg='#accdf5', font=LARGEFONT)
        activeCases.config(font=("Courier", 14))
        activeCases.place(x=80, y=140)
        total = f'   {data[0]}'
        # T1.insert(INSERT, total)
        T1.place(x=40, y=165, height=35, width=200)


        # total cases
        Confirmedcases = tk.Label(self, text="Confirmed Cases", bg='#accdf5', font=LARGEFONT)
        Confirmedcases.config(font=("Courier", 14))
        Confirmedcases.place(x=290, y=140)
        total = f'   {data[0]}'
        # T2.insert(INSERT, total)
        T2.place(x=280, y=165, height=35, width=200)

        # total deaths
        total_deaths = tk.Label(self, text="Total Deaths", bg='#accdf5', font=LARGEFONT)
        total_deaths.config(font=("Courier", 14))
        total_deaths.place(x=540, y=140)
        deaths = f'   {data[1]}'
        # T3.insert(INSERT, deaths)
        T3.place(x=520, y=165, height=35, width=200)

        stateName_label = tk.Label(self, text="State Name: ", bg='#accdf5')
        stateName_label.config(font=("Courier", 14))
        stateName_label.place(x=50, y=435)

        state = tk.Entry(self, width=12, borderwidth=2)
        state.config(font=("Courier", 14))
        state.place(x=220, y=435)
        state.focus()

        update = tk.Button(self, text="Update state", bg='#4e74fc',
                           command=lambda: getStateData(state.get(), T1, T2, T3, stateName))
        update.config(font=("Courier", 12))
        update.place(x=400, y=430)

        districtName.place(x=40, y=255, height=35, width=200)

        T4 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T5 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T6 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)

        current = tk.Label(self, text="Active Cases", bg='#accdf5', font=LARGEFONT)
        current.config(font=("Courier", 14))
        current.place(x=80, y=315)
        cur = f'   {0}'
        # T4.insert(INSERT, cur)
        T4.place(x=40, y=340, height=35, width=200)

        mild = tk.Label(self, text="Mild Condition", bg='#accdf5', font=LARGEFONT)
        mild.config(font=("Courier", 14))
        mild.place(x=320, y=315)
        m = f'   {mild_serious[0]}'
        # T5.insert(INSERT, m)
        T5.place(x=280, y=340, height=35, width=200)

        critical = tk.Label(self, text="Critical Condition", bg='#accdf5', font=LARGEFONT)
        critical.config(font=("Courier", 14))
        critical.place(x=535, y=315)
        cri = f'   {mild_serious[1]}'
        # T6.insert(INSERT, cri)
        T6.place(x=520, y=340, height=35, width=200)

        districtName_label = tk.Label(self, text="District Name: ", bg='#accdf5')
        districtName_label.config(font=("Courier", 14))
        districtName_label.place(x=50, y=500)

        district = tk.Entry(self, width=12, borderwidth=2)
        district.config(font=("Courier", 14))
        district.place(x=220, y=500)
        district.focus()

        updatedistrict = tk.Button(self, text="Update district", bg='#4e74fc',
                           command=lambda: getDistrictData(district.get(), T4, T5, T6, districtName))
        updatedistrict.config(font=("Courier", 12))
        updatedistrict.place(x=400, y=495)
class countryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#accdf5')
        label = tk.Label(self, text="Indivisual Country", font=LARGEFONT, bg='#accdf5')
        label.place(x=150, y=10)

        countryName_label = tk.Label(self, text="Country Name: ", bg='#accdf5')
        countryName_label.config(font=("Courier", 14))
        countryName_label.place(x=50, y=300)

        country = tk.Entry(self, width=12, borderwidth=2)
        country.config(font=("Courier", 14))
        country.place(x=220, y=300)
        country.focus()

        data = [0, 0, 0]

        def getData(country, T1, T2, T3, T4, T5, T6):
            WORLD_URL = f"https://www.worldometers.info/coronavirus/country/{country}"
            total_request = requests.get(WORLD_URL)
            print(total_request.status_code)
            soup = BeautifulSoup(total_request.content, 'html.parser')
            if str(soup.title) != '<title>404 Not Found</title>':
                total_deaths_recevored = soup.findAll('div', attrs={'class': 'maincounter-number'})
                i = 0
                for d in total_deaths_recevored:
                    data[i] = d.span.text
                    i = i + 1
                T1.delete("1.0", "end")
                T2.delete("1.0", "end")
                T3.delete("1.0", "end")
                total = f'   {data[0]}'
                T1.insert(INSERT, total)
                deaths = f'   {data[1]}'
                T2.insert(INSERT, deaths)
                recovered = f'   {data[2]}'
                T3.insert(INSERT, recovered)
                getData2(country, T4, T5, T6)
            else:
                tk.messagebox.showwarning('Wrong Country Name', 'Please Enter Correct Country Name!!!')

        T1 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T2 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T3 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        # total cases
        total_cases = tk.Label(self, text="Total Cases", bg='#accdf5', font=LARGEFONT)
        total_cases.config(font=("Courier", 14))
        total_cases.place(x=80, y=100)
        total = f'   {data[0]}'
        T1.insert(INSERT, total)
        T1.place(x=40, y=125, height=35, width=200)

        # total deaths
        total_deaths = tk.Label(self, text="Total Deaths", bg='#accdf5', font=LARGEFONT)
        total_deaths.config(font=("Courier", 14))
        total_deaths.place(x=320, y=100)
        deaths = f'   {data[1]}'
        T2.insert(INSERT, deaths)
        T2.place(x=280, y=125, height=35, width=200)

        # total recovered
        total_recovered = tk.Label(self, text="Total Recovered", bg='#accdf5', font=LARGEFONT)
        total_recovered.config(font=("Courier", 14))
        total_recovered.place(x=535, y=100)
        recovered = f'   {data[2]}'
        T3.insert(INSERT, recovered)
        T3.place(x=520, y=125, height=35, width=200)

        # row 2 active cases data

        def getData2(country, T4, T5, T6):
            WORLD_URL = f"https://www.worldometers.info/coronavirus/country/{country}"
            total_request = requests.get(WORLD_URL)
            soup = BeautifulSoup(total_request.content, 'html.parser')
            curr = soup.find('div', attrs={'class': 'number-table-main'})
            mild_serious_fetch = soup.findAll('span', attrs={'class': 'number-table'})
            mild_serious = [0, 0, 0, 0]
            i = -1
            c = curr.text
            for md in mild_serious_fetch:
                i = i + 1
                mild_serious[i] = md.text
            if country == 'india':
                url = "https://worldometers.p.rapidapi.com/api/coronavirus/country/India"

                headers = {
                    'x-rapidapi-key': "4de5bae009msh3d690447f433304p1d9fe1jsnf5600d22cfc9",
                    'x-rapidapi-host': "worldometers.p.rapidapi.com"
                }

                response = requests.request("GET", url, headers=headers)
                data = response.json()
                print(data['data']['Active Cases'])
                c = data['data']['Active Cases']
                mild_serious[0] = 0
                mild_serious[1] = data['data']['Critical']
            elif country == 'us':
                url = "https://worldometers.p.rapidapi.com/api/coronavirus/country/USA"

                headers = {
                    'x-rapidapi-key': "4de5bae009msh3d690447f433304p1d9fe1jsnf5600d22cfc9",
                    'x-rapidapi-host': "worldometers.p.rapidapi.com"
                }

                response = requests.request("GET", url, headers=headers)
                data = response.json()
                print(data['data']['Active Cases'])
                c = data['data']['Active Cases']
                mild_serious[0] = 0
                mild_serious[1] = data['data']['Critical']

            T4.delete("1.0", "end")
            T5.delete("1.0", "end")
            T6.delete("1.0", "end")
            cur = f"   {c}"
            T4.insert(INSERT, cur)
            m = f'   {mild_serious[0]}'
            T5.insert(INSERT, m)
            cri = f"   {mild_serious[1]}"
            T6.insert(INSERT, cri)


        T4 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T5 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        T6 = tk.Text(self, height=5, width=52, bg='#accdf5', font=SMALLFONT)
        mild_serious = [0, 0, 0, 0]
        c = 0

        current = tk.Label(self, text="Active Cases", bg='#accdf5', font=LARGEFONT)
        current.config(font=("Courier", 14))
        current.place(x=80, y=175)
        cur = f'     {c}'
        T4.insert(INSERT, cur)
        T4.place(x=40, y=200, height=35, width=200)

        mild = tk.Label(self, text="Mild Condition", bg='#accdf5', font=LARGEFONT)
        mild.config(font=("Courier", 14))
        mild.place(x=320, y=175)
        m = f'       {mild_serious[0]}'
        T5.insert(INSERT, m)
        T5.place(x=280, y=200, height=35, width=200)

        critical = tk.Label(self, text="Critical Condition", bg='#accdf5', font=LARGEFONT)
        critical.config(font=("Courier", 14))
        critical.place(x=535, y=175)
        cri = f'       {mild_serious[1]}'
        T6.insert(INSERT, cri)
        T6.place(x=520, y=200, height=35, width=200)

        update = tk.Button(self, text="update", bg='#4e74fc',
                           command=lambda: getData(country.get(), T1, T2, T3, T4, T5, T6))
        update.config(font=("Courier", 12))
        update.place(x=400, y=295)

        def plotGraph(country, n):
            COUNTRY_URL = f"https://www.worldometers.info/coronavirus/country/{country}"
            r = requests.get(COUNTRY_URL)

            soup = BeautifulSoup(r.content, 'html.parser')
            num = []
            days = []

            caseList = soup.findAll('li', attrs={'class': 'news_li'})
            date = soup.findAll('button', attrs={'class': 'btn btn-light date-btn'})

            for (cases, day) in zip(caseList, date):
                case = cases.text.split(" ")
                case[n] = case[n].split(",")
                num.append(int(''.join(case[n])))
                days.append(str(day.text[:-1]))
                print(str(day.text[:-1]) + " : " + str(''.join(case[n])))

            num.reverse()
            days.reverse()
            plt.figure(figsize=(8, 7))
            plt.plot(days[1:], num[:-1], marker='o', label='Case Trend')
            plt.title('Last 5 Day Graph')
            plt.xlabel('Date')
            plt.ylabel('Number of Cases')
            plt.legend()
            plt.show()
        plotCases = tk.Button(self, text="Plot Cases", bg='#4e74fc',
                           command=lambda: plotGraph(country.get(), 0))
        plotCases.config(font=("Courier", 12))
        plotCases.place(x=605, y=335)

        plotDeaths = tk.Button(self, text="Plot Deaths", bg='#4e74fc',
                         command=lambda: plotGraph(country.get(), 4))
        plotDeaths.config(font=("Courier", 12))
        plotDeaths.place(x=600, y=295)

        back = tk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage), bg='#4e74fc',
                            font=("Courier", 10))
        back.place(x=30, y=30)
app = tkinterApp()
app.mainloop()
