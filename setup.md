# SchoolBot Setup
This is a setup guide to install and run the SchoolBot from the source code provided

## Before we start...

We understand that technology does not always go as planned, if you are not able to get the bot working, or feel that our instructions do not work, please don't hesitate to contact us in a way laid out below.

#### Github issues
1. Navigate to the Github repo for this bot
2. Open the 'issue' tab
3. Create a new issue. When creating your issue, please describe the issue you are having in detail, including any error outputs. No information is too much!

#### Discord server
- Our discord support server can be found [here](https://discord.gg/Fhukqpu), where you can contact both of us with quick replies.
- If you are in need of quick support, don't be afraid to @us, it will enable us to help you faster
- Make sure you provide enough detail of your issue, the more detail, the better

#### The internet!
- If you believe that the solution is obvious, the internet is a great place to find it
- If you believe your issue is to do with our code, it would be better to contact us, but for general install errors, the internet could do just great

<br>

Now that that's out of the way, lets get into it. Please follow the instructions in order, they are desinged to be followed in this way.

## Installing Python

Note: Python 3.10a, 3.9 and very old versions aren't yet supported by discord.py, so please use recommended Python 3.8.5

#### macOS:
1. Install brew if you do not already have it installed using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
2. Using brew, install python3 using the command `brew install python`
3. Check that python is installed using the command `python3 --version`, this should return `Python 3.x.x`

#### Windows
1. Download python from [here](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe) (official python website) and install. While completing the installation, please make sure you have the **'add to path'** option selected
2. Check that python is installed by running `python --version` in powershell

#### Linux
1. Check that python3 is installed, using `python3 --version`. This should return `python 3.x.x`
2. If not installed, please consult the internet, you will find an answer soon


## Downloading the bot files

#### Using Github desktop
1. Clone the repo using the url: `https://github.com/mattmoody05/SchoolBot.git`
2. Navigate to the folder your Github desktop folder and open the `SchoolBot` folder

#### Direct Download
1. Navigate [here](https://github.com/mattmoody05/SchoolBot) and click the 'code' button
2. Select the 'download zip' option
3. Unzip the file and navigate into it (should be called `SchoolBot-main`)


## Installing Pip Dependencies

#### Requirements.txt working
1. Navigate to the folder of the bot within terminal / powershell
2. Run `pip3 install requirements.txt`

#### Requirements.txt not working
1. Navigate to the folder of the bot within terminal / powershell
2. In the case that the last step did not work, please see the list of dependencies [here](./other/Dependencies.md). To install these dependencies, use `pip3 install DependencyName`


## Installing JDK

#### Use the links below and follow the install process

- [Windows](https://download.oracle.com/otn-pub/java/jdk/15.0.1%2B9/51f4f36ad4ef43e39d0dfdbaf6549e32/jdk-15.0.1_windows-x64_bin.exe)
- [macOS](https://download.oracle.com/otn-pub/java/jdk/15.0.1%2B9/51f4f36ad4ef43e39d0dfdbaf6549e32/jdk-15.0.1_osx-x64_bin.dmg)
- [Linux](https://download.oracle.com/otn-pub/java/jdk/15.0.1%2B9/51f4f36ad4ef43e39d0dfdbaf6549e32/jdk-15.0.1_linux-x64_bin.deb)


## Installing the postgreSQL database

Please note, the instructions for this section are designed in a way that they are able to be used on all platforms, use common sense when applying them

1. Downlaod the latest supported version of PostgreSQL for you operating system from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2. Follow the installation process making sure that the option to install pgadmin4 is selected if you come accross it. In the installation, you will be asked to input a password and port, make sure that you write these two pieces of information down somewhere, they will be important later. (The default port is 5432)
3. Run the pgadmin4 application that should've been installed during the installation process, a web browser should open, this is where you will need to enter the password you provided before
4. Download [this](./other/postgreSQL-install.py) file
5. In the file, in the variables at the start of the file,input the password and port you entered before (the default port already being there)
6. Run the now modified python file

## Discord bot account

#### Creating the bot account
1. Navigate to [this](https://discord.com/developers/applications) website and sign in with your discord account if you are not already
2. Click the 'new application' button in the top right hand corner and name the bot a recognisable name (this doe not have to be the final name of the bot account)
3. Open the 'Bot' tab of your discord application
4. Click 'Add Bot', then 'Yes, do it!'
5. If you would like to rename your bot, you are able to do it on this page

#### Getting your bot token
1. Still on the bot page of your application, underneath the name of your bot, click the 'Copy' button. Now, paste this token somewhere you can find later.
2. **IMPORTANT** - Do not give this token out to anyone else, it would allow them to take complete control of your bot account.

#### Adding the bot to your server
1. Navigate to the 'OAuth2' page
2. Under the 'scopes' category, tick the 'bot' box
3. Under the newly revealed 'Bot Permissions' category, tick the 'Administrator' box
4. Scrolling back up to the 'scopes' section, there should now be a link generated, open this link and follow the normal bot adding process for discord

## Configuring the config.json file

#### Discord config
1. In the 'token' field, input the bot token you generated and wrote down earlier
2. In the 'prefix' field, input your desired bot prefix (by default this is `$`)

#### Database Config
1. Input the port of the database you specified earlier into the 'port' field, by default this will be 5432
2. Input the password you spefified earlier in the 'password' field

### Lavalink Config
1. Before you run the bot, open cmd in the parent folder and make sure you have Java 13 installed.
2. Type `java -jar .\Lavalink.jar` and hit enter.
3. Lavalink server should be start running.

## Running the bot

#### Windows
1. Navigate to the bot folder within powershell
2. Run the command `py -3 bot.py`
3. If all working properly, your should see `x.py has been loaded` and `logged in as BotAccountName#1234` in your powershell window

#### macOS / Linux
1. Navigate to the bot folder within powershell
2. Run the command `python3 bot.py`
3. If all working properly, your should see `x.py has been loaded` and `logged in as BotAccountName#1234` in your terminal window

## Still having issues?
Yes, even if you have followed these instructions exactly, you may still be having issues, and we are happy to help. Just follow one of the ways outlined below to get help.

#### Github issues
1. Navigate to the Github repo for this bot
2. Open the 'issue' tab
3. Create a new issue. When creating your issue, please describe the issue you are having in detail, including any error outputs. No information is too much!

#### Discord server
- Our discord support server can be found [here](https://discord.gg/Fhukqpu), where you can contact both of us with quick replies.
- If you are in need of quick support, don't be afraid to @us, it will enable us to help you faster
- Make sure you provide enough detail of your issue, the more detail, the better

#### The internet!
- If you believe that the solution is obvious, the internet is a great place to find it
- If you believe your issue is to do with our code, it would be better to contact us, but for general install errors, the internet could do just great
