
# 🐾 Pet Care Assistant - Dummy Veterinarian Data
# ⚠️ All doctors, ratings and reviews below are fictional demo data.


doctors = [
    # 🏥 SHIRPUR - 5 DEMO DOCTORS
    {
        "id": 1,
        "name": "Dr. Amit Kulkarni",
        "emoji": "👨‍⚕️",
        "specialization": ["Dogs 🐶", "Cats 🐱"],
        "pet_types": ["Dog", "Cat"],
        "city": "Shirpur",
        "experience": 8,
        "rating": 4.8,
        "total_reviews": 124,
        "consultation_fee": 350,
        "availability": "Available 🟢",
        "languages": ["Marathi", "Hindi", "English"],
        "badge": "⭐ General Pet Care",
        "about": "Demo profile for general pet care and vaccinations.",
        "reviews": [
            {"user": "Pet Parent 🐾", "rating": 5,
             "comment": "Very caring and helpful! ❤️"},
            {"user": "Dog Lover 🐶", "rating": 4,
             "comment": "Explained pet care clearly. 😊"}
        ]
    },
    {
        "id": 2,
        "name": "Dr. Priya Deshmukh",
        "emoji": "👩‍⚕️",
        "specialization": ["Dogs 🐶", "Cats 🐱"],
        "pet_types": ["Dog", "Cat"],
        "city": "Shirpur",
        "experience": 6,
        "rating": 4.7,
        "total_reviews": 86,
        "consultation_fee": 400,
        "availability": "Available 🟢",
        "languages": ["Marathi", "Hindi"],
        "badge": "💖 Caring Vet",
        "about": "Demo profile focused on routine checkups and pet wellness.",
        "reviews": [
            {"user": "Pet Parent 🐕", "rating": 5,
             "comment": "Friendly and patient. ❤️"},
            {"user": "Cat Parent 🐈", "rating": 4,
             "comment": "Helpful suggestions for daily care. 🌿"}
        ]
    },
    {
        "id": 3,
        "name": "Dr. Sagar Patil",
        "emoji": "👨‍⚕️",
        "specialization": ["Dogs 🐶", "Rabbits 🐰"],
        "pet_types": ["Dog", "Rabbit"],
        "city": "Shirpur",
        "experience": 5,
        "rating": 4.6,
        "total_reviews": 58,
        "consultation_fee": 300,
        "availability": "By Appointment 📅",
        "languages": ["Marathi", "Hindi"],
        "badge": "🐾 Pet Wellness",
        "about": "Demo profile for preventive care and nutrition guidance.",
        "reviews": [
            {"user": "Dog Parent 🐕", "rating": 5,
             "comment": "Good nutrition tips! 🥗"},
            {"user": "Pet Lover 🐾", "rating": 4,
             "comment": "Explained things simply. 😊"}
        ]
    },
    {
        "id": 4,
        "name": "Dr. Sneha Pawar",
        "emoji": "👩‍⚕️",
        "specialization": ["Cats 🐱", "Dogs 🐶"],
        "pet_types": ["Cat", "Dog"],
        "city": "Shirpur",
        "experience": 4,
        "rating": 4.9,
        "total_reviews": 73,
        "consultation_fee": 450,
        "availability": "Available 🟢",
        "languages": ["Marathi", "English"],
        "badge": "🌟 Top Rated Demo Profile",
        "about": "Demo profile for general health checks and preventive care.",
        "reviews": [
            {"user": "Cat Parent 🐈", "rating": 5,
             "comment": "Lovely experience! 💕"},
            {"user": "Pet Parent 🐾", "rating": 5,
             "comment": "Very informative and kind. ✨"}
        ]
    },
    {
        "id": 5,
        "name": "Dr. Kunal Chavan",
        "emoji": "👨‍⚕️",
        "specialization": ["Birds 🦜", "Hamsters 🐹"],
        "pet_types": ["Bird", "Hamster"],
        "city": "Shirpur",
        "experience": 3,
        "rating": 4.5,
        "total_reviews": 36,
        "consultation_fee": 250,
        "availability": "By Appointment 📅",
        "languages": ["Marathi", "Hindi"],
        "badge": "🐹 Small Pet Care",
        "about": "Demo profile for small-pet care information.",
        "reviews": [
            {"user": "Bird Parent 🦜", "rating": 5,
             "comment": "Useful bird-care tips! 💚"},
            {"user": "Pet Parent 🐹", "rating": 4,
             "comment": "Helpful general guidance. 🌼"}
        ]
    },

    # 📍 NANDURBAR - 2 DEMO DOCTORS
    {
        "id": 6,
        "name": "Dr. Aditi Sharma",
        "emoji": "👩‍⚕️",
        "specialization": ["Dogs 🐶", "Cats 🐱"],
        "pet_types": ["Dog", "Cat"],
        "city": "Nandurbar",
        "experience": 8,
        "rating": 4.8,
        "total_reviews": 124,
        "consultation_fee": 500,
        "availability": "Available 🟢",
        "languages": ["Marathi", "Hindi", "English"],
        "badge": "⭐ Pet Wellness",
        "about": "Demo profile for vaccinations and general pet wellness.",
        "reviews": [
            {"user": "Pet Parent 🐾", "rating": 5,
             "comment": "Caring and helpful! ❤️"},
            {"user": "Dog Lover 🐶", "rating": 4,
             "comment": "Clear and useful advice. 😊"}
        ]
    },
    {
        "id": 7,
        "name": "Dr. Manish Patil",
        "emoji": "👨‍⚕️",
        "specialization": ["Dogs 🐶", "Rabbits 🐰"],
        "pet_types": ["Dog", "Rabbit"],
        "city": "Nandurbar",
        "experience": 5,
        "rating": 4.6,
        "total_reviews": 51,
        "consultation_fee": 300,
        "availability": "By Appointment 📅",
        "languages": ["Marathi", "Hindi"],
        "badge": "💚 Caring Vet",
        "about": "Demo profile for routine checkups and pet nutrition.",
        "reviews": [
            {"user": "Dog Parent 🐕", "rating": 5,
             "comment": "Helpful nutrition guidance. 🥗"},
            {"user": "Pet Lover 🐾", "rating": 4,
             "comment": "Friendly and informative. 😊"}
        ]
    },

    # 📍 DHULE - 2 DEMO DOCTORS
    {
        "id": 8,
        "name": "Dr. Neha Deshmukh",
        "emoji": "👩‍⚕️",
        "specialization": ["Birds 🦜", "Rabbits 🐰", "Hamsters 🐹"],
        "pet_types": ["Bird", "Rabbit", "Hamster"],
        "city": "Dhule",
        "experience": 7,
        "rating": 4.9,
        "total_reviews": 67,
        "consultation_fee": 600,
        "availability": "By Appointment 📅",
        "languages": ["Marathi", "Hindi", "English"],
        "badge": "🦜 Exotic Pet Care",
        "about": "Demo profile for bird and small-pet care information.",
        "reviews": [
            {"user": "Bird Parent 🦜", "rating": 5,
             "comment": "Great bird-care guidance! 💕"},
            {"user": "Pet Parent 🐹", "rating": 5,
             "comment": "Helpful feeding advice. ✨"}
        ]
    },
    {
        "id": 9,
        "name": "Dr. Rahul More",
        "emoji": "👨‍⚕️",
        "specialization": ["Dogs 🐶", "Cats 🐱"],
        "pet_types": ["Dog", "Cat"],
        "city": "Dhule",
        "experience": 6,
        "rating": 4.7,
        "total_reviews": 62,
        "consultation_fee": 350,
        "availability": "Available 🟢",
        "languages": ["Marathi", "Hindi"],
        "badge": "🐾 General Pet Care",
        "about": "Demo profile for routine checkups and preventive care.",
        "reviews": [
            {"user": "Cat Parent 🐈", "rating": 5,
             "comment": "Very helpful advice! ❤️"},
            {"user": "Dog Parent 🐕", "rating": 4,
             "comment": "Explained general care clearly. 😊"}
        ]
    },

    # 📍 NASHIK - 1 DEMO DOCTOR
    {
        "id": 10,
        "name": "Dr. Rohan Patil",
        "emoji": "👨‍⚕️",
        "specialization": ["Dogs 🐶", "Cats 🐱", "Rabbits 🐰"],
        "pet_types": ["Dog", "Cat", "Rabbit"],
        "city": "Nashik",
        "experience": 6,
        "rating": 4.6,
        "total_reviews": 89,
        "consultation_fee": 400,
        "availability": "Available 🟢",
        "languages": ["Marathi", "Hindi", "English"],
        "badge": "💚 Caring Vet",
        "about": "Demo profile for pet nutrition and routine care.",
        "reviews": [
            {"user": "Pet Parent 🐕", "rating": 5,
             "comment": "Great nutrition advice! 🥗"},
            {"user": "Animal Lover 🐾", "rating": 4,
             "comment": "Friendly and informative. 😊"}
        ]
    }
]