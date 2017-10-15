#!/bin/bash

mkdocs build --clean &&
rm -rf ../app/site ;
mv site ../app &&
rm -rf ../app/templates/* &&
mv ../app/site/index.html ../app/site/sitemap.xml ../app/templates/ &&
mv ../app/site/about ../app/templates/about &&
mv ../app/site/database ../app/templates/database &&
rm -rf ../app/site
