#!/usr/bin/env python3
def processlingrapixel(col, row, data, pixelWidth, pixelHeight, xO, yO, plot, netcdffile, rsdir):
	"""
	Launch a single pixel of processing for LingraRS
	:param col: column in Grassland raster file
	:param row: row in Grassland raster file
	:param data: Value of pixel in Grassland raster file (0/1)
	:param pixelWidth: Projected pixel width size
	:param pixelHeight: Projected pixel height size
	:param xO: Projected X origin
	:param yO: Projected Y Origin
	:param plot: Do you plot graphs of the run (False or True)
	:param netcdffile: ERA5 netcdf file to extract weather data from
	:param rsdir: RS data directory
	:return: tiller, yielD, wlvg, wlvd1, parcu, grass, tracu, evacu
	"""
	# Import local libraries
	from libmkMeteo import mkmeteo4lingrars
	# import main lingraRS library
	from liblingraRS import lingrars

	if data == 1:
		longitude = col * pixelWidth + xO
		latitude = yO - row * pixelHeight
		print(col, row, longitude, latitude, data[col][row])
		# Create the Meteo and RS data parameterisation for lingraRS
		meteolist = mkmeteo4lingrars(netcdffile, rsdir, longitude, latitude)
		# Run the model
		(tiller, yielD, wlvg, wlvd1, parcu, grass, tracu, evacu) = lingrars(latitude, meteolist, plot)
		# exit() TODO plot the graphs and check if all ok
		# Let the pixels fit into each map (*1000 bc INT32 maps)
		# TODO check values out for print("parcu=", parcu)
		return tiller*1000, yielD*1000, wlvg*1000, wlvd1*1000, parcu, grass*1000, tracu, evacu
