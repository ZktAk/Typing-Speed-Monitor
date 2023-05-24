#!/bin/sh

main_path=.../Typing-Speed-Monitor/src
sessions_path=$main_path/sessions

export sessions_path

start(){
  python $main_path/main.py &
}

lst() {
  n=0
  cd $sessions_path || exit
  for i in *; do
    n=$(($n + 1))
	  echo "$n. $i"
	done
}

dp() {

  if [ "x$1" = "x" ]; then
    filename=$(ls $sessions_path | tail -n 1)
    export filename
  elif [ -n "$1" ] && [ $1 -eq $1 ] 2>/dev/null; then
    filename=$(ls $sessions_path | sed -n $1p)
    export filename
  else
    export export filename=$1
  fi
  echo "loading wpm graph"
  python $main_path/graph_display.py 2> /dev/null &
}

del() {
  filename=$1
  rm -r "$sessions_path/$filename"
  echo "removed $filename"
}

"$@"
