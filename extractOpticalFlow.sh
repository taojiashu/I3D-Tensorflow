for i in `ls ../Datasets/UCF-101/`
do
	for j in `ls ../Datasets/UCF-101/$i`
	do
		mkdir -p ./data/UCF-101/$i/${j%.*}/{i,x,y}
		./denseFlow -f=../Datasets/UCF-101/$i/$j -x=./data/UCF-101/$i/${j%.*}/x/x -y=./data/UCF-101/$i/${j%.*}/y/y -i=./data/UCF-101/$i/${j%.*}/i/i -d=1
	done
echo $i is ready
done
