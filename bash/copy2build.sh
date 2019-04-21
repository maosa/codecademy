#!/bin/bash

: '
In this project, we will create a release script to copy certain files from a source directory into a build directory
'

echo "Welcome"

firstline=$(head -n 1 source/changelog.md)

read -a splitfirstline <<< $firstline

version=${splitfirstline[1]}

echo "Build version: $version"

echo "Do you wish to continue? Enter 1 for yes and 0 to exit:"

read versioncontinue

if [ $versioncontinue -eq 1 ]
then
	echo -e "\nOK\n"
	for file in source/*
  do
		#echo $file
		if [ $file == "source/secretinfo.md" ]
    then
    	echo "Encrypting and copying $file"
      touch build/secretinfo.md | sed 's/42/XX/' $file > build/secretinfo.md
    else
    	echo "Copying $file"
      cp $file build/
    fi
  done

  cd build/
  echo -e "\nBuild version $version contains:"
  ls -t
  cd ..

else
	echo "Please come back when you are ready"
fi
