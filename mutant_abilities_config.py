from collections import defaultdict

# Mutant Abilities
ABILITIES = [
    "Telepathy: Reading minds, mental communication.",
    "Telekinesis: Moving objects with the mind.",
    "Teleportation: Instantaneous travel from one place to another.",
    "Shape-shifting: Changing physical form.",
    "Elemental Control: Manipulating elements (fire, water, earth, air).",
    "Healing: Rapid recovery from injuries.",
    "Regeneration: Ability to regrow lost limbs or organs.",
    "Super Strength: Enhanced physical strength.",
    "Super Speed: Enhanced speed and reflexes.",
    "Flight: Ability to fly.",
    "Invisibility: Becoming unseen.",
    "Energy Manipulation: Creating, absorbing, and controlling energy.",
    "Weather Control: Manipulating weather patterns.",
    "Time Manipulation: Altering the flow of time.",
    "Precognition: Seeing the future.",
    "Retrocognition: Seeing past events.",
    "Illusions: Creating false perceptions.",
    "Phasing: Passing through solid matter.",
    "Force Fields: Creating protective barriers.",
    "Mind Control: Influencing others' actions and thoughts.",
    "Animal Communication: Talking to and controlling animals.",
    "Plant Manipulation: Controlling plant life.",
    "Size Alteration: Changing physical size.",
    "Duplication: Creating copies of oneself.",
    "Sound Manipulation: Controlling and creating sound.",
    "Density Control: Altering one's density.",
    "Intangibility: Becoming non-solid, ghost-like.",
    "Gravity Control: Manipulating gravitational forces.",
    "Magnetism: Controlling magnetic fields.",
    "Technopathy: Controlling and communicating with machines.",
    "Molecular Manipulation: Changing the molecular structure of objects.",
    "Enhanced Senses: Heightened sensory perception.",
    "Power Absorption: Absorbing and using others' powers.",
    "Power Mimicry: Copying others' powers.",
    "Power Negation: Cancelling out others' powers.",
    "Energy Projection: Emitting energy blasts.",
    "Pyrokinesis: Controlling and creating fire.",
    "Cryokinesis: Controlling and creating ice.",
    "Electrokinesis: Controlling and creating electricity.",
    "Hydrokinesis: Controlling and creating water.",
    "Geokinesis: Controlling and manipulating earth/rock.",
    "Aerokinesis: Controlling and creating air/wind.",
    "Biokinesis: Altering living organisms' biology.",
    "Toxikinesis: Creating and controlling toxins and poisons.",
    "Blood Manipulation: Controlling and using blood.",
    "Bone Manipulation: Controlling and using bones.",
    "Light Manipulation: Controlling and creating light.",
    "Shadow Manipulation: Controlling and creating shadows.",
    "Darkness Manipulation: Controlling and creating darkness.",
    "Solar Manipulation: Controlling and using solar energy.",
    "Lunar Manipulation: Controlling and using lunar energy.",
    "Plasma Manipulation: Controlling and creating plasma.",
    "Radiation Manipulation: Controlling and creating radiation.",
    "Elasticity: Stretching and reshaping the body.",
    "Seismic Manipulation: Creating and controlling earthquakes.",
    "Psionic Constructs: Creating physical objects with the mind.",
    "Telempathy: Sensing and manipulating emotions.",
    "Umbrakinesis: Controlling and creating shadows.",
    "Photokinesis: Controlling and creating light.",
    "Vitakinesis: Healing and altering life force.",
    "Atmospheric Manipulation: Controlling the atmosphere.",
    "Temperature Manipulation: Controlling and altering temperature.",
    "Pressure Manipulation: Controlling pressure in the environment.",
    "Psionic Energy: Using psionic energy for various effects.",
    "Chlorokinesis: Controlling plant life.",
    "Ecokinesis: Controlling the ecosystem.",
    "Spatial Manipulation: Altering space and dimensions.",
    "Dimensional Travel: Moving between dimensions.",
    "Reality Warping: Altering reality.",
    "Dream Manipulation: Controlling and entering dreams.",
    "Memory Manipulation: Altering and erasing memories.",
    "Sonic Scream: Emitting powerful sonic waves.",
    "Acid Generation: Creating and controlling acid.",
    "Explosion Manipulation: Creating and controlling explosions.",
    "Adoptive Muscle Memory: Learning physical tasks instantly.",
    "Omnilingualism: Understanding all languages.",
    "Enhanced Intellect: Superhuman intelligence.",
    "Enhanced Agility: Superhuman agility and reflexes.",
    "Tactile Telekinesis: Moving objects through touch.",
    "Omniscience: Knowing everything.",
    "Omnipresence: Being present everywhere simultaneously.",
    "Omnipotence: Unlimited power.",
    "Matter Ingestion: Consuming any form of matter.",
    "Substance Mimicry: Turning into any material.",
    "Vibration Manipulation: Controlling vibrations.",
    "Frequency Manipulation: Controlling frequencies of sound, light, etc.",
    "Fire Resistance: Immunity to fire.",
    "Ice Resistance: Immunity to cold and ice.",
    "Electric Resistance: Immunity to electricity.",
    "Poison Resistance: Immunity to toxins and poisons.",
    "Bulletproof: Impervious to bullets.",
    "Invulnerability: Complete resistance to physical harm.",
    "Enhanced Durability: Increased physical resilience.",
    "Emotion Control: Influencing and controlling emotions.",
    "Magic: Using magical spells and abilities.",
    "Alchemy: Transmuting matter.",
    "Cyberpathy: Controlling and communicating with computers.",
    "Summoning: Calling forth beings or objects.",
    "Animal Transformation: Changing into animals.",
    "Time Travel: Moving through time."
]

