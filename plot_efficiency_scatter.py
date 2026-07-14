df = pd.read_csv(r"C:\Users\Gene\OneDrive\Desktop\VS-Code Python\DataPractice\eurocup_box_score_clean.csv")

SEASON = 2025
s = df[df.season_year == SEASON]

player = s.groupby(["player_id", "player", "team_id"]).agg(
    games=("game_id", "nunique"),          
    points=("points", "sum"),
    fga=("field_goals_attempted", "sum"),   
    fta=("free_throws_attempted", "sum"),
    minutes=("minutes_played", "sum"),
).reset_index()

player["mpg"] = player.minutes / player.games   
player = player[(player.games >= 10) & (player.mpg >= 10)]
player["ppg"] = player.points / player.games
player["ts_pct"] = player.points / (2 * (player.fga + 0.44 * player.fta)) * 100

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#0f1117"
FG = "#f5f5f5"
GRID = "#2a2d38"
ACCENT = "#4ea8de"      
HIGHLIGHT = "#ff7a3d" 

fig, ax = plt.subplots(figsize=(11, 7.5), dpi=200)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

scatter = ax.scatter(
    player.ts_pct, player.ppg,
    s=player.mpg * 8,              
    c=player.mpg,                   
    cmap="Blues",
    alpha=0.75,
    edgecolors=BG, linewidths=0.6,  
    zorder=3,
)

ax.axvline(player.ts_pct.median(), color=GRID, linewidth=1, linestyle="--", zorder=1)
ax.axhline(player.ppg.median(), color=GRID, linewidth=1, linestyle="--", zorder=1)

top = player.sort_values("ppg", ascending=False).head(8)
for i, (_, row) in enumerate(top.iterrows()):
    y_offset = 10 if i % 2 == 0 else -14
    ax.annotate(
        row.player.split(",")[0],   
        (row.ts_pct, row.ppg),
        xytext=(6, y_offset), textcoords="offset points",
        fontsize=9, color=FG, fontweight="bold",
        zorder=4,
    )

ax.set_facecolor(BG)
ax.tick_params(colors=FG, labelsize=10)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlabel("True Shooting % (scoring efficiency)", color=FG, fontsize=11, labelpad=10)
ax.set_ylabel("Points per Game (scoring volume)", color=FG, fontsize=11, labelpad=10)
ax.xaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))
ax.grid(color=GRID, linewidth=0.7, zorder=0)

cbar = fig.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label("Minutes per Game", color=FG, fontsize=10)
cbar.ax.tick_params(colors=FG, labelsize=9)
cbar.outline.set_visible(False)

fig.text(0.06, 0.96, "Scoring Volume vs. Efficiency — EuroCup 2024–25",
          fontsize=18, fontweight="bold", color=FG)
fig.text(0.06, 0.925,
          f"Players with 10+ games and 10+ minutes/game (n={len(player)}). Bubble size = minutes per game.",
          fontsize=10.5, color="#a0a3ad")

fig.text(0.06, 0.02, "Source: EuroCup box score data, 2024–25 season", fontsize=8.5, color="#6b6e78")

plt.tight_layout(rect=[0, 0.04, 1, 0.90])
print(f"Players plotted: {len(player)}")
