	{
	printf ("<tr>\n")
	printf ("<td align=center>%s</td>\n", $1)
	printf ("<td><a href=%s><tt>%s</tt></a></td>\n", $2, $2)
	printf ("</tr>\n\n")
	}
