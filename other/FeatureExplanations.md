# SchoolBot Feature Descriptions

A description of every feature in the bot separated into their categories. Full use of the features can be found using the 'help' command. In the help command, proper use of arguments for each command can also be found.
Any command that has restricted access (e.g kick/ban), will have this noted in the description.
Features are grouped as they are in cogs.


## Other
- ***ping*** - Gets the current latency of the bot
- ***timer*** - Setting a timer that will notify you when it has completed
- ***roll_dice*** - Gets a random number between 1 and 6, emulating a dice being rolled
- ***stone_paper_scissor*** - A stone, paper, scissor game that can be played with the bot
- ***number_guess*** - A higher lower number guessing game that can be played with the bot
- ***member_count*** - Displays information about the number of members in the bot's current server
- ***announcement*** - Creates an embed in the server's announcement channel with the message of your choice (RESTRICTED)
- ***roman*** - Converts any number into roman numerals
- ***bmi*** - Finds the BMI index for you
- ***whois*** - Gives information about a user
- ***avatar*** - Gets a user's profile picture / avatar
- ***spellcheck*** - Checks the spelling of a word
- ***poll*** - Generates a poll, which using reactions, people can vote on. The poll is formatted as an embed with up to 10 options
- ***suggest*** - Creates a yes or no poll
- ***source*** - Allows the user to view the source code for a command within discord
- ***study_mode*** - Turns on the 'study mode' feature so you are not disturbed by discord during your studies
- ***youtube*** - Returns YouTube video information on the search query provided
- ***github*** - Returns some information about the bot, including a link to the Github repo


## Complaints
When the bot gets a DM, the content of this DM will be sent the the specified 'complaints' channel within discord (the ID of this channel is specified in the config.json file). Then, a person in authority is able to deal with the complaint


## Currency Conversion
- ***currency convert*** - Converts a specific amount of one currency to another
- ***currency value*** - Gets the value of the chosen currency in USD
- ***currency list*** - List all the available currencies that the bot can interchange


## Dictionary & Thesaurus
- ***dict define*** - Defines a given word
- ***dict urban*** - Defines a given word using urban dictionary
- ***dict synonym*** - Finds synonyms for a given word


## Error Handling
All errors in the bot should be handled and the user notified that there has been an error. Within the `errors.py` cog, the following errors are covered.
- ***Command not found*** - The bot could not find a command matching the user's input
- ***User has incorrect permissions*** - If the user required specific permissions to use a command (e.g kick/ban) but does not had them
- ***Incorrect arguments provided*** - Either too many, or too little number of arguments are provided
- ***Bot has incorrect permissions*** - The bot does not have permissions to perform certain commands (e.g kick / ban)
- ***Member cannot be found*** - A member that has been specified cannot be found by the bot
- ***Incorrect data type*** - An incorrect data type (e.g number instead of text) has been given to the bot
- ***404 Error*** - The bot has experienced a 404 error


## Math
The names of these commands are pretty self explanitary, the mathmatical functions that they provide are part of their name.
Below, the list of math commands is given.
- ***math add***
- ***math multiply***
- ***math divide***
- ***math power***
- ***math root***
- ***math sin***
- ***math cos***
- ***math tan***
- ***math cossec***
- ***math sec***
- ***math cot***
- ***math hcf***
- ***math lcm***
- ***math factorial***
- ***math gamma***
- ***math round***
- ***math average***


## Moderation
- ***kick*** - Kicks the specified user from the server (RESTRICTED)
- ***ban*** - Bans the specified user from the server (RESTRICTED)
- ***purge*** - Purges the specified amount of messages, or 100 if not specified (RESTRICTED)


## Music
- ***music play*** - Plays the given youtube URL or youtube search
- ***music disconnect*** - Disconnects the bot from the current voice channel
- ***music pause*** - Pauses the music that is currently being played by the bot
- ***music resume*** - Resumes the previously paused music that is currently being played by the bot
- ***music volume*** - Changes the volume of the music currently being played by the bot
- ***music skip*** - Skips to the next song in the music queue
- ***music current*** - Shows the song that is currently being played by the bot
- ***music queue*** - Shows the current music queue of the bot


## Note Sharing
Allows for easy note sharing using embeds. The embed contains the user's profile picture and name so other students will know who posted those specific notes.
When notes are posted in the specific note channel, they are formatted into an embed and the formatted version is sent


## Password Generator
For generating passwords, your privacy and security it our main priority. When you generate your password, an explanation of how the password was generated is sent to you. We do not store any passwords and the source code is available to view and we are always transparent. The command to generate a password is below.
- ***password_generate*** - Generates a password of the desired length (privacy details and password are DMed to you)


## Tagging system
- ***tag create*** - Creates a tag with the name and content specified
- ***tag edit*** - Edits a previously created tag
- ***tag rename*** - Renames a previously created tag
- ***tag delete*** - Deletes the specified tag
- ***tag info*** - Gives the relevant information of the specified tag
- ***tag list*** - Lists all the tags a specified member has created
- ***tag all*** - Sends the user a list of all their tags


## Timetable management
- ***time_table insert*** - Adds an item to your timetable, when the event it happening, you are notified in your DMs
- ***time_table delete*** - Deletes the specified event in your time table
- ***time_table all*** - Sends you your full schedule


## Todo system
- ***todo insert*** - Adds a piece of work to your todo list
- ***todo delete*** - Deletes the specified piece of work from your todo list
- ***todo all*** - Sends you the contents of your todo list


## Translation
- ***translate*** - Translates the text given from the language given into English
- ***translate detect*** - Detects what language the given text is in
- ***language all*** - Lists all of the unicode languages supported


## Wikipedia
- ***wiki summary*** - Gives the wikipedia summary of the provided topic
- ***wiki full*** - Gives the full article of the provided topic


## Help
Using the help commands in discord displays the correct use of arguments alongside all of these commands. The explanation of each command can also be viewed using the set of help commands.

- ***help*** - Displays the areas of help that can be accessed using the help commands
- ***help other*** - Displays help for the 'other' category
- ***help math*** - Displays help for the 'math' category
- ***help wiki*** - Displays help for the 'wikipedia' category
- ***help dict*** - Displays help for the 'dictionary' category
- ***help mod*** - Displays help for the 'moderation' category
- ***help yt*** - Displays help for the 'youtube' category
- ***help tt*** - Displays help for the 'timetable' category
- ***help td*** - Displays help for the 'todo' category
- ***help ns*** - Displays help for the 'note sharing' category
- ***help tag*** - Displays help for the 'tagging' category
- ***help translate*** - Displays help for the 'translation' category
- ***help currency*** - Displays help for the 'currency conversion' category
- ***help music*** - Displays help for the 'music' category
