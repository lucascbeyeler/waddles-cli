Waddles-CLI - Backup Script for Zimbra OSE
=========

Waddles-CLI is a reliable tool for mail backup in general. Using API services, it will download the content locally and save inside your local storage. Waddles-CLI is part of a bigger solution called Waddles - the Zmbackup next-gen, which will solve most of the issues presented but the first one, but we couldn't solve because of how limited is Bash Shell script.

[![Zimbra Version](https://img.shields.io/badge/Zimbra%20OSE-8.8.15-orange.svg)](https://www.zimbra.com/downloads/zimbra-collaboration-open-source/)
![Branch](https://img.shields.io/badge/Branch-Development-yellow.svg)
![Release](https://img.shields.io/badge/Release-1.0.0-green.svg)

Features
------------
* Online Backup and Restore - no need to stop the server to do;
* Backup routines for one, many, or all mailbox, accounts, alias and distribution lists;
* Restore the routines in your respective places, or inside another account using Restore on Account;
* Multithreading - Execute each rotine quickly as possible;
* Have some insights about eacho backup routine;
* Receive alert everytime a backup session begins/end;
* Better internal garbage manager;
* Filter the accounts that should not be execute with blacklists;
* Log management compatible with rsyslog;

Requirements
------------
* Python 3.7 or above;
* MySQL Server 5.7 or SQLite3;

Installation
------------
COMMING SOON

Usage
------------
COMMING SOON

Get Involved
------------------
At the moment we are looking for Python developers - any skill level - interested in working on a new and exciting project. If you want to help with this project please sent an e-mail to sysdevbey@gmail.com and I will enter in contact with you as soon as possible.

We are also looking for peoples who want to help managing communication between the developers and the users. Zmbackup was an amazing project, but was really difficult handle requests for bugfix at the same time we were trying to create new features. If you have good comunication skills, please apply to this position sending an e-mail to sysdevbey@gmail.com and I will enter in contact with you as soon as possible.

If you don't have time to donate your code skills or your patience to organize the issues and talk with costumers, please try at least donate some coins to this project. We are looking for some donations for the following:

* Pycharm licenses for full-time developers;
* Pay for domain and AWS servers for integration tests with Zimbra OSE;

I will update this README with more details about the donation once I setup everything.

License
-------

[![GNU GPL Affero v3.0](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl.html)

View official GNU site <http://www.gnu.org/licenses/gpl.html>.

Author Information
------------------

* [Lucas Costa Beyeler](https://github.com/lucascbeyeler) - sysdevbey@gmail.com
