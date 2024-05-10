import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from mplsoccer import Sbopen, Pitch, VerticalPitch,FontManager
from statsbombpy import sb
import cmasher as cmr
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap,to_rgba
from scipy.ndimage import gaussian_filter
from mplsoccer import Pitch, VerticalPitch, FontManager,Sbopen

def assists(df,selected_team):
   mask1=(df.pass_shot_assist.notnull())
   df_shot_assist=df.loc[mask1]
   try:
     mask2=(df.pass_goal_assist.notnull())
   except AttributeError:
       team1=selected_team
       robotto_regular = FontManager()
       path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
       DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
       NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
       LINEWIDTH = 0.5
       ALPHA_PITCH_LINE = 0.2
       ALPHA_PASS_LINE = 0.6
       cmap='Oranges'
       back='none'
       LINE_COLOR="w"
       PASS_COLOR='w'
       flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ,'white'], N=400)
       pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=4, linestyle='-')
       fig, axs= pitch.grid(figheight=10, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.05,grid_width=0.88)
       fig.set_facecolor(back)
       pitch.scatter(df_shot_assist.x,df_shot_assist.y,c='w',ax=axs['pitch'],s=200,edgecolor="w",marker="o",alpha=.5)
       for i in range(1, NUM_GLOW_LINES + 1):
             pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
    
       pitch.draw(ax=axs['pitch'])  # we plot on-top of our previous axis from pitch.grid
       pitch.lines(df_shot_assist.x, df_shot_assist.y,
                df_shot_assist.end_x,df_shot_assist.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color=PASS_COLOR, comet=True, ax=axs['pitch'],label='Shot assist')
       axs['title'].text(0.5, 0.6,f'{team1} Assists', color='#F5F5DC',fontsize=35,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
       axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
       axs['pitch'].legend(facecolor='#0B6B51', handlelength=2, edgecolor='None', fontsize=20, loc='upper left')

   else:
      df_goal_assist=df.loc[mask2]
      team1=selected_team
      robotto_regular = FontManager()
      path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
      DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
      NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
      LINEWIDTH = 0.5
      ALPHA_PITCH_LINE = 0.2
      ALPHA_PASS_LINE = 0.6
      cmap='Oranges'
      back='none'
      LINE_COLOR="w"
      PASS_COLOR='w'
      flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ,'white'], N=400)
      pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=4, linestyle='-')
      fig, axs= pitch.grid(figheight=10, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.05,grid_width=0.88)
      fig.set_facecolor(back)

      pitch.scatter(df_shot_assist.x,df_shot_assist.y,c='w',ax=axs['pitch'],s=200,edgecolor="w",marker="o",alpha=.5)

      pitch.scatter(df_goal_assist.x,df_goal_assist.y,c='w',ax=axs['pitch'],s=200,edgecolor="w",marker="o",alpha=.8)
      for i in range(1, NUM_GLOW_LINES + 1):
          pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
    
      pitch.draw(ax=axs['pitch'])  # we plot on-top of our previous axis from pitch.grid
      pitch.lines(df_shot_assist.x, df_shot_assist.y,
                df_shot_assist.end_x,df_shot_assist.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color=PASS_COLOR, comet=True, ax=axs['pitch'],label='Shot assist')
      pitch.lines(df_goal_assist.x, df_goal_assist.y,
                df_goal_assist.end_x,df_goal_assist.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color='Red', comet=True, ax=axs['pitch'],label='Goal assist')
      axs['title'].text(0.5, 0.6,f'{team1} Assists', color='#F5F5DC',fontsize=35,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
      axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
      axs['pitch'].legend(facecolor='#0B6B51', handlelength=2, edgecolor='None', fontsize=20, loc='upper left')

   
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)




