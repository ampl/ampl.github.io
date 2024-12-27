	{
	printf ("<tr>\n<td>")

	if ($1 != "-")
		printf ("<a href=%s><tt>%s</tt></a>", $1, $1)
	else
		printf ("<br>")

	if ($2 != "-")
		printf ("</td>\n<td align=center>%s</td>\n<td>", $2)
	else
		printf ("</td>\n<td><br></td>\n<td>")

	if ($3 != "")
		printf ("<a href=%s><tt>%s</tt></a>", $3, $3)
	else
		printf ("<br>")

	if ($4 != "")
		printf ("</td>\n<td align=center>%s</td>\n</tr>\n\n", $4)
	else
		printf ("</td>\n<td><br></td>\n</tr>\n\n")
	}
