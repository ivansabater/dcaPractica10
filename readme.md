# Crear repositorio en GitHub
https://github.com/ivansabater/dcaPractica10.git

# Crear algunos alias locales y globales:
## Global
Para crear un alias global he tenido que poner:
```
git config --global alias.st status
```
### Prueba:

Cuando lo he probado en un repositorio distinto me ha salido: 
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/MADS/Practica/Practica Grupal/todolist-equipo-04$ git st
On branch develop
Your branch is up to date with 'origin/develop'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .github/workflows/developer-tests.yml
        modified:   .github/workflows/integration-tests.yml
        modified:   .gitignore
        modified:   .mvn/wrapper/MavenWrapperDownloader.java
        modified:   .mvn/wrapper/maven-wrapper.properties
```

Y en el que lo he configurado:
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git st
On branch master
Your branch is up to date with 'origin/master'.
```


## Local
Para crear un alias local he puesto:
```
git config alias.l log
```

### Prueba:
Cuando lo he probado en un repositorio distinto me ha salido: 
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/MADS/Practica/Practica Grupal/todolist-equipo-04$ git l
git: 'l' is not a git command. See 'git --help'.

The most similar commands are
        log
        lfs
```
Mientras que en el repositorio que lo he configurado me ha puesto 
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git l
commit 3bdb792a89f526363c5e71cdedc4fe41f49f718c (HEAD -> master, origin/master)
Author: Ivan Sabater <ivansabater@gmail.com>
Date:   Wed Dec 21 16:36:53 2022 +0100

    1.3.4

```

## Fichero config:
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno/.git$ cat config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        ignorecase = true
[remote "origin"]
        url = https://github.com/ivansabater/dcaPractica10.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[alias]
        l = log
```