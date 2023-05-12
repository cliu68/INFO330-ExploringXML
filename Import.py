import sqlite3
import sys
import xml.etree.ElementTree as ET


if len(sys.argv) < 2:
    print("You must pass at least one XML file name containing Pokemon to insert")

for i, arg in enumerate(sys.argv):
    # Skip if this is the Python filename (argv[0])
    if i == 0:
        continue

        import sqlite3
        import sys
        import xml.etree.ElementTree as ET
        import os

        if len(sys.argv) < 2:
            print("Usage: python Import.py <xml_file>")
            sys.exit(1)

        xml_file = sys.argv[1]
        if not os.path.isfile(xml_file):
            print(f"Error: {xml_file} is not a valid file")
            sys.exit(1)

        # check command-line arguments
        if len(sys.argv) != 2:
            print("Usage: python Import.py <xml_file>")
            sys.exit(1)

        # parse XML file
        tree = ET.parse(sys.argv[1])
        root = tree.getroot()

        # connect to SQLite database
        conn = sqlite3.connect('pokemon.sqlite')
        c = conn.cursor()

        # loop through each pokemon in the XML file
        for pokemon in root.findall('pokemon'):
            # get data from XML
            name = pokemon.find('name').text
            pokedexNumber = int(pokemon.get('pokedex'))
            type1 = pokemon.findall('type')[0].text
            type2 = pokemon.findall('type')[1].text
            hp = int(pokemon.find('hp').text)
            attack = int(pokemon.find('attack').text)
            defense = int(pokemon.find('defense').text)
            speed = int(pokemon.find('speed').text)
            sp_attack = int(pokemon.find('sp_attack').text)
            sp_defense = int(pokemon.find('sp_defense').text)
            height = float(pokemon.find('height/m').text)
            weight = float(pokemon.find('weight/kg').text)
            ability1_id = pokemon.findall('abilities/ability')[0].text
            ability2_id = pokemon.findall('abilities/ability')[1].text
            classification = pokemon.get('classification')

            # Check if pokemon already exists in database
            c.execute("SELECT * FROM pokemon WHERE name=? AND pokedexNumber=?", (name, pokedexNumber))
            if c.fetchone() is not None:
                print(f"{name} (#{pokedexNumber}) already exists in database")
                continue

            # Insert ability data into ability table
            c.execute("INSERT INTO ability (name) VALUES (?)", (ability1,))
            ability1_id = c.lastrowid
            c.execute("INSERT INTO ability (name) VALUES (?)", (ability2,))
            ability2_id = c.lastrowid

            # Insert pokemon data into pokemon table
            c.execute(
                "INSERT INTO pokemon (name, pokedexNumber, classification, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, height, weight, ability1_id, ability2_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name, pokedexNumber, classification, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense,
                 height, weight, ability1_id, ability2_id))
            print(f"{name} (#{pokedexNumber}) added to database")

        # Commit changes and close database connection
        conn.commit()
        conn.close()

        # Incoming Pokemon MUST be in this format
        #
        # <pokemon pokedex="" classification="" generation="">
        #     <name>...</name>
        #     <hp>...</name>
        #     <type>...</type>
        #     <type>...</type>
        #     <attack>...</attack>
        #     <defense>...</defense>
        #     <speed>...</speed>
        #     <sp_attack>...</sp_attack>
        #     <sp_defense>...</sp_defense>
        #     <height><m>...</m></height>
        #     <weight><kg>...</kg></weight>
        #     <abilities>
        #         <ability />
        #     </abilities>
        # </pokemon>

        # Read pokemon XML file name from command-line
        # (Currently this code does nothing; your job is to fix that!)
        if len(sys.argv) < 2:
            print("You must pass at least one XML file name containing Pokemon to insert")

        for i, arg in enumerate(sys.argv):
            # Skip if this is the Python filename (argv[0])
            if i == 0:
                continue



