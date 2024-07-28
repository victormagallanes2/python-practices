from bokeh.plotting import figure, output_file, show

# Preparamos los datos
x = [1, 2, 3, 4, 5, 3, 6]
y = [6, 7, 2, 4, 5, 8, 6]

# Salida estática HTML
output_file("lines.html")

# Creamos un nuevo gráfico con un titulo y dos ejes (x e y)
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# Agregamos la linea con los datos
p.line(x, y, legend="Temp.", line_width=2)

# Mostramos el resultado
show(p)