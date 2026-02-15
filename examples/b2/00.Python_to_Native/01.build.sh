#!/bin/sh

set -uxe

pushd modules_to_compile

./build.sh

popd
