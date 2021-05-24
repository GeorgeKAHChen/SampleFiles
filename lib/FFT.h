/*=================================================================
//
//		ESC project
//		Fast Flourier Transformation in 2nd Dimension
//		Copyright(c) by Kazuki Amakawa, all right reserved
//
=================================================================*/
#ifndef FFT2DINIT
#define FFT2DINIT
#define PI 3.1415926535897932384626

float *FFT2D(int width, int height, unsigned char *array2d, int Kwidth, int Kheight, float *kernel, float *result){
	/*
	Convolution without FFT...
	You are right, I AM LAZE!!
	*/
	int i, j, p, q;

	for (i = 0; i < width; i ++)
		for (j = 0; j < height; j ++){
			float tmp = 0;
			for (p = (int)(-Kwidth / 2); p < (int)((Kwidth)/2) + 1; p ++)
				for (q = (int)(-Kheight / 2); q < (int)((Kheight)/2) + 1; q ++){
					if ( (i + p) < 0 || (i + p) >= width || (j + q) < 0 || (j + q) >= height )
										continue;
					tmp += ((int)array2d[(i + p) * height + j + q]) * kernel[((int)Kwidth/2 + p) * Kheight + q + (int)Kheight / 2];
				}
			result[i * height + j] = tmp;
		}
	return result;
}
#endif
