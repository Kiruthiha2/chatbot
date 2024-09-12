import pyttsx3


import speech_recognition as sr
from fuzzywuzzy import fuzz

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm currently unable to process your request.")
        return ""

# Function for fuzzy matching and getting the response
def get_response(query):
    # Predefined cases for questions and corresponding responses
    predefined_cases = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm good. Thank you!",
        "goodbye": "Goodbye! Have a nice day.",
        "how to become a game designer": '''Obtain a bachelor's degree.
                                           Brush up your math and physics skills.
                                           Expand your software engineering skills.
                                           Develop your storytelling skills.
                                           Build a game developer portfolio.
                                           Get an entry-level game developer position.
                                           Prepare for stiff competition in the job market.''',
        "what are the source we are having to develop a game?": """To develop a game, you can utilize various sources and resources. Here are some common sources for game development:

                                                                1. Game Engines: Game engines are software frameworks that provide tools, libraries, and functionalities to streamline game development. Some popular game engines include Unity, Unreal Engine, Godot, and Cocos2d.

                                                                2. Programming Languages: You can choose from a variety of programming languages for game development. Common languages include C++, C#, Python, JavaScript, and Lua. The choice of language often depends on the game engine or platform you are targeting.

                                                                3. Graphics and Art Assets: Games require visual elements such as character models, environments, textures, animations, and user interfaces. You can create your own assets using graphic design tools like Adobe Photoshop, Blender for 3D modeling, or use pre-made assets from online marketplaces.

                                                                4. Sound and Music: Games often involve audio elements like sound effects and background music. You can create or obtain audio assets using software tools for sound editing and music composition, or you can license royalty-free audio from websites specializing in game audio.

                                                                5. Game Design and Documentation: Before starting development, it's important to have a clear game design document outlining the concept, gameplay mechanics, level design, and overall structure of the game. Tools like GDD templates or specialized game design software can assist in this process.

                                                                6. Online Resources and Communities: There are numerous online resources and communities dedicated to game development. Websites, forums, tutorials, and YouTube channels provide valuable learning materials, code examples, and guidance for various aspects of game development.

                                                                7. Testing and Quality Assurance: During development, it's crucial to test the game for bugs, glitches, and performance issues. Testers and quality assurance processes ensure that the game functions as intended and provides an optimal user experience.

                                                                8. Documentation and Version Control: Documenting your code, assets, and project milestones is important for collaboration and future reference. Version control systems like Git can help manage and track changes to your game project.

                                                                9. Learning Materials and Courses: Books, online courses, and tutorials are available to learn game development concepts, programming languages, game design principles, and specific tools or game engines.

                                                                Remember that this is a general overview, and the specific sources and tools you use may vary based on your game's requirements, platform, and personal preferences.""",
        "What is Cloud gaming?":"In Cloud gaming, the game is hosted on a game server in a data center, and the user is only running a client locally which forwards game controller actions upstream to the game server",
        "Name some of the HTML5 framework game engines" :'''Some of the HTML 5 framework game engines are

a) Construct 2
b) Turbulence
c) CAAT
d) Phaser etc.''',
    "How good Bitbucket/Github is for game development?":"Bitbucket is a code hosting service and not a file sharing service. It is compatible for small size game development, but if you are handling extremely large files or frequently changing binary files Github would not be useful. Bitbucket can’t display differences on binaries",
    " What are the Android tools used for developing games" :'''Various tools required for developing games are

a) Eclispse: Integrated Development Environment (IDE)
b) ADT- Android’s Eclipse Plugin
c) Android SDK-includes ADB
d) Hudson- Automatic build tool
''',
                "What are the essential programming languages for game development?": """The essential programming languages for game development are:

                                                                            1. C++: Widely used for high-performance games and engines like Unreal Engine.
                                                                            2. C#: Commonly used with Unity game engine for cross-platform game development.
                                                                            3. Python: Known for its ease of use and used in various game development libraries.
                                                                            4. JavaScript: Often used for web-based games and with game engines like Phaser.
                                                                            5. Lua: Frequently used for scripting in game engines like Corona SDK and Love2D.""",
                                                                            
        "Explain the concept of game mechanics.": """Game mechanics refer to the rules, systems, and interactions that define how a game works. They govern the gameplay and provide challenges and goals for players to achieve. Game mechanics include things like movement controls, combat systems, scoring mechanisms, puzzles, and more. Well-designed game mechanics contribute to the overall fun and engagement of a game.""",
        
        "How can I optimize game performance for better FPS (Frames Per Second)?": """Optimizing game performance for better FPS involves various techniques, such as:

                                                                                    1. Efficient Rendering: Use modern rendering techniques, like GPU instancing and occlusion culling, to reduce the rendering workload.
                                                                                    2. Level of Detail (LOD): Implement LOD for game objects to render simpler models when they are far away from the camera.
                                                                                    3. Texture Compression: Use compressed textures to reduce GPU memory usage and improve rendering performance.
                                                                                    4. Code Optimization: Profile and optimize CPU-intensive code segments to avoid bottlenecks.
                                                                                    5. Threading: Utilize multi-threading to distribute tasks across CPU cores and improve performance.
                                                                                    6. Memory Management: Avoid memory leaks and unnecessary allocations that can lead to performance degradation.
                                                                                    7. Benchmarking: Regularly benchmark your game on target platforms to identify performance issues.
                                                                                    8. Graphics Settings: Offer various graphics settings to users to allow them to adjust performance based on their hardware capabilities.""",

        "What are the different types of game testing?": """Different types of game testing include:

                                                            1. Functionality Testing: Ensuring all game features and mechanics work as intended.
                                                            2. Compatibility Testing: Checking the game's compatibility with various devices and platforms.
                                                            3. Performance Testing: Assessing the game's performance under different conditions.
                                                            4. Usability Testing: Evaluating the user-friendliness and intuitiveness of the game.
                                                            5. Localization Testing: Verifying the game's adaptation to different languages and regions.
                                                            6. Regression Testing: Rechecking previously tested functionalities after bug fixes or updates.
                                                            7. Load Testing: Testing the game's performance under heavy player loads.
                                                            8. Security Testing: Identifying and addressing potential security vulnerabilities.
                                                            9. Beta Testing: Releasing the game to a limited audience for feedback and bug identification.
                                                            10. Playtesting: Having players experience the game to provide subjective feedback on gameplay and enjoyment.""",

        "Describe the process of level design in game development.": """Level design is the process of creating the various levels or stages that make up a game. It involves:

                                                                        1. Conceptualization: Defining the overall theme, setting, and goals of each level.
                                                                        2. Paper Prototyping: Creating rough sketches or diagrams of the level layout and key elements.
                                                                        3. Blockout: Building a basic, non-detailed version of the level to test gameplay flow.
                                                                        4. Iteration: Continuously refining and playtesting the level to ensure a balanced and engaging experience.
                                                                        5. Asset Integration: Adding visual elements, objects, and interactive elements to the level.
                                                                        6. Lighting and Atmosphere: Setting the appropriate lighting and ambiance to enhance the level's mood.
                                                                        7. Sound Design: Adding sound effects and background music to complement the gameplay.
                                                                        8. Polish: Finalizing the level with attention to detail and addressing any remaining issues.""",

        "How can I implement physics-based interactions in a game?": """To implement physics-based interactions in a game, you can use a physics engine or library, such as:

                                                                            1. Unity Physics: Built-in physics engine for Unity with rigidbodies, colliders, and joints.
                                                                            2. Unreal Engine Physics: Integrated physics system in Unreal Engine supporting various types of physics interactions.
                                                                            3. Box2D: Open-source physics engine for 2D games, widely used and available in various programming languages.
                                                                            4. Chipmunk: Lightweight 2D physics engine suitable for mobile games and simple physics interactions.
                                                                            5. Bullet Physics: A popular open-source physics engine for simulating rigid body dynamics and collisions in 3D games.

                                                                        By integrating the physics engine into your game, you can define physics properties for game objects, apply forces, detect collisions, and simulate realistic interactions between objects in the game world.""",

          "What are the essential programming languages for game development?": """The essential programming languages for game development are:

                                                                            1. C++: Widely used for high-performance games and engines like Unreal Engine.
                                                                            2. C#: Commonly used with Unity game engine for cross-platform game development.
                                                                            3. Python: Known for its ease of use and used in various game development libraries.
                                                                            4. JavaScript: Often used for web-based games and with game engines like Phaser.
                                                                            5. Lua: Frequently used for scripting in game engines like Corona SDK and Love2D.""",
                                                                            
        "Explain the concept of game mechanics.": """Game mechanics refer to the rules, systems, and interactions that define how a game works. They govern the gameplay and provide challenges and goals for players to achieve. Game mechanics include things like movement controls, combat systems, scoring mechanisms, puzzles, and more. Well-designed game mechanics contribute to the overall fun and engagement of a game.""",
        
        "How can I optimize game performance for better FPS (Frames Per Second)?": """Optimizing game performance for better FPS involves various techniques, such as:

                                                                                    1. Efficient Rendering: Use modern rendering techniques, like GPU instancing and occlusion culling, to reduce the rendering workload.
                                                                                    2. Level of Detail (LOD): Implement LOD for game objects to render simpler models when they are far away from the camera.
                                                                                    3. Texture Compression: Use compressed textures to reduce GPU memory usage and improve rendering performance.
                                                                                    4. Code Optimization: Profile and optimize CPU-intensive code segments to avoid bottlenecks.
                                                                                    5. Threading: Utilize multi-threading to distribute tasks across CPU cores and improve performance.
                                                                                    6. Memory Management: Avoid memory leaks and unnecessary allocations that can lead to performance degradation.
                                                                                    7. Benchmarking: Regularly benchmark your game on target platforms to identify performance issues.
                                                                                    8. Graphics Settings: Offer various graphics settings to users to allow them to adjust performance based on their hardware capabilities.""",

        "What are the different types of game testing?": """Different types of game testing include:

                                                            1. Functionality Testing: Ensuring all game features and mechanics work as intended.
                                                            2. Compatibility Testing: Checking the game's compatibility with various devices and platforms.
                                                            3. Performance Testing: Assessing the game's performance under different conditions.
                                                            4. Usability Testing: Evaluating the user-friendliness and intuitiveness of the game.
                                                            5. Localization Testing: Verifying the game's adaptation to different languages and regions.
                                                            6. Regression Testing: Rechecking previously tested functionalities after bug fixes or updates.
                                                            7. Load Testing: Testing the game's performance under heavy player loads.
                                                            8. Security Testing: Identifying and addressing potential security vulnerabilities.
                                                            9. Beta Testing: Releasing the game to a limited audience for feedback and bug identification.
                                                            10. Playtesting: Having players experience the game to provide subjective feedback on gameplay and enjoyment.""",

        "Describe the process of level design in game development.": """Level design is the process of creating the various levels or stages that make up a game. It involves:

                                                                        1. Conceptualization: Defining the overall theme, setting, and goals of each level.
                                                                        2. Paper Prototyping: Creating rough sketches or diagrams of the level layout and key elements.
                                                                        3. Blockout: Building a basic, non-detailed version of the level to test gameplay flow.
                                                                        4. Iteration: Continuously refining and playtesting the level to ensure a balanced and engaging experience.
                                                                        5. Asset Integration: Adding visual elements, objects, and interactive elements to the level.
                                                                        6. Lighting and Atmosphere: Setting the appropriate lighting and ambiance to enhance the level's mood.
                                                                        7. Sound Design: Adding sound effects and background music to complement the gameplay.
                                                                        8. Polish: Finalizing the level with attention to detail and addressing any remaining issues.""",

        "How can I implement physics-based interactions in a game?": """To implement physics-based interactions in a game, you can use a physics engine or library, such as:

                                                                            1. Unity Physics: Built-in physics engine for Unity with rigidbodies, colliders, and joints.
                                                                            2. Unreal Engine Physics: Integrated physics system in Unreal Engine supporting various types of physics interactions.
                                                                            3. Box2D: Open-source physics engine for 2D games, widely used and available in various programming languages.
                                                                            4. Chipmunk: Lightweight 2D physics engine suitable for mobile games and simple physics interactions.
                                                                            5. Bullet Physics: A popular open-source physics engine for simulating rigid body dynamics and collisions in 3D games.

                                                                        By integrating the physics engine into your game, you can define physics properties for game objects, apply forces, detect collisions, and simulate realistic interactions between objects in the game world.""",

        "What is the role of AI in game development?": """AI (Artificial Intelligence) plays a crucial role in game development, enhancing the player's experience and creating dynamic and engaging gameplay. Some key roles of AI in game development include:

                                                            1. Enemy Behavior: Creating intelligent and challenging enemy behaviors for NPCs (Non-Playable Characters) in single-player and multiplayer games.
                                                            2. Pathfinding: Implementing pathfinding algorithms to enable NPCs to navigate complex game environments efficiently.
                                                            3. Procedural Content Generation: Using AI algorithms to generate game content, such as levels, quests, and landscapes, dynamically.
                                                            4. Player Adaptation: Designing AI systems that adapt to the player's actions and adjust the game difficulty accordingly.
                                                            5. Decision Making: Enabling NPCs to make intelligent decisions based on the game's context and the player's actions.
                                                            6. Dynamic Storytelling: Using AI to create dynamic and branching narratives that respond to the player's choices.
                                                            7. Player Analytics: Utilizing AI for player data analysis to understand player behavior and preferences for game improvement.
                                                            8. Realistic NPCs: Creating AI-driven NPCs with emotions, personalities, and realistic social interactions.

                                                        AI in game development can significantly enhance the game's replayability, immersion, and overall player experience.""",                                            
        
    }
    
    # Threshold for fuzzy matching
    match_threshold = 50
    
    # Check for fuzzy matches with predefined cases
    for case in predefined_cases:
        similarity_score = fuzz.ratio(query.lower(), case.lower())
        if similarity_score >= match_threshold:
            return predefined_cases[case]
    
    # Default response if no match is found
    return "I'm sorry, I don't have the information you're looking for."


# Main program loop
while True:
    # Listen for user input
    query = listen()

    # Check for exit keyword
    if "exit" in query.lower():
        speak("Goodbye! Have a nice day.")
        break

    # Get bot response
    response = get_response(query)

    # Print and speak the response
    print(f"Bot: {response}")
    speak(response)
