# GR_Guide

A guide to Grand Rapids from Joe

This project organizes recommendations for restaurants, bars, breweries, and attractions in Grand Rapids. Each location is categorized and includes notes, address, and whether food is available.

## todo: 
- [] The json files can contain scheduling things like "trivia on tuesdays" - lets get those worked in. 
- [] Assemble evening event calendar based on whats going on around town. 
- [] Add distinct recommendation for each place.

## Categories

- **Restaurant**: Sit-down and casual dining spots. No fast food, and no blind recommendations. 
- **Bar**: Bars and pubs, some with food options.
- **Brewery**: Local breweries of BEER CITY.
- **Attraction**: Notable places to visit.

---

## Places

| Name                  | Category    | Description                                                                                                   | Address                                 | Food? |
|-----------------------|-------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------|:-----:|
| Monarch's Corner Bar  | Bar         | A great bar to shoot pool at or sit at the bar and chat - but the tables are uncomfortable                    | 646 Stocking Ave NW, Grand Rapids, MI   | Yes   |
| The Pyramid Scheme    | Bar         | A live music venue and bar with several pinball machines. Variety of events and concerts.                     | 68 Commerce Ave SW, Grand Rapids, MI    | No    |
| House Rules           | Bar         | Relaxed atmosphere, board games, trivia nights, good beers and cocktails. Park across the street is a bit sketchy, but not dangerous. | 404 Ionia Ave SW, Grand Rapids, MI      | Yes   |
| One Bourbon           | Bar         | Great selection of bourbons and whiskeys. Affordable for the quality.                                         | 608 Bridge St NW, Grand Rapids, MI      | Yes   |
| Butcher's Union       | Restaurant  | Steakhouse and bar known for meat dishes and extensive drink menu. Upscale and a bit pricey, but worth it.    | 438 Bridge St NW, Grand Rapids, MI      | No    |
| Atwater Brewing       | Restaurant  | Detroit-based brewery with a full kitchen, pub fare, craft beers, river views, lively atmosphere.             | 201 Michigan St NW, Grand Rapids, MI    | Yes   |
| Frederik Meijer Gardens | Attraction | Beautiful gardens and sculptures. Summer concerts in the amphitheater. Tuesdays evenings are free.            | 1000 East Beltline Ave NE, Grand Rapids | No    |
| John Ball Zoo         | Attraction  | Great zoo with a variety of animals. Check out the porcupine!                                                 | 1300 West Fulton St, Grand Rapids, MI   | No    |
| Grand Rapids Art Museum | Attraction | Modern art museum with a variety of exhibits. Great for an afternoon.                                         | 101 Monroe Center St NW, Grand Rapids, MI | No  |

*...and more! See the map for the full list.*

---

## How to Use

- Open `index.html` in your browser to view the interactive map and filter locations by category.
- Use the checkboxes above the map to show/hide categories.
- Click on map markers for more details about each place.

---

## Data Structure

- All locations are organized in `categories/` as separate JSON files per category.
- A combined `places.json` is generated for the map.

---

## Contributing

Feel free to suggest new places or improvements by submitting a pull request!
