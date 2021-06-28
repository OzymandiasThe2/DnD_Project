from random import randint, choice


class Weapon:
    def __init__(self, weapon_type, modifier=None):
        self.weaponType = weapon_type
        self.modifier = modifier


# USER DEFINED WEAPONS

# def gun_attributes(primary_material=None, barrel=None, chamber_method=None, mechanism=None, trigger=None,
#                    ammunition=None, reload_methods=None, additional_traits=None, additional_grips=None,
#                    ammunition_materials=None, caliber=None):
#     attributes = {
#         primary_material: ["Oak Wood", "Stone", "Bronze Steel Alloy", "Aluminium Alloy", "Khezine", "Nitinol",
#                            "Gunmetal",
#                            "Ironwood", "Titanium", "Molybdenum Steel", "Stainless Steel", "Uranium"],
#         barrel: ["Short Barrel", "Wide Barrel", "Medium Barrel", "Long Barrel", "Spinning Barrel",
#                  "Sound Dampening Barrel", "Extra-fluted Barrel", "Heavy Barrel", "Handled Barrel", "Enhanced Barrel",
#                  "Sub-Barrel"],
#
#         chamber_method: ["Manual", "Generic Action", "Pump Action", "Lever Action", "Gravity Flick",
#                          "Bolt Action", "Semi Automatic"],
#
#         mechanism: ["Fuse", "Matchlock", "Flintlock", "Caplock", "Sparklock", "Chemlock", "Chemlock",
#                     "Firing Pin", "Gemlock"],
#
#         trigger: ["Press", "Lightning Press", "Enhancing Press", "Aim Press", "Hell-Fire Press Trigger",
#                   "Ready Press", "Reflex", "Gesture"],
#
#         ammunition: ["Musket Ball", "Generic Ammo", "Fuel Pods", "Shells", "Slug", "Bullet", "Propelled Rods",
#                      "Energy Cell"],
#
#         reload_methods: ["Non Repeating", "Internal Magazines", "Clip Loaded", "Ammunition Belt", "Magazines",
#                          "Back Mounted Ammuntion Feeder"],
#
#         additional_traits: ["Bulky", "Hazard", "Single Shot", "Sidearm", "Quickdraw", "Pentrating",
#                             "Short Range", "Compact", "Automatic", "Disguised", "Intimidating", "Ambush", "Plantable",
#                             "Hands Free", "Disposable", "Holding"],
#
#         additional_grips: ["Hallow Grip", "Lightning Foregrip", "Quickdraw Grip", "Aerial Grip"],
#
#         ammunition_materials: ["Lead", "Rubber Wax", "Copper", "Tungsten"],
#
#         caliber: ["d2", "d4", "d6", "d8", "d10", "d12"],
#     }
#     primary_material = choice(primary_material)
#     return (primary_material)

#
primary_material = ["Oak Wood", "Stone", "Bronze Steel Alloy", "Aluminium Alloy", "Khezine", "Nitinol", "Gunmetal",
                    "Ironwood", "Titanium", "Molybdenum Steel", "Stainless Steel", "Uranium"]

barrel = ["Short Barrel", "Wide Barrel", "Medium Barrel", "Long Barrel", "Spinning Barrel", "Sound Dampening Barrel",
          "Extrafluted Barrel", "Heavy Barrel", "Handled Barrel", "Enhanced Barrel", "Sub-Barrel"]

chamber_method = ["Manual", "Generic Action", "Pump Action", "Lever Action", "Gravity Flick", "Bolt Action",
                  "Semi Automatic"]

mechanism = ["Fuse", "Matchlock", "Flintlock", "Caplock", "Sparklock", "Chemlock", "Chemlock", "Firing Pin", "Gemlock"]

trigger = ["Press", "Lightning Press", "Enhancing Press", "Aim Press", "Hell-Fire Press Trigger", "Ready Press",
           "Reflex", "Gesture"]

ammunition = ["Musket Ball", "Generic Ammo", "Fuel Pods", "Shells", "Slug", "Bullet", "Propelled Rods", "Energy Cell"]

reload_method = ["Non Repeating", "Internal Magazines", "Clip Loaded", "Ammunition Belt", "Magazines",
                 "Back Mounted Ammuntion Feeder"]

