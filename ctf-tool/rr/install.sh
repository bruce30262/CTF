#!/usr/bin/env bash

set -e

# https://gist.github.com/lukechilds/a83e1d7127b78fef38c2914c4ececc3c
get_latest_release() {
  curl --silent "https://api.github.com/repos/$1/releases/latest" | # Get latest release from GitHub api
    grep '"tag_name":' |                                            # Get tag line
    sed -E 's/.*"([^"]+)".*/\1/'                                    # Pluck JSON value
}

echo "Getting latest rr version on github..."
VERSION="$(get_latest_release rr-debugger/rr)"
FILENAME=rr-$VERSION-Linux-x86_64.deb
echo "Latest rr release: $VERSION"

echo "Downloading rr .deb package..."
wget https://github.com/rr-debugger/rr/releases/download/$VERSION/$FILENAME

echo "Installing rr .deb package..."
sudo dpkg -i $FILENAME
rm $FILENAME

# write perf_event_paranoid
echo "Writing perf_event_paranoid..."
sudo bash -c 'echo 1 >/proc/sys/kernel/perf_event_paranoid'
sudo bash -c 'echo kernel.perf_event_paranoid=1 > /etc/sysctl.d/local.conf'

echo "Done installing rr"
PEP=$(cat /proc/sys/kernel/perf_event_paranoid) # get perf_event_paranoid
echo "Current /proc/sys/kernel/perf_event_paranoid = $PEP ( should <= 1 for rr to work )"
echo "If you're in VMware, make sure to enable \"Virtualize CPU performance counters\" option"

