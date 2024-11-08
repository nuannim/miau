This is example for using Partii in Java Maven project.
Quick start for gRPC java can go to https://grpc.io/docs/languages/java/quickstart/

In this example show you how to record audio or process audio file and stream to Partii service :
Before use this example you need to install IntelliJ IDEA editer (https://www.jetbrains.com/idea/) for open and compile java project.
Then you can start with open IntelliJ IDEA and open Java project.
- Add .proto files into project file tree under src/main/proto directories.
- Right click on Java project select Maven -> Generate Sources and Update folders
- Go to menu Build -> Rebuild Project.
- main class is src/main/java/grpc.partii/Main.java
- Create runnable .jar file by go to Build -> Build Artifacts... -> partii-java:jar -> Rebuild. Output will save at out/artifacts/partii_java_jar/partii-java.jar

- For record from microphone use this parameter (Main-mic):
    cd out/artifacts/partii_java_jar/
    java -jar partii-java.jar -server-ip partii.aiforthai.in.th -server-port 27016 -apikey xxxx -o temp.wav -use-mic true

- For proces wav file use this parameter (Main-file):
    cd out/artifacts/partii_java_jar/
    java -jar partii-java.jar -server-ip partii.aiforthai.in.th -server-port 27016 -apikey xxxx -i test.wav -use-mic false