additional_trait = ["Bulky", "Hazard", "Single Shot", "Sidearm", "Quickdraw", "Pentrating", "Short Range", "Compact",
                    "Automatic", "Disguised", "Intimidating", "Ambush", "Plantable", "Hands Free", "Disposable",
                    "Holding"]

additional_grip = ["Hallow Grip", "Lightning Foregrip", "Quickdraw Grip", "Aerial Grip"]

ammunition_material = ["Lead", "Rubber Wax", "Copper", "Tungsten"]

caliber = ["d2", "d4", "d6", "d8", "d10", "d12"]

# weapon_categories = ['Sword', 'Ranged', 'Hammer', 'Magic']


#
# def reloading():
#     reload = "proficiency bonus" + "point total"
#
#
# def properties():
#     properties = ""
#     if primary_material =
point_cost = {
    -1: ["Bulky", "Hazard", "Single Shot"],
    0: ["Oak Wood", "Short Barrel", "Manual", "Fuse", "Matchlock", "Flintlock" "Press", "Musket Ball",
        "Generic Ammo", "Non Repeating"],
    1: ["Stone", "Bronze Steel Alloy", "Wide Barrel", "Medium Barrel", "Generic Action", "Pump Action", "Caplock", "Lightning Press","Internal", "Enhancing", "Lead", "Rubber Wax"],
    2: ["Aluminium Alloy", "Khezine", "Nitinol", "Gunmetal", "Ironwood", "Long barrel", "Spinning", "Sound", "Extra-Fluted", "Heavy", "Handled", "Enhanced", "Lever Action", "Gravity Flick", "Bolt Action", "Sparklock", "Chemlock", "Firing pin", "Clip Loaded", "Sidearm", "Quickdraw", "Penetrating", "Aim Press", "Ready Press", "Fuel Pods", "Shells", "Hollow Grip", "Lighting Foregrip", "Copper"],
    3: ["Titanium", "Molybdenum Steel", "Stainless Steel", "Sub-barrel", "Gemlock", "Bullet", "Propelled Rods", "Ammunition Belt", "Magazines", "Hell-Fire Press Trigger", "Reflex", "Slug", "Short range", "Compact", "Automatic", "Quickdraw Grip", "Aerial Grip", "Tungsten"],
    4: ["Gesture", "Back Mounted Ammunition Feeder", "Disguised", "Intimidating", "Ambush", "d4"],
    5: ["Semi", "Plantable"],
    6: ["Hands Free", "Disposable", "Holding", "d6"],
    8: ["Uranium", "d8"],
    10: ["d10"],
    12: ["d12"]
}
primary_materials = choice(primary_material)
barrels = choice(barrel)
chamber_methods = choice(chamber_method)
mechanisms = choice(mechanism)
triggers = choice(trigger)
ammunitions = choice(ammunition)
reload_methods = choice(reload_method)
additional_traits = choice(additional_trait)
additional_grips = choice(additional_grip)
ammunition_materials = choice(ammunition_material)
calibers = choice(caliber)


# # FUNCTIONS
def generate_random_gun():
    gun = (
            "Primary Material: " + primary_materials +
            "\nBarrel: " + barrels +
            "\nChamber Method: " + chamber_methods +
            "\nMechanism: " + mechanisms +
            "\nTrigger: " + triggers +
            "\nAmmunition: " + ammunitions +
            "\nReload Method: " + reload_methods +
            "\nAdditional Trait: " + additional_traits +
            "\nAdditional Grip: " + additional_grips +
            "\nAmmunition Material: " + ammunition_materials +
            "\nCaliber: " + calibers
    )

    return gun


#
# def generate_random_weapon_modifier():
#     if (randint(0, 2) == 0): return None  # 50% chance of no modifier
#     if (randint(0, 99) == 0): return choice(magic_modifiers)  # 1/100 chance
#     return choice(basic_modifiers)

#

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None


print(generate_random_gun())
print(
    search(point_cost, primary_materials),
    search(point_cost, barrels),
    search(point_cost, mechanisms),
    search(point_cost, triggers),
    search(point_cost, ammunitions),
    search(point_cost, reload_methods),
    search(point_cost, additional_traits),
    search(point_cost, additional_grips),
    search(point_cost, ammunition_materials),
    search(point_cost, calibers),
)
