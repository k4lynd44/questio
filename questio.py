from openpyxl import load_workbook
wb = load_workbook(filename = 'proviamo.xlsx',data_only=True)

#Il test viene effettuato SOLO sullo sheet Human Resource per il momento
sh = wb["HR"]
l=len(sh.rows)

for i in range(2,l):
	cell_obj=sh.cell(row=i,column=1)
	print(cell_obj.value)
