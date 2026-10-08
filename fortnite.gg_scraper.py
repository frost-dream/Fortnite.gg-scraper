import requests

dict_of_skin_names = {"Rapscallion": "https://fortnite.gg/cosmetics?id=792",
                      "Scoundrel": "https://fortnite.gg/cosmetics?id=793",
                      "Absolute Zero": "https://fortnite.gg/cosmetics?id=891",
                      "Arctic Assassin": "https://fortnite.gg/cosmetics?id=890",
                      "Metal Mouth": "https://fortnite.gg/cosmetics?id=323",
                      "Zadie": "https://fortnite.gg/cosmetics?id=324",
                      "Velocity": "https://fortnite.gg/cosmetics?id=531",
                      "Raptor": "https://fortnite.gg/cosmetics?id=896",
                      "Raven": "https://fortnite.gg/cosmetics?id=825",
                      "Ravage": "https://fortnite.gg/cosmetics?id=734",
                      "Skull Trooper": "https://fortnite.gg/cosmetics?id=897",
                      "Skull Ranger": "https://fortnite.gg/cosmetics?id=683",
                      "Oro": "https://fortnite.gg/cosmetics?id=277",
                      "Orelia": "https://fortnite.gg/cosmetics?id=4750",
                      "Cozy Chomps": "https://fortnite.gg/cosmetics?id=169",
                      "Comfy Chomps": "https://fortnite.gg/cosmetics?id=168",
                      "Batman Zero": "https://fortnite.gg/cosmetics?id=4707",
                      "Catwoman Zero": "https://fortnite.gg/cosmetics?id=4760",
                      "Batman Comic Book Outfit": "https://fortnite.gg/cosmetics?id=417",
                      "Catwoman Comic Book Outfit": "https://fortnite.gg/cosmetics?id=415",
                      "Beach Bod Batman": "https://fortnite.gg/cosmetics?id=23737",
                      "Coastal Catwoman": "https://fortnite.gg/cosmetics?id=23743",
                      "The Joker": "https://fortnite.gg/cosmetics?id=48",
                      "Harley Quinn": "https://fortnite.gg/cosmetics?id=250",
                      "Mr. Incredible": "https://fortnite.gg/cosmetics?id=14952",
                      "Mrs. Incredible": "https://fortnite.gg/cosmetics?id=14955",
                      "Spider-Man (Miles Morales)": "https://fortnite.gg/cosmetics?id=9656",
                      "Lois Griffin": "https://fortnite.gg/cosmetics?id=22888",
                      "Hinata Hyuga": "https://fortnite.gg/cosmetics?id=8021",
                      "Naruto Uzumaki": "https://fortnite.gg/cosmetics?id=5858",
                      "Mikasa Ackermann": "https://fortnite.gg/cosmetics?id=9434",
                      "Ryu": "https://fortnite.gg/cosmetics?id=4399",
                      "Chun-Li": "https://fortnite.gg/cosmetics?id=4400",
                      "Chun-Li (Street Fighter 2026)": "https://fortnite.gg/cosmetics?id=24799",
                      "Ryu (Street Fighter 2026)": "https://fortnite.gg/cosmetics?id=24798",
                      }

for skin, url in dict_of_skin_names.items():
    response = requests.get(url)
    if response.status_code == 200:
        if b" (today)<" in response.content:
            print(f"{skin} is available today.")
    else:
        print(f"Failed to fetch data for {skin}. Status code: {response.status_code}")

print("Finished checking skin availability.")