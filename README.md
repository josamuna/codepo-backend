[![](https://user-images.githubusercontent.com/46261770/79870277-9a490b00-8397-11ea-88ac-e8dc25124084.png)](https://monitor-engine.com)

# Monitor Engine (Backend)

> Cette partie est une suite de la documentation du projet se trouvant à ce repository: [Documentation initiale du projet Monitor-Engine](https://github.com/josamuna/codepo-fontend)

## Table des Matières

1. [Structure du projet](#Structure-Projet)
2. [Environnement de développement](#Environnement)
3. [Dépendances du projet](#Dépendances)
4. [Exécution du projet](#Exécution)
5. [Console d'administration](#Console-Administration)
6. [Déploiement / Hébergement](#Déploiement)
7. [Récommendations](#Récommandations)

### Structure du projet

***

#### `1.` Backend 
La structure du projet reprend les dossiers et fichiers suivants détaillés dans cette arborescence:

```
../monitor/
│
├── rptree/
│   ├── __pycache__/
│   │   ├── rptree.cpython-36.pyc
│   │   ├── cli.cpython-36.pyc
│   │   └── __init__.cpython-36.pyc
│   │
│   ├── __init__.py
│   ├── rptree.py
│   └── cli.py
│
├── monitor_engine/
│   ├── migrations/
│   │   ├── 0006_auto_20210714_1443.py
│   │   ├── 0003_auto_20210708_0919.py
│   │   ├── 0004_auto_20210708_1246.py
│   │   ├── 0012_notification_caseid.py
│   │   ├── 0014_auto_20210723_1042.py
│   │   ├── 0017_measured_autonomy.py
│   │   ├── 0018_auto_20210730_0853.py
│   │   ├── 0011_auto_20210719_1029.py
│   │   ├── 0008_userpreference.py
│   │   ├── 0007_auto_20210715_1035.py
│   │   ├── 0009_auto_20210717_0450.py
│   │   ├── __init__.py
│   │   ├── 0016_auto_20210726_1205.py
│   │   ├── 0021_auto_20220222_2134.py
│   │   ├── 0010_userpreference_user_id.py
│   │   ├── 0020_alter_command_id_alter_commandhistory_id_and_more.py
│   │   ├── 0019_auto_20210730_0857.py
│   │   ├── 0015_device_total_capacity.py
│   │   ├── 0005_auto_20210708_1251.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20210708_0918.py
│   │   └── 0013_auto_20210723_1041.py
│   │
│   ├── __pycache__/
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   └── __init__.cpython-36.pyc
│   │
│   ├── tests.py
│   ├── codepoBackend
│   ├── admin.py
│   ├── consumers.py
│   ├── tasks.py
│   ├── routing.py
│   ├── serializers.py
│   ├── urls.py
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── .admin.py.swp
│   └── views.py
│
├── monitor/
│   ├── __pycache__/
│   │   ├── wsgi.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── celery.cpython-36.pyc
│   │   └── __init__.cpython-36.pyc
│   │
│   ├── asgi.py
│   ├── settings.py
│   ├── celery.py
│   ├── routing.py
│   ├── urls.py
│   ├── __init__.py
│   └── wsgi.py
│
├── celerybeat-schedule.dat
├── tree.py
├── manage.py
├── package-lock.json
├── package.json
├── celerybeat-schedule.dir
├── info
├── start-celery-process.sh
├── start-python.sh
├── dump.rdb
└── celerybeat-schedule.bak
```

- `monitor` est le module principal. 
- `../monitor/start-celery-process.sh` permet de démarrer `celery-beat` en background task qui à son tour se chargera de lancer le `celery-worker` qui exécute une tâche (Celle de mise à jour des paramètres du device).
- `../monitor/start-python.sh` démarre le `runserver` de python en background task en mode production en utilisant `gunicorn` et non en mode developpement, afin de prendre en charge le backend.
- `../monitor/monitor-engine/migrations` répertorie toutes les migrations déjà exécutées dans le projet (Lors de la traduction du modèle vers le Système de Gestion de Base de Données MySQL).
- `../monitor/monitor/celery.py` pour la gestion de l'écoute du serveur et le cadensement du scheduler.
- `../monitor/monitor/routing.py` rédirige correctement le .........
- `../monitor/monitor/settings.py` comprend tous les paramètres de configuration pour la gestion des différentes intéractions entre l'interface utilisateur et les autres parties du système: Assure le bon fonctionnement du Backend.
- `../monitor/monitor/urls.py` pour la spécification des URL d'accès.
- `../monitor/monitor/asgi.py` .........
- `../monitor/monitor-engine/admin.py` .........
- `../monitor/monitor-engine/apps.py` spécifie le nom de l'application.
- `../monitor/monitor-engine/codepoBackend` spécifie les adresses pour le serveur distant et celui en local.
- `../monitor/monitor-engine/consumers.py` .........................
- `../monitor/monitor-engine/models.py` reprend le modèle (de la partie Modèle du MVC) qui servira au reverse engineering pour la création de la Base de Données en mode commande.
- `../monitor/monitor-engine/routing.py` ..................................
- `../monitor/monitor-engine/serializers.py` ..............................
- `../monitor/monitor-engine/tasks.py` gère les actions automatisées par celery.
- `../monitor/monitor-engine/urls.py` ..............................
- `../monitor/monitor-engine/views.py` ..............................
- `../monitor/rptree/` contient les fichiers nécessaire pour générer le fichier `markdown-file-tree.md` en mode commande en utilisant le fichier `../monitor/tree.py`.
- `../monitor/manage.py` fichier principal pour l'exécution des taches en mode administrateur (Comme l'installation d'un pacquet, l'exécution de l'application, etc.).

Pour arriver à générer le fichier relatif à l'arborescence des dossiers et fichiers `markdown-file-tree.md` ([Voir dans ce repository](https://github.com/javitocor/Python-Direcory-Tree-Generator)), procéder comme suit:
- Se positionner dans le répertoire principale du module: 

    ```
    cd codepo-backend/monitor/
    ```
- Taper la commande: 
    
    ```
    python3 tree.py ../monitor -o ../markdown-file-tree.md
    ```

#### `2.` Frontend 

La structure du projet reprend les dossiers et fichiers suivants détaillés dans cette arborescence:

- [..\codepo\-frontend](codepo\-frontend)
    - [CHANGELOG.md](CHANGELOG.md)
   - [CONTRIBUTING.md](CONTRIBUTING.md)
   - [LICENSE.md](LICENSE.md)
   - [README.md](README.md)
   - [dump.rdb](dump.rdb)
   - [jsconfig.json](jsconfig.json)
   - [markdown\-file\-tree.md](markdown-file-tree.md)
   - [node\_modules](node_modules)
   - [package\-lock.json](package-lock.json)
   - [package.json](package.json)
   - __public__
     - [\_redirects](public/_redirects)
     - [favicon.ico](public/favicon.ico)
     - __image__
       - [loginImg.png](public/image/loginImg.png)
     - [index.html](public/index.html)
     - [manifest.json](public/manifest.json)
     - __static__
       - __images__
         - [auth.jpeg](public/static/images/auth.jpeg)
         - __avatars__
           - [avatar\_6.png](public/static/images/avatars/avatar_6.png)
         - [not\_found.png](public/static/images/not_found.png)
         - __products__
           - [product\_1.png](public/static/images/products/product_1.png)
           - [product\_2.png](public/static/images/products/product_2.png)
           - [product\_3.png](public/static/images/products/product_3.png)
           - [product\_4.png](public/static/images/products/product_4.png)
           - [product\_5.png](public/static/images/products/product_5.png)
           - [product\_6.png](public/static/images/products/product_6.png)
         - [thingstream\_click.jpeg](public/static/images/thingstream_click.jpeg)
         - [undraw\_page\_not\_found\_su7k.svg](public/static/images/undraw_page_not_found_su7k.svg)
         - [undraw\_resume\_folder\_2\_arse.svg](public/static/images/undraw_resume_folder_2_arse.svg)
       - [logo.svg](public/static/logo.svg)
   - __src__
     - [App.js](src/App.js)
     - __assets__
       - [Add\_files\_re\_v09g.png](src/assets/Add_files_re_v09g.png)
       - [Add\_files\_re\_v09g.svg](src/assets/Add_files_re_v09g.svg)
       - [Notify\_re\_65on.png](src/assets/Notify_re_65on.png)
       - [Notify\_re\_65on.svg](src/assets/Notify_re_65on.svg)
       - [Throw\_away\_re\_x60k.png](src/assets/Throw_away_re_x60k.png)
       - [Throw\_away\_re\_x60k.svg](src/assets/Throw_away_re_x60k.svg)
       - [Updates\_re\_o5af.png](src/assets/Updates_re_o5af.png)
       - [Updates\_re\_o5af.svg](src/assets/Updates_re_o5af.svg)
       - [broadcast\_jhwx.png](src/assets/broadcast_jhwx.png)
       - [broadcast\_jhwx.svg](src/assets/broadcast_jhwx.svg)
       - [empty\_cart\_co35.png](src/assets/empty_cart_co35.png)
       - [empty\_xct9.png](src/assets/empty_xct9.png)
       - [empty\_xct9.svg](src/assets/empty_xct9.svg)
       - [loginImg.png](src/assets/loginImg.png)
       - [server\_down\_s4lk.png](src/assets/server_down_s4lk.png)
       - [server\_down\_s4lk.svg](src/assets/server_down_s4lk.svg)
       - [warning\_cyit.png](src/assets/warning_cyit.png)
       - [warning\_cyit.svg](src/assets/warning_cyit.svg)
     - [auth\-header.js](src/auth-header.js)
     - [axios.js](src/axios.js)
     - __components__
       - [GlobalStyles.js](src/components/GlobalStyles.js)
       - [Logo.js](src/components/Logo.js)
       - __Modal__
         - [AddCmdDeviceModal.js](src/components/Modal/AddCmdDeviceModal.js)
         - [AddCommandModal.js](src/components/Modal/AddCommandModal.js)
         - [AddDeviceForm.js](src/components/Modal/AddDeviceForm.js)
         - [AddUserModal.js](src/components/Modal/AddUserModal.js)
         - [CommandDevice.js](src/components/Modal/CommandDevice.js)
         - [ConfirmationMessage.js](src/components/Modal/ConfirmationMessage.js)
         - [FollowingDevice.js](src/components/Modal/FollowingDevice.js)
         - [Modal.js](src/components/Modal/Modal.js)
         - [ModalStyle.css](src/components/Modal/ModalStyle.css)
         - [SuccessMessage.js](src/components/Modal/SuccessMessage.js)
       - __Modal2__
         - [ErrorMessage.js](src/components/Modal2/ErrorMessage.js)
         - [Modal.js](src/components/Modal2/Modal.js)
       - [Page.js](src/components/Page.js)
       - [errorToastNotification.js](src/components/errorToastNotification.js)
       - [infoToastNotification.js](src/components/infoToastNotification.js)
       - [successToastNotification.js](src/components/successToastNotification.js)
     - [history.js](src/history.js)
     - __i18n__
       - [en.json](src/i18n/en.json)
       - [fr.json](src/i18n/fr.json)
     - [i18n.js](src/i18n.js)
     - __icons__
       - [Facebook.js](src/icons/Facebook.js)
       - [Google.js](src/icons/Google.js)
     - __image__
       - [Image.js](src/image/Image.js)
       - [loginImg.jpg](src/image/loginImg.jpg)
       - [loginImg.png](src/image/loginImg.png)
       - [loginImg1.png](src/image/loginImg1.png)
       - [undraw\_empty\_cart\_co35 (1).svg](src/image/undraw_empty_cart_co35%20(1).svg)
       - [undraw\_empty\_xct9 (1).svg](src/image/undraw_empty_xct9%20(1).svg)
     - [index.js](src/index.js)
     - __layouts__
       - __DashboardLayout__
         - [CardNotification.js](src/layouts/DashboardLayout/CardNotification.js)
         - __NavBar__
           - [NavItem.js](src/layouts/DashboardLayout/NavBar/NavItem.js)
           - [index.js](src/layouts/DashboardLayout/NavBar/index.js)
         - [Notification.js](src/layouts/DashboardLayout/Notification.js)
         - [NotificationObject.js](src/layouts/DashboardLayout/NotificationObject.js)
         - __Profile__
           - __Profile__
             - [Profile.js](src/layouts/DashboardLayout/Profile/Profile/Profile.js)
             - [index.js](src/layouts/DashboardLayout/Profile/Profile/index.js)
         - [TopBar.js](src/layouts/DashboardLayout/TopBar.js)
         - [index.js](src/layouts/DashboardLayout/index.js)
       - __MainLayout__
         - [TopBar.js](src/layouts/MainLayout/TopBar.js)
         - [index.js](src/layouts/MainLayout/index.js)
     - __mixins__
       - [chartjs.js](src/mixins/chartjs.js)
     - [routes.js](src/routes.js)
     - [serviceWorker.js](src/serviceWorker.js)
     - __theme__
       - [index.js](src/theme/index.js)
       - [shadows.js](src/theme/shadows.js)
       - [typography.js](src/theme/typography.js)
     - [user\-connected.js](src/user-connected.js)
     - __utils__
       - [getInitials.js](src/utils/getInitials.js)
     - __views__
       - __Login__
         - [Login.js](src/views/Login/Login.js)
       - __Redux__
         - [MagasinEtat.js](src/views/Redux/MagasinEtat.js)
         - [Store.js](src/views/Redux/Store.js)
       - __User__
         - [Results.js](src/views/User/Results.js)
         - [Toolbar.js](src/views/User/Toolbar.js)
         - [UserView.js](src/views/User/UserView.js)
         - [data.js](src/views/User/data.js)
       - __commande__
         - [ComandeView.js](src/views/commande/ComandeView.js)
         - [FormValidation.js](src/views/commande/FormValidation.js)
         - [Results.js](src/views/commande/Results.js)
         - [Toolbar.js](src/views/commande/Toolbar.js)
         - [data.js](src/views/commande/data.js)
       - __corbeille__
         - __CorbeilleView__
           - [Results.js](src/views/corbeille/CorbeilleView/Results.js)
           - [Toolbar.js](src/views/corbeille/CorbeilleView/Toolbar.js)
           - [commandTable.js](src/views/corbeille/CorbeilleView/commandTable.js)
           - [devicesTable copy.js](src/views/corbeille/CorbeilleView/devicesTable%20copy.js)
           - [devicesTable.js](src/views/corbeille/CorbeilleView/devicesTable.js)
           - [index.js](src/views/corbeille/CorbeilleView/index.js)
           - [userTable.js](src/views/corbeille/CorbeilleView/userTable.js)
       - __devices__
         - __DeviceListView__
           - [DeviceCard.js](src/views/devices/DeviceListView/DeviceCard.js)
           - [Results.js](src/views/devices/DeviceListView/Results.js)
           - [Toolbar.js](src/views/devices/DeviceListView/Toolbar.js)
           - [index.js](src/views/devices/DeviceListView/index.js)
       - __errors__
         - [NotFoundView.js](src/views/errors/NotFoundView.js)
       - __maps__
         - __MapView__
           - [AngularGauge.js](src/views/maps/MapView/AngularGauge.js)
           - [DevicesDrow.js](src/views/maps/MapView/DevicesDrow.js)
           - [GaugeView.js](src/views/maps/MapView/GaugeView.js)
           - [Map.css](src/views/maps/MapView/Map.css)
           - [MapsView.js](src/views/maps/MapView/MapsView.js)
           - [SearchControl.js](src/views/maps/MapView/SearchControl.js)
           - [index.js](src/views/maps/MapView/index.js)
           - [react\-leaflet\-geosearch.css](src/views/maps/MapView/react-leaflet-geosearch.css)
           - [savedMap.js](src/views/maps/MapView/savedMap.js)
           - [style.css](src/views/maps/MapView/style.css)
       - __reports__
         - __DashboardView__
           - [ActiveDevices.js](src/views/reports/DashboardView/ActiveDevices.js)
           - [ActiveUsers.js](src/views/reports/DashboardView/ActiveUsers.js)
           - [BatteryLevel.js](src/views/reports/DashboardView/BatteryLevel.js)
           - [DevicesResults.js](src/views/reports/DashboardView/DevicesResults.js)
           - [TotalDevices.js](src/views/reports/DashboardView/TotalDevices.js)
           - [TotalUsers.js](src/views/reports/DashboardView/TotalUsers.js)
           - [index.js](src/views/reports/DashboardView/index.js)
       - __search__
         - __SearchDeviceListView__
           - [HistoryDetaille.js](src/views/search/SearchDeviceListView/HistoryDetaille.js)
           - [Results.js](src/views/search/SearchDeviceListView/Results.js)
           - [Toolbar.js](src/views/search/SearchDeviceListView/Toolbar.js)
           - [index.js](src/views/search/SearchDeviceListView/index.js)
       - __services__
         - [WebSocket.js](src/views/services/WebSocket.js)
         - [config.js](src/views/services/config.js)
       - __settings__
         - __SettingsView__
           - [ChangeColor.js](src/views/settings/SettingsView/ChangeColor.js)
           - [ColorLevel1.js](src/views/settings/SettingsView/ColorLevel1.js)
           - [Level2.js](src/views/settings/SettingsView/Level2.js)
           - [Level3.js](src/views/settings/SettingsView/Level3.js)
           - [Notifications.js](src/views/settings/SettingsView/Notifications.js)
           - [Password.js](src/views/settings/SettingsView/Password.js)
           - [index.js](src/views/settings/SettingsView/index.js)


- `codepo-frontend` est le répertoire principal du projet. 
- `../public/favicon.ico` est le fichier correspondant à l'icône de l'application.
- `../src` ...........................
- `../src/assets` ...........................
- `../src/components` ...........................
- `../src/icons` ...........................
- `../src/image` ...........................
- `../src/layouts` ...........................
- `../src/layouts\DashboardLayout` ...........................
- `../src/layouts\NavBar` ...........................
- `../src/layouts\Profile` ...........................
- `../src/layouts\MainLayout` ...........................
- `../src/theme` ...........................
- `../src/utils` ...........................
- `../src/views` ...........................
- `../src/views/Login` ...........................
- `../src/views/Redux` ...........................
- `../src/views/User` ...........................
- `../src/views/commande` ...........................
- `../src/views/corbeille` ...........................
- `../src/views/corbeille/CorbeilleView` ...........................
- `../src/views/devices` ...........................
- `../src/views/corbeille/DeviceListView` ...........................
- `../src/views/errors` ...........................
- `../src/views/maps` ...........................
- `../src/views/corbeille/MapView` ...........................
- `../src/views/reports` ...........................
- `../src/views/corbeille/DaschboardView` ...........................
- `../src/views/search` ...........................
- `../src/views/corbeille/SearchDeviceListView` ...........................
- `../src/views/services` ...........................
- `../src/views/settings` ...........................
- `../src/views/settings/SettingsView` ...........................

Pour arriver à générer le fichier relatif à l'arborescence des dossiers et fichiers `markdown-file-tree.md` ([Voir dans ce repository](https://github.com/michalbe/md-file-tree)), procéder comme suit:

`Les commandes pour cette opération ne sont valide que sur un shell Linux, à defaut sur Windows, `***Git Bash***` pourrait être utilisé à la place`.

- Se positionner dans le répertoire principale du projet: 

    ```
    cd codepo-frontend/
    ```
    
- Installer le paquet nécessaire pour la génération de l'arborescence: 
    
    ```
    npm install md-file-tree
    ```
    
- Générer le fichier `.md` par la commande suivante (Il n'est pas nécessaire de créer le fichier avant, la commande le fait à notre place): 
    
    ```
    md-file-tree > markdown-file-tree.md
    ```

### Environnement de développement

***

Le projet dans son intégralité (***Frontend*** et ***Backend***) a été développé avec la plateforme [Linux Mint 19.3 Tricia](https://linuxmint.com/edition.php?id=274) qui est basé sur [Ubuntu 18.04 bionic](https://releases.ubuntu.com/18.04/). 
L'editeur de texte utilisé pour le projet est [Visual Studio Code](https://code.visualstudio.com/#alt-downloads) en sa version `1.64.2`, et le navigateur web Mozilla Firefox For Linux Mint en sa version `97.0.1`.
    
### Dépendances du projet

***

Pour arriver à effectuer un **build** du projet, un certain nombre des dépendances est requise (Néanmoins avec un IDE telque [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) l'installation de ces dernières devient plus au moins aisée: *Quand bien même cette option semble plus au moins aisée, elle peut conduire à beaucoup d'incompatibilités comme cela a été le cas; et par conséquent Linux a servis de dernier recours*) suivant cet ordre:

#### `1.` Serveur Linux (Linux Mint ou autre) 

- Avant tout, effectué la mise à jour des paquets du Système d'Exploitation en tapant la commande :

    ```
    sudo apt-get update
    ```
    
- `python` (v3.8.3) et ***P***ip ***I***nstalls ***P***ython ou `pip` (v20.1.1 ou v21.3.1) : Pour la prise en charge du Backend en Django pour le premier et la gestion des paquets installés, et écrits en Python; pour le second. Pour l'installer, taper la commande suivante pour l'installer:

    ```
    sudo apt-get install python3 python3-pip
    ```
    
    vérifier la version par la commande:
    
    ```
    python3 --version
    ```
    
    Pour python et:
    
    ```
    pip3 --version
    ```
    
    Pour pip.
    
    En raison des problèmes qui peuvent surgir lors du changement de la version par défaut de python (`3.8.3` pour notre cas en lieu et place de `3.6` qui s'installe par defaut avec la commande précédente et de `2.7` qui vient par défaut avec le Système d'exploitation installé), une alternative est d'installer [Anaconda3](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh) (v1.7.2) qui s'installe par défaut avec la version `3.8.3 de python`.
- `redis-server` (v4.0.9) ou ultérieure: Permet de manager celery (worker et beat). Pour l'installer, taper la commande suivante:

    ```
    sudo apt-get install redis-server
    ```

- `gunicorn` (version par défaut) : Permet la prise en charge du démarrage de python en production. Pour l'installer, taper la commande suivante:

    ```
    sudo apt-get install gunicorn
    ```

#### `2.` Python et Django

Pour prendre en charge le démarrage de python ainsi que le déploiement du projet Django, les dépendances suivantes sont requises dans l'ordre de leur enumération:

- `django` (v3.2.12) : Assure la prise en charge du backend après le déploiement dans le serveur. Pour l'installer, taper la commande:

    ```
    pip3 install -Iv django==3.2.12
    ```
    
    Vérifier la version par la commande:
    
    ```
    django-admin --version
    ```

- `celery` (v4.4.2) : Doit être installé pour la prise en charge de certaines taches utilisant la commande `celery`. Pour l'installer, taper la commande:

    ```
    pip3 install -Iv celery==4.4.2
    ```

- `channels` (version par défaut) : Pour l'installer, taper la commande suivante:

    ```
    pip3 install channels
    ```

- `django-cors-headers` (version par défaut) : Pour l'installer, taper la commande suivante:

    ```
    pip3 install django-cors-headers
    ```

- `django-rest-framework` (version par défaut) : Pour l'installer, taper la commande suivante:

    ```
    pip3 install djangorestframework
    ```
    
- `celery beat` (v2.2.0) : Permet le démarrage de la tache de fonds avec celery worker. Pour l'installer taper la commande suivante:

    ```
    pip3 install -Iv django-celery-beat==2.2.0
    ```
  
 - `mysqlclient` (version par défaut) : Pour la prise en charge de la création de la Base de Données MySQL par l'intermédiaire du model. Pour l'installer taper la commande suivante:

    ```
    pip3 install mysqlclient
    ```
    
    Si la commande échoue, installer les dépendances requises par la commande:
    
    ```
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
    ```
    
- `djangorestframework-simplejwt` (version par défaut) : Pour l'installer taper la commande suivante:

    ```
    pip3 install djangorestframework-simplejwt
    ```
    
- `paho-mqtt` (version par défaut) : Permet la prise en charge du client MQTT facilitant la publication et la réception des messages entre le module électronique et Logiciel. Pour l'installer taper la commande suivante:

    ```
    pip3 install paho-mqtt
    ```
    
- `redis` (version par défaut) : Module python pour redis. Pour l'installer taper la commande suivante:

    ```
    pip3 install redis
    ```
    
- `django-webserver` et `gunicorn` (version par défaut) : Module python pour la prise en charge de gunicorn. Pour l'installer taper la commande suivante:

    ```
    pip3 install django-webserver gunicorn
    ```

Tous les autres paquets sous-jacents sont installées automatiquement, et rien d'autre n'est requis pour cela.

>***Les dépendances du Frontend sont totatement gérées par l'utilitaire `npm` qui se charge d'installer tout ce qui est nécessaire pour le projet, voir corriger des failles de sécurité et autres***.

### Exécution du projet

***

#### `1.` Backend

L'exécution du projet s'effectue de la façon suivante:

- Se positionner dans le répertoire `codepo-backend/monitor/` :

    ```
    cd codepo-backend/monitor/
    ```
    
- Taper la commande:

    ```
    python3 manage.py runserver
    ```
    
    Si tout s'est bien passé, vous devez avoir ceci au niveau de l'interface de commande:
    
    ```
    .........
    System check identified 12 issues (0 silenced).
    February 02, 2022 - 14:10:04
    Django version 3.2.11, using settings 'monitor.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    
- Pour démarrer python avec la prise en charge de de gunicorn (***En production***), taper la commande suivante (Dans le répertoire contenant le module de l'application):

    ```
    cd codepo-backend/monitor
    python3 manage.py gunicorn --bind 0.0.0.0:8000
    ```

- Le scripte linux suivant (A retrouver dans le fichier `codepo-backend/monitor/start-python.sh`) permet de lancer cette en background et de le logger dans un fichier log:

    ```
    #!bin/bash
    # Specify the project directory
    project_dir="codepo-backend/monitor"
    cd "$(dirname $HOME/$project_dir/.)"
    
    echo "******************************************************************************************************"
    echo "********`date`****************START PYTHON TASK*********************************"
    python3 $HOME/$project_dir/manage.py gunicorn --bind 0.0.0.0:8000 >> "$HOME/log/python/python-monitor.log" 2>&1 &
    echo "*********************************************SUCCESSFULY STARTED**************************************"
    ```

- Exécuter ce fichier sur le shell par la commande suivante :

    ```
    sh codepo-backend/monitor/start-python.sh
    ```
    
Il faudra se rassurer que les paramètres de la Base de Données sont corrects et qu'un ***superutilisateur*** a été créé à cette fin (Cela permettra d'accéder facilement à la console d'administration de Django). Pour cela, suivre les étapes suivantes (Si c'est déjà le cas, démarrer directement `le scheduler` et continuer le reste des étapes.):

- Créer le schéma de la Base de Données par la commande :

    ```
    python3 manage.py makemigrations
    ```
    
- Créer la Base de Données par la commande :

    ```
    python3 manage.py migrate
    ```
    
- Créer un super-utilisateur par la commande:

    ```
    python3 manage.py createsuperuser
    ```
 
- Spécifier successivement le `nom d'utilisateur`, l' `adresse email` et le `mot de passe` pour l'administration.

***`Si le super-utilisateur est déjà créé et la Base de Données déjà exportée, continuer à partir d'ici.`***

- Démarrer le scheduleur par la commande suivante (Ouvrir une autre interface en mode commande dans le IDE):
   
    ```
    celery -A monitor worker -l info
    ```
 
- Démarrer l'écouteur des requêtes en provenance du module électronique (Ouvrir une autre interface en mode commande dans le IDE):
   
    ```
    celery -A monitor beat -l info
    ```  
  
- Pour une prise en charge aisée du scheduler et de l'automatisation des taches, le script linux suivant facilite le démarrage de ***celery-beat*** et de ***celery-worker*** (A retrouver dans le fichier `codepo-backend/monitor/start-celery-process.sh`) en background tout en gardant une trace dans des fichiers log :
   
    ```
    #!/bin/sh
    # /shared-exec/start-celery-process.sh
    # Script cannot be used as root user
    
    # Specify the project directory
    project_dir="codepo-backend/monitor"
    # Get the current user
    user=$USER
    if [ user != "root" ] 
    then  
    	# Force kill all running celery process
        pkill celery
    	# Kill celery worker if it was started with a certain PID
    	# celery -A monitor multi stop worker-monitor --loglevel=INFO --pidfile="$HOME/run/celery/worker-monitor.pid" --logfile="$HOME/log/celery/worker-monitor.log"
    	celery_worker_pid=`cat $HOME/run/celery/worker-monitor.pid`
    	if [ ! -z $celery_worker_pid ]
    	then
    		# If the celery worker PID file is not null, kill also the celery worker process corresponding to the one located in the pid file
    		kill $celery_worker_pid
    		echo "-------`date`------------------Stop celery worker PID $celery_worker_pid-----------------------------"
    	fi
    	
    	celery_beat_pid=`cat $HOME/run/celery/beat-monitor.pid`
    	if [ ! -z $celery_beat_pid ]
    	then
    		# If the celery beat PID file is not null, kill also the celery worker process corresponding to the one located in the pid file
    		kill $celery_beat_pid
    		echo "-------`date`-------------------Stop celery beat PID: $celery_beat_pid------------------------------"
    	fi
    
    	# Change the current directory to be in the expected project directory
    	cd "$(dirname $HOME/$project_dir/.)"
    	# Starting celery worker task as a background task
    	sleep 2s
    	celery -A monitor multi start worker-monitor --loglevel=INFO --pidfile="$HOME/run/celery/worker-monitor.pid" --logfile="$HOME/log/celery/worker-monitor.log" &
    	sleep 2s
    	echo "*****`date`*************Celery worker started successfuly in background************************"
    	
    	# wait 2 seconds and then start celery beat task as a background task
    	sleep 2s
    	celery -A monitor beat --detach --loglevel=INFO --pidfile="$HOME/run/celery/beat-monitor.pid" --logfile="$HOME/log/celery/beat-monitor.log" &
    	sleep 2s
    	echo "*****`date`*************Celery beat started successfuly in background**************************"
    else
        echo "You can't run this file as root user !!!"
        exit 1                                  
    fi
    ```

- Exécuter ce fichier sur le shell par la commande suivante :

    ```
    sh codepo-backend/monitor/start-celery-process.sh
    ```
   
#### `2.` Frontend

Pour ce qui est du Frontend (Ou de la partie affichable à l'utilisateur), ***son exécution se fait après que le Backend le soit*** et non l'inverse, car elle dépends de ce dernier et non l'inverse. Ainsi pour exécuter le Backend, procéder comme suit :

- Accéder à la console d'éxécution de l'IDE, et taper la commande suivante :

    ```
    npm start
    ```
    
 En effet, l'utilitaire `npm` prends en charge bon nombre d'exécution et se charge pas mal de toutes les dépendances nécessaires au fonctionnement correcte de cette partie (Interface Utilisateur ou UI).  
 Ainsi, si tout s'es bien passé lors de l'xécution de cette commande et que le Backend est bien exécuté, `la page de Login` du site Web devrait s'afficher sur votre navigateur par défaut via le lien [http://localhost:3000/Login](http://localhost:3000/Login) si l'exécution est en local, ou [https://monitor-engine.com/](https://monitor-engine.com/) pour un accès directement du serveur en production.
 
- Ainsi, la console de l'IDE devrait afficher quelque chose semblable à ceci:

    ```
    .........
     Line 34:8:  'notifyInformation' is defined but never used  no-unused-vars

    src/views/search/SearchDeviceListView/HistoryDetaille.js
      Line 23:6:  React Hook useEffect has a missing dependency: 'props.id'. Either include it or remove the dependency array  react-hooks/exhaustive-deps
    
    Search for the keywords to learn more about each warning.
    To ignore, add // eslint-disable-next-line to the line before.
    ```

### Console d'administration

***

Pour accéder à la ***console d'administration de Django***, procéder ainsi:

- Démarrer le projet Backend par les commandes :
   
    ```
    cd codepo-backend/monitor
    python3 manage.py runserver
    ```
 
- Aller dans un navigateur web et taper l'URL suivante :
   
    ```
    http://localhost:8000/admin/
    ```  
    
- Spécifier `le nom d'utilisateur` et le `mot de passe` définies lors des opérations précédentes.
- Appliquer les modifications nécessaires en tant qu'administrateur.

### Déploiement / Hébergement

***

Le déploiement est l'opération par laquelle, le logiciel est mis en production pour pouvoir être utilisé (***C'est la mise en service de l'application***). En outre, elle s'avère être la partie la plus importante qui couronne les deux repository.
A ce niveau, seul les paramètres généraux seront donnés de sorte à ne pas mettre la sécurité du système en péril. `

> Il est plus procice d'héberger les deux modules (Backend et Frontend) dans des serveurs différents pour améliorer la sécurité, ou soit le faire dans un même serveur si cela n'est pas possible (Etant donné que le coût peut varier d'une approche à une autre). 

#### `1.` Etape 1

- Build du code du Backend (Et si necessaire, changer le contenu des fichiers utiles pour aller dans le serveur).
- Uploader tout le code source du Backend dans un serveur (***VPS*** par exemple).

#### `2.` Etape 2

- Exécuter le Backend dans le serveur (Pour cela, installer en cas de besoin les dépendances nécessaires, Cfr. section ***`Dépendances du projet`***):
    
    ***Exécution de python (En shell script) pour rendre le backend disponible***.
    ```
    sh backend-server-path/start-python.sh
    ```
    
    `backend-server-path` sera le chemin d'accès du fichier `manage.py` dans le serveur de déploiement du Backend.
    
    ***Démarrage Scheduler (En shell script) pour exécuter des taches***.
    
    ```
    sh codepo-backend/monitor/start-celery-process.sh
    ``` 

#### `3.` Etape 3

- Créer un exécutable pour le Frontend, prêt à être uploader dans le serveur en tapant la commande:

    ```
    npm run build
    ```  
    
- Uploader le dossier `codepo-frontend/build/` résultant du build dans le serveur.

#### `4.` Etape 4

- Accéder au logiciel en tapant l'URL appropriée: [https://monitor-engine.com](https://monitor-engine.com).

#### `5.` Etape 5

D'autres taches doivent être directement exécutée dans le serveur pour qu'il soit pleinement opérationnel:
- Installation de `nginx` : Permettant de prendre en charge le frontend.
    
    ```
    sudo apt-get install nginx
    ```
        
- Configuration de nginx.
- Configuration de la prise en charge des certificats SSL (***S***ecure ***S***ocket ***L***ayer) pour la sécurité de la navigation.
- Configuration de la Base de Données de sorte à ne pas l'utiliser en tant que `root`, mais créer un autre utilisateur qui sera propriétaire de la BD à gérer.

### Récommendations

***

Cette partie relève les différentes recommandations susceptibles d'être soulevées pour une quelconque amélioration de la plateforme web afin de satisfaire le besoin des utilisateurs.
