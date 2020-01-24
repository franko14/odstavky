import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px

odstavky_excel = pd.read_excel('odstavky_kapacit.xlsx', header=0)
#print (odstavky_excel)

#odstavky_excel = odstavky_excel.melt(id_vars=['Datum'], var_name='data')
odstavky_excel.set_index('Datum', inplace=True)
#odstavky_excel = odstavky_excel.sort_values(by=['data', 'Datum'])
#print (odstavky_excel)

#exit()
colors = {
            'CZ->DE-LU' : 'gold',
            'DE-LU->CZ' : '#ff5a00',
            'PL->CZ'    : 'red',
            'CZ->PL'    : 'indianred',
            'CZ->SK'    : 'limegreen',
            'CZ->AT'    : 'darkgreen',
            'AT->CZ'    : 'darkblue',
            'AT->HU'    : 'skyblue'
}

fig = go.Figure()
for color_no, ts in enumerate(odstavky_excel):
    #print(ts)
    #continueodstavky_excel.index
    fig.add_trace(go.Scatter(x=odstavky_excel.loc[pd.Timestamp('20200201'):pd.Timestamp('20200301')].index, y=odstavky_excel[ts].loc[pd.Timestamp('20200201'):pd.Timestamp('20200301')],
                            mode='lines',
                            line=dict(color=colors[ts]),
                            line_width=2,
                            name=ts,
                            )
                )
fig.update_layout(title={'text' : 'Odstávky prenosových kapacít',
                        #'y':0.9,
                        'x' : 0.5,
                        'xanchor' : 'center',
                        'font' :  dict(
                                    size=30,
                                    color="#000000"
                                )
                        },
                xaxis_tickformat = '%d.%m.',# %H:00<br>%Y',
                #xaxis_rangeslider_visible=True,
                xaxis = dict(
                            tickmode = 'auto',
                            ticklen = 30,
                            #dtick = 86400000.0,
                            tickfont =  dict(
                                        size=15,
                                        color="#000000"
                                    )
                        ),
                template = "plotly_white",
                legend_orientation = "h",
                #legend_title = "Linka",
                legend =  dict(y=-.1),
                height=600,
                width=1300
                )
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridwidth=0.5, gridcolor='gray', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridwidth=0.3, gridcolor='gray', mirror=True)
fig.show()
