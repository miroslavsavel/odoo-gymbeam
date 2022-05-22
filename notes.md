instalacia
-> pridaj na git

>> win pycharm
https://www.odoo.com/documentation/15.0/administration/install/install.html

>>setup in pycharm
https://amirulm.medium.com/how-i-setup-pycharm-to-ease-odoo-development-e17a4089422f

>>first module
https://amirulm.medium.com/create-custom-module-odoo-9ce1234da3a7

nainstaloval som ho do C:\Users\miros\PycharmProjects>
?? difference python 2x and 3x
stiahol som do downloads postgre sql 14.3.1



-------------------------zadanie

instalacia docker odoo 13

https://www.how2shout.com/linux/how-to-install-odoo-13-or-14-on-docker-container/

https://blog.desdelinux.net/en/instalar-odoo-docker-anadir-modulos-externos/

https://techviewleo.com/how-to-run-odoo-in-docker-containers/

 

 

# create new addon

https://blog.desdelinux.net/en/instalar-odoo-docker-anadir-modulos-externos/

 

https://medium.com/@dupski/creating-and-installing-your-first-odoo-module-using-docker-and-visual-studio-code-41ebdfd362e4

https://medium.com/@dupski/odoo-development-running-odoo-in-docker-85a4cd41b4f0

https://medium.com/@dupski/odoo-development-running-postgresql-in-docker-702406520c03

 

https://www.odoo.com/documentation/15.0/administration/odoo_sh/getting_started/first_module.html

https://quickhax.com/install-odoo-docker-add-external-modules/

https://www.holdenrehg.com/blog/2021-06-03_odoo-docker-quickstart

 

add employee field

https://www.odoo.com/forum/help-1/add-a-field-in-employee-module-178377

https://www.odoo.com/forum/help-1/new-field-for-employe-157928

              https://www.cybrosys.com/blog/adding-custom-fields-to-existing-views-in-odoo-v12

             

             

///

Odoo dev mode

https://www.cybrosys.com/blog/what-is-odoo-developer-mode#:~:text=Developer%20mode%20in%20Odoo%20is,for%20various%20features%20in%20Odoo.

 

 

--docker check na work PC

-docker compose - tento volam

-docker file tam kde su zdrojaky ako zbuildit masinu



==================================================
# nejde ubuntu VM 21.5.2022
https://www.cyberithub.com/solved-cannot-enable-nested-vt-x-amd-v-without-nested-paging/

stiahol som novu verziu virtualboxu

stiahnem ubuntu

nejdu stale ni ostatne virtualne operacne systemy
preto znova zapnem funcionality

C:\>bcdedit /set hypervisorlaunchtype off
a vo windows features virtual machine platform>>
https://parsons-technology.com/how-do-i-turn-on-hypervisorlaunchtype/#:~:text=How%20do%20you%20use%20Hypervisorlaunchtype,entry%20to%20auto%20start%20hypervisor.

https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/

# what is hyper-v and how it works?
https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview

- zrejme bola stara verzia virtualboxu a ja som iba po reinstalle zabudol zapnut opat vo windows features virtual machine platform>>
lebo bcdedit /set hypervisorlaunchtype off som neprepinal

# fresh install ubuntu
- https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview

- instalujem virtualbox guest addition
- po device a vybere insert guest adition
https://askubuntu.com/questions/22743/how-do-i-install-guest-additions-in-a-virtualbox-vm
idem spustit autoruns.sh na virtualnom CD

vo windows features som aktivoval vsetko ohladom hyper-V
pri spusteni autorun skriptu
-> potrebujem rozchodit clipboard a resolution

pri instalacii VBox_Gas mi hadze pri spusteni mi nechce spustit autorun.sh
skusam sudo apt-get install virtual-box-guest-additions-iso

///vyriesene
https://help.ubuntu.com/community/VirtualBox/GuestAdditions
./autorun.sh
->>>> funguje clipboard!!!


------------------------------------------------------
# fresh docker install
- https://docs.docker.com/engine/install/ubuntu/
Set up the repository
Update the apt package index and install packages to allow apt to use a repository over HTTPS:

 sudo apt-get update
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
Add Docker’s official GPG key:

 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.

 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 

>> tee command reads the standard input and writes it to both the standard output and one or more files. The command is named after the T-splitter used in plumbing. It basically breaks the output of a program so that it can be both displayed and saved in a file. It does both the tasks simultaneously, copies the result into the specified files or variables and also display the result.



# overenie dockeru
Verify that Docker Engine is installed correctly by running the hello-world image.

 sudo docker run hello-world

>>OK
Hello from Docker!
This message shows that your installation appears to be working correctly.
To generate this message, Docker took the following steps:

 1. The Docker client contacted the Docker daemon.

 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.

    (amd64)

 3. The Docker daemon created a new container from that image which runs the

    executable that produces the output you are currently reading.

 4. The Docker daemon streamed that output to the Docker client, which sent it

    to your terminal.
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash


??what is docker image
??what is docker pull
??how docker works pozri network chucka
??docker file
??docker compose
??docker container

 # install Odoo 13
 Install Odoo Docker Image
