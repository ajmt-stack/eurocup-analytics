df = pd.read_csv(r"C:\Users\Gene\OneDrive\Desktop\VS-Code Python\DataPractice\eurocup_box_score_clean.csv")

season = df.groupby('season_year').agg(
    threes_att =("three_points_attempted", "sum"),
    twos_att = ("two_points_attempted", "sum"),
    threes_made = ("three_points_made", "sum"),
    pts = ("points", "sum"),
    games = ("game_id", pd.Series.nunique),
).reset_index()

season["three_pt_rate"] = season.threes_att / (season.threes_att + season.twos_att) * 100
season["pts_per_game"] = season.pts / (season.games * 2)

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#0f1117"
FG = "#f5f5f5"
ACCENT1 = "#ff7a3d"
ACCENT2 = "#4ea8de"
GRID = "#2a2d38"
fig, ax1 = plt.subplots(figsize = (11, 6.5), dpi = 200)
fig.patch.set_facecolor(BG)
ax1.set_facecolor(BG)

ax1.plot(season.season_year, season.three_pt_rate, 
         color = ACCENT1, 
         linewidth = 2.8,
         marker = 'o',
         markersize = 5,
         zorder = 3,
         label = "3PT Attempt Rate")
ax1.fill_between(season.season_year, season.three_pt_rate, 
                 color = ACCENT1,
                 alpha = 0.08)
ax2 = ax1.twinx()
ax2.plot(season.season_year, season.pts_per_game, 
         color = ACCENT2, 
         linewidth = 2.2,
         linestyle="--",
         marker = 'D',
         markersize = 4,
         zorder = 3,
         label = "Points per Team per Game")

for ax in (ax1, ax2):
    ax.set_facecolor(BG)
    ax.tick_params(colors = FG, labelsize = 10)
    for spine in ax.spines.values():
        spine.set_visible(False)
    
ax.set_ylabel("Share of Shot Attempts That Are 3-Pointers", color = ACCENT1, fontsize = 11, labelpad = 10)
ax2.set_ylabel("Avg. Points per Team per Game", color = ACCENT2, fontsize = 11, labelpad = 10)
ax1.yaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))
ax1.tick_params(axis = "y", colors = ACCENT1)
ax2.tick_params(axis = "y", colors = ACCENT2)

ax1.set_ylim(0, 45)
ax2.set_ylim(60, 90)

ax1.set_xticks(season.season_year)
ax1.set_xticklabels(season.season_year, rotation = 45, ha = "right")
ax1.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
ax1.set_xlim(season.season_year.min() - 0.5, season.season_year.max() + 0.5)

fig.text(0.06, 0.96, "The Three-Point Revolution in EuroCup Basketball",
         fontsize=18, fontweight="bold", color=FG)
fig.text(0.06, 0.915, "Shot selection and scoring pace across 19 seasons (2007\u201325), from 89,300+ player box scores",
        fontsize=10.5, color="#a0a3ad")   

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=False, 
           fontsize=10, labelcolor=FG, bbox_to_anchor=(0.0, 1.0))

fig.text(0.06, 0.02, "Source: EuroCup box score data, 2007\u201308 \u2013 2024\u201325 seasons", 
         fontsize=8.5, color="#6b6e78")  

plt.tight_layout(rect=[0, 0.04, 1, 0.90])
      
