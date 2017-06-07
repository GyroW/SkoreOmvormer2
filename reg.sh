sed -e 's/<[^>]*>//g' origin1 > 1stage1
sed '/^\s*$/d' 1stage1 > 1stage2
sed '/\/\//d' 1stage2 > 1stage3
sed '/Nieuwe/d' 1stage3 > 1stage4
sed -e "s/[[:space:]]\+/ /g" 1stage4 > pk1
sed -e 's/<[^>]*>//g' origin2 > 1stage1
sed '/^\s*$/d' 1stage1 > 1stage2
sed '/\/\//d' 1stage2 > 1stage3
sed '/Nieuwe/d' 1stage3 > 1stage4
sed -e "s/[[:space:]]\+/ /g" 1stage4 > pk2
sed -e 's/<[^>]*>//g' origin3 > 1stage1
sed '/^\s*$/d' 1stage1 > 1stage2
sed '/\/\//d' 1stage2 > 1stage3
sed '/Nieuwe/d' 1stage3 > 1stage4
sed -e "s/[[:space:]]\+/ /g" 1stage4 > pk3
sed -e 's/<[^>]*>//g' origin4 > 1stage1
sed '/^\s*$/d' 1stage1 > 1stage2
sed '/\/\//d' 1stage2 > 1stage3
sed '/Nieuwe/d' 1stage3 > 1stage4
sed -e "s/[[:space:]]\+/ /g" 1stage4 > pk4