def passnetwork(match_id,selected_team):
   parser = Sbopen()
   for i in match_id:
      events, related, freeze, players =parser.event(i)
   TEAM = selected_team
   events.loc[events.tactics_formation.notnull(), 'tactics_id'] = events.loc[
   events.tactics_formation.notnull(), 'id']
   events[['tactics_id', 'tactics_formation']] = events.groupby('team_name')[[
    'tactics_id', 'tactics_formation']].ffill()
   formation_dict = {1: 'GK', 2: 'RB', 3: 'RCB', 4: 'CB', 5: 'LCB', 6: 'LB', 7: 'RWB',
                  8: 'LWB', 9: 'RDM', 10: 'CDM', 11: 'LDM', 12: 'RM', 13: 'RCM',
                  14: 'CM', 15: 'LCM', 16: 'LM', 17: 'RW', 18: 'RAM', 19: 'CAM',
                  20: 'LAM', 21: 'LW', 22: 'RCF', 23: 'ST', 24: 'LCF', 25: 'SS'}
   players['position_abbreviation'] = players.position_id.map(formation_dict)
   sub = events.loc[events.type_name == 'Substitution',
                 ['tactics_id', 'player_id', 'substitution_replacement_id',
                  'substitution_replacement_name']]
   players_sub = players.merge(sub.rename({'tactics_id': 'id'}, axis='columns'),
                            on=['id', 'player_id'], how='inner', validate='1:1')
   players_sub = (players_sub[['id', 'substitution_replacement_id', 'position_abbreviation']]
               .rename({'substitution_replacement_id': 'player_id'}, axis='columns'))
   players = pd.concat([players, players_sub])
   players.rename({'id': 'tactics_id'}, axis='columns', inplace=True)
   players = players[['tactics_id', 'player_id', 'position_abbreviation']]
# add on the position the player was playing in the formation to the events dataframe
   events = events.merge(players, on=['tactics_id', 'player_id'], how='left', validate='m:1')
# add on the position the receipient was playing in the formation to the events dataframe
   events = events.merge(players.rename({'player_id': 'pass_recipient_id'},
                                     axis='columns'), on=['tactics_id', 'pass_recipient_id'],
                      how='left', validate='m:1', suffixes=['', '_receipt'])
   formation=events[events['team_name']==TEAM].tactics_formation.unique()
   selected_formation=st.selectbox('FORMATION', formation)

   FORMATION = selected_formation
   pass_cols = ['id', 'position_abbreviation', 'position_abbreviation_receipt']
   passes_formation = events.loc[(events.team_name == TEAM) & (events.type_name == 'Pass') &
                              (events.tactics_formation == FORMATION) &
                              (events.position_abbreviation_receipt.notnull()), pass_cols].copy()
   location_cols = ['position_abbreviation', 'x', 'y']
   location_formation = events.loc[(events.team_name == TEAM) &
                                (events.type_name.isin(['Pass', 'Ball Receipt'])) &
                                (events.tactics_formation == FORMATION), location_cols].copy()
   average_locs_and_count = (location_formation.groupby('position_abbreviation')
                          .agg({'x': ['mean'], 'y': ['mean', 'count']}))
   average_locs_and_count.columns = ['x', 'y', 'count']

   passes_formation['pos_max'] = (passes_formation[['position_abbreviation',
                                                'position_abbreviation_receipt']]
                               .max(axis='columns'))
   passes_formation['pos_min'] = (passes_formation[['position_abbreviation',
                                                'position_abbreviation_receipt']]
                               .min(axis='columns'))
   passes_between = passes_formation.groupby(['pos_min', 'pos_max']).id.count().reset_index()
   passes_between.rename({'id': 'pass_count'}, axis='columns', inplace=True)
   passes_between = passes_between.merge(average_locs_and_count, left_on='pos_min', right_index=True)
   passes_between = passes_between.merge(average_locs_and_count, left_on='pos_max', right_index=True,
                                      suffixes=['', '_end'])
   average_locs_and_count = (location_formation.groupby('position_abbreviation')
                          .agg({'x': ['mean'], 'y': ['mean', 'count']}))
   average_locs_and_count.columns = ['x', 'y', 'count']