Well. once you have Docker on your system, to install Odoo Container, we just need to run a single command. It is because the Docker hub already has a pre-built official image of Odoo.
- sudo docker pull odoo:13

Install PostgreSQL Database Docker Image
The next thing we need to set up is the database for Odoo to save its data on Docker. Well, just like any other popular app, we already have a pre-built image for this database as well. Hence, just on your command terminal type-
- sudo docker pull postgres

Create Database Container
Well, we already have downloaded the PostgreSQL image above, now we will use the same to create a container with a database.
- sudo docker run -d -v odoo-db:/var/lib/postgresql/data -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres

Create and Run Odoo Container
- sudo docker run -v odoo-data:/var/lib/odoo -d -p 8069:8069 --name odoo --link db:db -t odoo:13

 Open Port in firewall
- sudo ufw allow 8069

http://127.0.0.1:8069/

http://127.0.0.1:8069/web/database/selector
db name > gymbeam
miroslav.savel@gmail.com
pass> gymbeam
http://127.0.0.1:8069/web/database/selector

ako si stopnut docker container?
https://linuxhandbook.com/docker-stop-container/
docker stop odoo
docker stop db


>>OK system bezi ale teraz chcem vytvorit vlastny addon:
https://blog.desdelinux.net/en/instalar-odoo-docker-anadir-modulos-externos/

# Creating our docker-compose.yml file
Once we have installed docker, we must create the file docker-compose.yml In the directory of our preference, it will contain basically all the information necessary to deploy our service with Odoo.
- install vs code with software

folder>
/home/ubuntu/Odoo
pridam ju do VS code
vytvorim docker-compose.yml

into this file i will ad
version: '2' services: odoo: image: odoo: 8 restart: always ports: - "8069: 8069" links: - db volumes: - ./extra-addons:/mnt/extra-addons db: image: postgres: 9.4 restart: always environment: - POSTGRES_USER = odoo - POSTGRES_PASSWORD = odoo

??how docker compose works
https://strapi.io/blog/what-is-docker-compose-all-you-need-to-know
Docker puts several tools at the disposal of developers to help them create containerized applications, including Dockerfile, Docker image, Docker run, Docker Hub, Docker Engine, and more

One of the main benefits of Docker Compose is its huge portability. The command 
docker-compose up 
alone is enough to bring up a whole development environment, which can then be torn down by utilizing 
docker-compose down.
- docker-compose up -d

# installation of program Docker-compose
pip install docker-compose

instalujem pip
sudo apt install python3-pip
pip install docker-compose
sudo service docker restart
docker-compose up -d

ako si pisu yaml???
ako si napisat spravne docker-compose??
https://stackoverflow.com/questions/44450265/what-is-a-docker-compose-yml-file

>>
# tuto najdes postup!!!!na pridanie addonu
https://hub.docker.com/_/odoo/
Mount custom addons
You can mount your own Odoo addons within the Odoo container, at /mnt/extra-addons

Start a PostgreSQL server
- docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13

            docker: Error response from daemon: Conflict. The container name "/db" is already in use by container "8a66f71856b11019effccdb12b80cef8c740f9f5b1913e3175294da8d92f53c8". You have to remove (or rename) that container to be able to reuse that name.
            See 'docker run --help'.

            docker how to remove container??
            https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/
            The docker system prune command removes all stopped containers, dangling images, and unused networks:

            docker system prune!!!!!!!!!!!!!!!!!!
            pokracujem >>
    - docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13

Start an Odoo instance
    - sudo docker run -p 8069:8069 --name odoo --link db:db -t odoo

Stop and restart an Odoo instance
    $ docker stop odoo
    $ docker start -a odoo

Use named volumes to preserve data
    When the Odoo container is created like described above, the odoo filestore is created inside the container. If the container is removed, the filestore is lost. The preferred way to prevent that is by using a Docker named volume.

    http://127.0.0.1:8069/web/database/selector
    dal som heslo do odoo db

    sudo docker run -v odoo-data:/var/lib/odoo -d -p 8069:8069 --name odoo --link db:db -t odoo
    /hlasi mi konflik medzi menami containerov
    therefore I will kill them all
    sudo docker system prune
    sudo docker run -v odoo-data:/var/lib/odoo -d -p 8069:8069 --name odoo --link db:db -t odoo

    sudo docker run -d -v odoo-db:/var/lib/postgresql/data -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13

    1, stopnut kontainery prikazom stop
        sudo docker stop odoo
        sudo docker stop db
        sudo docker ps
    2, premazat ich system prune
        sudo docker system prune
    3, znova ich oba na novo pridat
        sudo docker run -v odoo-data:/var/lib/odoo -d -p 8069:8069 --name odoo --link db:db -t odoo

        sudo docker run -d -v odoo-db:/var/lib/postgresql/data -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13


znova som pustil odoo a db kontainery

ked chcem vytvorit volume 
docker: Error response from daemon: Conflict. The container name "/odoo" is already in use by container "4c45d44511e542a5914da2b837d4b1e0010bad18bfad8e768889ed733d263efe". You have to remove (or rename) that container to be able to reuse that name.

