
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.style as style

# Color blind proof RGB colors
colors = [
            [0, 0, 0],
            [230, 159, 0],
            [86, 180, 233],
            [0, 158, 115],
            [213, 94, 0],
            [0, 114, 178]
        ]

# Changes RGB value to range from 0 to 1
colors = list(map(lambda i: list(map(lambda j: j / 255, i)), colors))

# Gets the study data
link = 'http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv'
women_majors = pd.read_csv(link)

# Extracts majors that less than 20% of bachelors were women in 1970
under_20 = women_majors.loc[0, women_majors.loc[0] < 20]

# Sets the 538 default matplotlib theme
style.use('fivethirtyeight')

# Plots graph
under_20_graph = women_majors.plot(x='Year', y=under_20.index, figsize=(12, 8), color=colors, legend=False)

# Various graph styling configurations
under_20_graph.tick_params(axis='both', which='major', labelsize=18)
under_20_graph.set_yticklabels(labels=[-10, '0   ', '10   ', '20   ', '30   ', '40   ', '50%'])
under_20_graph.axhline(y=0, color='black', linewidth=1.3, alpha=.7)
under_20_graph.set_xlim(left=1969, right=2011)
under_20_graph.xaxis.label.set_visible(False)

# Sets graph title and subtitle
under_20_graph.text(x=1966.65, y=57.7, s='The gender gap is transitory - even for extreme cases', fontsize=26, weight='bold', alpha=.75)
under_20_graph.text(x=1966.65, y=52, s='Percentage of Bachelors conferred to women from 1970 to 2011 in the US for\nextreme cases where the percentage was less than 20% in 1970', fontsize=19, alpha=.85)

# Sets graph labels
under_20_graph.text(x=1994, y=44, s='Agriculture', color=colors[0], weight='bold', rotation=33, backgroundcolor='#f0f0f0')
under_20_graph.text(x=1985, y=42.2, s='Architecture', color=colors[1], weight='bold', rotation=18, backgroundcolor='#f0f0f0')
under_20_graph.text(x=2004, y=51, s='Business', color=colors[2], weight='bold', rotation=-7,   backgroundcolor='#f0f0f0')
under_20_graph.text(x=2001, y=30, s='Computer Science', color=colors[3], weight='bold', rotation=-42.5, backgroundcolor='#f0f0f0')
under_20_graph.text(x=1987, y=11.5, s='Engineering', color=colors[4], weight='bold', backgroundcolor='#f0f0f0')
under_20_graph.text(x=1976, y=25, s='Physical Sciences', color=colors[5], weight='bold', rotation=27, backgroundcolor='#f0f0f0')

# Displays the graph
plot.show()
