/*=================================================================
//
//		ESC project
//		ImageIO.h
//		Copyright(c) by Kazuki Amakawa, all right reserved
//
=================================================================*/

#ifndef IMAGEIOInit
#define IMAGEIOInit
unsigned char *ReadFromFile(char *FileName, unsigned char *img, int *Owidth, int *Oheight)
{
	/*
	This function will read image from file, it will save image as unsigned char
	If you want to work this algorithm from other function directly, DO NOT USE IT
	*/
	/*
	For every image, it is necessary change them into .dat file
	You can find this function in KANN program
	*/
	int i, j;
	FILE *File;
	File = fopen(FileName, "r");
	
	int tmp, width, height;
	fscanf(File, "%d%d%d", &tmp, &width, &height);
	
	img = (unsigned char *) malloc(width * height);
	*Owidth = width;
	*Oheight = height;
	
	for (i = 0; i < width; i ++){
		char tmpchar;
		for(j = 0; j < height; j ++){
			float tmp;
			fscanf(File, "%f", &tmp);
			img[i * height + j] = (unsigned char)(int)(tmp * 256);

		}
	}
	return img;
}



void WriteToFile(char *FileName, unsigned char *img, int width, int height){
	#ifdef DEBUG
		printf("%s\n", FileName);
	#endif
	int i, j;
	FILE *File;
	File = fopen(FileName, "wb");
	if(File != NULL)
	{	
		fprintf(File, "%d %d %d\n", 1, width, height);
		for (i = 0; i < width; i ++){
			for (j = 0; j < height; j ++){

				fprintf(File, "%f ", (float)img[i * height + j] / 255);
			}
			fprintf(File, "\n");
		}
		fclose(File);
		File = NULL;
	}
	return ;
}




void FloatWriteToFile(char *FileName, float *img, int width, int height){
	#ifdef DEBUG
		printf("%s\n", FileName);
	#endif
	int i, j;
	FILE *File;
	File = fopen(FileName, "wb");
	if(File != NULL)
	{
		fprintf(File, "%d %d %d\n", 1, width, height);
		for (i = 0; i < width; i ++){
			for (j = 0; j < height; j ++){
				fprintf(File, "%f ", img[i * height + j]);
			}
			fprintf(File, "\n");
		}
		fclose(File);
		File = NULL;
	}
	return ;
}

#endif


