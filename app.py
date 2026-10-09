from doctors_data import doctors
from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(
    page_title="Pet Care Assistant",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PET CARE ASSISTANT")
st.write("Choose a pet and explore information about different breeds and types.")

# --------------------------------------------------
# PET DATA
# --------------------------------------------------

pet_breeds = {

    "Dog": [
        "Labrador Retriever",
        "Golden Retriever",
        "German Shepherd",
        "Pug",
        "Beagle",
        "Rottweiler",
        "Pomeranian",
        "Shih Tzu",
        "Husky",
        "Bulldog",
        "Dachshund"
    ],

    "Cat": [
        "Persian",
        "Siamese",
        "Maine Coon",
        "British Shorthair",
        "Bengal",
        "Ragdoll",
        "Indian Shorthair",
        "Sphynx",
        "Turkish Angora",
        "Abyssinian",
        "Scottish Fold"
    ],

    "Bird": [
        "Parrot",
        "Budgerigar (Budgie)",
        "Cockatiel",
        "Lovebird",
        "Finch",
        "Canary",
        "Macaw",
        "Pigeon",
        "Rainbow Lorikeet",
        "Indian Hill Mynah"
    ],

    "Rabbit": [
        "Holland Lop",
        "Netherland Dwarf",
        "Lionhead",
        "Mini Rex",
        "Flemish Giant",
        "Angora Rabbit",
        "Californian Rabbit",
        "New Zealand Rabbit",
        "Tan Rabbit",
        "Rex Rabbit",
        "Havana Rabbit"
    ],

    "Hamster": [
        "Syrian Hamster",
        "Roborovski Hamster",
        "Campbell's Dwarf Hamster",
        "Winter White Hamster",
        "Chinese Hamster",
        "Djungarian Hamster",
        "Brandt's Hamster",
        "Striped Dwarf Hamster",
        "European Hamster",
        "Teddy Bear Hamster"
    ],

    "Turtle": [
        "Red-Eared Slider",
        "Indian Flapshell Turtle",
        "Painted Turtle",
        "Box Turtle",
        "Softshell Turtle",
        "Musk Turtle",
        "Map Turtle",
        "Wood Turtle",
        "Diamondback Terrapin",
        "Blanding's Turtle"
    ],

    "Fish": [
        "Goldfish",
        "Betta Fish",
        "Guppy",
        "Molly fish",
        "Angelfish",
        "Tetra Fish",
        "Corydoras Catfish",
        "Pleco",
        "Koi Fish",
        "Discus Fish",
        "Neon Tetra"
    ],

    "Reptile": [
        "Leopard Gecko",
        "Bearded Dragon",
        "Corn Snake",
        "Crested Gecko",
        "Ball Python",
        "Green Tree Python",
        "Iguana",
        "Monitor Lizard",
        "King Cobra",
        "Red-Tailed Boa"
    ]
}


# --------------------------------------------------
# BREED INFORMATION
# --------------------------------------------------

breed_info = {

 # DOG BREED
    
    "Labrador Retriever": {
        "about": "A friendly, intelligent and energetic dog breed that is popular as a family pet.",
        "appearance": "Medium to large-sized dog with a short, dense coat.",
        "behavior": "Friendly, playful, social and easy to train.",
        "lifespan": "10–12 years",
        "diet": "Balanced dog food with appropriate portions and fresh water.",
        "care": "Regular exercise, grooming, training and routine veterinary care."
    },

    "Golden Retriever": {
        "about": "A friendly and intelligent dog known for its gentle nature.",
        "appearance": "Medium to large dog with a dense golden-colored coat.",
        "behavior": "Friendly, active, affectionate and eager to learn.",
        "lifespan": "10–12 years",
        "diet": "Balanced dog food, appropriate portions and fresh water.",
        "care": "Daily activity, brushing, training and regular veterinary checkups."
    },

    "German Shepherd": {
        "about": "An intelligent and versatile dog breed often known for its loyalty and working ability.",
        "appearance": "Large dog with an athletic body and thick coat.",
        "behavior": "Loyal, intelligent, alert and protective.",
        "lifespan": "9–13 years",
        "diet": "Complete and balanced dog food with suitable portions.",
        "care": "Regular exercise, mental stimulation, grooming and training."
    },

    "Pug": {
        "about": "A small companion dog known for its distinctive face and playful personality.",
        "appearance": "Small dog with a short coat and compact body.",
        "behavior": "Playful, affectionate and social.",
        "lifespan": "12–15 years",
        "diet": "Balanced food with carefully controlled portions.",
        "care": "Moderate activity, regular grooming and attention to breathing and heat."
    },

    "Beagle": {
        "about": "A small-to-medium hound known for its excellent sense of smell.",
        "appearance": "Compact body with short coat and long floppy ears.",
        "behavior": "Curious, energetic, friendly and playful.",
        "lifespan": "10–15 years",
        "diet": "Balanced dog food and fresh water.",
        "care": "Daily walks, playtime, training and regular grooming."
    },

    "Rottweiler": {
        "about": "A large, powerful dog breed known for its loyalty and protective nature.",
        "appearance": "Large dog with a black coat and tan markings.",
        "behavior": "Confident, loyal, and protective. Good family guardian.",
        "lifespan": "8-11 years",
        "diet": "High-quality dog food with appropriate portions.",
        "care": "Regular exercise, mental stimulation, training and socialization."
    },

    "Pomeranian": {
        "about": "A small companion dog breed known for its fluffy coat and big personality.",
        "appearance": "Small dog with a thick, fluffy double coat in various colors.",
        "behavior": "Alert, intelligent, and playful despite small size.",
        "lifespan": "12-16 years",
        "diet": "Small portions of high-quality dog food.",
        "care": "Regular grooming, indoor play, and gentle training."
    },

    "Shih Tzu": {
        "about": "A small dog breed from China known for its long hair and friendly nature.",
        "appearance": "Small dog with long, silky coat and a distinctive face.",
        "behavior": "Affectionate, playful, and loves human companionship.",
        "lifespan": "10-18 years",
        "diet": "Small portions of balanced dog food.",
        "care": "Daily grooming, regular bathing, and gentle exercise."
    },

    "Husky": {
        "about": "A large, energetic dog breed from Siberia known for its thick coat and blue eyes.",
        "appearance": "Large dog with thick gray and white coat and striking blue eyes.",
        "behavior": "Energetic, friendly, intelligent and loves cold weather.",
        "lifespan": "12-15 years",
        "diet": "High-quality dog food suitable for active dogs.",
        "care": "Regular exercise, grooming, training and outdoor activities."
    },

    "Bulldog": {
        "about": "A medium-sized dog breed known for its wrinkled face and calm demeanor.",
        "appearance": "Stocky dog with wrinkled face, pushed-in nose and muscular body.",
        "behavior": "Calm, affectionate, stubborn but friendly.",
        "lifespan": "8-10 years",
        "diet": "Quality dog food appropriate for their size.",
        "care": "Regular exercise, facial wrinkle cleaning and veterinary care."
    },

    "Dachshund": {
        "about": "A small dog breed known for its long body and short legs.",
        "appearance": "Small elongated dog with short legs and long body.",
        "behavior": "Playful, curious, loyal and sometimes stubborn.",
        "lifespan": "12-16 years",
        "diet": "Quality small breed dog food.",
        "care": "Regular exercise, back care and gentle handling."
    },

 
 #CAT BREED

    "Persian": {
        "about": "A long-haired cat known for its calm personality and distinctive appearance.",
        "appearance": "Long, thick coat with a rounded face.",
        "behavior": "Calm, gentle and affectionate.",
        "lifespan": "12–17 years",
        "diet": "Complete cat food with fresh water.",
        "care": "Frequent brushing, eye care and regular veterinary checkups."
    },

    "Siamese": {
        "about": "A social and vocal cat breed known for its distinctive color pattern.",
        "appearance": "Slim body, short coat and blue eyes.",
        "behavior": "Social, intelligent, active and vocal.",
        "lifespan": "12–20 years",
        "diet": "Balanced cat food and fresh water.",
        "care": "Playtime, interaction, grooming and regular veterinary care."
    },

    "Maine Coon": {
        "about": "A large cat breed known for its long coat and friendly nature.",
        "appearance": "Large body, long coat and prominent tail.",
        "behavior": "Friendly, intelligent and playful.",
        "lifespan": "12–15 years",
        "diet": "High-quality balanced cat food.",
        "care": "Regular brushing, playtime and routine veterinary checkups."
    },

    "British Shorthair": {
        "about": "A calm and sturdy cat breed with a dense short coat.",
        "appearance": "Round face, sturdy body and dense coat.",
        "behavior": "Calm, independent and affectionate.",
        "lifespan": "12–20 years",
        "diet": "Balanced cat food with appropriate portions.",
        "care": "Regular brushing, exercise and routine health checks."
    },

    "Bengal": {
        "about": "An active cat breed known for its spotted or marbled coat.",
        "appearance": "Athletic body with a patterned coat.",
        "behavior": "Active, intelligent, curious and playful.",
        "lifespan": "12–16 years",
        "diet": "Complete and balanced cat food.",
        "care": "Plenty of play, climbing opportunities and mental stimulation."
    },

    "Ragdoll": {
        "about": "A large, gentle cat breed known for its blue eyes and color-point pattern.",
        "appearance": "Large cat with blue eyes, light colored body with darker points on face, ears, paws and tail.",
        "behavior": "Calm, gentle, affectionate and loves human companionship.",
        "lifespan": "12-17 years",
        "diet": "Complete cat food with fresh water.",
        "care": "Regular brushing, gentle handling and routine veterinary checkups."
    },

    "Indian Shorthair": {
        "about": "A common domestic cat breed found in India, adaptable and hardy.",
        "appearance": "Medium-sized cat with short coat in various colors and patterns.",
        "behavior": "Independent, playful, intelligent and adaptable to environment.",
        "lifespan": "12-18 years",
        "diet": "Quality cat food and fresh water.",
        "care": "Regular grooming, playtime, exercise and routine veterinary care."
    },

    "Sphynx": {
        "about": "A hairless cat breed known for its unique appearance and affectionate nature.",
        "appearance": "Hairless or very short-haired cat with wrinkled skin and large ears.",
        "behavior": "Affectionate, energetic, friendly and loves human attention.",
        "lifespan": "8-14 years",
        "diet": "Quality cat food with proper nutrition.",
        "care": "Regular bathing, skin care, ear cleaning and temperature control."
    },

    "Turkish Angora": {
        "about": "A graceful cat breed from Turkey known for its silky coat and agility.",
        "appearance": "Slender cat with long silky coat, often white colored.",
        "behavior": "Intelligent, playful, active and affectionate.",
        "lifespan": "12-18 years",
        "diet": "Quality cat food suitable for active cats.",
        "care": "Regular brushing, playtime and interactive activities."
    },

    "Abyssinian": {
        "about": "An active cat breed known for its distinctive ticked coat and playful nature.",
        "appearance": "Slender cat with short ticked coat and large ears.",
        "behavior": "Energetic, playful, curious and intelligent.",
        "lifespan": "9-13 years",
        "diet": "Quality cat food with high protein content.",
        "care": "Daily playtime, exercise, toys and mental stimulation."
    },
    
    "Scottish Fold": {
        "about": "A cat breed known for its distinctive folded ears and sweet expression.",
        "appearance": "Medium cat with folded ears, round face and short coat.",
        "behavior": "Calm, affectionate, playful and adaptable.",
        "lifespan": "11-15 years",
        "diet": "Balanced cat food with fresh water.",
        "care": "Regular ear cleaning, grooming and veterinary checkups."
    },


 #BIRD BREED

    "Parrot": {
        "about": "Intelligent and colorful bird breed known for mimicking sounds and speech.",
        "appearance": "Colorful plumage with curved beak and strong feet.",
        "behavior": "Intelligent, social, playful and can live very long.",
        "lifespan": "20-80 years depending on species",
        "diet": "Seeds, nuts, fruits and leafy greens.",
        "care": "Large cage, toys, social interaction and regular exercise."
    },

    "Budgerigar (Budgie)": {
        "about": "A small, colorful and social bird that is commonly kept as a companion pet.",
        "appearance": "Small body with colorful feathers and a curved beak.",
        "behavior": "Social, active and capable of learning sounds.",
        "lifespan": "5–10 years",
        "diet": "Suitable bird pellets/seeds along with appropriate vegetables and fresh water.",
        "care": "Clean cage, social interaction, exercise and safe toys."
    },

    "Cockatiel": {
        "about": "A friendly companion bird known for its crest and ability to whistle.",
        "appearance": "Medium-sized bird with a distinctive head crest.",
        "behavior": "Friendly, social and playful.",
        "lifespan": "15–20 years",
        "diet": "Balanced bird food, suitable vegetables and fresh water.",
        "care": "Daily interaction, safe exercise space and regular cage cleaning."
    },

    "Lovebird": {
        "about": "A small, colorful and social companion bird.",
        "appearance": "Small body with a short tail and colorful feathers.",
        "behavior": "Active, social and playful.",
        "lifespan": "10–15 years",
        "diet": "Balanced bird food with suitable fresh foods.",
        "care": "Social interaction, toys, exercise and a clean cage."
    },

    "Finch": {
        "about": "A small colorful bird breed known for its beautiful singing and social nature.",
        "appearance": "Small bird with colorful plumage in various patterns and colors.",
        "behavior": "Active, social, cheerful and males are known for singing.",
        "lifespan": "5-10 years",
        "diet": "Quality finch seed, millet and occasional fresh fruits.",
        "care": "Medium-sized cage, toys, perches and daily care."
    },

    "Canary": {
        "about": "A small, colorful bird breed known for its beautiful singing.",
        "appearance": "Small bird with bright yellow or orange plumage.",
        "behavior": "Active, cheerful and males are known for singing.",
        "lifespan": "10-15 years",
        "diet": "Quality bird seed and fresh fruits and vegetables.",
        "care": "Medium cage, toys, natural light and daily care."
    },

    "Macaw": {
        "about": "A large, colorful parrot breed known for its intelligence and vibrant plumage.",
        "appearance": "Large bird with bright blue, red, yellow and green feathers.",
        "behavior": "Intelligent, social, loud and requires lots of attention.",
        "lifespan": "30-50 years",
        "diet": "Nuts, seeds, fruits, vegetables and specialized pellets.",
        "care": "Very large cage, toys, social interaction and regular exercise."
    },

    "Pigeon": {
        "about": "A common bird breed known for its cooing sounds and homing ability.",
        "appearance": "Medium-sized bird with gray, white or brown plumage.",
        "behavior": "Gentle, social, calm and good fliers.",
        "lifespan": "8-10 years",
        "diet": "Seeds, grains, vegetables and fresh water.",
        "care": "Loft or cage with perches, nesting boxes and regular cleaning."
    },

    "Rainbow Lorikeet": {
        "about": "A colorful parrot breed from Australia known for its vibrant rainbow colors.",
        "appearance": "Small parrot with rainbow colored plumage in all colors.",
        "behavior": "Playful, social, intelligent and very vocal.",
        "lifespan": "20-30 years",
        "diet": "Nectar, fruits, vegetables and specialized lorikeet pellets.",
        "care": "Medium-large cage, toys, social interaction and regular exercise."
    },

    "Indian Hill Mynah": {
        "about": "A popular talking bird breed from India known for its speaking ability.",
        "appearance": "Black bird with yellow beak, feet and patches near eyes.",
        "behavior": "Intelligent, playful, social and can mimic speech.",
        "lifespan": "15-20 years",
        "diet": "Fruits, vegetables, seeds and specialized mynah food.",
        "care": "Large cage, toys, social interaction and daily care."
    },

 #RABBIT BREED
    "Holland Lop": {
        "about": "A small rabbit breed recognized by its floppy ears.",
        "appearance": "Small, compact body with characteristic lop ears.",
        "behavior": "Generally gentle, social and curious.",
        "lifespan": "7–10 years",
        "diet": "Mostly hay, with suitable vegetables and rabbit pellets.",
        "care": "Clean living space, exercise, hay and regular grooming."
    },

    "Netherland Dwarf": {
        "about": "A very small rabbit breed known for its compact size.",
        "appearance": "Small body with short ears and compact features.",
        "behavior": "Active, curious and sometimes cautious.",
        "lifespan": "7–10 years",
        "diet": "Hay, appropriate vegetables, pellets and fresh water.",
        "care": "Safe exercise, clean habitat and regular grooming."
    },

    "Lionhead": {
        "about": "A small rabbit breed known for its lion-like mane of fur around its head.",
        "appearance": "Small rabbit with thick fur around head like a mane, compact body.",
        "behavior": "Playful, curious and friendly.",
        "lifespan": "7-10 years",
        "diet": "Hay, fresh greens and rabbit pellets.",
        "care": "Regular grooming, exercise and interactive play."
    },

    "Mini Rex": {
        "about": "A small rabbit breed known for its soft, velvety coat and compact size.",
        "appearance": "Small rabbit with incredibly soft short velvety fur in various colors.",
        "behavior": "Calm, friendly and enjoys gentle handling.",
        "lifespan": "5-7 years",
        "diet": "Quality hay, fresh vegetables and pellets.",
        "care": "Gentle grooming, moderate exercise and proper housing."
    },

    "Flemish Giant": {
        "about": "A large rabbit breed known for its impressive size and gentle temperament.",
        "appearance": "Large rabbit breed with long body and long ears.",
        "behavior": "Gentle, calm and friendly despite large size.",
        "lifespan": "5-9 years",
        "diet": "Plenty of hay, fresh vegetables and pellets.",
        "care": "Very large enclosure, space for movement and proper care."
    },

    "Angora Rabbit": {
        "about": "A fluffy rabbit breed known for its long silky wool and gentle nature.",
        "appearance": "Large rabbit with very long, soft wool in white or other colors.",
        "behavior": "Gentle, calm and friendly but needs regular handling.",
        "lifespan": "7-12 years",
        "diet": "Hay, fresh vegetables and rabbit pellets.",
        "care": "Daily grooming to prevent matting, regular wool harvesting and proper housing."
    },

    "Californian Rabbit": {
        "about": "A medium-sized rabbit breed known for its white body with dark points.",
        "appearance": "White rabbit with dark brown or black markings on face, ears and feet.",
        "behavior": "Calm, gentle and friendly.",
        "lifespan": "5-10 years",
        "diet": "Quality hay, fresh vegetables and pellets.",
        "care": "Regular grooming, moderate exercise and proper housing."
    },

    "New Zealand Rabbit": {
        "about": "A large rabbit breed known for its solid coloring and calm temperament.",
        "appearance": "Large rabbit with solid color coat, often red, black or white.",
        "behavior": "Calm, gentle, friendly and easy to handle.",
        "lifespan": "8-12 years",
        "diet": "Plenty of hay, fresh vegetables and pellets.",
        "care": "Large enclosure, regular grooming and veterinary care."
    },

    "Tan Rabbit": {
        "about": "A small rabbit breed known for its distinctive two-tone coloring.",
        "appearance": "Small rabbit with dark body and tan colored markings.",
        "behavior": "Active, playful and friendly.",
        "lifespan": "7-10 years",
        "diet": "Hay, fresh vegetables and rabbit pellets.",
        "care": "Regular exercise, grooming and interactive play."
    },

    "Rex Rabbit": {
        "about": "A rabbit breed known for its soft velvety coat and calm nature.",
        "appearance": "Medium rabbit with short, dense velvety fur.",
        "behavior": "Calm, friendly and enjoys gentle handling.",
        "lifespan": "5-7 years",
        "diet": "Quality hay, vegetables and pellets.",
        "care": "Gentle grooming, moderate exercise and proper housing."
    },

    "Havana Rabbit": {
        "about": "A small rabbit breed from Cuba known for its glossy chocolate-colored coat.",
        "appearance": "Small rabbit with rich chocolate-brown glossy coat.",
        "behavior": "Calm, gentle, friendly and good for families.",
        "lifespan": "7-10 years",
        "diet": "Hay, fresh vegetables and pellets.",
        "care": "Regular grooming, playtime and routine veterinary care."
    },

    #HAMSTER BREED

    "Syrian Hamster": {
        "about": "A small pet hamster that is generally kept alone.",
        "appearance": "Small body with soft fur and a short tail.",
        "behavior": "Usually active during the evening and night.",
        "lifespan": "2–3 years",
        "diet": "Balanced hamster food with suitable fresh foods.",
        "care": "Spacious enclosure, bedding, exercise wheel and clean water."
    },

    "Roborovski Hamster": {
        "about": "One of the smallest commonly kept hamster types.",
        "appearance": "Very small body with sandy-colored fur.",
        "behavior": "Fast, active and often energetic.",
        "lifespan": "2–3 years",
        "diet": "Balanced hamster food with suitable fresh foods.",
        "care": "Secure enclosure, exercise and appropriate bedding."
    },

    "Campbell's Dwarf Hamster": {
        "about": "A small dwarf hamster breed known for its active nature and small size.",
        "appearance": "Tiny hamster with gray-brown body and darker stripe down the back.",
        "behavior": "Active, curious, playful and can be social with proper handling.",
        "lifespan": "2-3 years",
        "diet": "Quality hamster food, fresh vegetables and water.",
        "care": "Large cage with bedding, wheel, toys and regular cleaning."
    },

    "Winter White Hamster": {
        "about": "A small dwarf hamster breed known for its white coat in winter months.",
        "appearance": "Tiny hamster that turns white in winter, gray-brown in summer.",
        "behavior": "Active, gentle, curious and can be handled with care.",
        "lifespan": "1.5-2 years",
        "diet": "Quality hamster food, fresh vegetables and water.",
        "care": "Large cage with bedding, wheel, toys and regular maintenance."
    },

    "Chinese Hamster": {
        "about": "A small hamster breed known for its long tail and active nature.",
        "appearance": "Small hamster with gray-brown body and distinctive long tail.",
        "behavior": "Active, curious, playful and can be social with proper handling.",
        "lifespan": "2.5-3 years",
        "diet": "Quality hamster food, fresh vegetables and water.",
        "care": "Large cage with bedding, wheel, toys and regular cleaning."
    },

    "Djungarian Hamster": {
        "about": "A small dwarf hamster breed also called Winter White variety.",
        "appearance": "Tiny hamster with gray-brown coat and white markings.",
        "behavior": "Active, gentle, curious and can be handled with care.",
        "lifespan": "1.5-2.5 years",
        "diet": "Quality hamster food, fresh vegetables and water.",
        "care": "Large cage with bedding, wheel, toys and regular maintenance."
    },

    "Brandt's Hamster": {
        "about": "A small hamster breed known for its friendly and social nature.",
        "appearance": "Small hamster with golden-brown colored coat.",
        "behavior": "Active, friendly, social and enjoys interaction.",
        "lifespan": "2-3 years",
        "diet": "Quality hamster food, seeds and fresh vegetables.",
        "care": "Large cage with enrichment, toys, wheel and regular care."
    },

    "Striped Dwarf Hamster": {
        "about": "A small hamster breed known for its distinctive stripe down its back.",
        "appearance": "Tiny hamster with dark stripe running down center of back.",
        "behavior": "Active, playful, curious and can be social.",
        "lifespan": "2-3 years",
        "diet": "Quality hamster food, vegetables and occasional seeds.",
        "care": "Large cage with bedding, wheel, toys and regular cleaning."
    },

    "European Hamster": {
        "about": "A larger hamster breed known for its distinctive coloring and behavior.",
        "appearance": "Medium-sized hamster with black and brown coloring.",
        "behavior": "Active, curious, can be territorial and needs proper handling.",
        "lifespan": "3-4 years",
        "diet": "Quality hamster food, grains, vegetables and water.",
        "care": "Large cage with space, bedding, wheel and regular maintenance."
    },

    "Teddy Bear Hamster": {
        "about": "A Syrian hamster variety known for its fluffy coat and cute appearance.",
        "appearance": "Medium hamster with fluffy thick coat and round face.",
        "behavior": "Calm, friendly, playful and good for beginners.",
        "lifespan": "2.5-3 years",
        "diet": "Quality hamster food, vegetables and occasional treats.",
        "care": "Large cage with bedding, wheel, toys and regular grooming."
    },

    #TURTLE BREED

    "Red-Eared Slider": {
        "about": "A popular freshwater turtle breed known for its red ear markings and aquatic nature.",
        "appearance": "Green turtle with red stripe behind ear and yellow plastron.",
        "behavior": "Active, social and spends most time in water.",
        "lifespan": "20-40 years",
        "diet": "Aquatic plants, insects and occasional vegetables.",
        "care": "Large aquarium with basking area, UVB light and proper water conditions."
    },

    "Indian Flapshell Turtle": {
        "about": "A freshwater turtle breed from India known for its flat shell.",
        "appearance": "Flat brown shell with soft leathery texture and flaps.",
        "behavior": "Aquatic, peaceful and mostly stays in water.",
        "lifespan": "15-20 years",
        "diet": "Aquatic plants, small fish and insects.",
        "care": "Large aquarium with plants, basking area and proper water maintenance."
    },

    "Painted Turtle": {
        "about": "A colorful freshwater turtle breed known for its vibrant markings.",
        "appearance": "Dark shell with red and yellow markings on body and plastron.",
        "behavior": "Active, peaceful and semi-aquatic.",
        "lifespan": "25-35 years",
        "diet": "Aquatic plants, insects and small fish.",
        "care": "Large aquarium with basking area, UVB light and clean water."
    },

    "Box Turtle": {
        "about": "A terrestrial turtle breed known for its domed shell and land-dwelling nature.",
        "appearance": "High domed brown shell with yellow markings.",
        "behavior": "Slow-moving, shy and prefers land over water.",
        "lifespan": "50-100 years",
        "diet": "Vegetables, fruits, insects and occasional worms.",
        "care": "Large enclosure with soil, hiding spots, UVB light and humidity."
    },

    "Softshell Turtle": {
        "about": "A freshwater turtle breed known for its soft, leathery shell and agile swimming.",
        "appearance": "Flat soft shell instead of hard shell, brownish color.",
        "behavior": "Aquatic, active, aggressive feeders and mostly stays in water.",
        "lifespan": "15-20 years",
        "diet": "Small fish, insects and aquatic plants.",
        "care": "Large aquarium with deep water, basking area and proper filtration."
    },

    "Musk Turtle": {
        "about": "A small freshwater turtle breed known for its musky smell defense mechanism.",
        "appearance": "Small dark brown turtle with smooth rounded shell.",
        "behavior": "Aquatic, peaceful, shy and mostly stays in water.",
        "lifespan": "15-25 years",
        "diet": "Small fish, insects, plants and occasional vegetables.",
        "care": "Medium-sized aquarium with plants, gentle conditions and regular maintenance."
    },

    "Map Turtle": {
        "about": "A freshwater turtle breed known for the map-like patterns on its shell.",
        "appearance": "Green shell with yellow map-like patterns and markings.",
        "behavior": "Semi-aquatic, peaceful, shy and likes basking.",
        "lifespan": "15-20 years",
        "diet": "Small fish, insects and aquatic plants.",
        "care": "Large aquarium with basking area, UVB light and clean water."
    },

    "Wood Turtle": {
        "about": "A semi-terrestrial turtle breed known for its ridged shell and intelligence.",
        "appearance": "Brown shell with prominent ridges and yellow markings.",
        "behavior": "Semi-aquatic, intelligent, curious and friendly.",
        "lifespan": "40-55 years",
        "diet": "Plants, fruits, insects and occasional small fish.",
        "care": "Large enclosure with water area, land area, UVB light and humidity."
    },

    "Diamondback Terrapin": {
        "about": "A brackish water turtle breed known for its diamond-patterned shell.",
        "appearance": "Shell with diamond-shaped pattern and yellow coloring.",
        "behavior": "Semi-aquatic, peaceful and prefers brackish or saltwater.",
        "lifespan": "20-40 years",
        "diet": "Snails, clams, small crustaceans and aquatic plants.",
        "care": "Brackish water aquarium, salinity control and proper basking area."
    },

    "Blanding's Turtle": {
        "about": "A freshwater turtle breed known for its distinctive yellow markings and gentle nature.",
        "appearance": "Dark shell with yellow spots and distinctive yellow chin.",
        "behavior": "Semi-aquatic, peaceful, friendly and intelligent.",
        "lifespan": "20-30 years",
        "diet": "Small fish, aquatic insects, plants and vegetables.",
        "care": "Large aquarium with land area, basking spot, UVB light and proper conditions."
    },

    # FISH BREED

    "Goldfish": {
        "about": "A popular freshwater fish commonly kept as a pet.",
        "appearance": "Usually orange or gold, with many different varieties.",
        "behavior": "Generally peaceful and active.",
        "lifespan": "Can live for many years with proper care.",
        "diet": "Good-quality goldfish food in suitable amounts.",
        "care": "Proper tank size, clean water, filtration and regular water maintenance."
    },

    "Betta Fish": {
        "about": "A colorful freshwater fish known for its flowing fins.",
        "appearance": "Small fish available in many colors and fin shapes.",
        "behavior": "Generally active; males can be territorial toward other males.",
        "lifespan": "Around 2–5 years with proper care.",
        "diet": "Suitable betta pellets and occasional appropriate foods.",
        "care": "Proper tank setup, clean conditioned water and stable temperature."
    },

    "Guppy": {
        "about": "A small, colorful freshwater fish that is popular with beginners.",
        "appearance": "Small body with colorful patterns, especially in males.",
        "behavior": "Active, peaceful and social.",
        "lifespan": "Around 1–3 years.",
        "diet": "Quality fish food in appropriate amounts.",
        "care": "Clean water, filtration, suitable tank size and regular maintenance."
    },

    "Molly Fish": {
        "about": "A popular freshwater fish known for its peaceful nature and attractive colors.",
        "appearance": "Small fish available in black, white, orange and other colors.",
        "behavior": "Peaceful, active and generally social with other peaceful fish.",
        "lifespan": "Around 3-5 years with proper care.",
        "diet": "Fish flakes, pellets and suitable vegetables.",
        "care": "Clean water, proper tank size, filtration and regular water changes."
    },

    "Anglerfish": {
        "about": "A unique deep-sea fish known for its glowing lure and unusual appearance.",
        "appearance": "Dark-colored body with a large mouth, sharp teeth and a light-producing lure.",
        "behavior": "Mostly solitary and waits for prey using its glowing lure.",
        "lifespan": "Around 10-20 years depending on the species.",
        "diet": "Small fish, crustaceans and other marine animals.",
        "care": "Requires a large marine aquarium with suitable water conditions and low light."
    },

    "Tetra Fish": {
        "about": "A small colorful fish breed popular in freshwater aquariums.",
        "appearance": "Small fish with bright colors like red, blue and silver.",
        "behavior": "Peaceful, social, active and loves swimming in groups.",
        "lifespan": "3-5 years",
        "diet": "Quality fish flakes and small live food.",
        "care": "Planted aquarium, moderate temperature and regular water changes."
    },

    "Corydoras Catfish": {
        "about": "A small bottom-dwelling fish breed known for its cleaning behavior.",
        "appearance": "Small catfish with armored body and barbels around mouth.",
        "behavior": "Peaceful, bottom-feeder, active at night and social.",
        "lifespan": "3-5 years",
        "diet": "Sinking pellets, algae wafers and plant matter.",
        "care": "Sandy substrate, hiding spots and regular tank maintenance."
    },

    "Pleco": {
        "about": "A large bottom-dwelling fish breed known for eating algae.",
        "appearance": "Large fish with sucker mouth and spotted or striped pattern.",
        "behavior": "Peaceful, nocturnal, solitary and excellent algae eater.",
        "lifespan": "10-15 years",
        "diet": "Algae wafers, vegetables and specialized pellets.",
        "care": "Large aquarium with driftwood, caves and regular maintenance."
    },

    "Koi Fish": {
        "about": "A large ornamental fish breed known for its beautiful colors and patterns.",
        "appearance": "Large colorful fish with various patterns in red, white, black and gold.",
        "behavior": "Peaceful, social, intelligent and can recognize their owner.",
        "lifespan": "25-40 years",
        "diet": "Quality koi pellets, vegetables and occasional live food.",
        "care": "Large pond or aquarium, filtration, aeration and regular cleaning."
    },

    "Discus Fish": {
        "about": "A round-shaped fish breed known for its vibrant colors and peaceful nature.",
        "appearance": "Circular disc-shaped fish with colorful patterns and stripes.",
        "behavior": "Peaceful, social, shy and enjoys warm water.",
        "lifespan": "8-10 years",
        "diet": "Quality fish flakes, live food and frozen food.",
        "care": "Large aquarium, warm water, plants and peaceful tank mates."
    },

    "Neon Tetra": {
        "about": "A small colorful fish breed known for its bright neon stripe.",
        "appearance": "Small fish with bright blue upper body and red lower body stripe.",
        "behavior": "Peaceful, social, active and loves swimming in groups.",
        "lifespan": "5-8 years",
        "diet": "Quality fish flakes and small live food.",
        "care": "Planted aquarium, moderate temperature and regular water changes."
    },

    #REPTILE BREED

    "Leopard Gecko": {
        "about": "A small terrestrial lizard commonly kept as a companion reptile.",
        "appearance": "Small lizard with a patterned body and thick tail.",
        "behavior": "Generally calm and mostly active around dusk and night.",
        "lifespan": "10–20 years with proper care.",
        "diet": "Appropriate insect-based diet with necessary supplementation.",
        "care": "Proper enclosure, heating, hiding places and clean water."
    },

    "Bearded Dragon": {
        "about": "A medium-sized lizard known for its distinctive throat area.",
        "appearance": "Broad-bodied lizard with textured skin.",
        "behavior": "Generally calm and curious.",
        "lifespan": "8–14 years.",
        "diet": "A suitable combination of vegetables and appropriate insects.",
        "care": "Proper lighting, temperature, enclosure and nutrition."
    },

    "Corn Snake": {
        "about": "A popular non-venomous snake known for its attractive patterns.",
        "appearance": "Slender body with orange, red and brown patterns.",
        "behavior": "Generally calm and active.",
        "lifespan": "15–20 years or more with proper care.",
        "diet": "Appropriately sized prey according to veterinary/reptile-care guidance.",
        "care": "Secure enclosure, suitable temperature gradient, hides and clean water."
    },

    "Crested Gecko": {
        "about": "A small arboreal gecko known for the ridges above its eyes.",
        "appearance": "Small lizard with a soft body and distinctive crest.",
        "behavior": "Generally calm and active at night.",
        "lifespan": "15–20 years with proper care.",
        "diet": "Suitable prepared gecko diet and appropriate insects.",
        "care": "Vertical enclosure, suitable humidity, temperature and hiding areas."
    },    
    
    "Ball Python": {
        "about": "A popular snake breed known for its docile temperament and coiled posture.",
        "appearance": "Medium-sized snake with brown and gold pattern.",
        "behavior": "Calm, docile, tends to coil up when stressed and slow feeders.",
        "lifespan": "20-30 years",
        "diet": "Frozen-thawed mice or rats.",
        "care": "Secure enclosure, heat source, humidity control and proper care."
    },

    "Green Tree Python": {
        "about": "A beautiful arboreal snake breed known for its bright green color.",
        "appearance": "Bright green snake with yellow belly and distinctive perching posture.",
        "behavior": "Arboreal, docile, slow-moving and prefers climbing.",
        "lifespan": "15-20 years",
        "diet": "Frozen-thawed mice or small rats.",
        "care": "Tall enclosure with branches, high humidity and temperature control."
    },

    "Iguana": {
        "about": "A large lizard breed known for its impressive size and vegetarian diet.",
        "appearance": "Large green lizard with crest down back and long tail.",
        "behavior": "Intelligent, can be aggressive when mature and territorial.",
        "lifespan": "15-20 years",
        "diet": "Leafy greens, vegetables and fruits.",
        "care": "Very large enclosure, UVB light, heating and proper humidity."
    },

    "Monitor Lizard": {
        "about": "A large lizard breed known for its intelligence and active behavior.",
        "appearance": "Large lizard with patterned scales and powerful claws.",
        "behavior": "Active, intelligent, territorial and requires experienced keeper.",
        "lifespan": "15-20 years",
        "diet": "Insects, small animals and occasional vegetables.",
        "care": "Very large enclosure, heating, UVB light and proper handling."
    },

    "King Cobra": {
        "about": "A large venomous snake breed known for its hood display and intelligence.",
        "appearance": "Large brown or black snake with distinctive hood when threatened.",
        "behavior": "Intelligent, can be docile in captivity but requires respect.",
        "lifespan": "20-30 years",
        "diet": "Frozen-thawed snakes or large rodents.",
        "care": "Secure large enclosure, heat source, humidity and expert care only."
    },

    "Red-Tailed Boa": {
        "about": "A large constrictor snake breed known for its vibrant colors and docile nature.",
        "appearance": "Brown or red body with distinctive red tail marking.",
        "behavior": "Calm, docile, slow-moving and generally good for experienced keepers.",
        "lifespan": "20-30 years",
        "diet": "Frozen-thawed rats or rabbits.",
        "care": "Large enclosure, proper heating, humidity control and regular maintenance."
    }
}


# --------------------------------------------------
# PET SELECTION
# --------------------------------------------------

st.header("Choose your pet:")

if "selected_pet" not in st.session_state:
    st.session_state.selected_pet = None


# First row
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🐶 Dog", use_container_width=True):
        st.session_state.selected_pet = "Dog"

with col2:
    if st.button("🐱 Cat", use_container_width=True):
        st.session_state.selected_pet = "Cat"

with col3:
    if st.button("🐦 Bird", use_container_width=True):
        st.session_state.selected_pet = "Bird"

with col4:
    if st.button("🐰 Rabbit", use_container_width=True):
        st.session_state.selected_pet = "Rabbit"


# Second row
col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("🐹 Hamster", use_container_width=True):
        st.session_state.selected_pet = "Hamster"

with col6:
    if st.button("🐢 Turtle", use_container_width=True):
        st.session_state.selected_pet = "Turtle"

with col7:
    if st.button("🐠 Fish", use_container_width=True):
        st.session_state.selected_pet = "Fish"

with col8:
    if st.button("🦎 Reptile", use_container_width=True):
        st.session_state.selected_pet = "Reptile"


# --------------------------------------------------
# BREED / TYPE SELECTION
# --------------------------------------------------

if st.session_state.selected_pet:

    pet = st.session_state.selected_pet

    st.divider()

    st.subheader(f"{pet}")

    selected_breed = st.selectbox(
        f"Choose your {pet.lower()}'s breed/type:",
        pet_breeds[pet]
    )


    # --------------------------------------------------
    # SHOW INFORMATION
    # --------------------------------------------------

    if selected_breed in breed_info:

        info = breed_info[selected_breed]

        st.divider()

st.header("🤖 AI Pet Care Assistant")

question = st.text_input("Ask anything about your pet:")

if st.button("🤖 Ask AI"):
    if question.strip():
        prompt = f"""
You are a helpful pet-care assistant.
Give simple, safe, general information.
Do not diagnose serious medical conditions.
If the pet may be seriously ill or injured, recommend contacting a veterinarian.

Pet: {st.session_state.selected_pet}
Question: {question}
"""

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.write(response.choices[0].message.content)

        except Exception as e:
            if "429" in str(e):
                st.warning("⏳ AI service limit reached. Please try again shortly.")
            else:
                st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please enter a question first.")
        
# 🩺 Find Your Veterinarian
st.title("🐾 Find a Veterinarian")
st.caption("Meet our demo veterinary profiles ❤️")

city = st.selectbox(
    "📍 Choose City",
    ["All Cities", "Nandurbar", "Nashik", "Dhule","Shirpur"]
)

pet_type = st.selectbox(
    "🐶 Choose Pet Type",
    ["All Pets", "Dog", "Cat", "Bird", "Rabbit", "Hamster", "Turtle"]
)

filtered_doctors = []
for doctor in doctors:
    city_name = doctor["city"].replace(" 📍", "")

    city_match = city == "All Cities" or city_name == city
    pet_match = (
        pet_type == "All Pets"
        or pet_type in doctor["pet_types"]
    )

    if city_match and pet_match:
        filtered_doctors.append(doctor)

if filtered_doctors:
    for doctor in filtered_doctors:
        with st.container(border=True):
            st.subheader(f"{doctor['emoji']} {doctor['name']}")
            st.success(doctor["badge"])

            st.write("📍 **City:**", doctor["city"])
            st.write(
                "🩺 **Specialization:**",
                ", ".join(doctor["specialization"])
            )
            st.write("🎓 **Experience:**", f"{doctor['experience']} years")
            st.write("⭐ **Rating:**", f"{doctor['rating']}/5")
            st.write("💬 **Reviews:**", doctor["total_reviews"])
            st.write("💰 **Demo consultation fee:** ₹", doctor["consultation_fee"])
            st.write("🟢 **Availability:**", doctor["availability"])
            st.write("ℹ️", doctor["about"])

            with st.expander("💖 Read Reviews"):
                for review in doctor["reviews"]:
                    st.write(
                        f"⭐ {review['rating']}/5 — "
                        f"**{review['user']}**"
                    )
                    st.write(f"💬 {review['comment']}")
                    st.divider()
else:
    st.info("🐾 No demo doctors found for this selection.")