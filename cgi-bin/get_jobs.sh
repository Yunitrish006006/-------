#!/bin/bash
printf "Content-type: text/html\n\n"
printf "
<head>
	<style>
		table,
		td {
			border: 0px solid rgb(61, 45, 45);
		}

		thead,
		tfoot {
			background-color: rgb(41, 34, 34);
			color: #fff;
		}
	</style>
</head>
"
printf "<table>"
printf "<thead><tr><th>___person___</th><th>___job___</th></tr></thead>"
printf "<tbody>"
while read -r a b; do
	printf "<tr><td>$a</td><td>$b</td><tr>"
done < ../database/jobs.txt
printf "</tbody>"
printf "</table>"