# calculate the number of passes between each position (using min/ max so we get passes both ways)
   passes_formation['pos_max'] = (passes_formation[['position_abbreviation',
                                                'position_abbreviation_receipt']]
                               .max(axis='columns'))
   passes_formation['pos_min'] = (passes_formation[['position_abbreviation',
                                                'position_abbreviation_receipt']]
                               .min(axis='columns'))
   passes_between = passes_formation.groupby(['pos_min', 'pos_max']).id.count().reset_index()
   passes_between.rename({'id': 'pass_count'}, axis='columns', inplace=True)

   passes_between = passes_between.merge(average_locs_and_count, left_on='pos_min', right_index=True)
   passes_between = passes_between.merge(average_locs_and_count, left_on='pos_max', right_index=True,
                                      suffixes=['', '_end'])
   MAX_LINE_WIDTH = 18
   MAX_MARKER_SIZE = 3000
   passes_between['width'] = (passes_between.pass_count / passes_between.pass_count.max() *
                           MAX_LINE_WIDTH)
   average_locs_and_count['marker_size'] = (average_locs_and_count['count']
                                         / average_locs_and_count['count'].max() * MAX_MARKER_SIZE)
   MIN_TRANSPARENCY = 0.3
   color = np.array(to_rgba('white'))
   color = np.tile(color, (len(passes_between), 1))
   c_transparency = passes_between.pass_count / passes_between.pass_count.max()
   c_transparency = (c_transparency * (1 - MIN_TRANSPARENCY)) + MIN_TRANSPARENCY
   color[:, 3] = c_transparency
   pitch = Pitch(pitch_type='statsbomb', pitch_color='None', line_color='w')
   fig, ax = pitch.draw( constrained_layout=True, tight_layout=False)
   fig.set_facecolor("None")
   pass_lines = pitch.lines(passes_between.x, passes_between.y,
                         passes_between.x_end, passes_between.y_end, lw=passes_between.width,
                         color=color, zorder=1, ax=ax)
   pass_nodes = pitch.scatter(average_locs_and_count.x, average_locs_and_count.y,
                           s=average_locs_and_count.marker_size,
                           color='red', edgecolors='black', linewidth=1, alpha=1, ax=ax)
   for index, row in average_locs_and_count.iterrows():
      pitch.annotate(row.name, xy=(row.x, row.y), c='white', va='center',
                   ha='center', size=16, weight='bold', ax=ax)

   fig, axs = pitch.grid(figheight=10, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.05,grid_width=0.88)
   fig.set_facecolor("#22312b")
   pass_lines = pitch.lines(passes_between.x, passes_between.y,
                         passes_between.x_end, passes_between.y_end, lw=passes_between.width,
                         color=color, zorder=1, ax=axs['pitch'])
   pass_nodes = pitch.scatter(average_locs_and_count.x, average_locs_and_count.y,
                           s=average_locs_and_count.marker_size,
                           color='red', edgecolors='black', linewidth=1, alpha=1, ax=axs['pitch'])
   for index, row in average_locs_and_count.iterrows():
       pitch.annotate(row.name, xy=(row.x, row.y), c='white', va='center',
                   ha='center', size=16, weight='bold', ax=axs['pitch'])
   URL = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Regular.ttf'
   robotto_regular = FontManager(URL)
   axs['endnote'].text(1, 0.5, '@SoccerbyNumber6', color='#c7d5cc',
                    va='center', ha='right', fontsize=15,
                    fontproperties=robotto_regular.prop)
   TITLE_TEXT = f'{TEAM}, {FORMATION} formation'
   axs['title'].text(0.5, 0.7, TITLE_TEXT, color='#F5F5DC',
                  va='center', ha='center', fontproperties=robotto_regular.prop, fontsize=30)
   
   return  selected_formation,st.pyplot(fig, dpi=100, facecolor= 'None' ,bbox_inches=None)