https://stackoverflow.com/questions/65768782/how-to-fix-docker-error-response-from-daemon-cannot-link-to-a-non-running-con
how to remove volumes docker

docker volume ls
docker volume inspect odoo-data


---------DAY D
https://github.com/minhng92/odoo-13-docker-compose
https://www.cybrosys.com/blog/how-to-install-odoo-13-using-docker

curl -s https://raw.githubusercontent.com/minhng92/odoo-13-docker-compose/master/run.sh | sudo bash -s odoo-one 10013 20013
curl -s https://raw.githubusercontent.com/minhng92/odoo-13-docker-compose/master/run.sh | sudo bash -s odoo-two 11013 21013
docker-compose up

otvorim prehliadac a zapisem master password
minhng.info
db name > db
miroslav.savel@gmail.com
pass> odoo

1,zapnut dev mode v odoo
https://www.odoo.com/forum/help-1/how-to-activate-developer-mode-in-odoo-13-ce-157346#:~:text=You%20can%20activate%20the%20developer%20mode%20in%20Odoo,the%20Developer%20Mode%20option%20with%20three%20different%20categories
Just an additional comment, the "General Settings" won't appear if you haven't enabled any apps. So if you just see "Users & Companies" in the "Settings" menu, enable ANY one app (e.g. CRM.) Then follow the instructions by Niyas (10/15/19) or Odoo Tools (10/15/19)
- nainstalujem CRM aplikaciu

teraz sa mi uz zobrazi settings a general settings
https://medium.com/@dupski/creating-and-installing-your-first-odoo-module-using-docker-and-visual-studio-code-41ebdfd362e4

Now that Developer mode is enabled; in the Apps area of Odoo, you should see an “Update Apps List” menu item. Hit that, then hit the “Update” button on the screen that appears, to refresh the list of available apps.

create folder on odoo-one/prvy_addon
    __init__.py
    __manifest__.py

dam do vyhladavaca Prvy-custom
nainstaloval som employees module


https://www.odoo.com/forum/help-1/add-a-field-in-employee-module-178377



# /////////////////////////////////////////INSTALL from source - WIN11
C:\Users\miros\PycharmProjects\odoo>
- zdrojaky

# PostgreSQL
Odoo uses PostgreSQL as database management system. Download and install PostgreSQL (supported version: 10.0 and later).
C:\Program Files\PostgreSQL\14\bin

superuser postgres
postgres
port na ktorom server pocuva 5432

pridam pgAdmin do windows path
https://stackoverflow.com/questions/11460823/setting-windows-path-for-postgres-tools
echo %PATH%

stiahol som pgAdmin
https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.9/windows/
nainstalovane do users local Admin pgAdmin
- masterpass postgres

vytvoril som ucet odoo v pgAdmine
teraz idem instalovat dependencie

Navigate to the path of your Odoo Community installation (CommunityPath) and run pip on the requirements file in a terminal with Administrator privileges:

C:\> cd \CommunityPath
C:\> pip install setuptools wheel
C:\> pip install -r requirements.txt

# Running Odoo
Once all dependencies are set up, Odoo can be launched by running odoo-bin, the command-line interface of the server. It is located at the root of the Odoo Community directory.

python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb

python odoo-bin -r odoo -w odoo --addons-path=addons -d mydb

toto mi hlasi chybu v odoo



# ///////////////////////////instalacia Odoo from source Linux
sekcia Linux
https://www.odoo.com/documentation/15.0/administration/install/install.html
stahujem z git repozitar

zatial skusam vytvorit prvy addon 
https://www.cybrosys.com/blog/how-create-module-odoo
vo VS code sa da naformatovat XML tak ze kliknes pravym a das format



##  Zadanie vypracujem na dockery, nakolko win from source mi nejde odo-bin a nie je uz cas na hranie sa so source v linuxe
""""""""""""""""""https://www.odoo.com/forum/help-1/add-a-field-in-employee-module-178377
funguje!!

pridal som char field pod work_email
ale ed chcem pridat dalsi field tak mi nejde

skusim zastavit a spustit kontainer!!!!!!!!!!!!!!!!!!!
http://localhost:10013
sudo docker stop odoo-one_odoo13_1
sudo docker start odoo-one_odoo13_1

screenshot na github
<a href="https://ibb.co/kMftcfs"><img src="https://i.ibb.co/vDGSzG6/1.png" alt="1" border="0"></a><br /><a target='_blank' href='https://usefulwebtool.com/russian-keyboard'>russian keyboard online</a><br />


2. create 3 new integer fields on the Private information tab
https://www.odoo.com/sk_SK/forum/pomoc-1/use-onchange-on-one-record-to-change-fields-on-other-records-185600
https://www.odoo.com/documentation/15.0/developer/howtos/rdtraining/09_compute_onchange.html
https://www.odoo.com/documentation/15.0/developer/howtos/rdtraining/03_newapp.html

chcem pridat tax za pole salary
onchange, depends, compute...)


