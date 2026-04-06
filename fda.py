import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config("India OdI analysis")
st.title("**INDIA MEN'S ODI ANAYLSIS**")
st.subheader("2021-2025 Complete Performace Dashbord")
if "page" not in st.session_state:
        st.session_state.page="HOME"
if "player" not in st.session_state:
    st.session_state.player="" 
if "series" not in  st.session_state:
    st.session_state.series=""  
if "tournment" not in st.session_state:
     st.session_state.tour=""             
tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["OVERVEIW","PLAYERS","SERIES","ICC TOURNAMENTS",
                                                      "BATTING","BOWLING"])  
with tab1:
    st.write("OVERVEIW")
    st.session_state.page="OVERVIEW"
    df=pd.read_csv("year.csv")
    wins=df["Wins"].sum()
    matches=df["Matches"].sum()
    winrate=((wins/matches)*100).round(2)
    df["Win%"]=((df["Wins"]/df["Matches"]))*100 
    st.metric("WIN%:",winrate)
    for idx,row in df.iterrows():
          
        st.write(f"Player peak performance in {row["Year"]}:***{row["Peak Batter"]}***")   
    x=df["Year"]
    y=df["Win%"]
    fig,ax=plt.subplots(figsize=(8,4))
    ax.plot(x,y,color="red",linewidth=2,label="Win%")
    ax.set_facecolor("black")
    ax.set_xlabel("Years")
    ax.set_ylabel("Win%")
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)

with tab2:
    st.session_state.page ="PLAYERS"
    st.write("PLAYERS") 
    batters= ["Rohit", "Dhawan", "Virat", "Gill", "Iyer",
           "Surya", "Ruturaj","Jaiswal", "Mayank", "Prithvi"]
    bowlers=["JASPRIT","SHAMI","SIRAJ","B.KUMAR","ARSDEEP","HARSITH"]
    all_rounders= ["Hardik","Axar","W.Sundar","R.Jadeja","Thakur","Krunal"]
    spin_bowlers=["Chahal", "Kuldeep", "Ravi", "Chahar", "Varun"]
    wk_keeper= ["KL  Rahul", "Pant", "Ishan", "Sanju", "Jurel"]
    # -------- Session State --------
# -------- HOME PAGE --------
    st.header("Top order Batters")
    col= st.columns(5)
    for i in range(5):
                with col[i]:
                    if st.button(batters[i]):
                        st.session_state.player = batters[i]
                        st.session_state.page = "Details"  
                          
    col= st.columns(5)
    for i in range(5,10):  
                with col[i-5]:
                    if st.button(batters[i]):
                        st.session_state.player =batters[i]
                        st.session_state.page = "Details"
    st.header("Fast Bowlers")
    col= st.columns(5)
    for i in range(5):
                with col[i]:
                    if st.button(bowlers[i]):
                        st.session_state.player = bowlers[i]
                        st.session_state.page = "Details"
    col= st.columns(5)
    for i in range(5,6):
                with col[i-5]:
                    if st.button(bowlers[i]):
                        st.session_state.player = bowlers[i]
                        st.session_state.page = "Details"   
    st.header("All Rounders")
    col= st.columns(5)
    for i in range(5):
                with col[i]:
                    if st.button(all_rounders[i]):
                        st.session_state.player = all_rounders[i]
                        st.session_state.page = "Details"
    
    col= st.columns(5)
    for i in range(5,6):
                with col[i-5]:
                    if st.button(all_rounders[i]):
                        st.session_state.player = all_rounders[i]
                        st.session_state.page = "Details"  
    st.header("Spin Bowlers")
    col= st.columns(5)
    for i in range(5):
                with col[i]:
                    if st.button(spin_bowlers[i]):
                        st.session_state.player = spin_bowlers[i]
                        st.session_state.page = "Details"                                                        
    st.header("Wicket Keeper")
    col= st.columns(5)
    for i in range(5):
                with col[i]:
                    if st.button(wk_keeper[i]):
                        st.session_state.player = wk_keeper[i]
                        st.session_state.page = "Details"
    if st.session_state.page == "Details":
        player = st.session_state.player

        st.title(player)
        df=pd.read_csv("batter.csv") 
        dd=pd.read_csv("bowler.csv")
        dp=pd.read_csv("all_rounder.csv")
        dr=pd.read_csv("spin_dept.csv")
        dq=pd.read_csv("wk_dept.csv")
        ds=pd.concat([df,dd,dp,dr,dq],ignore_index=True)
        row=ds[ds["Player"]==player].iloc[0]
        st.image(row["Image"],width=250)
        st.write(row["Details"])
        st.write("Date of Birth:",row["DOB"])
        st.write("Age:", row["Age"])
    # Back button
        if st.button("⬅ Back"):
            st.session_state.page = "PLAYERS"                       
    
