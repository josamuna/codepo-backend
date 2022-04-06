[![](https://user-images.githubusercontent.com/46261770/79870277-9a490b00-8397-11ea-88ac-e8dc25124084.png)](https://monitor-engine.com)

# Monitor Engine (Backend)

> Cette partie est une suite de la documentation du projet se trouvant à ce repository: [Documentation initiale du projet Monitor-Engine](https://github.com/josamuna/codepo-fontend)

## Table des Matières

1. [Structure du projet](#Structure-Projet)
2. [Dépendances du projet](#Dépendances)
3. [Exécution du projet](#Exécution)
4. [Console d'administration](#Console-Administration)
5. [Déploiement / Hébergement](#Déploiement)
6. [Modes de fonctionnement](Modes-fonctionnement)
7. [Récommendations](#Récommandations)

### Structure du projet

***

#### `1.` Backend 
La structure du projet reprend les dossiers et fichiers suivants détaillés dans cette arborescence:

```
..\monitor\
│
├── monitor\
│   ├── __pycache__\
│   │   ├── asgi.cpython-38.pyc
│   │   ├── celery.cpython-38.pyc
│   │   ├── celery.cpython-39.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-38.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── wsgi.cpython-38.pyc
│   │   ├── wsgi.cpython-39.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── asgi.py
│   ├── celery.py
│   ├── routing.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
│
├── monitor_engine\
│   ├── migrations\
│   │   ├── __pycache__\
│   │   │   ├── 0001_initial.cpython-38.pyc
│   │   │   ├── 0001_initial.cpython-39.pyc
│   │   │   ├── 0002_auto_20210708_0918.cpython-38.pyc
│   │   │   ├── 0002_auto_20210708_0918.cpython-39.pyc
│   │   │   ├── 0003_auto_20210708_0919.cpython-38.pyc
│   │   │   ├── 0003_auto_20210708_0919.cpython-39.pyc
│   │   │   ├── 0004_auto_20210708_1144.cpython-38.pyc
│   │   │   ├── 0004_auto_20210708_1246.cpython-38.pyc
│   │   │   ├── 0004_auto_20210708_1246.cpython-39.pyc
│   │   │   ├── 0005_auto_20210708_1145.cpython-38.pyc
│   │   │   ├── 0005_auto_20210708_1251.cpython-38.pyc
│   │   │   ├── 0005_auto_20210708_1251.cpython-39.pyc
│   │   │   ├── 0006_auto_20210714_1443.cpython-38.pyc
│   │   │   ├── 0006_auto_20210714_1443.cpython-39.pyc
│   │   │   ├── 0007_auto_20210715_1035.cpython-38.pyc
│   │   │   ├── 0007_auto_20210715_1035.cpython-39.pyc
│   │   │   ├── 0008_userpreference.cpython-38.pyc
│   │   │   ├── 0008_userpreference.cpython-39.pyc
│   │   │   ├── 0009_auto_20210717_0450.cpython-38.pyc
│   │   │   ├── 0009_auto_20210717_0450.cpython-39.pyc
│   │   │   ├── 0010_userpreference_user_id.cpython-38.pyc
│   │   │   ├── 0010_userpreference_user_id.cpython-39.pyc
│   │   │   ├── 0011_auto_20210719_1029.cpython-38.pyc
│   │   │   ├── 0011_auto_20210719_1029.cpython-39.pyc
│   │   │   ├── 0012_notification_caseid.cpython-38.pyc
│   │   │   ├── 0012_notification_caseid.cpython-39.pyc
│   │   │   ├── 0013_auto_20210723_1041.cpython-38.pyc
│   │   │   ├── 0013_auto_20210723_1041.cpython-39.pyc
│   │   │   ├── 0014_auto_20210723_1042.cpython-38.pyc
│   │   │   ├── 0014_auto_20210723_1042.cpython-39.pyc
│   │   │   ├── 0015_device_total_capacity.cpython-38.pyc
│   │   │   ├── 0015_device_total_capacity.cpython-39.pyc
│   │   │   ├── 0016_auto_20210726_1205.cpython-38.pyc
│   │   │   ├── 0016_auto_20210726_1205.cpython-39.pyc
│   │   │   ├── 0017_measured_autonomy.cpython-38.pyc
│   │   │   ├── 0017_measured_autonomy.cpython-39.pyc
│   │   │   ├── 0018_auto_20210730_0853.cpython-38.pyc
│   │   │   ├── 0018_auto_20210730_0853.cpython-39.pyc
│   │   │   ├── 0019_auto_20210730_0857.cpython-38.pyc
│   │   │   ├── 0019_auto_20210730_0857.cpython-39.pyc
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20210708_0918.py
│   │   ├── 0003_auto_20210708_0919.py
│   │   ├── 0004_auto_20210708_1246.py
│   │   ├── 0005_auto_20210708_1251.py
│   │   ├── 0006_auto_20210714_1443.py
│   │   ├── 0007_auto_20210715_1035.py
│   │   ├── 0008_userpreference.py
│   │   ├── 0009_auto_20210717_0450.py
│   │   ├── 0010_userpreference_user_id.py
│   │   ├── 0011_auto_20210719_1029.py
│   │   ├── 0012_notification_caseid.py
│   │   ├── 0013_auto_20210723_1041.py
│   │   ├── 0014_auto_20210723_1042.py
│   │   ├── 0015_device_total_capacity.py
│   │   ├── 0016_auto_20210726_1205.py
│   │   ├── 0017_measured_autonomy.py
│   │   ├── 0018_auto_20210730_0853.py
│   │   ├── 0019_auto_20210730_0857.py
│   │   └── __init__.py
│   │
│   ├── __pycache__\
│   │   ├── admin.cpython-38.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── consumers.cpython-38.pyc
│   │   ├── consumers.cpython-39.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── routing.cpython-38.pyc
│   │   ├── serializers.cpython-38.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── tasks.cpython-38.pyc
│   │   ├── tasks.cpython-39.pyc
│   │   ├── urls.cpython-38.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── views.cpython-38.pyc
│   │   ├── views.cpython-39.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── .admin.py.swp
│   ├── admin.py
│   ├── apps.py
│   ├── codepoBackend
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
│
├── rptree\
│   ├── __pycache__\
│   │   ├── cli.cpython-39.pyc
│   │   ├── rptree.cpython-39.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── cli.py
│   ├── rptree.py
│   └── __init__.py
│
├── celerybeat-schedule.bak
├── celerybeat-schedule.dat
├── celerybeat-schedule.dir
├── dump.rdb
├── info
├── manage.py
└── tree.py
```

- `monitor` est le module principal. 
- `..\monitor\monitor-engine\migrations` répertorie toutes les migrations déjà exécutées dans le projet (Lors de la traduction du modèle vers le Système de Gestion de Base de Données MySQL).
- `..\monitor\monitor\celery.py` pour la gestion de l'écoute du serveur et le cadensement du scheduler.
- `..\monitor\monitor\settings.py` comprend tous les paramètres de configuration pour la gestion des différentes intéraction entre l'interface utilisateur et les autres parties du système: Assure le bon fonctionnement du Backend.
- `..\monitor\monitor\urls.py` pour la spécification des URLs d'accès.
- `..\monitor\monitor\asgi.py` (**A**synchronous **S**erver **G**ateway **I**nterface): est le remplaçant du fichier wsgi et permet de définir la façon dont le(s) serveur(s) Django communique(ent) avec l'application.
- `..\monitor\monitor-engine\admin.py` permet l'enregistrement du model de l'application dans la console d'Administration de Django.
- `..\monitor\monitor-engine\apps.py` spécifie le nom de l'application.
- `..\monitor\monitor-engine\codepoBackend` spécifie les adresses pour le serveur distant et celui en local.
- `..\monitor\monitor-engine\consumers.py`.
- `..\monitor\monitor-engine\models.py` reprend le modèle (de la partie Modèle du MVC) qui servira au reverse engineering pour la création de la Base de Données en mode commande.
- `..\monitor\monitor-engine\routing.py`.
- `..\monitor\monitor-engine\serializers.py`.
- `..\monitor\monitor-engine\tasks.py` est le fichier contenant les actions devant être exécutées de façon automatisée par **celery**.
- `..\monitor\monitor-engine\urls.py` permet de faire la correspondance (Ou le lien) entre les URLs des requêtes de l'utilisateur avec leurs pages correspondantes.
- `..\monitor\monitor-engine\views.py` permet d'avoir une interface d'interaction pour l'utilisateur avec l'application. Il contients les views ou vues sous forme des classes.

We use the concept of Serializers in Django Rest_Framework for making different types of views. Some of these are CustomFilter Views, Class-Based List Views, and Detail Views.
- `..\monitor\rptree\` contient les fichiers nécessaire pour générer le fichier `markdown-file-tree.md` en mode commande en utilisant le fichier `..\monitor\tree.py`.
- `..\monitor\manage.py` fichier principal pour l'exécution des taches en mode administrateur (Comme l'installation d'un pacquet, l'exécution de l'application, etc.).

Pour arriver à générer le fichier relatif à l'arborescence des dossiers et fichiers `markdown-file-tree.md` ([Voir dans ce repository](https://github.com/javitocor/Python-Direcory-Tree-Generator)), procéder comme suit:
- Se positionner dans le répertoire principale du module: 

    ```
    cd codepo-backend\monitor\
    ```
- Taper la commande: 
    
    ```
    python tree.py ..\monitor -o ..\markdown-file-tree.md
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
- `..\public\favicon.ico` est le fichier correspondant à l'icône de l'application.
- `..\public\package.json` est l'un des fichiers le plus important qui permet de gérer les dépendances du projets ainsi que d'autres informations utiles (Comme le nom du projet, sa version, etc.), ainsi il garde la trace de tous ce qui est installé dans le projet.
- `..\src` est le répertoire contenant les fichiers sources de l'application React où l'on peut créer d'autres sous-répertoire à volonté. Ce répertoire est automatiquement créé par le Webpack. De cette façon un certain nombre des sous-répertoires et automatiquement générés pour bien organisé le projet (Pages web, images, bannières, etc.).
- `..\src\assets` contient certaines images des pages web.
- `..\src\components` contient les composants de l'application.
- `..\src\icons` contient un certain nombre d'icônes de l'application.
- `..\src\image` contient les images de l'applications.
- `..\src\layouts` contient les différentes bannières de l'application.
- `..\src\theme` contient les différents themes de l'application.
- `..\src\utils` permet la gestion des fonctions utilitaires pour le projet.
- `..\src\views` contients les différentes vues (d'un à plusieurs fichiers JavaScript) de l'application.
- `..\src\views\Login` permet la gestion du login de l'utilisateur.
- `..\src\views\Redux` permet la gestion des paramètres Redux.
- `..\src\views\User` permet la gestion des utilisateurs.
- `..\src\views\commande` permet la gestion des commandes à envoyé au devices / et ou des devices eux-même.
- `..\src\views\corbeille` permet la gestion de la corbeille après suppression.
- `..\src\views\devices` permet la gestion des devices.
- `..\src\views\errors` permet la gestion des erreurs (Comme 404 ou Page not found).
- `..\src\views\maps` permet la gestion de tout ce qui est lié à l'affichage de la Map.
- `..\src\views\reports` permet la gestion des information de summarsation (Summarizing).
- `..\src\views\search` permet la gestion de la recherche pour l'application.
- `..\src\views\services` permet la gestion de certains paramètres de fonctionnement de l'application (Comme la configuration des sockets, etc.).
- `..\src\views\settings` permet la gestion des paramétrages de l'application (Comme les préférences de couleurs, les notifications, etc.).

Pour arriver à générer le fichier relatif à l'arborescence des dossiers et fichiers `markdown-file-tree.md` ([Voir dans ce repository](https://github.com/michalbe/md-file-tree)), procéder comme suit:

`Les commandes pour cette opération ne sont valide que sur un shell Linux, à defaut sur Windows, `***Git Bash***` pourrait être utilisé à la place`.

- Se positionner dans le répertoire principale du projet: 

    ```
    cd codepo-frontend\
    ```
    
- Installer le paquet nécessaire pour la génération de l'arborescence: 
    
    ```
    npm install md-file-tree
    ```
    
- Générer le fichier `.md` par la commande suivante (Il n'est pas nécessaire de créer le fichier avant, la commande le fait à notre place): 
    
    ```
    md-file-tree > markdown-file-tree.md
    ```
    
### Dépendances du projet

***

Pour arriver à effectuer un **build** du projet, un certain nombre des dépendances est requis (Néanmoins avec un IDE telque [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) l'installation de ces dernières devient plus au moins aisée.) suivant cet ordre:

- `python` (v3.8.3): Doit être installé pour la prise en charge du projet.
- `pip` (version par defaut): ***P***ip ***I***nstalls ***P***ython, un gestionnaire de paquets utilisé pour installer et gérer des paquets écrits en Python.

    ```
    sudo apt-get install python3-pip
    ```
    
    Si nécessaire, **pip** peut être mis à jour par la commande:
    
    ```
    python3 -m pip install --upgrade pip setuptools wheel
    ```
    
- `django` (v3.2.12): Doit être installé pour la prise en charge du projet.

    ```
    pip3 install -Iv django==3.2.12
    ```
    
- `celery` (v4.4.2): Doit être installé pour la prise en charge du scheduler et des tasks devant être executées périodiquement (Réception des messages des modules électroniques).
    
    ```
    pip3 install -Iv celery==4.4.2
    ```
    
- `channels` (version par défaut).
    
    ```
    pip3 install channels
    ```
    
- `django-cors-headers`	(version par défaut).
    
    ```
    pip3 install django-cors-headers
    ```
    
- `django-rest-framework` (version par défaut).*
   
    ```
    pip3 install djangorestframework
    ```
    
- `django-celery-beat` (v2.2.0).
   
    ```
    pip3 install -Iv django-celery-beat==2.2.0
    ```
    
- `mysqlclient` (v2.1.0): Pour la prise en charge de la création de la Base de Données MySQL par l'intermédiaire du model.
   
    ```
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
    pip3 install mysqlclient
    ```
    
- `djangorestframework-simplejwt` (version par défaut).
    
    ```
    pip3 install djangorestframework-simplejwt
    ```
    
- `paho-mqtt` (version par défaut): Prise en charge du client MQTT.
   
    ```
    pip3 install paho-mqtt
    ```
    
- `redis` (version par défaut): Le serveur Redis permet de gérer les commandes celery (**worker** et **beat**). 
    
    ```
    pip3 install redis
    ```
    
    En mode developpement, le Serveur Redis est aussi important, mais pa nécessaire en mode production.
    
    ```
    sudo apt install python-celery-common
    ```
    
Certains autres paquets sous-jacents sont installées automatiquement, et rien d'autre n'est requis pour cela.

>***Les dépendances du Frontend sont totatement gérées par l'utilitaire `npm` qui se charge d'installer tout ce qui est nécessaire pour le projet, voir corriger des failles de sécurité et autres***.

### Exécution du projet

***

#### `1.` Backend

L'exécution du projet s'effectue de la façon suivante:

- Se positionner dans le répertoire `..\monitor\` :

    ```
    cd codepo-backend\monitor\
    ```
    
- Taper la commande:

    ```
    python manage.py runserver
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
    
Il faudra se rassurer que les paramètres de la Base de Données sont corrects et qu'un ***superutilisateur*** a été créé à cette fin (Cela permettra d'accéder facilement à la console d'administration de Django). Pour cela, suivre les étapes suivantes (Si c'est déjà le cas, démarrer directement `le scheduler` et continuer le reste des étapes.):

- Créer le schéma de la Base de Données par la commande :

    ```
    python manage.py makemigrations
    ```
    
- Créer la Base de Données par la commande :

    ```
    python manage.py migrate
    ```
    
- Créer un super-utilisateur par la commande:

    ```
    python manage.py createsuperuser
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
    
#### `2.` Frontend

Pour ce qui est du Frontend (Ou de la partie affichable à l'utilisateur), ***son exécution se fait après que le Backend le soit*** et non l'inverse, car elle dépends de ce dernier et non l'inverse. Ainsi pour exécuter le Backend, procéder comme suit :

- Accéder à la console d'éxécution de l'IDE, et taper la commande suivante :

    ```
    npm start
    ```
    
 En effet, l'utilitaire `npm` prends en charge bon nombre d'exécution et se charge pas mal de toutes les dépendances nécessaires au fonctionnement correcte de cette partie (Interface Utilisateur ou UI).  
 Ainsi, si tout s'es bien passé lors de l'xécution de cette commande et que le Backend est bien exécuté, `la page de Login` du site Web devrait s'afficher sur votre navigateur par défaut via le lien [http://localhost:3000/Login](http://localhost:3000/Login) si l'exécution est en local, ou [https://monitor-engine.com/](https://monitor-engine.com/) pour un accès directement du serveur en production.
 
- Ainsi la console de l'IDE devrait afficher quelque chose de semblable à ceci:

    ```
    .........
     Line 34:8:  'notifyInformation' is defined but never used  no-unused-vars

    src\views\search\SearchDeviceListView\HistoryDetaille.js
      Line 23:6:  React Hook useEffect has a missing dependency: 'props.id'. Either include it or remove the dependency array  react-hooks/exhaustive-deps
    
    Search for the keywords to learn more about each warning.
    To ignore, add // eslint-disable-next-line to the line before.

    ```

### Console d'administration

***

Pour accéder à la ***console d'administration de Django***, procéder ainsi:

- Démarrer le projet Backend par la commande :
   
    ```
    python manage.py runserver
    ```
 
- aller dans un navigateur web et taper l'URL suivante:
   
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

- Build le code du Backend (Et si necessaire, changer le contenu des fichiers utiles pour aller dans le serveur).
- Uploader tout le code source du Backend dans un serveur (***VPS*** par exemple).

#### `2.` Etape 2

- Exécuter le Backend dans le serveur (Pour cela, installer en cas de besoin les dépendances nécessaires, Cfr. section ***`Dépendances du projet`***):
    
    ***Exécution du projet***.
    ```
    cd monitor
    python manage.py runserver
    ```   
    
    ***Démarrage Scheduler***.
    ```
    cd monitor
    celery -A monitor worker -l info
    ```  
    
    ***Démarrer l'écouteur des requêtes***.
    ```
    cd monitor
    celery -A monitor beat -l info
    ```  

#### `3.` Etape 3

- Créer un exécutable pour le Frontend, prêt à être uploader dans le serveur en tapant la commande:

    ```
    npm run build
    ```  
    
- Uploader le dossier `codepo-frontend\build\` résultant du build dans le serveur.

#### `4.` Etape 4

- Accéder au logiciel en tapant l'URL appropriée: [https://monitor-engine.com](https://monitor-engine.com).

### Modes de fonctionnement

***

Pour un bon fonctionnement du système, ***quatre modes*** de fonctionnement ont été prévus, à savoir `BAT_GPS`, `BAT`, `ECONOMY` et `CALIBRATION` dont le comportement est décris ici-bàs:
- **BAT_GPS**: Permet au device d'envoyer à la plateforme web non seulement les informations concernant le SOC (**S**tate **O**f **C**harge ou le niveau de la batterie), mais aussi les informations GPS (***Latitude*** et ***Longitude***) à des intervalles de temps spécifiques appelé ***intervalle d'envoi*** (Correspondant à `Sending interval` exprimé en heure, et se trouvant sur l'interface graphique, précisement dans les paramètres de commande du device). Le paramètre `Sampling interval` ou ***intervalle de prélèvement*** corresponds à l'intervalle de temps (Exprimé en secondes) pendant lequel le microcontrolleur (Du module électronique) doit prélever le SOC ou niveau de la batterie (Option à retrouver sur l'interface graphique, dans les paramètres de commande du device).
- **BAT**: Permet au device d'envoyer à la plateforme web uniquement les informations du SOC à des intervalles spécifiques (Cfr. point précédent). 
- **ECONOMY**: Est le mode pour lequel les ***intervalles de prélèvement*** (Pour le SOC par le module électronique) et ***d'envoi*** (Du module électronique vers la plateforme web) sont relativement long (Par exemple de plusieurs jours pour le premier à quelques semaines pour le sécond). C'est le mode qui consomme le moins d'énergie possible pour le module électronique car ce dernier est moins sollicité.
- **CALIBRATION**: Est le mode pour lequel on commande les paramètres de mesure du module électronique directement via la plateforme web. Ces paramètres de mesure sont les suivants:
    - `Sampling interval` (En seconds): Intervalle de prélèvement du SOC par le microcontrolleur du module électronique.
    - `Sending interval` (En heure): Intervalle d'envoi d'informations du microcontrolleur à la plateforme web.
    - `Total capacity` (Nombre entier): Correspondant à la capacité totale de la batterie en Ampères-Heure (AH).
    - `Pourcentage` (En pourcentage): Force le changement du pourcentage de la batterie du device sélectionné (Compte tenu du glissement que cela pourrait connaître au cours du temps).
> **NB**: Il est nécessaire de devoir activer le suivi du device au niveau de la plateforme web pour pouvoir recévoir des notifications par mail lorsque le niveau de sa batterie atteint des seuils critiques (***Seuil au rouge***). Pour cela Cfr. [le manuel utilisateur](https://github.com/josamuna/codepo-fontend/blob/main/Manuel%20utilisateur%20Projet%20monitor-engine.pdf) de la plateforme web.

> Pour une bonne gestion de la ***publication*** et de la ***réception*** des messages, il a été prevu que ***le nom de chaque Topic corresponde à celui de l'identifiant du device***, et ainsi avoir un topic par device. Ceci facilite ainsi le suivis des messages reçu et de l'associer correctement au divice concerné (Cfr. le fichier [tasks.py](https://github.com/josamuna/codepo-backend/blob/main/monitor/monitor_engine/tasks.py) de ce repository).

### Récommendations

***

Cette partie relève les différentes recommandations susceptibles d'être soulevées pour une quelconque amélioration de la plateforme web afin de satisfaire le besoin des utilisateurs.