def passe(df,selected_team):
   team1=selected_team
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   mask=((df.type_name=='Pass')&(df.team_name==selected_team))
   df_pass=df.loc[mask]
   #mask=(df_pass.outcome_name.isnull())
   #df_complete=df_pass.loc[mask,['x', 'y', 'end_x', 'end_y']]
   #df_incom=df_pass[~mask]
   #df_ball_recit=df[df['type_name']=='Ball Receipt']
   mask1=((df.type_name=='Ball Receipt')&(df.team_name==selected_team))
   df_ball_receipt=df.loc[mask1,['x','y']]
   #df_reciep_inc=df_ball_recit[~mask1]
   DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
   LINEWIDTH = 0.5
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.2
   ALPHA_PASS_LINE = 0.6
   cmap='Oranges'
   back='none'
   LINE_COLOR="w"
   PASS_COLOR='w'
   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ,'white'], N=400)
   pitch = VerticalPitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=4, linestyle='-')
   fig, axs= pitch.grid(ncols=2,grid_height=0.7, title_height=0.05,  axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0,grid_width=0.88,figheight= 10)
   fig.set_facecolor(back)

   kde_Pass = pitch.kdeplot(df_pass.x,df_pass.y, ax=axs['pitch'][0],
                          levels=200, shade_lowest=True,
                          cut=50, cmap=flamingo_cmap,fill=True)
   #pitch.scatter(df_incom.x,df_incom.y,color='red',s= 40, marker='x',ax=axs['pitch'][0],label='Incomplete')
   #pitch.scatter(df_reciep_inc.x,df_reciep_inc.y,color='red',s= 40, marker='x',ax=axs['pitch'][1])
   
   kde_receipt=pitch.kdeplot(df_ball_receipt.x,df_ball_receipt.y, ax=axs['pitch'][1],levels=200,shade_lowest=True,cut=100,cmap=flamingo_cmap,fill=True)
   
   #axs["pitch"][0].legend(facecolor='#22312b', handlelength=5, edgecolor='None', fontsize=10, loc='upper right')
   
   # endnote and title
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
   axs['title'].text(0.5, 1.5,f'{team1}  Passes ', color='#F5F5DC',fontsize=25,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
   
   axs['pitch'][0].set_title('Ball Pass',color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)
   axs['pitch'][1].set_title('Ball Receipt',color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)




def shot(df):
  robotto_regular = FontManager()
  path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
  df=df[df['type_name']=='Shot']
  mask=(df.outcome_name=='Goal')
  df_goal=df.loc[mask]
  DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
  NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
  LINEWIDTH = 0.5
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
  ALPHA_PITCH_LINE = 0.2
  ALPHA_PASS_LINE = 0.6
  cmap=cmr.jungle
  back='none'
  LINE_COLOR="w"
  PASS_COLOR='#F5F5DC'
  pitch = VerticalPitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=4, linestyle='-',half=True)
  fig, axs= pitch.grid(figheight=10, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.05,grid_width=0.88)
  fig.set_facecolor(back)
  pitch.scatter(df_goal.x,df_goal.y,c='Green',ax=axs['pitch'],s=450,edgecolor="w",marker="*",alpha=.8,label='Goal')
  pitch.scatter(df[~mask].x,df[~mask].y,c='w',ax=axs['pitch'],s=300,edgecolor="w",marker="o",alpha=.4)

  for i in range(1, NUM_GLOW_LINES + 1):
      pitch = VerticalPitch(line_color=LINE_COLOR, pitch_color=back,half=True,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
      
      pitch.draw(ax=axs['pitch'])
  axs['title'].text(0.5, 0.6,'Shots', color='#F5F5DC',fontsize=35,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
  axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
  axs['pitch'].legend(facecolor='w', handlelength=2, edgecolor='None', fontsize=20, loc='upper left')

  return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)



def pass_cross(df):
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),path_effects.Normal()]
   mask=(df.pass_cross.notnull())
   df=df[mask]
   ### LINEWIDTH = 1  # starting linewidth
   DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
   LINEWIDTH = 0.3
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.2
   ALPHA_PASS_LINE = 1

   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ,'white'], N=100)
   cmap=cmr.jungle 
   PASS_COLOR = 'w'#"pink" #'#89103F'   
   LINE_COLOR =  'w'#"#0FF4FF" #'#BF7117'  #'#FE53BB' 
   DIVISION_LINES='#800080'
   back='none'#'#73737
   pitch = VerticalPitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=2, linestyle='-',half=True)
   fig, axs= pitch.grid(figheight=10, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.05,grid_width=0.88)
   fig.set_facecolor(back)
    
   pitch.lines(df.x,df.y,df.end_x,df.end_y,ax=axs['pitch'],capstyle='butt',  # cut-off the line at the end-location.
            linewidth=LINEWIDTH, color=PASS_COLOR,label='Crosses')
   pitch.scatter(df.x,df.y, color="w",s=100,edgecolor="w",marker="o",alpha=.5,ax=axs['pitch'])
   for i in range(1, NUM_GLOW_LINES + 1):
       pitch = VerticalPitch(line_color=LINE_COLOR, pitch_color=back,half=True,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
    
   pitch.draw(ax=axs['pitch'])  # we plot on-top of our previous axis from pitch.grid
   pitch.lines(df.x, df.y,
                df.end_x,df.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color=PASS_COLOR, comet=True, ax=axs['pitch'])
   axs['title'].text(0.5, 0.6,'Crosses', color='#F5F5DC',fontsize=35,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)



def transition(df):
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   mask= ((df.end_x >= 80)&(df.x<= 60))
   df=df[mask]
   DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
   LINEWIDTH = 0.3
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.2
   ALPHA_PASS_LINE = 1

   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ], N=10)
   cmap=cmr.jungle 
   PASS_COLOR = 'w'#'#0FF4FF'#"pink" #'#89103F'   
   LINE_COLOR = "w" #'#BF7117'  #'#FE53BB' 
   DIVISION_LINES='#800080'
   back='none'#'#73737

   pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=2, linestyle='-')
   fig, axs= pitch.grid(figheight=9, title_height=0.08, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_space=0, grid_height=0.82, endnote_height=0.04,grid_width=0.88)
   fig.set_facecolor(back)
    
   pitch.lines(df.x,df.y,df.end_x,df.end_y,ax=axs['pitch'],capstyle='butt',  # cut-off the line at the end-location.
            linewidth=LINEWIDTH, color=PASS_COLOR)
   for i in range(1, NUM_GLOW_LINES + 1):
       pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
    
   pitch.draw(ax=axs['pitch'])  # we plot on-top of our previous axis from pitch.grid
   pitch.lines(df.x, df.y,
                df.end_x,df.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color=PASS_COLOR, comet=True, ax=axs['pitch'])
   axs['title'].text(0.5, 0.6,'Forward passes', color='#F5F5DC',fontsize=35,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)