# -------- DETAILS PAGE --------

            


with tab3:
        st.session_state.page="SERIES"
        st.header("SERIES")
        teams = [
        "India vs England","India vs Sri Lanka","India vs West Indies",
        "India vs South Africa","India vs England","India vs New Zealand",
        "India vs Zimbabwe","India vs Bangladesh","India vs Sri Lanka",
        "India vs New Zealand","India vs Australia","India vs South Africa",
        "India vs Sri Lanka","India vs Australia","India vs South Africa"
    ]
    # -------- Row 1 (0–5) --------
        col = st.columns(5)
        for i in range(5):
            with col[i]:
                if st.button(teams[i], key=f"team_{i}"):
                    st.session_state.series = teams[i]
                    st.session_state.page = "DETAILS"

    # -------- Row 2 (6–11) --------
        col = st.columns(5)
        for i in range(5, 10):
            with col[i-5]:
                if st.button(teams[i], key=f"team_{i}"):
                    st.session_state.series = teams[i]
                    st.session_state.page = "DETAILS"

    # -------- Row 3 (12–17) --------
        col = st.columns(5)
        for i in range(10, len(teams)):
            with col[i-12]:
                if st.button(teams[i], key=f"team_{i}"):
                    st.session_state.series = teams[i]
                    st.session_state.page = "DETAILS"
        if st.session_state.page=="DETAILS":
            team=st.session_state.series
            df=pd.read_csv("series.csv")
            row=(df[df["teams"]==team].iloc[0])
            st.write("***YEAR:***",row["year"])
            st.write("***Series***:",row["teams"])
            st.write("***Winner:***",row["winner"])
            st.write("***Won by***",row["margin"])
            st.write("***Player of series:***",row["player_of_series"])
            if st.button("⬅ Back"):
                st.session_state.page="SERIES"                                                      

                

            
            