# Ability Weights
WEIGHTS_DICT = defaultdict(lambda: 5)  # Default weight is 5 (uncommon)

COMMON_ABILITIES = [
    "Super Strength: Enhanced physical strength.",
    "Super Speed: Enhanced speed and reflexes.",
    "Flight: Ability to fly.",
    "Invisibility: Becoming unseen.",
    "Healing: Rapid recovery from injuries.",
    "Regeneration: Ability to regrow lost limbs or organs.",
    "Enhanced Senses: Heightened sensory perception.",
    "Fire Resistance: Immunity to fire.",
    "Ice Resistance: Immunity to cold and ice.",
    "Electric Resistance: Immunity to electricity.",
    "Poison Resistance: Immunity to toxins and poisons.",
    "Bulletproof: Impervious to bullets.",
    "Enhanced Durability: Increased physical resilience."
]

RARE_ABILITIES = [
    "Teleportation: Instantaneous travel from one place to another.",
    "Force Fields: Creating protective barriers.",
    "Mind Control: Influencing others' actions and thoughts.",
    "Phasing: Passing through solid matter.",
    "Power Absorption: Absorbing and using others' powers.",
    "Power Mimicry: Copying others' powers.",
    "Power Negation: Cancelling out others' powers.",
    "Pyrokinesis: Controlling and creating fire.",
    "Electrokinesis: Controlling and creating electricity.",
    "Molecular Manipulation: Changing the molecular structure of objects.",
    "Reality Warping: Altering reality.",
    "Time Manipulation: Altering the flow of time.",
    "Dimensional Travel: Moving between dimensions."
]

OMEGA_ABILITIES = [
    "Telepathy: Reading minds, mental communication.",
    "Weather Control: Manipulating weather patterns.",
    "Reality Warping: Altering reality.",
    "Time Travel: Moving through time.",
    "Omniscience: Knowing everything.",
    "Omnipresence: Being present everywhere simultaneously.",
    "Omnipotence: Unlimited power."
]

for power in COMMON_ABILITIES:
    WEIGHTS_DICT[power] = 10

for power in RARE_ABILITIES:
    WEIGHTS_DICT[power] = 2

for power in OMEGA_ABILITIES:
    WEIGHTS_DICT[power] = 1

WEIGHTS = [WEIGHTS_DICT[power] for power in ABILITIES]