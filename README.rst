===============================
ClearCode toolkit
===============================

ClearCode is a simple tool to fetch and sync all ClearlyDefined data locally.

ClearlyDefined data are organized as deeply nested trees of JSON files.

The data that are synchronized include with this tool include:

 - the "definitions" that contain the aggregated data from running multiple scan
   tools and if available a manual expert curation
 - the "harvests" that contain the actual detailed output of scans (e.g. scancode runs)

The items are not fetched for now:

 - the "attachments" that are whole original files such as a README file
 - the "deadletters" that are scan failure traces when things fail: these are 
   not available through the API
 

Here are some stats on the ClearlyDefined data files set as of 2020-02-26,
excluding "deadletters" and most attachments:

+----------------+-------------+-------------+--------------+-----------------+---------+
|                |  JSON Files | Directories | Files & Dirs |    Gzipped Size | On disk |
+================+=============+=============+==============+=================+=========+
| ScanCode scans |   9,087,479 |  29,052,667 |   38,140,146 | 139,754,303,291 | ~400 GB |
+----------------+-------------+-------------+--------------+-----------------+---------+
|  Defs. & misc. |  38,796,760 |  44,825,854 |   83,622,614 | 304,861,913,800 |   ~1 TB |
+----------------+-------------+-------------+--------------+-----------------+---------+
|          Total |  47,884,239 |  73,878,521 |  121,762,760 | 444,616,217,091 |   ~2 TB |
+----------------+-------------+-------------+--------------+-----------------+---------+

Such a large number of files breaks about any filesystem: a mere directory
listing can take days to complete. To avoid these file size and number issues,
the JSON data fetched from the ClearlyDefined API are stored as gzipped-compressed
JSON as blobs in a PosgresSQL database keyed by the file path.
That path is the same as the path used in the ClearlyDefined "blob" storage on Azure. 
You can also save these as real files gzipped-compressed JSON files (with the caveat
that this will make the filesystem crumble and this may require a specila mkfs
invocation to create a filesystems with enough inodes.


Requirements
------------

To run this tool, you need:

- a POSIX OS (Linux)
- Python 3.6+
- PosgresSQL 9.5+
- plenty of space, bandwidth and CPU.


Quick start
-----------

First create a PostgreSQL database.
This requires sudo access. This is tested on Debian and Ubuntu.
::

    $ ./createdb.sh



Then run these commands to get started::

    $ source configure
    $ clearsync --help


For instance, try this command::

    $ clearsync --save-to-db  --output-dir clearly-local --verbose -n3 

This will fetch all the latest data items and save them in the clearly-local/
directory as well as the "clearcode" PostgresDB using three processes for fetching.


Or this command::

    $ clearsync --output-dir clearly-local --verbose -n3 

This will fetch all the latest data items and save them in the clearly-local/
directory using a single process for fetching.


TODO
----

- Add unit and integration tests
- Add export capability for delta/increments
