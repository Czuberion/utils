#!/usr/bin/bash

#EX_KEY_SOURCE="$(dirname "$0")/extract_key.py"
#EX_KEY_SOURCE="$(dirname "$(realpath "$0")")/extract_key.py"
#EX_KEY_SOURCE="$(dirname "$(realpath "${BASH_SOURCE[0]}")")/extract_key.py"

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

EX_KEY_SOURCE="$DIR/extract_key.py"
SOCKET_NAME=$(echo -n "$(qtile cmd-obj -o group -f info | $EX_KEY_SOURCE name)")

nvr -s --servername "/tmp/nvimsocket_$SOCKET_NAME" --remote-tab "$@"