def persure_juego(df,team_choice):
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   mask=( df.team_name==team_choice)
   df_selected_team=df.loc[mask]
   df_vs=df.loc[~mask]
   df_vs=df_vs[df_vs['type_name']=='Pressure']
   df_selected_team=df_selected_team[df_selected_team['type_name']=='Pressure']
   team1,=df_selected_team.team_name.unique()
   team2,=df_vs.team_name.unique()
   # setup pitch
   back='none'   
   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#B3C14D','#A03109' ], N=200) 
   pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 10 colors",
                                                       [ '#4393c4','#15242e'], N=10)

   
##############################################################################
# Plot the chart again with a title
# ---------------------------------
# We will use mplsoccer's grid function to plot a pitch with a title and endnote axes.
   pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2, pitch_color=back)
   fig, axs = pitch.grid(ncols=2,endnote_height=0.004, endnote_space=0,
                      grid_height=0.7, title_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      figheight=10, title_height=0.09)
   fig.set_facecolor(back)
   

# heatmap and labels
   bin_statistic = pitch.bin_statistic_positional(df_selected_team.x, df_selected_team.y, statistic='count',
                                               positional='full', normalize=True)
   pitch.heatmap_positional(bin_statistic, ax=axs['pitch'][0],
                         cmap=flamingo_cmap)
   labels = pitch.label_heatmap(bin_statistic, color='#F5F5DC', fontsize=18,
                             ax=axs['pitch'][0], ha='center', va='center',
                             str_format='{:.0%}')

   bin_statistic = pitch.bin_statistic_positional(df_vs.x, df_vs.y, statistic='count',
                                               positional='full', normalize=True)
   pitch.heatmap_positional(bin_statistic, ax=axs['pitch'][1],
                         cmap=flamingo_cmap)
   labels = pitch.label_heatmap(bin_statistic, color='#F5F5DC', fontsize=18,
                             ax=axs['pitch'][1], ha='center', va='center',
                             str_format='{:.0%}')

# endnote and title
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')
   axs['title'].text(0.5, 0.6,'Pressure applied by', color='#F5F5DC',fontsize=25,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
   axs['pitch'][0].set_title(f'{team1}',color='white',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)
   axs['pitch'][1].set_title(f'{team2}',color='white',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)

   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)

