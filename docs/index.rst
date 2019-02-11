.. GREASE documentation master file, created by
   sphinx-quickstart on Sun Feb 10 16:46:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
GREASE: *Automating Operations*
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tgt_grease

GREASE is a method to enable I.T. Administrators, Operations Teams, and SREs to take care of toil. We aim to make
automation of these "toil" tasks as simple as possible and flexible. Simply install the system, hook it up to
MongoDB, and configure your triggers (we call them sources) for your jobs (also known as commands). Don't worry though,
We'll be here along the way to help you get up and running!

GREASE's Background
====================

In 2017 Target's operations team (Guest Reliability Engineering) was searching for a way to automate away support &
remediation work that typically their team members had to do. James Bell & Grant Gordon came up with the idea of
GREASE (Guest Reliability Engineering Automated Service Engine). The goal of the project was to design and implement
a system that would enable the automated running of scripts/programs to perform tasks generally left to humans.

Core Concept
==============

GREASE has a very simple programming interface for automation developers. Below are the ideals we strive to achieve
and hopefully in the examples they will shine!

---------------------------------
Step 1: scanning an environment
---------------------------------

First we must understand the environment around us if we wish to automate an action inside of it. To GREASE, an
environment is anything from an API, to a database, a Kafka topic, or anything else you could imagine. See the docs
on how to building a source for more information on how to build a source for your environment.

A *source* is a specific class construction that is executed by grease to inform the system of the environment the source
is scanning. Scanning via sources happens continuously, thus the *"runs 24/7/365"* aspect of GREASE. If something is
configured to trigger action will take place due to something coming from scanning.

---------------------------------
Step 2: detecting from scan data
---------------------------------

GREASE determines if something should happen via its' detection system. This happens once new source data from a scan
is scheduled for detection via the cluster. Your job configuration to trigger your command explains to detection what
elements matching the "detector" you configure (Regex, Date Range, etc.) should be, and what data should be put into
the context element for the job.

---------------------------------
Step 3: scheduling the job
---------------------------------

The cluster now determines where the job needs to be executed. There could be multiple nodes that are available to
execute a given job, and the cluster will ensure the most optimal node executes the triggered job. It then is
scheduled on the execution server to perform final execution.

GREASE is designed for modern environments that may have segmented networks, or complicated deployment patterns. Each
node in a GREASE cluster has a set of *"roles"* that explain to the job scheduler what kind of node a node in the cluster
is. An example of this is Windows Server. Your jobs may have specific PowerShell requirements. You can install GREASE in
a Kubernetes environment and the Windows Server you have, joining the Windows server with a role of `windows`. Your jobs
with the environment of `windows` will now be scheduled to execute there.

---------------------------------
Step 4: executing the job
---------------------------------

Finally your job is now due to execute on your execution node. On large clusters the average time-to-execute is around
a second. This is where your specifically crafted Python class is executed by GREASE for you. It will retry as many times
as the node is configured to.

Our goal is, after initial setup, your problem scope is to configure your source and construct your command. After that
GREASE monitors your sources, scanning them, and determining if it has detected something it needs to take action on.
If so, it schedules the job to the server it can most optimally execute on, and finally executes it for you; hopefully
allowing you to focus less on knowledge base articles and toil-ful end user support, instead focusing on making your
organization better.

Getting Help & Contributing
=============================

We love to hear GREASE being used to help support/operations/SRE engineers. If you have questions, or having problems,
feel free to reach out to us on GitHub! If you're looking to contribute please read our contribution guidelines and
then submit a PR after forking our repo, thanks!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
