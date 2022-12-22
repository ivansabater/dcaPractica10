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
Para el bisect he hecho estos pasos:
```
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect start
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git checkout e5a687bdd57ca722bd9e292b54635d2dc371e533
Note: switching to 'e5a687bdd57ca722bd9e292b54635d2dc371e533'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at e5a687b 1.1.0
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect good
Bisecting: 6 revisions left to test after this (roughly 3 steps)
[12f2449760ddc8e6b52a67ca9e4d3c1878b1cd09] 1.2.5
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
Bisecting: 3 revisions left to test after this (roughly 2 steps)
[c294dc41f741dc910b3bc4cf454f9ce94f722b93] 1.2.1
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect good
Bisecting: 1 revision left to test after this (roughly 1 step)
[c5224deecac0a03a2ac7d81a79000ddd64baab0f] 1.2.3
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[3ffd7285a455bd0ad296e7c2a328e04186583b5b] 1.2.2
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect bad
3ffd7285a455bd0ad296e7c2a328e04186583b5b is the first bad commit
commit 3ffd7285a455bd0ad296e7c2a328e04186583b5b
Author: Ivan Sabater <ivansabater@gmail.com>
Date:   Wed Dec 21 16:17:18 2022 +0100

    1.2.2

 holaMundo.py | 9 +++++++--
 1 file changed, 7 insertions(+), 2 deletions(-)
ivan@DESKTOP-BEGS1AS:/mnt/c/Users/ivans/Desktop/Universidad/Mi Universidad/Cuarto Curso/Primer Cuatri/DCA/Practica/Practica 10/dca-ramas_Bueno$ git bisect reset
Previous HEAD position was 3ffd728 1.2.2
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
```
El fallo lo había metido en el commit 1.2.2 y he comenzado a comprobar desde el commit Añadir 1.3.3 como bad y con la versión 1.1.0 como good
Hay 14 commits entre medias. 
- Primero me ha saltado al commit 1.2.5 que estaba mal
- Después al commit 1.2.1 que estaba bien
- Después al 1.2.3 que estaba mal
- Y por último al 1.2.2 que estaba mal
Entonces ha terminado diciendo que el bug se ha introducido en el commit 1.2.2 como ha sucedido.
El bug era que cuando comprobaba si el usuario era mayor de edad. Lo comprobaba con 21 años en vez de con 18.

Entonces en la versión 1.3.4 he corregido el fallo poniendo >= 18 en la línea 92 en la versión 1.3.4
```
def mayorEdad(self):
        if (int(self.edad) >= 18):
            return "Eres mayor de edad"
        else:
            return "Eres menor de edad"

```
# Hook
He añadido este código en el fichero pre-commit (sin el sample)
```
#!/bin/sh

STAGED_PY_FILES=$(git diff --cached --name-only | grep "\.py$")

if [[ "$STAGED_PY_FILES" = "" ]]; then
    exit 0
fi

echo "Running flake8 on python files..."
if ! flake8 $STAGED_PY_FILES; then
    echo "ERROR: flake8 failed, committing is not allowed."
    exit 1
fi

exit 0

```
Lo que hace este fichero es verificar si se han modificado archivos con extensiones .py y, en caso afirmativo, ejecuta flake8 para verificar si hay errores de estilo
y calidad de código en Python.
Algunas pruebas que realiza son: 
- Líneas demasiado largas
- Falta de espacio entre palabras clave y paréntesis
- Nombres de variables poco descriptivos o inadecuados
- Importaciones no necesarias o inadecuadas
- Falta de comentarios o documentación adecuados

Hay que instalar flake8 en python con pip flake8 y cada vez que cambies un .py te comprueba con flake8