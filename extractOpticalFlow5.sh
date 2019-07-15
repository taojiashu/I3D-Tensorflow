for i in `ls ../Datasets/UCF-101-5/`
do
	for j in `ls ../Datasets/UCF-101-5/$i`
	do
		if [ ! -d ./data/UCF-101/$i/${j%.*}/i ]; then
			mkdir -p ./data/UCF-101/$i/${j%.*}/{i,x,y}
			./denseFlow -f=../Datasets/UCF-101-5/$i/$j -x=./data/UCF-101/$i/${j%.*}/x/x -y=./data/UCF-101/$i/${j%.*}/y/y -i=./data/UCF-101/$i/${j%.*}/i/i -d=1
		fi
	done
echo $i is ready
done
