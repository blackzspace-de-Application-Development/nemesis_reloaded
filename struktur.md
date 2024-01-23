package-name = nemesis

package-dir: nemesis

package-src:
             nemesis/
             nemesis/nemesis.py
             nemesis/__init__.py
             nemesis/kern/*
             nemesis/kern/basis/*
             nemesis/kern/dienste/*
             nemesis/farben/*
             nemesis/modules/*

package-pip:
            @nemesis/nemesis/setup.py
            @nemesis/blacksploit/requirements.txt
            @nemesis/blacksploit/MANIFEST.md
            @nemesis/blacksploit/LICENSE.txt
            @nemesis/blacksploit/README.md
