from inventory import Inventory
from guitar import Guitar 
from Enum_types import type_, builder, wood  
from guitar_spec import GuitarSpec

if __name__ == '__main__':
    inventory = Inventory()

    def initialize_inventory(inventory):
        inventory.add_guitar("11277", 3999.95, builder.Builder.COLLINGS.value, "CJ", type_.Type.ACOUSTIC.value, wood.Wood.INDIAN_ROSEWOOD.value, wood.Wood.STIKA.value)
        inventory.add_guitar("V95693", 1499.95, builder.Builder.FENDER.value, "Stratocastor", type_.Type.ELECTRIC.value, wood.Wood.ALDER.value, wood.Wood.ALDER.value)
        inventory.add_guitar("V9512", 1549.95, builder.Builder.FENDER.value, "Stratocastor", type_.Type.ELECTRIC.value, wood.Wood.ALDER.value, wood.Wood.ALDER.value)
        inventory.add_guitar("122784", 5495.95, builder.Builder.MARTIN.value, "D-18", type_.Type.ACOUSTIC.value, wood.Wood.MAHOGANY.value, wood.Wood.ADIRONDACK.value)
        inventory.add_guitar("76531", 6295.95, builder.Builder.MARTIN.value, "OM-28", type_.Type.ACOUSTIC.value, wood.Wood.BRAZILIAN_ROSEWOOD.value, wood.Wood.ADIRONDACK.value)
        inventory.add_guitar("70108276", 2295.95, builder.Builder.GIBSON.value, "Les Paul", type_.Type.ELECTRIC.value, wood.Wood.MAHOGANY.value, wood.Wood.MAHOGANY.value)
        inventory.add_guitar("82765501", 1890.95, builder.Builder.GIBSON.value, "SG '61 Reissue", type_.Type.ELECTRIC.value, wood.Wood.MAHOGANY.value, wood.Wood.MAHOGANY.value)
        inventory.add_guitar("77023", 6275.95, builder.Builder.MARTIN.value, "D-28", type_.Type.ACOUSTIC.value, wood.Wood.BRAZILIAN_ROSEWOOD.value, wood.Wood.ADIRONDACK.value)
        inventory.add_guitar("1092", 12995.95, builder.Builder.OLSON.value, "SJ", type_.Type.ACOUSTIC.value, wood.Wood.INDIAN_ROSEWOOD.value, wood.Wood.CEDAR.value)
        inventory.add_guitar("566-62", 8999.95, builder.Builder.RYAN.value, "Cathedral", type_.Type.ACOUSTIC.value, wood.Wood.COCOBOLO.value, wood.Wood.CEDAR.value)
        inventory.add_guitar("6 29584", 2100.95, builder.Builder.PRS.value, "Dave Navarro Signature", type_.Type.ELECTRIC.value, wood.Wood.MAHOGANY.value, wood.Wood.MAPLE.value)

    initialize_inventory(inventory)
    what_Erin_likes = GuitarSpec(builder.Builder.FENDER.value, "Stratocastor", type_.Type.ELECTRIC.value, wood.Wood.ALDER.value, wood.Wood.ALDER.value)
    matching_guitars = inventory.search(what_Erin_likes)

    if matching_guitars != []:
        print('Erin, You might like these guitars:')

        for guitar in matching_guitars:
            guitar_spec = guitar.get_spec()
            status = (f' We have a {guitar_spec.get_builder()} {guitar_spec.get_model()} {guitar_spec.get_type()} guitar:\n'
            f'  {guitar_spec.get_back_wood()} back and sides,\n'
            f'  {guitar_spec.get_top_wood()} top.\n'
            f' You can have it for only ${guitar.price}!')

            print(f'{status}\n ------')
    else:
        print('Sorry, Erin, we have nothing for you.')
    
