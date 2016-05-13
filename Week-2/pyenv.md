## python 버전 바꾸기
pyenv shell 3.5.1
python --version

## python 가상환경 만들기
pyenv virtualenv 3.5.1 [name]

## python 가상환경 들어가기
pyenv activate [name]
pyenv deactivate [name]

## 해당 name으로 들어갔을때 자동으로 pyenv activate 설정
mkdir [directoy name]
cd [directory name]
vi .env
echo "--------------"
echo "WebProgramming"
echo "-------------"
**pyenv activate [directory name]**