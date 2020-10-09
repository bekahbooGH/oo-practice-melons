############
# Part 1   #
############  


class MelonType(object):
    
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        

        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    Muskmelon.add_pairing('mint')

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('mint and strawberries')
    
    cren = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    Crenshaw.add_pairing('proscuitto')
    
    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    Yellow_Watermelon.add_pairing('ice-cream')
    
    all_melon_types = []

    all_melon_types.extend([Muskmelon, Casaba, Crenshaw, Yellow_Watermelon])

    
#     # Fill in the rest

    return all_melon_types

def print_pairing_info(all_melon_types):
#     """Prints information about each melon type's pairings."""
    for melon in all_melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print (f'- {pairing}')
        print()


    
    

def make_melon_type_lookup(all_melon_types):
    # """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_code_d={}
    for melon in all_melon_types:
        if melon.code is not in melon_code_d:
            melon_code_d[melon.code] = melon
    return melon_code_d

   

############
# Part 2   #
############
# categorized - sellable - if shape rating> 5  and color rating> 5 and  > 5 and harvest!= field 3 
#                          else non- sellable 





class Melon(object):
"""A melon in a melon harvest."""

    def __init__ (self, melon_type, shape_rating, color_rating, field, harvester):

        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating 
        self.field = field
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, field):
        if shape_rating > 5 and color_rating > 5 and field != 3:
            return True

        else:
            return False

def make_melons(self, melon_types):
    
    melons_by_id= make_melon_type_lookup(all_melon_types)
    objects_melon=[]


    melon_1= melon(melons_by_id [yw],8,7,2,'sheila')
    objects_melon.append(melon_1)

    melon_2 = melon(melons_by_id [yw], 3, 4, 2, 'sheila')
    objects_melon.append(melon_2)
    
    melon_3 = melon(melons_by_id [yw], 9, 8, 3, 'sheila')
    objects_melon.append(melon_3)
    
    melon_4 = melon(melons_by_id [cas], 10, 6, 35, 'sheila')
    objects_melon.append(melon_4)
    
    melon_5 = melon(melons_by_id [cren], 8, 9, 35, 'michael')
    objects_melon.append(melon_5)
    
    melon_6 = melon(melons_by_id [cren], 8, 2, 35, 'michael')
    objects_melon.append(melon_6)

    melon_7 = melon(melons_by_id [cren], 2, 3, 4, 'michael')
    objects_melon.append(melon_7)
    
    
    melon_8 = melon(melons_by_id [musk], 6, 7, 4, 'michael')
    objects_melon.append(melon_8)

    melon_9 = melon(melons_by_id [yw], 7, 10, 3, 'sheila')
    objects_melon.append(melon_9)
    

    return objects_melon    
#     # """Returns a list of Melon objects."""

#     # Fill in the rest

# def get_sellability_report(melons):
    # """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



