## Git 정리

## 최초 설정

git config라는 도구로 설정 내용을 확인하고 변경할 수 있다. Git은 이 설정에 따라 동작한다. 이때 사용하는 설정 파일은 세 가지나 된다.

`/etc/gitconfig 파일`: 시스템의 모든 사용자와 모든 저장소에 적용되는 설정이다. git config --system 옵션으로 이 파일을 읽고 쓸 수 있다.

`~/.gitconfig, ~/.config/git/config 파일`: 특정 사용자에게만 적용되는 설정이다. git config --global 옵션으로 이 파일을 읽고 쓸 수 있다.

`.git/config`: 이 파일은 Git 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용된다.

각 설정은 역순으로 우선시 된다. 그래서 `.git/config가 /etc/gitconfig`보다 우선한다.

## 도움말

명령어에 대한 도움말이 필요할 때 도움말을 보는 방법은 세 가지다.

```
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

를 들어 아래와 같이 실행하면 config 명령에 대한 도움말을 볼 수 있다.
```
$ git help config
```

## 파일 상태를 짤막하게 확인하기
git status 명령으로 확인할 수 있는 내용이 좀 많아 보일 수 있다. 사실 그렇다. 좀 더 간단하게 변경 내용을 보여주는 옵션이 있다. git status -s 또는 git status --short 처럼 옵션을 주면 현재 변경한 상태를 짤막하게 보여준다.

```
$ git status -s
 M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
```

## Staged와 Unstaged 상태의 변경 내용을 보기
단순히 파일이 변경됐다는 사실이 아니라 어떤 내용이 변경됐는지 살펴보기엔 `git status` 명령이 아니라 `git diff` 명령을 사용해야 한다. 보통 우리는 수정했지만, 아직 Staged 파일이 아닌것?과 어떤 파일이 Staged 상태인지가 궁금하기 때문에 `git status` 명령으로도 충분하다. 

꼭 잊지 말아야 할 것이 있는데 `git diff` 명령은 마지막으로 커밋한 후에 수정한 것들 전부를 보여주지 않는다. `git diff`는 Unstaged 상태인 것들만 보여준다. 이 부분이 조금 헷갈릴 수 있다. 수정한 파일을 모두 Staging Area에 넣었다면 git diff 명령은 아무것도 출력하지 않는다.


## 파일 삭제하기

Git에서 파일을 제거하려면 `git rm` 명령으로 Tracked 상태의 파일을 삭제한 후에(정확하게는 Staging Area에서 삭제하는 것) 커밋해야 한다. 이 명령은 워킹 디렉토리에 있는 파일도 삭제하기 때문에 실제로 지워진다.

또 Staging Area에서만 제거하고 워킹 디렉토리에 있는 파일은 지우지 않고 남겨둘 수 있다. 다시 말해서 하드디스크에 있는 파일은 그대로 두고 Git만 추적하지 않게 한다. 이것은 `.gitignore` 파일에 추가하는 것을 빼먹었거나 대용량 로그 파일이나 컴파일된 파일인 .a 파일 같은 것을 실수로 추가했을 때 쓴다. --cached 옵션을 사용하여 명령을 실행한다.

```
$ git rm --cached README
```

여러 개의 파일이나 디렉토리를 한꺼번에 삭제할 수도 있다. 아래와 같이 `git rm` 명령에 file-glob 패턴을 사용한다.

```
$ git rm log/\*.log
*앞에 \을 사용한 것을 기억하자. 파일명 확장 기능은 쉘에만 있는 것이 아니라 Git 자체에도 있기 때문에 필요하다. 이 명령은 log/ 디렉토리에 있는 .log 파일을 모두 삭제한다. 아래의 예제처럼 할 수도 있다.

$ git rm \*~
이 명령은 ~로 끝나는 파일을 모두 삭제한다.
```

## commit history 조회

원하는 히스토리를 검색할 수 있도록 git log 명령은 매우 다양한 옵션을 지원한다. 여기에서는 자주 사용하는 옵션을 설명한다.

여러 옵션 중 `-p`는 굉장히 유용한 옵션이다. `-p`는 각 커밋의 diff 결과를 보여준다. 다른 유용한 옵션으로 `-2`가 있는데 최근 두 개의 결과만 보여주는 옵션이다

```
$ git log -p -2
```

## 되돌리기
일을 하다보면 모든 단계에서 어떤 것은 되돌리고(Undo) 싶을 때가 있다.

종종 완료한 커밋을 수정해야 할 때가 있다. 너무 일찍 커밋했거나 어떤 파일을 빼먹었을 때 그리고 커밋 메시지를 잘못 적었을 때 한다. 다시 커밋하고 싶으면 --amend 옵션을 사용한다.

```
$ git commit --amend
```

커밋을 했는데 Stage 하는 것을 깜빡하고 빠트린 파일이 있으면 아래와 같이 고칠 수 있다.

```
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend
```

## 리모트 저장소를 Pull 하거나 Fetch 하기
앞서 설명했듯이 리모트 저장소에서 데이터를 가져오려면 간단히 아래와 같이 실행한다.

```
$ git fetch [remote-name]
```

이 명령은 로컬에는 없지만, 리모트 저장소에는 있는 데이터를 모두 가져온다. 그러면 리모트 저장소의 모든 브랜치를 로컬에서 접근할 수 있어서 언제든지 Merge를 하거나 내용을 살펴볼 수 있다.

저장소를 Clone 하면 명령은 자동으로 리모트 저장소를 `origin` 이라는 이름으로 추가한다. 그래서 나중에 `git fetch origin`을 실행하면 Clone 한 이후에(혹은 마지막으로 가져온 이후에) 수정된 것을 모두 가져온다. `git fetch` 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 Merge 하지 않는다. 그래서 당신이 로컬에서 하던 작업을 정리하고 나서 **수동으로 Merge** 해야 한다.

그냥 쉽게 `git pull` 명령으로 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 Merge 시킬 수 있다. 먼저 `git clone` 명령은 자동으로 로컬의 `master` 브랜치가 리모트 저장소의 `master` 브랜치를 추적하도록 한다(물론 리모트 저장소에 `master` 브랜치가 있다는 가정에서). 그리고 `git pull` 명령은 `Clone` 한 서버에서 데이터를 가져오고 그 데이터를 자동으로 현재 작업하는 코드와 Merge 시킨다.

`fetch` - 가져오나 자동 merge 안함 **임시폴더(.git)에 저장**<br>
`pull` - 가져오고 현재 브랜치에 자동 merge 함



## alias 설정

```
$ git checkout -b iss53
Switched to a new branch "iss53"
위 명령은 아래 명령을 줄여놓은 것이다.

$ git branch iss53
$ git checkout iss53
```