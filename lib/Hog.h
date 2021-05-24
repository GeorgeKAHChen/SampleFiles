/*=================================================================
//
//		ESC project
//		Hog algorithm part, Hog in C
//		Copyright(c) by Kazuki Amakawa, all right reserved
//
=================================================================*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h> 
#include "ImageIO.h"

#define DEBUG
#ifndef Initialization
/*
Define of Global parameter
*/
float *HogResult;
unsigned char *HogImg;
float *Gradient;
float *Angle;
#define Initialization
#define PI 3.1415926535897932384626
#endif


struct HOGDescriptor
{
	/*
	Parameter in HOG
	Once you changed these parameters of Hog, it is necessary to run the init function again
	*/

	float Gamma;
	int width, height;
	int BlockX, BlockY;
	int StrideX, StrideY;
	int CellX, CellY;
	int nbins;
	int BlockOutput;
	//Gamma, width, height, BlockX, BlockY, StrideX, StrideY, CellX, CellY, nbins
	
	int BlockLength;
	int BlockTtl;
	float GammaTable[256];
}Hog = {0.5, 270, 480, 270, 480, 270, 480, 9, 16, 9, 0};



int HogInit()
{
	/*
	This function is initila of hog algorithm,
	It will initial values in HOGDescriptor and get memory location of Result and HogImg
	Once you changed the parameter of Hog, it is necessary to run this init function again
	*/
	int i;
	float f;
	for (i = 0; i < 256; i ++){
		f = (i + 0.5) / 256;
		f = (float) pow(f, Hog.Gamma);
		Hog.GammaTable[i] = (int)(f * 256 - 0.5);
	}

	if (Hog.width % Hog.BlockX != 0 && Hog.height % Hog.BlockY != 0)	return -1;
	if (Hog.BlockX % Hog.CellX != 0 && Hog.BlockY % Hog.CellY != 0)		return -2;
	
	Hog.BlockLength = (int)Hog.BlockX / Hog.CellX * Hog.BlockY / Hog.CellY * Hog.nbins;
	Hog.BlockTtl = (int)(((Hog.width - Hog.BlockX) / Hog.StrideX) + 1) * (((Hog.height - Hog.BlockY) / Hog.StrideY) + 1) ;
	//HogResult = (float *)malloc(Hog.BlockLength * Hog.BlockTtl);
	HogResult = (float *)malloc(Hog.nbins * Hog.width * Hog.height);
	
	HogImg = (unsigned char*)malloc(Hog.width * Hog.height);
	Gradient = (float *)malloc(Hog.width * Hog.height);
	Angle = (float *)malloc(Hog.width * Hog.height);
	if (Hog.BlockOutput != 0 && Hog.BlockOutput != 1)					Hog.BlockOutput = 0;
	
	return 0;
}


void GetImage(unsigned char *img, int Owidth, int Oheight)
{
	int i, j;
	/*
	Gamma transformation
	*/
	for (i = 0; i < Hog.width; i ++){
		for(j = 0; j < Hog.height; j ++){
			int TrueX = (int) i * (Owidth / Hog.width);
			int TrueY = (int) j * (Oheight / Hog.height);

			HogImg[i * Hog.height + j] = (unsigned char)Hog.GammaTable[(int)img[TrueX * Oheight + TrueY]];
		}
	}
	/*
	Get gradient figure and angle
	*/
	float ValX, ValY;
	int x1, x2, y1, y2;

	for (i = 0; i < Hog.width; i ++){
		for (j = 0; j < Hog.height; j ++){
			if(j - 1 < 0)					x1 = 0;
			else							x1 = (int)img[i * Hog.height + j - 1];
			
			if(j + 1 > Hog.height)			x2 = 0;
			else							x2 = (int)img[i * Hog.height + j + 1];

			if(i - 1 < 0)					y1 = 0;
			else							y1 = (int)img[(i-1) * Hog.height + j];

			if(i + 1 > Hog.width)			y2 = 0;
			else							y2 = (int)img[(i+1) * Hog.height + j];


			ValX = x2 - x1;
			ValY = y2 - y1;

			if (ValY == 0 || ValX == 0)		Angle[i * Hog.height + j] = 0;
			else					Angle[i * Hog.height + j] = atan(ValY / ValX) * 180 / PI;
			Gradient[i * Hog.height + j] = sqrt(ValX * ValX + ValY * ValY);
			//printf("%f    %f\n", Angle[i * Hog.height + j], Gradient[i * Hog.height + j]);
		}
	}
	FloatWriteToFile("tmp1.out", Gradient, Hog.width, Hog.height);
	//free(HogImg);

	return ;
}

