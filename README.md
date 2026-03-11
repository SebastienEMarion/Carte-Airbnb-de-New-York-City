# Carte Airbnb de New-York-City
Carte Airbnb de New York City, source : Inside Airbnb [4], septembre 2025. L'intérêt d'une telle carte est de voir le potentiel impact des politiques voulues par le nouveau maire de la ville de New York, Zhoran Mamdani. Cependant, une loi déjà en place allait dans ce sens : la Local Law 18 de 2022. </br >
Réalisée en programmation Python, partiellement à l'aide d'**intelligence artificielle**, et des bibliothèques Python suivantes : **matplotlib.pyplot** (pour l'interface graphique), **pandas** (pour la manipulation d'images), **osmnx** (pour l'accès à l'API d'Open Street Maps _Nominatim_), **geopandas** (pour la manipulation de géocoordonnées), **time** (pour calculer l'exécution d'un programme à des fins d'optimisation), **mpl_toolkits** (pour l'insertion du graphique de visualisation statistique). 

<img width="1920" height="967" alt="NYC séjours Airbnb de septembre 2025" src="https://github.com/user-attachments/assets/21c80c40-fdce-40a0-882d-d47ee7ad433b" />

# Procédé du script Python

# Intérêt de la carte

La cartographie des locations Airbnb selon la durée minimum en terme de nuitées de la ville de New-York est intéressante car le sujet fait l'objet d'une législation ayant désormais plusieurs décennies. On peut à cet égard penser à la Local Law 18 de 2022, qui est complexe : c'est à la fois l'enregistrement des locations à court terme par les particuliers [1] "*§ 26-3102 Enregistrement des locations à court terme. a. Ce sera illégal pour une personne qui possède, gère, occupe ou autrement contrôle une unité de logement d'offrir, de gérer ou d'administrer la location à court terme de ladite unité de logement avant que cette dernière ne soit enregistrée en accord avec ce chapitre, qu'une telle unité de logement n'aie reçu un numéro unique d'enregistrement de location à court terme, et que cet enregistrement soit actuellement valide.* [...]" et par les entreprises de réservation [1] "*Ce sera illégal pour un service de réservation de charger, collecter ou recevoir des frais d'une personne en relation à la location à court terme d'une unité de logement ou d'un hébergement résidentiel avant qu'un tel service de réservation n'aie utilisé le service électronique de vérification maintenu par l'agence administrative.*" qui est visé par cette dernière.

</br >
C'est aussi un des enjeux politiques de Zohran Mamdani, nouveau maire de New-York-City qui attire le regard de nombreux observateurs étrangers. Dans un article traitant de l'industrie locative, on peut lire [2] "Airbnb a dépensé 5 millions de dollars pour influencer les élections de 2025 à New York, pourtant l’un des candidats qu’elle a essayé de bloquer, Zohran Mamdani, vient tout juste de remporter la primaire démocrate pour la mairie. Âgé de 33 ans, ce socialiste démocrate et critique affiché des locations de courte durée n’est pas encore maire — il doit encore affronter l’élection générale de novembre — mais sa victoire surprise sur l’ancien gouverneur Andrew Cuomo annonce de potentielles turbulences pour Airbnb et l’industrie STR [short-term rentals] au sens large."

</br >
La répartition par points des nuitées à long terme en bleu, celles légales, domine celle en rouge, à court terme. Cela rend difficile la lecture des points rouges, et la comparaison absolue entre les deux. Là où on pourrait croire à une domination absolue des locations à long terme, le graphique montre cependant une répartition environnant le 40% court terme, 60% long terme. On remarque également une inégale répartition des locations sur la ville de New-York-City, qui se divise en cinq _boroughs_ ou arrondissements : Brooklyn, Queens, Manhattan, Bronx, Staten Island. Vers Manhattan, le *Central Business District* (CBD) centralise la population, les services publics ou même l'activité de bureau, on peut y voir un hypercentre et le sud de Queens, de Staten Island ainsi que l'est de Bronx semblent moins attirer. On peut aussi y voir une métropolisation et ses alentours en recomposition. La présence de locations Airbnb est à replacer dans un contexte de stagflation possible. L'offre en logement par les entreprises pour la location se confronte aux besoins des classes laborieuses en logement. D'après un article de 2025 par Kiplinger, éditeur américain de finance [3] : "_Aucun endroit ne bat le centre de_ Big Apple _quand il s'agit d'être le marché de logement le plus cher des États-Unis. Avec l'espace un luxe et la location dominante, le prix moyen d'un logement à Manhattan est de 3 205 267 $, ou 4,7 fois plus que la moyenne nationale. Et même, le prix du logement moyen qu'on trouve à Manhattan est trois fois celui de Bethesda_ [quinzième du classement] *, et 55% plus que ce que San Jose a à offrir. Les paiements mensuels du prêt hypothécaire et des taux d'intérêts sur les* [mortgages] *sont à 14 401 $, ce qui surpasse toute autre ville dans les États-Unis (San Jose arrive en second avec 9 662 $, tandis que la moyenne nationale est à 2 512 $. Le loyer moyen à Manhattan est à 5 654 $ par mois, ce qui est aussi sans équivoque le plus haut de toute ville étasunienne. En conclusion ? Les habitants de Manhattan paient presque cinq fois la moyenne nationale pour le logement.*

# Bibliographie :
[1] "Registration Rules and Laws",</br >
*Int. No. 2309-A*, 13 mars 2021 à 11 h 07, Council Members Kallos, Rivera, Rosenthal, Reynoso, Gibson, Powers, Ayala, Brannan, Gennaro, Moya, Adams, Dromm, Levine, Salamanca, Holden, Dinowitz, Treyger, Koslowitz, Riley and Feliz</br >
_Office of Special Enforcement_</br >
(https://www.nyc.gov/site/specialenforcement/registration-law/registration-rules-and-laws.page)

[2] "La campagne politique d’Airbnb à New York se retourne contre elle alors que Zohran Mamdani progresse",
novembre 24 2025, Uvika Wahi,</br >
*RentalScaleup.com*</br >
(https://www.rentalscaleup.com/fr/la-campagne-politique-dairbnb-a-new-york-se-retourne-contre-elle-alors-que-zohran-mamdani-progresse/)

[3] "The 15 Most Expensive Housing Markets in the US: Real Estate with the Highest Average Home Prices",</br >
dernière mise à jour le 19 août 2025, Dan Burrows,</br >
_Kiplinger.com_</br >
(https://www.kiplinger.com/real-estate/603612/15-us-cities-with-the-highest-average-home-prices)

[4] "Get the Data",</br >
_New York City, New York, United States_, 01 October, 2025
 </br >
_Inside Airbnb_,</br >
(https://insideairbnb.com/get-the-data/)