def pressure_heatmap(df, team_choice):
    # fontmanager for google font (robotto)
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]

   pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 10 colors",
                                                       ['#15242e', '#4393c4'], N=10)
   mask=( df.team_name==team_choice)
   df_selected_team=df.loc[mask]
   df_vs=df.loc[~mask]
   df_vs=df_vs[df_vs['type_name']=='Pressure']
   df_selected_team=df_selected_team[df_selected_team['type_name']=='Pressure']
   
  
   back='none'  
   cmap=cmr.jungle 
   PASS_COLOR = '#F5F5DC'#'#0FF4FF'#"pink" #'#89103F'   
   LINE_COLOR = "w" #'#BF7117'  #'#FE53BB' 
   DIVISION_LINES='#800080' 
   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#B3C14D','#A03109' ], N=200) 
   pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2,
              pitch_color=back, line_color=LINE_COLOR)
   fig, axs = pitch.grid(ncols=2,endnote_height=0.03, endnote_space=0,
                      # leave some space for the colorbar
                      grid_width=0.88, left=0.025,
                      title_height=0.08, title_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      grid_height=0.86)
   bin_statistic = pitch.bin_statistic(df_selected_team.x, df_selected_team.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0], cmap='hot', edgecolors='#22312b')
   bin_statistic = pitch.bin_statistic(df_vs.x, df_vs.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][1], cmap='hot', edgecolors='#22312b')

   ax_cbar = fig.add_axes((0.915, 0.093, 0.03, 0.786))
   cbar = plt.colorbar(pcm, cax=ax_cbar)
   cbar.outline.set_edgecolor('#efefef')
   cbar.ax.yaxis.set_tick_params(color='#efefef')
   plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')
   for label in cbar.ax.get_yticklabels():
      label.set_fontproperties(robotto_regular.prop)
      label.set_fontsize(15)


   team1,=df_selected_team.team_name.unique()
   team2,=df_vs.team_name.unique()
  
   
   axs['title'].text(0.5, 0.9,'Pressure applied by', color='#F5F5DC',fontsize=30,va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop)
   axs['pitch'][0].set_title(f'{team1}',color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)
   axs['pitch'][1].set_title(f'{team2}',color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=20)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color='#F5F5DC')

   
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)



def mistake(df):
    # fontmanager for google font (robotto)
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   team,=df.team_name.unique()

   pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 10 colors",
                                                      ['#15242e', '#4393c4'], N=10)
   mask= (df.type_name=='Error')
   df_error=df.loc[mask]
   df_dispos=df[df['type_name']=='Dispossessed']
   df_foul_com=df[df["type_name"]=='Foul Committed']
   df_miscontrol=df[df['type_name']=='Miscontrol']
   text_color='#F5F5DC'
   ### LINEWIDTH = 1  # starting linewidth
   DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
   LINEWIDTH = 0.3
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.2
   ALPHA_PASS_LINE = 1

   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['#064534','#e88013' ,'white'], N=100)
   cmap=cmr.jungle 
   PASS_COLOR = 'w'#"pink" #'#89103F'   
   LINE_COLOR =  'w'#"#0FF4FF" #'#BF7117'  #'#FE53BB' 
   DIVISION_LINES='#800080'
   back='none'#'#73737
   pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=2, linestyle='-',half=False)
   fig, axs= pitch.grid(ncols=2,nrows=2,grid_height=0.6, title_height=0.05,  axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0,grid_width=0.88,figheight= 10)
   fig.set_facecolor(back)
    
   pitch.scatter(df_dispos.x,df_dispos.y, color="w",s=100,edgecolor="w",marker="o",alpha=.5,ax=axs['pitch'][0][0])
   bin_statistic = pitch.bin_statistic(df_dispos.x, df_dispos.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0][0], cmap='hot', edgecolors='#22312b',label=f'{team} Clearances')
   bin_statistic = pitch.bin_statistic(df_miscontrol.x, df_miscontrol.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0][1], cmap='hot', edgecolors='#22312b')
   bin_statistic = pitch.bin_statistic(df_foul_com.x, df_foul_com.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][1][0], cmap='hot', edgecolors='#22312b')
   bin_statistic = pitch.bin_statistic(df_error.x, df_error.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pc = pitch.heatmap(bin_statistic, ax=axs['pitch'][1][1], cmap='hot', edgecolors='#22312b')
   ax_cbar = fig.add_axes((0.035, 0.15, 0.93, 0.03))
   cbar = plt.colorbar(pcm, orientation='horizontal', cax=ax_cbar)
   cbar.outline.set_edgecolor('#efefef')
   cbar.ax.yaxis.set_tick_params(color='#efefef')
   plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')
   for label in cbar.ax.get_yticklabels():
       label.set_fontproperties(robotto_regular.prop)
       label.set_fontsize(15)

# endnote and title
   text_color='#F5F5DC'
   ax_title = axs['title'].text(0.5, 1.5, f"{team} Mistakes", color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=25)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color=text_color)
   axs['pitch'][0][0].set_title('Dispossessed',color='#F5F5DC',
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][0][1].set_title('Miscontrols',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][0].set_title('Fouls Committed',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][1].set_title('Errors',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)


