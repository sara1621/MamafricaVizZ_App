import streamlit as st
import numpy as np
import pandas as pd
from mplsoccer import Sbopen
import cmasher as cmr

#for saving data as ajson file
import json
#For Visualizations
from player_viz import passe,shot,pass_cross,transition, persure_juego, pressure_heatmap,mistake,defensive_actions,passnetwork,assists,player

from mplsoccer import Pitch, FontManager
import matplotlib.patheffects as path_effects
from PIL import Image
from matplotlib import rcParams
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from PIL import Image
from mplsoccer import Pitch, VerticalPitch, add_image, FontManager
from scipy.spatial import Voronoi, voronoi_plot_2d
import seaborn as sns
from statsbombpy import sb
#st.set_page_config(layout='wide')

# Définir le style CSS pour utiliser la police Roboto
st.markdown("""
    <style>
    .title {
        font-family: 'Inter', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

background_style = """
    <style>
    /* Dégradé Savane */
    .stApp {
        background: linear-gradient(to right, #0B6B51, #064534, #064534);
        background-size: cover;
        background-position: center;
    }
    </style>
"""


st.markdown(background_style, unsafe_allow_html=True)
image_path = 'https://miro.medium.com/v2/resize:fit:1200/1*5vUpi5z_tdzRvOleCqBwpQ.png'  
statsbomb='https://mma.prnewswire.com/media/881169/Statsbomb_Logo.jpg?p=facebook'
palestine_path='https://img2.freepng.fr/20190628/o/kisspng-palestinian-national-authority-flag-of-palestine-c-stop-the-war-palestine-peace-dove-clipart-full-5d16b0ac1a97c0.8831415215617681081089.jpg'
title_html = """
<h1 style="margin: 0; font-family: Tahoma, sans-serif;margin-left: 3px;">
    <span style="color: Orange;">Mamafrica</span><span style="color: #F5F5DC;">VizZ</span>
</h1>
"""



bannerh_html = f"""
<div style="position: fixed; left: 0; top: 0; width: 100%; padding: 20px; background-image: url('{image_path}'); background-size: cover;z-index: 1000">
\\
\\ {title_html}
</div>
"""

st.markdown(bannerh_html, unsafe_allow_html=True)

sidebar_style = """
    <style>
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0);  /* Définit le fond de la barre latérale comme transparent */
        /* Centre les widgets dans la barre latérale */}

    /* Personnalisation du titre de la barre latérale */
    [data-testid="stSidebar"] > div:first-child h2 {
    color: #F5F5DC; /* Couleur beige */
    margin-left: 10px;
    font-size: 25px; /* Taille de la police */
    font-family: Inter,sans-serif /* Choisir la police de caractères */
    ;
}
    
    </style>
"""
st.markdown(sidebar_style,unsafe_allow_html=True)


st.sidebar.title('')


#st.sidebar.header("")   
st.sidebar.header('')
st.sidebar.header('Visualization filters')                                                                                                                                                                                                                                                                                                                                                                      
# Ajoutez le style à l'application Streamlit
st.markdown(sidebar_style, unsafe_allow_html=True)
#rajouter une image sidebar
# Chemin de l'image à afficher dans la barre latérale (remplacez par le chemin de votre image)
image_path = 'https://ichef.bbci.co.uk/images/ic/1200x675/p0h4mqdq.jpg'

title_style = """
    <style>
    .custom-title {
        font-family: 'Inter', sans-serif; /* Remplacez 'Arial' par la police de votre choix */
        font-size: 30px; /* Taille de la police */
        color: #F5F5DC; /* Couleur du texte */
        font-weight: bold; /* Poids de la police (bold, normal, etc.) */
    }
    </style>
"""
st.markdown(title_style, unsafe_allow_html=True)


subheader_style = """
    <style>
    .custom-subheader {
        font-family: 'Inter', sans-serif; /* Remplacez 'Arial' par la police de votre choix */
        font-size: 20px; /* Taille de la police */
        color: #F5F5DC; /* Couleur du texte */
        font-weight: bold; /* Poids de la police (bold, normal, etc.) */
    }
    </style>
"""
st.markdown(subheader_style, unsafe_allow_html=True)




header_style = """
    <style>
    .custom-header {
        font-family: 'Tahoma', sans-serif; /* Remplacez 'Arial' par la police de votre choix */
        font-size: 22px; /* Taille de la police */
        color: #F5F5DC; /* Couleur du texte */
        font-weight: bold; /* Poids de la police (bold, normal, etc.) */
    }
    </style>
"""
st.markdown(header_style, unsafe_allow_html=True)
# Add CSS to style the footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: None;
        text-align: center;
        padding: 10px 0;
        z-index=0
    }
    </style>
    """,
    unsafe_allow_html=True
)







