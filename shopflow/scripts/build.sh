#!/usr/bin/env bash
# Compiles all three modules into out/. Run from anywhere:
#   bash scripts/build.sh
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p out/common out/backend out/frontend
SEP=":"
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) SEP=";" ;;
esac

compile() {
  local name="$1" cp="${2:-}"
  echo "Compiling $name..."
  # serial/this-escape are noise for Swing classes that are never serialized.
  local lint="-Xlint:all,-serial,-this-escape"
  if [ -n "$cp" ]; then
    javac $lint -Werror -cp "$cp" -d "out/$name" $(find "$name/src" -name '*.java')
  else
    javac $lint -Werror -d "out/$name" $(find "$name/src" -name '*.java')
  fi
}

compile common
compile backend "out/common"
compile frontend "out/common"
echo "Build OK. Classpath separator for this platform: '$SEP'"
