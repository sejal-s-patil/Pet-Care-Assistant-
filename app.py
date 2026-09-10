import streamlit as st

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
        "Shih Tzu"
    ],

    "Cat": [
        "Persian",
        "Siamese",
        "Maine Coon",
        "British Shorthair",
        "Bengal",
        "Ragdoll",
        "Indian Shorthair"
    ],

    "Bird": [
        "Parrot",
        "Budgerigar (Budgie)",
        "Cockatiel",
        "Lovebird",
        "Finch",
        "Canary",
        "Macaw"
    ],

    "Rabbit": [
        "Holland Lop",
        "Netherland Dwarf",
        "Lionhead",
        "Mini Rex",
        "Flemish Giant"
    ],

    "Hamster": [
        "Syrian Hamster",
        "Roborovski Hamster",
        "Campbell's Dwarf Hamster",
        "Winter White Hamster"
    ],

    "Turtle": [
        "Red-Eared Slider",
        "Indian Flapshell Turtle",
        "Painted Turtle",
        "Box Turtle"
    ],

    "Fish": [
        "Goldfish",
        "Betta Fish",
        "Guppy",
        "Molly",
        "Angelfish"
    ],

    "Reptile": [
        "Leopard Gecko",
        "Bearded Dragon",
        "Corn Snake",
        "Crested Gecko"
    ]
}


# --------------------------------------------------
# BREED INFORMATION
# --------------------------------------------------

breed_info = {

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
    }
}


# --------------------------------------------------
# PET SELECTION
# --------------------------------------------------

st.header("Choose your pet:")

<<<<<<< HEAD
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

        st.subheader(f"🐾 About {selected_breed}")

        st.write(info["about"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 👀 Appearance")
            st.write(info["appearance"])

            st.markdown("### 🧠 Behavior")
            st.write(info["behavior"])

            st.markdown("### ⏳ Lifespan")
            st.write(info["lifespan"])

        with col2:
            st.markdown("### 🍽️ Diet")
            st.write(info["diet"])

            st.markdown("### ❤️ Care Tips")
            st.write(info["care"])
=======
if st.button("🐶 Dog"):
    st.switch_page("pages/dog_breed.py")
    
if st.button("🐱 Cat"):
    
    st.switch_page("pages/cat_breed.py")

if st.button("🐦 Bird"):
    st.switch_page("pages/bird.py")
>>>>>>> ad85af91cd7730819d33c4a112c88e850e42feff