def defensive_actions(df):
   team,=df.team_name.unique()
   df_clearance=df[df['type_name']=='Clearance']
   df_block=df[df['type_name']=='Block']
   df_interception=df[df['type_name']=='Interception']
   df_ball_recovery=df[df['type_name']=='Ball Recovery']
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   DIFF_LINEWIDTH = 2.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 3  # the amount of loops, if you increase the glow will be wider
   LINEWIDTH = 0.3
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.2
   ALPHA_PASS_LINE = 1
   text_color='#F5F5DC'
   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['black','#394a13' ,'#a4e610','white'], N=100)
   LINE_COLOR =  'w'#"#0FF4FF" #'#BF7117'  #'#FE53BB' 
   back='none'#'#73737
   pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=2, linestyle='-',half=False)
   fig, axs= pitch.grid(ncols=2,nrows=2,grid_height=0.6, title_height=0.05,  axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0,grid_width=0.88,figheight= 10)
   fig.set_facecolor(back)
   bin_statistic = pitch.bin_statistic(df_clearance.x, df_clearance.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0][0], cmap='hot', edgecolors='#22312b',label=f'{team} Clearances')
   bin_statistic = pitch.bin_statistic(df_block.x, df_block.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0][1], cmap='hot', edgecolors='#22312b')
   bin_statistic = pitch.bin_statistic(df_interception.x, df_interception.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][1][0], cmap='hot', edgecolors='#22312b')
   bin_statistic = pitch.bin_statistic(df_ball_recovery.x, df_ball_recovery.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][1][1], cmap='hot', edgecolors='#22312b')
   ax_cbar = fig.add_axes((0.035, 0.15, 0.93, 0.03))
   cbar = plt.colorbar(pcm, orientation='horizontal', cax=ax_cbar)
   cbar.outline.set_edgecolor('#efefef')
   cbar.ax.yaxis.set_tick_params(color='#efefef')
   plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')
   for label in cbar.ax.get_yticklabels():
       label.set_fontproperties(robotto_regular.prop)
       label.set_fontsize(15)

# endnote and title
   
   ax_title = axs['title'].text(0.5, 1.5, f"{team} Defensive actions", color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=25)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color=text_color)
   axs['pitch'][0][0].set_title('Clearances',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][0][1].set_title('Blocks',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][0].set_title('Interceptions',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][1].set_title('Ball recovries',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   return st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)


def player(df):
   players=df.player_name.unique()
   selected_player=st.selectbox('PLAYER', players)
   player=selected_player
   mask=(df.player_name==player)
   df=df.loc[mask]
   passes=df[df.type_name=='Pass']
   carry=df[df.type_name=="Carry"]
   under_pressure=df[df.under_pressure.notnull()]
   counter_press=df[df.counterpress.notnull()]
   robotto_regular = FontManager()
   path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
            path_effects.Normal()]
   LINEWIDTH = 1  # starting linewidth
   DIFF_LINEWIDTH = 1.2  # amount the glow linewidth increases each loop
   NUM_GLOW_LINES = 10  # the amount of loops, if you increase the glow will be wider
   PASS_COLOR='w'
