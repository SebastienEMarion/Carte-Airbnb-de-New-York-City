#================
# INCLUDES
#================
import matplotlib.pyplot as plt
import pandas as pd
import osmnx as ox
import geopandas as gpd
import time
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#================
# GLOBALS
#================
start = time.time()
city_name = "New York, New York, United States"

county_to_borough = {
    "Bronx County": "Bronx",
    "Kings County": "Brooklyn",
    "New York County": "Manhattan",
    "Queens County": "Queens",
    "Richmond County": "Staten Island"
}

borough_colors = {
    "Bronx": "#da70f5",          
    "Brooklyn": "#85cece",       
    "Manhattan": "#ddd579",      
    "Queens": "#47be47",         
    "Staten Island": "#4649f8"   
}

# Local CSV path
airbnb_csv_path = "listings.csv"

#================
# HELPERS
#================
def fetch_airbnb_from_csv(csv_path, filter_year=2025):
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Failed to load CSV: {e}")
        return gpd.GeoDataFrame(columns=['geometry'], geometry='geometry')

    df = df.dropna(subset=['latitude', 'longitude'])

    if 'last_review' in df.columns:
        df['last_review'] = df['last_review'].astype(str)
        df = df[df['last_review'].str[:4] == str(filter_year)]

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.longitude, df.latitude),
        crs="EPSG:4326"
    )
    return gdf

#================
# MAIN
#================
def main():
    # Fetch city boundary
    city = ox.geocode_to_gdf(city_name)

    # Fetch boroughs
    tags = {"admin_level": "6"}
    try:
        boroughs = ox.features_from_place(city_name, tags)
    except Exception as e:
        print(f"Failed to fetch boroughs: {e}")
        return

    boroughs = boroughs[boroughs.geometry.type.isin(["Polygon", "MultiPolygon"])]
    if "name" not in boroughs.columns:
        boroughs["name"] = "Unknown"
    boroughs["name"] = boroughs["name"].map(county_to_borough).fillna(boroughs["name"])

    print(f"Fetched NYC and boroughs in {time.time() - start:.2f} seconds")

    # Fetch waterways
    tags_water = {"natural": "water"}
    try:
        water = ox.features_from_place(city_name, tags_water)
        water = water[water.geometry.type.isin(["Polygon", "MultiPolygon"])]
    except Exception as e:
        print(f"Failed to fetch water features: {e}")
        water = gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    # Fetch Airbnb points
    airbnb_gdf = fetch_airbnb_from_csv(airbnb_csv_path, filter_year=2025)
    print(f"Fetched {len(airbnb_gdf)} Airbnb listings for 2025")

    # Plot base city
    ax = city.plot(facecolor="none", edgecolor="black", linewidth=3, figsize=(12, 12), zorder=5)

    # Plot waterways
    if not water.empty:
        water.plot(ax=ax, facecolor="#a6cee3", edgecolor="#1f78b4", alpha=0.6, zorder=6)

    # Plot boroughs
    for _, row in boroughs.iterrows():
        color = borough_colors.get(row["name"], "#ffffff")
        gpd.GeoSeries(row.geometry).plot(
            ax=ax,
            facecolor=color,
            edgecolor="red",
            linewidth=1.5,
            alpha=0.8,
            zorder=5
        )

    # Split Airbnb listings
    if not airbnb_gdf.empty and 'minimum_nights' in airbnb_gdf.columns:
        airbnb_gdf['minimum_nights'] = pd.to_numeric(
            airbnb_gdf['minimum_nights'], errors='coerce'
        ).fillna(0)

        short_term = airbnb_gdf[airbnb_gdf['minimum_nights'] < 30]
        long_term = airbnb_gdf[airbnb_gdf['minimum_nights'] >= 30]

        if not short_term.empty:
            short_term.plot(
                ax=ax, markersize=5, color="red", alpha=0.5,
                label="Airbnb court terme (<30 nuitées)", zorder=8
            )
        if not long_term.empty:
            long_term.plot(
                ax=ax, markersize=5, color="blue", alpha=0.5,
                label="Airbnb long terme (≥30 nuitées)", zorder=8
            )

    # Borough labels
    for _, row in boroughs.iterrows():
        if row.geometry.is_empty:
            continue
        if row["name"] in borough_colors:
            plt.text(
                row.geometry.centroid.x,
                row.geometry.centroid.y,
                row["name"],
                ha="center",
                fontsize=12,
                fontweight="bold",
                zorder=10
            )

    # Source dummy legend entry
    plt.scatter([], [], color="none", label="Source : Inside Airbnb (septembre 2025)")

    # Title & styling
    plt.title(
        "Offres Airbnb par durée du séjour à New York City (septembre 2025). MARION Sébastien, 3 janvier 2026.",
        fontsize=14, fontweight="bold"
    )
    plt.legend()
    plt.tight_layout()
    ax.set_axis_off()

    # =================
    # INSET: Airbnb count comparison
    # =================
    inset_ax = inset_axes(
        ax,
        width="28%", height="28%",
        loc="center left",
        borderpad=2
    )

    counts = [len(short_term), len(long_term)]

    inset_ax.bar(
        ["Court terme", "Long terme"],
        counts,
        color=["red", "blue"]
    )

    inset_ax.set_title(
        "Nombre d'offres Airbnb",
        fontsize=10,
        fontweight="bold"
    )

    # Opaque white background
    inset_ax.patch.set_facecolor("white")
    inset_ax.patch.set_alpha(1.0)
    inset_ax.set_zorder(20)

    # Subtle frame
    for spine in inset_ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(0.8)

    inset_ax.tick_params(axis='x', labelsize=9)
    inset_ax.tick_params(axis='y', labelsize=8)
    
    print(f"Script execution in {time.time() - start:.2f} seconds")
    plt.show()
# ===================
# Main entrypoint
# ===================
if __name__ == "__main__": #__name__ communique à l'interpréteur d'exécuter la main(),
    # Mais Python autorise d'autres paradigmes qu'une main(), programmation impérative structurée
    main()
