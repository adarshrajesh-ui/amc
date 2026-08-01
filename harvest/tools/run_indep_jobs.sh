#!/bin/bash
# Launch the two slow verification fetchers. Kept in a script so the tmux panes
# do not have to carry a long argv that pkill -f would also match.
cd /workspace/harvest || exit 1
case "$1" in
proxy)
  exec python3 -u tools/indep_proxy.py \
    d246abad8571a8 a0d52d06d56471 8b33567e30f80a 6738b3c866f5b1 \
    a0bcca6b3398ae a4b2a2f34feb69 4471b3c8b600fe 0d43aee4c7ba97 11d533c3cca8db 5f1e42a6733de3 \
    51ca13558f45e3 c6553cd14443ae 763fa06c7247a2 a251ce474a305f 36d7b6d1250340 e53a4249b6b409 a6e874dd06850b
  ;;
wayback)
  exec python3 -u tools/indep_wayback.py \
    c6553cd14443ae 763fa06c7247a2 36d7b6d1250340 e53a4249b6b409 a6e874dd06850b \
    51ca13558f45e3 a251ce474a305f 8b33567e30f80a 6738b3c866f5b1
  ;;
esac