# in each loop, for the glow, we plot the alpha divided by the num_glow_lines
# I have a lower alpha_pass_line value as there is a slight overlap in
# the pass comet lines when using capstyle='round'
   ALPHA_PITCH_LINE = 0.3
   ALPHA_PASS_LINE = 0.15
   text_color='#F5F5DC'
   flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                  ['black','#394a13' ,'#a4e610','white'], N=100)
   LINE_COLOR =  'w'#"#0FF4FF" #'#BF7117'  #'#FE53BB' 
   back='none'#'#73737
   pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,line_zorder=2, linestyle='-',half=False)
   fig, axs= pitch.grid(ncols=2,nrows=2,grid_height=0.6, title_height=0.05,  axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0,grid_width=0.88,figheight= 10)
   fig.set_facecolor(back)
   pitch.lines(passes.x,passes.y,passes.end_x,passes.end_y,ax=axs['pitch'][0][0],capstyle='butt',  # cut-off the line at the end-location.
            linewidth=LINEWIDTH, color=PASS_COLOR)
   pitch.scatter(passes.x,passes.y, color="w",s=100,edgecolor="w",marker="o",alpha=.5,ax=axs['pitch'][0][0])
   pitch.scatter(carry.x,carry.y, color="w",s=70,edgecolor="w",marker="o",alpha=.5,ax=axs['pitch'][0][1])
   pitch.lines(carry.x,carry.y,carry.end_x,carry.end_y,ax=axs['pitch'][0][1],linewidth=0.9,color='Orange',comet=True)
   for i in range(1, NUM_GLOW_LINES + 1):
       pitch = Pitch(line_color=LINE_COLOR, pitch_color=back,half=False,
                  linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                  line_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_alpha=ALPHA_PITCH_LINE / NUM_GLOW_LINES,
                  goal_type='box')
    
   pitch.draw(ax=axs['pitch'][0][0])  # we plot on-top of our previous axis from pitch.grid
   pitch.lines(passes.x, passes.y,
                passes.end_x,passes.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='round',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color=PASS_COLOR, comet=True, ax=axs['pitch'][0][0])
   pitch.lines(carry.x,carry.y,carry.end_x,carry.end_y,
                linewidth=LINEWIDTH + (DIFF_LINEWIDTH * i),
                capstyle='projecting',  # capstyle round so the glow extends past the line
                alpha=ALPHA_PASS_LINE / NUM_GLOW_LINES,
                color='orange', comet=True, ax=axs['pitch'][0][1])
   bin_statistic = pitch.bin_statistic(under_pressure.x, under_pressure.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][1][0], cmap='hot', edgecolors='#22312b',label=f'{player} under pressure')
   bin_statistic = pitch.bin_statistic(counter_press.x, counter_press.y, statistic='count', bins=(25, 25))
   bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
   pc= pitch.heatmap(bin_statistic, ax=axs['pitch'][1][1], cmap='hot', edgecolors='#22312b')
   ax_cbar = fig.add_axes((0.035, 0.15, 0.93, 0.03))
   cbar = plt.colorbar(pcm, orientation='horizontal', cax=ax_cbar)
   cbar.outline.set_edgecolor('#efefef')
   cbar.ax.yaxis.set_tick_params(color='#efefef')
   plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')
   for label in cbar.ax.get_yticklabels():
       label.set_fontproperties(robotto_regular.prop)
       label.set_fontsize(15)

   
   ax_title = axs['title'].text(0.5, 1.5, f"{player} Performance", color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=25)
   axs['endnote'].text(1, 0.85, '@SoccerbyNumber6', va='center', ha='right', fontsize=10,
                    fontproperties=robotto_regular.prop, color=text_color)
   axs['pitch'][0][0].set_title('Passes',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][0][1].set_title('Carries',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][0].set_title('Under pressure',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   axs['pitch'][1][1].set_title('Counterpress',color=text_color,
                             va='center', ha='center', path_effects=path_eff,
                             fontproperties=robotto_regular.prop, fontsize=15)
   return  selected_player,st.pyplot(fig, dpi=100, facecolor= back ,bbox_inches=None)

   
   

   



   