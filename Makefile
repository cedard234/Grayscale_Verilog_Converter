.DEFAULT_GOAL := help
help:
	@echo "Welcome to use Grayscale_Verilog_Converter!"
	@echo "Usage: make requirements: install the required packages"
	@echo "       make image image=[image_path]: convert the grayscale image to verilog file"
	@echo "       make folder folder=[folder]: convert all the grayscale images in the folder to verilog files"
	@echo "       make test: convert all the grayscale images in the test folder to verilog files"
	@echo "       make clean: clean the build folder"

requirements:
	pip install -r requirements.txt

image:
	# create the build folder if not exist
	if [ ! -d "build" ]; then mkdir build; fi
	python3 src/main.py $(image)

folder:
	if [ ! -d "build" ]; then mkdir build; fi
	for file in $(folder)/*.png; do \
	python3 src/main.py $$file; \
	done

#phony test
.PHONY: test
test:
	if [ ! -d "build" ]; then mkdir build; fi
	for file in test/*.png; do \
	make image image=$$file; \
	done



clean:
	rm -rf build/*