/*
void HogMain(){
	int i = 0;
	int j = 0;
	int kase = 0;
	int ttl = 0;
	int p, q, m, n, point, Local;
	float Step = 180 / Hog.nbins;
	float BlockSum, Val, Ang;
	float Histogram[Hog.nbins];
	
	while (1){
		if (j + Hog.BlockY > Hog.height){
			j = 0;
			i += Hog.StrideX;
		}
		if (i + Hog.BlockX > Hog.width)			break;
		ttl ++;

		//Initial block valiables
		p = 0;
		q = 0;
		BlockSum = 0;
		point = 0;

		while (1){
			if (q + Hog.CellY > Hog.BlockY){
				q = 0;
				p += Hog.CellX;
			}
			if(p + Hog.CellX > Hog.BlockX)		break;

			memset(Histogram, 0, sizeof(Histogram));
			
			//Statistic histogram
			for (m = 0; m < Hog.CellX; m ++){

				for(n = 0; n < Hog.CellY; n ++){
					Val = Gradient[(i + p + m) * Hog.height + j + q + n];
					Ang = Angle[(i + p + m) * Hog.height + j + q + n];
					
					Local = 0;
					while (1){
						if (Ang > 180)			Ang -= 180;
						Ang -= Step;
						if (Ang < 0)			break;
						Local += 1;
					}
					
					if (Local >= Hog.nbins)			Local = Hog.nbins - 1;
					Histogram[Local] += Val;
					
					BlockSum += Val * Val;
				}
			}
			//write into result
			memcpy(HogResult + Hog.BlockLength * (ttl - 1) + (++point) * Hog.nbins , Histogram, sizeof(Histogram));
			q += Hog.CellY;
		}

		//Normalization
		BlockSum = sqrt(BlockSum);
		for (p = 0; p < Hog.BlockX * Hog.BlockY; p ++)
			HogResult[(ttl - 1)* Hog.BlockLength + p] /= BlockSum;

		j += Hog.StrideY;
	}

	return ;
}
*/


void HogMain(){
	//Hog algorithm main loop
	int i = 0;
	int j = 0;
	int kase = 0;
	int ttl = 0;
	int p, q, m, n, point, Local;
	float Step = 180 / Hog.nbins;
	float BlockSum = 0;
	float Val, Ang;
	float Histogram[Hog.nbins];

	for (i = 0; i < Hog.width; i ++){
		for (j = 0; j < Hog.height; j ++){
			printf("%d   %d\n", i, j);
			BlockSum = 0;
			memset(Histogram, 0, sizeof(Histogram));

			for (p = -Hog.CellX/2; p < (Hog.CellX + 1)/2; p ++){
				for (q = -Hog.CellY/2; q < (Hog.CellY + 1)/2; q ++){
					if (i + p < 0 || i + p > Hog.width || j + q < 0 || j + q > Hog.height)
												continue;

					Val = Gradient[(i + p) * Hog.height + j + q];
					Ang = Angle[(i + p) * Hog.height + j + q];

					if (Ang >= 180)				Ang -= 180;
					
					Local = 0;
					while (1){
						if (Ang < 0) 			break;
						Ang -= Step;
						Local += 1;
					}

					Histogram[Local] += Val;
					BlockSum += Val * Val;
				}
			}

			for (p = 0; p < Hog.nbins; p ++)	Histogram[p] /= BlockSum;

			memcpy(HogResult + (i * Hog.height + j) * Hog.nbins, Histogram, sizeof(Histogram));
		
			/*
			char str[128];
			sprintf(str, "./Output/EigenVal/Val_%d.dat", ttl);
			FloatWriteToFile(str, Histogram, 1, Hog.nbins);
			ttl += 1;
			*/

		}
	}
	return ;
}
 
