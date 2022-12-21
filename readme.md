# Crear repositorio en GitHub
https://github.com/ivansabater/dcaPractica10.git

# Crear algunos alias locales y globales:
## Global
Para crear un alias global he tenido que poner:
```
git config --global alias.co checkout
git config --global alias.st status
```
En el archivo ~/.gitconfig está esta información:
```
ivan@DESKTOP-BEGS1AS:~$ cat .gitconfig
[credential]
        helper = store
[alias]
        co = checkout
        st = status
```
Que son los alias --global que he creado antes

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

# Bisect

```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect start
Already on 'master'
Your branch is up to date with 'origin/master'.
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git checkout 82f7facdd08247cdef2ca32e68cded0dd4c32add
Note: switching to '82f7facdd08247cdef2ca32e68cded0dd4c32add'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 82f7fac 1.1.1
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
Bisecting: 0 revisions left to test after this (roughly 1 step)
[c294dc41f741dc910b3bc4cf454f9ce94f722b93] 1.2.1
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect good
3ffd7285a455bd0ad296e7c2a328e04186583b5b is the first bad commit
commit 3ffd7285a455bd0ad296e7c2a328e04186583b5b
Author: Ivan Sabater <ivansabater@gmail.com>
Date:   Wed Dec 21 16:17:18 2022 +0100

    1.2.2

 holaMundo.py | 9 +++++++--
 1 file changed, 7 insertions(+), 2 deletions(-)
```