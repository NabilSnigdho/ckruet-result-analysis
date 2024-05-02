import pandas as pd
import matplotlib.pyplot as plt

for series, date, r in [
    (20, "2022-3-2", ""),
    (21, "2022-10-26", ", Merit: 1-3899"),
    (22, "2023-9-26", ""),
    (23, "2024-4-30", ", Merit: 1-3500"),
]:
    df = pd.read_csv(f"{series}-series-{date}.csv", converters={"Merit": int})
    df.sort_values(by="Dept.-Univ.", inplace=True)

    print(f"{series} series", df.value_counts(["Dept.-Univ."]))

    departments = df["Dept.-Univ."].unique()

    df[["Merit", "Dept.-Univ."]].plot(
        kind="scatter",
        title=f"Result of {series} series{r} (last updated: {date})",
        x="Merit",
        y="Dept.-Univ.",
        c="#FF000033" if r else "#00000033",
        marker="|",
        edgecolors=None,
        zorder=3,
    )
    plt.xlim(0, 6000)
    plt.yticks(departments, fontsize="xx-small")
    plt.subplots_adjust(left=0.15)
    plt.grid(axis="y", zorder=0)

    plt.savefig(f"{series}-series-{date}.png", dpi=96 * 8)
