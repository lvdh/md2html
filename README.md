# md2html

A quick test of viash. Converts Markdown to HTML.

- Runtime: python
- Platform: docker

```bash
$ viash --version
viash 0.3.2 (c) 2020 Data Intuitive

$ head ipsum.md ipsum.html
==> ipsum.md <==
viash: from scripts to pipelines
================

viash helps you turn a script (Bash/R/Python/Scala/JavaScript) into a
reusable component. By providing some meta-data regarding its
functionality and the platform on which you want to run the software,
viash can help you:

-   wrap your script in an executable with a CLI and –help
    functionality,
head: cannot open ‘ipsum.html’ for reading: No such file or directory

$ make
viash build -p docker -m -s config.vsh.yaml
> docker build -t md2html:0.1.0 /tmp/viashsetupdocker-md2html-5rrVs0
Sending build context to Docker daemon  18.94kB

Step 1/2 : FROM python:3.9.1-slim
 ---> 8c84baace4b3
Step 2/2 : RUN pip install --upgrade pip &&   pip install --no-cache-dir "markdown2" "structlog"
 ---> Using cache
 ---> 3e23eb162046
Successfully built 3e23eb162046
Successfully tagged md2html:0.1.0
viash version:      0.3.2
config:             config.vsh.yaml
platform:           docker
executable:         output/md2html
output:             output/
remote git repo:    <NA>
viash run -p docker config.vsh.yaml -- --input ipsum.md --output ipsum.html
2021-02-12 13:26.26 [debug    ] Parameters                     par={'input': '/viash_automount/home/ec2-user/environment/src/md2html/ipsum.md', 'output': '/viash_automount/home/ec2-user/environment/src/md2html/ipsum.html'}
2021-02-12 13:26.26 [debug    ] Read input ...                 input=/viash_automount/home/ec2-user/environment/src/md2html/ipsum.md
2021-02-12 13:26.26 [debug    ] Process input ...
2021-02-12 13:26.26 [debug    ] Write output ...               input=/viash_automount/home/ec2-user/environment/src/md2html/ipsum.html

$ head ipsum.md ipsum.html
==> ipsum.md <==
viash: from scripts to pipelines
================

viash helps you turn a script (Bash/R/Python/Scala/JavaScript) into a
reusable component. By providing some meta-data regarding its
functionality and the platform on which you want to run the software,
viash can help you:

-   wrap your script in an executable with a CLI and –help
    functionality,

==> ipsum.html <==
<h1>viash: from scripts to pipelines</h1>

<p>viash helps you turn a script (Bash/R/Python/Scala/JavaScript) into a
reusable component. By providing some meta-data regarding its
functionality and the platform on which you want to run the software,
viash can help you:</p>

<ul>
<li>wrap your script in an executable with a CLI and –help
functionality,</li>
$ 
```
