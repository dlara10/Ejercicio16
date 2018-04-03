laminas.pdf : datos.txt grafica.py
	python grafica.py
datos.txt : laminas
	./laminas > datos.txt
laminas : album.cpp
	c++ album.cpp -o laminas
