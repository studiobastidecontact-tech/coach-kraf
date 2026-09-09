#!/usr/bin/env bash
# Pose le garde de coherence en pre-commit. A relancer apres un clone :
# les hooks git ne se versionnent pas, seul leur contenu le peut.
set -e
racine=$(git rev-parse --show-toplevel)
cible="$racine/.git/hooks/pre-commit"
if [ -e "$cible" ] && ! grep -q 'coherence.py' "$cible" 2>/dev/null; then
  echo "  Un pre-commit existe deja et ne nous appartient pas : $cible"
  echo "  Ajoutez-y a la main :  python3 \"\$(git rev-parse --show-toplevel)/_chantier/coherence.py\" || exit 1"
  exit 1
fi
cp "$racine/_chantier/hooks/pre-commit" "$cible"
chmod +x "$cible"
echo "  Garde de coherence pose sur $cible"