# Utiliser st.title() avec la classe de style spécifiée
parser = Sbopen()
df_competition = parser.competition()
matches = parser.match(competition_id=1267, season_id=107)
#une colone pour les mathes
matches['match'] = matches['home_team_name'] + ' vs. ' + matches['away_team_name']

@st.cache_data
def load_data(team_choice):
    mask=((matches.home_team_name==teams_choice)|(matches.away_team_name==teams_choice))
    games_selected = matches.loc[mask,["match",'match_date','kick_off','home_score','away_score','competition_stage_name','stadium_name','stadium_country_name','referee_name','referee_country_name']]
    return games_selected

teams=list(matches['home_team_name'].drop_duplicates())

#st.subheader('Select your team ')

#st.sidebar.markdown('Choose one or multiple teams')

st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            font-size: 20px;
            color: blue;
        }
    </style>
    """,
    unsafe_allow_html=True
)


teams_choice = st.sidebar.selectbox('Team', teams)



games = load_data(teams_choice)
game=games[["match",'match_date','kick_off','home_score','away_score','competition_stage_name','stadium_name','stadium_country_name','referee_name','referee_country_name']].reset_index(drop=True)
if teams_choice:
    # Définition de la couleur du titre (en hexa)
    header_color = '#F5F5DC'  # Choisissez une couleur appropriée



# Afficher un titre avec le style personnalisé
    st.markdown('<h1 class="custom-title">Match Information </h1>', unsafe_allow_html=True)

    text = "This table presents details of the matches played by the selected team in the 2023 Africa Cup of Nations."

# Utilisez le balisage HTML et CSS pour définir la couleur beige
    beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'

# Affichez le texte stylisé dans Streamlit
    st.markdown(beige_text, unsafe_allow_html=True)
    st.write(game)    

else: 
    st.header(' ')

# Ajoutez vos styles CSS personnalisés
mask_game=((matches.home_team_name==teams_choice)|(matches.away_team_name==teams_choice))
matches=matches.loc[mask_game]
match_list=list(matches['match'])
#st.sidebar.subheader("Match")
#st.sidebar.header('Match')

match_choice=st.sidebar.selectbox('Match',match_list,index=None)
#st.sidebar.header('VizZ type')

plot_options=["Passing Network",'Passes','Pressure heat map','Pressure heat map Juego de Posición','Shots',"Forward passes",'Crosses','Mistakes','Defensive actions',"Assists","Player performance"]
selected_plot = st.sidebar.selectbox('VizZ type:', plot_options)
st.markdown('<h1 class="custom-title">Visualizations </h1>', unsafe_allow_html=True)

st.sidebar.header('')
st.sidebar.header('')
st.sidebar.image("afcon.png", width=100)
st.sidebar.image("statsbomb.png", width=100)



#st.footer('[LinkedIn](https://www.linkedin.com/in/sara-bentelli-90a02516b/) [Twitter](https://twitter.com/SoccerbyNumber6)')
if match_choice:
    mask_2=matches[matches['match']==match_choice]
    match_id=mask_2.match_id.unique()
    def event_data(match_choice):
        mask_2=matches[matches['match']==match_choice]
        events=pd.DataFrame()
        for i in mask_2['match_id']:
            events =parser.event(i)[0]
        return events
    df=event_data(match_choice)
    selected_team = teams_choice
    df_team_selected=df[df['team_name']==selected_team]
    
    




    if selected_plot == 'Passing Network':
       #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
       st.markdown('<h1 class="custom-subheader">Passing Network: </h1>', unsafe_allow_html=True)
       text="A [passing network](https://statsbomb.com/articles/soccer/explaining-xgchain-passing-networks/) is  the application of network theory and social network analysis to passing data in football. Each player is a node, and the passes between them are connections."
       beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
       st.markdown(beige_text, unsafe_allow_html=True)
       passnetwork(match_id,selected_team)
       \
       \
       \
       \
       \
       \
       text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
       beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
       st.markdown(beige_text, unsafe_allow_html=True)

    if selected_plot == 'Passes':
       #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
       st.markdown('<h1 class="custom-subheader">Ball Pass: </h1>', unsafe_allow_html=True)
       text="Ball is passed between teammates."
       beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
       st.markdown(beige_text, unsafe_allow_html=True)
       st.markdown('<h1 class="custom-subheader">Ball Receipt: </h1>', unsafe_allow_html=True)
       text="The receipt or intended receipt of a pass."
       beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
       st.markdown(beige_text, unsafe_allow_html=True)
       passe(df,selected_team)
       \
       \
       \
       \
       \
       text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
       beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
       st.markdown(beige_text, unsafe_allow_html=True)
       

    elif selected_plot == 'Pressure heat map':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Pressure: </h1>', unsafe_allow_html=True)
         text="Applying pressure to an opposing player who’s receiving, carrying or releasing the ball."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         pressure_heatmap(df,selected_team)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

    elif selected_plot == 'Pressure heat map Juego de Posición':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Pressure Juego de Posición: </h1>', unsafe_allow_html=True)
         text="Percentage of pressure applied by the selected team according to [Juego de Posición](https://breakingthelines.com/tactical-analysis/what-is-juego-de-posicion/)."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

         persure_juego(df,selected_team) 
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
    elif selected_plot == 'Assists':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         #st.markdown('<h1 class="custom-subheader">Assists: </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Shot assist: </h1>', unsafe_allow_html=True)
         text="The pass was an assist to a shot (that did not score a goal)."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Goal assist: </h1>', unsafe_allow_html=True)
         text="The pass was an assist to a goal."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

         assists(df_team_selected,selected_team)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

    elif selected_plot == 'Shots':
          #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
          st.markdown('<h1 class="custom-subheader">Shot: </h1>', unsafe_allow_html=True)
          text="An attempt to score a goal, made with any (legal) part of the body."
          beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)

          shot(df_team_selected)
          \
          \
          \
          \
          \
          \
          text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
          beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)


    elif selected_plot == 'Forward passes':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Forward pass: </h1>', unsafe_allow_html=True)
         text='All passes into the final third of the pitch.'
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         transition(df_team_selected)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
    elif selected_plot == 'Crosses':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Cross: </h1>', unsafe_allow_html=True)

         text='A [cross](https://www.soccerhelp.com/terms/soccer-cross.shtml) is a "square pass" to the area in front of the goal.'
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         pass_cross(df_team_selected)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
    elif selected_plot == 'Mistakes':
          #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
          st.markdown('<h1 class="custom-subheader">Dispossessed: </h1>', unsafe_allow_html=True)
          text="Player loses ball to an opponent as a result of being tackled by a defender without attempting a dribble."
          beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)
          st.markdown('<h1 class="custom-subheader">Miscontrol: </h1>', unsafe_allow_html=True)
          text="Player loses ball due to bad touch."
          beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)
          st.markdown('<h1 class="custom-subheader">Foul Committed: </h1>', unsafe_allow_html=True)
          text="Any infringement that is penalised as foul play by a referee. Offside are not tagged as afoul committed.."
          beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)
          st.markdown('<h1 class="custom-subheader">Error: </h1>', unsafe_allow_html=True)
          text="When a player is judged to make an on-the-ball mistake that leads to a shot on goal."
          beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)
          mistake(df_team_selected)
          \
          \
          \
          \
          \
          \
          text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
          beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
          st.markdown(beige_text, unsafe_allow_html=True)

    

    elif selected_plot == 'Defensive actions':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)

         st.markdown('<h1 class="custom-subheader">Clearance: </h1>', unsafe_allow_html=True)
         text="Action by a defending player to clear the danger without an intention to deliver it to a teammate."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Block: </h1>', unsafe_allow_html=True)
         text="Blocking the ball by standing in its path."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

         st.markdown('<h1 class="custom-subheader">Interception: </h1>', unsafe_allow_html=True)
         text="Preventing an opponent's pass from reaching their teammates by moving to the passing lane/reacting to intercept it."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Ball Recovery: </h1>', unsafe_allow_html=True)
         text="An attempt to recover a loose ball."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         defensive_actions(df_team_selected)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
    elif selected_plot == 'Player performance':
         #st.markdown('<h1 class="custom-header">Description </h1>', unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Pass: </h1>', unsafe_allow_html=True)
         text="The Ball is passed by the player selected."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Carry: </h1>', unsafe_allow_html=True)
         text="The player controls the ball at their feet while moving or standing still."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)

         st.markdown('<h1 class="custom-subheader">Under pressure: </h1>', unsafe_allow_html=True)
         text='The action was performed while being pressured by an opponent.'
  
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         st.markdown('<h1 class="custom-subheader">Counterpress: </h1>', unsafe_allow_html=True)
         text="Pressing actions within 5 seconds of an open play turnover."
         beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
         player(df_team_selected)
         \
         \
         \
         \
         \
         \
         text='By [Sara](https://twitter.com/SoccerbyNumber6) [Bentelli](https://www.linkedin.com/in/sara-bentelli-90a02516b/)'
         beige_text = f'<span style="color: #F5F5DC;font-size: 25px;margin-left: 500px; font-family: Inter ">{text}</span>'
         st.markdown(beige_text, unsafe_allow_html=True)
else:
    text="Please select a match from 'Match' and the event type you would like to display on the screen from 'VizZ type' dropdown menu on the left."
    beige_text = f'<span style="color: #F5F5DC;font-size: 20px">{text}</span>'
    st.markdown(beige_text, unsafe_allow_html=True)




#if match_choice:
    #st.subheader('event data for the selected match')
    #st.write(df)
#else:
    #st.subheader('')

   







#data_load_state = st.text('Loading data...')
#data =parser.event(match_choice)[0]

#data_load_state.text("Done! (using st.cache_data)")

