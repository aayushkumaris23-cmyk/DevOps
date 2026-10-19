# DevOps Exercise 8 – Jenkins Hello World Job

## Objective
Configure a Jenkins Freestyle project and execute a shell script as part of a build.

## Prerequisites
- Jenkins is running and accessible in the browser.
- A GitHub repository contains the `hello-world.sh` script.

## Hello World Script
```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Job Configuration
- **Job type:** Freestyle project
- **Build step:** Execute shell
- **Build command:**
```bash
sh hello-world.sh
```

## Expected Output
```text
Hello, Jenkins!
Finished: SUCCESS
```

## Result
The Jenkins Hello World job executed successfully.