with tab4:

    st.session_state.page="ICC TOURAMENT"
    st.write("ICC TOURNAMENTS")  
    df=pd.read_csv("Tournament.csv")  
    df=df.fillna(0)  
    for i in df["Tournament"].unique():
         if st.button(i):
            st.session_state.tour=i
            st.session_state.page="Tour"
    if st.session_state.page=="Tour":
        tour=st.session_state.tour
        row=df[df["Tournament"]==tour].iloc[0] 
        st.write("***Tournament:***",row["Tournament"])
        st.write("***Position:***",row["Position"])
        st.write("***Player of tournament:***",row["Player of Tournament"])
        df=df[df["Tournament"]==tour]
        
        colors = ["blue","red","green","orange","yellow","brown"] 
        top = df.nlargest(6, "Runs")
        fig, ax = plt.subplots(figsize=(8,6), facecolor="black")
        ax.set_facecolor("black")
        bars = ax.bar(top["Player"], top["Runs"],
              color=colors, edgecolor="white")
        for b in bars:
                h = b.get_height()
                ax.text(b.get_x() + b.get_width()/2, h+0.5, h,
                ha="center", va="bottom", color="white")
        ax.set_title("MOST RUNS", color="white")
        ax.set_xlabel("Runs", color="white")
        ax.tick_params(axis='x', colors='white', rotation=45)
        ax.tick_params(axis='y', colors='white')
        plt.tight_layout()
        st.pyplot(fig)   
        colors = ["blue","red","green","orange","yellow","brown"] 
        top = df.nlargest(6, "Wickets")
        fig, ax = plt.subplots(figsize=(8,6), facecolor="black")
        ax.set_facecolor("black")
        bars = ax.bar(top["Player"], top["Wickets"],
        color=colors, edgecolor="white")
        for b in bars:
                h = b.get_height()
                ax.text(b.get_x() + b.get_width()/2, h+0.5, h,
            ha="center", va="bottom", color="white")
        ax.set_title("MOST Wickets", color="white")
        ax.set_xlabel("Runs", color="white")
        ax.tick_params(axis='x', colors='white', rotation=45)
        ax.tick_params(axis='y', colors='white')
        plt.tight_layout()
        st.pyplot(fig)           
        total_runs=df["Runs"].sum()
        total_wickets=df["Wickets"].sum()
        df["con%"]=((df["Runs"]/total_runs*100)+(df["Wickets"]/total_wickets*100))/2
        df["con%"]=df["con%"]/df["con%"].sum()
        plt.style.use("dark_background")
        colors=["blue","red","green","orange","purple","pink","olive","cyan","yellow","gold","violet","plum","lime","indigo","navy"]
        explode =(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        fig,ax=plt.subplots(figsize=(7,7))
        ax.pie(df["con%"],labels=df["Player"],colors=colors,explode=explode,
        autopct="%1.1f%%",startangle=0,shadow=True,
        wedgeprops={"edgecolor":"white","linewidth":2})
        center_circle=plt.Circle((0,0),0.50,fc="black")
        fig.gca().add_artist(center_circle)
        ax.set_title("Contribution")
        ax.set_facecolor("white")
        st.pyplot(fig)
        if st.button("⬅ Back"):
                st.session_state.page="ICC TOURNAMENT"               

with tab5:
    st.write("BATTING")
    st.session_state.page="BATTING"
    @st.cache_data
    def load_data():
        return pd.read_csv("batting.csv")
    df=load_data()
    st.dataframe(df)
    df=df.fillna(0) 
    st.dataframe(df)

    colors = ["blue","red","green","orange","yellow","brown"] 
    top = df.nlargest(6, "Runs")
    fig, ax = plt.subplots(2,2,figsize=(16,14), facecolor="black")
    ax[0,0].set_facecolor("black")
    bars = ax[0,0].bar(top["Player"], top["Runs"],
                                 color=colors, edgecolor="white")
    for b in bars:
                h = b.get_height()
                ax[0,0].text(b.get_x() + b.get_width()/2, h+0.5, h,
                ha="center", va="bottom", color="white")
    ax[0,0].set_title("MOST RUNS", color="white")
    ax[0,0].set_ylabel("Runs", color="white")
    ax[0,0].tick_params(axis='x', colors='white', rotation=45)
    ax[0,0].tick_params(axis='y', colors='white')
    ax[0,0].set_facecolor("black")

    topavg=df.nlargest(6,"Average")
    bars = ax[0,1].bar(topavg["Player"], topavg["Average"],
                                     color=colors, edgecolor="white")
    for c in bars:
                h = c.get_height()
                ax[0,1].text(c.get_x() + c.get_width()/2, h+0.5, h,
                ha="center", va="bottom", color="white")
    ax[0,1].set_title("MOST Average", color="white")
    ax[0,1].set_ylabel("Runs", color="white")
    ax[0,1].tick_params(axis='x', colors='white', rotation=45)
    ax[0,1].tick_params(axis='y', colors='white')
                  
    top100 = df.nlargest(6, "Hundreds") 
    top50 = df.nlargest(6, "Fifties") 
    x = np.arange(len(top100["Player"]))
    width = 0.35
    bars1 = ax[1,1].bar(x - width/2, top100["Hundreds"], width,
                    label='100s', color='cyan', edgecolor="white")
    bars2 = ax[1,1].bar(x + width/2, top100["Fifties"], width,
                    label='50s', color='orange', edgecolor="white")
    for d in bars1:
              h = d.get_height()
              ax[1,1].text(d.get_x() + d.get_width()/2, h+0.3, int(h),
                 ha="center", va="bottom", color="white")
    for e in bars2:
                    h = e.get_height()
                    ax[1,1].text(e.get_x() + e.get_width()/2, h+0.3, int(h),
                 ha="center", va="bottom", color="white")
    ax[1,1].set_xticks(x)
    ax[1,1].set_xticklabels(top100["Player"], rotation=45)
    ax[1,1].set_title("100s vs 50s", color="white")
    ax[1,1].set_xlabel("Players", color="white")
    ax[1,1].legend()
    ax[1,1].set_ylabel("Count", color="white")
    ax[1,1].tick_params(axis='x', colors='white')
    ax[1,1].tick_params(axis='y', colors='white')


    top4 = df.nlargest(6, "Fours") 
    top6 = df.nlargest(6, "Sixes") 
    x = np.arange(len(top6["Player"]))
    width = 0.35
    bars1 = ax[1,0].bar(x - width/2, top6["Sixes"], width,
                                            label='6s', color='cyan', edgecolor="white")
    bars2 = ax[1,0].bar(x + width/2, top4["Fours"], width,
                    label='4s', color='orange', edgecolor="white")
    for f in bars1:
              h = f.get_height()
              ax[1,0].text(f.get_x() + f.get_width()/2, h+0.3, int(h),
                 ha="center", va="bottom", color="white")
    for g in bars2:
                    h = g.get_height()
                    ax[1,0].text(g.get_x() + g.get_width()/2, h+0.3, int(h),
                 ha="center", va="bottom", color="white")
    ax[1,0].set_xticks(x)
    ax[1,0].set_xticklabels(top6["Player"], rotation=45)
    ax[1,0].set_title("6s vs 4s", color="white")
    ax[1,0].set_xlabel("Players", color="white")
    ax[1,0].set_ylabel("Count", color="white")
    ax[1,0].tick_params(axis='x', colors='white')
    ax[1,0].tick_params(axis='y', colors='white')
    ax[1,0].legend()
    st.pyplot(fig) 
    plt.close(fig)
      

with tab6:
    st.write("BOWLING")
    st.session_state.page="BOWLING"
    @st.cache_data
    def load_data():
        return pd.read_csv("bowling.csv")
    df=load_data()
    st.dataframe(df)
    df=df.fillna(0)
    st.dataframe(df)

    colors = ["blue","red","green","orange","yellow","brown"] 
    topwk = df.nlargest(6, "Wickets")
    fig, ax = plt.subplots(1,2,figsize=(8,5), facecolor="black")
    bars = ax[0].bar(topwk["Player"], topwk["Wickets"],
                                 color=colors, edgecolor="white")
    for b in bars:
                h = b.get_height()
                ax[0].text(b.get_x() + b.get_width()/2, h+0.5, h,
                ha="center", va="bottom", color="white")
    ax[0].set_title("Wickets", color="white")
    ax[0].set_ylabel("Runs", color="white")
    ax[0].tick_params(axis='x', colors='white', rotation=45)
    ax[0].tick_params(axis='y', colors='white')
    ax[0].set_facecolor("black")
    topav= df.nlargest(6, "Average")
    bars = ax[1].bar(topav["Player"], topav["Average"],
                                 color=colors, edgecolor="white")
    for b in bars:
                h = b.get_height()
                ax[1].text(b.get_x() + b.get_width()/2, h+0.5, h,
                ha="center", va="bottom", color="white")
    ax[1].set_title("Average", color="white")
    ax[1].set_ylabel("Averge", color="white")
    ax[1].tick_params(axis='x', colors='white', rotation=45)
    ax[1].tick_params(axis='y', colors='white') 
    st.pyplot(fig)
    plt.close()
