#!/bin/bash
while read fVIEWS; do
	COUNT=$(($fVIEWS+1))
done < fVIEWS
echo $COUNT > fVIEWS
export COUNT=$COUNT
printf "Content-type: text/html\n\n"
printf " \
<html> \
<head> \
	<script> \
		function Previous() { \
			window.history.back() \
		} \
	</script> \
</head> \
<body> \
	<input type='button' value='GoBack' onclick='Previous()'> \
	<h1>$COUNT</h1><br> \
</body> \
</html> \
"