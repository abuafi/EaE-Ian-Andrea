# EaE-Ian-Andrea

Google Drive document link:
https://docs.google.com/document/d/1Bz66onDZVRGiAFcm4n1_M7brH8vmUbTRXaVrDtrx2Mc/edit?usp=sharing

To build and run the experiment, the org.json library is required.
We include the jar for the org.json library version 20220320, which can be downloaded from
https://search.maven.org/search?q=g:org.json%20AND%20a:json&core=gav

The python script requires the Matplotlib library.
It can be installed with `pip3 install matplotlib`.

## Build Instructions:
To run the experiment (Gather data in output.json file):

- Compile with `javac -cp json-20220320.jar: $(find ./Ex1/src/* | grep .java)`
- Run with `java -cp Ex1/src/:json-20220320.jar Main`

To run the data analysis (Create plots):

- Run with `python3 visuals.py`