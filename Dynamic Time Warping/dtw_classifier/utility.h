int non_linear_quantization( float a )
{
  int return_value;
  if (abs(a) < 1)
    return_value = (int) (a * 10.0);
  else if (abs(a) < 2)
    return_value = 10 + (int) ((a - 1.0) * 2.0);
  else
    return_value = 16;

  return return_value;
  
}

int min3(int x, int y, int z)
{
  if ( (x < y) & (x < z) )
    return x;
  else if ( (y < x) & (y < z) )
    return y;
  else
    return z;
}

float d3_dist(int x[], int y[])
{
  return sqrt(pow((float)(x[0] - y[0]), 2) + pow((float) (x[1] - y[1]), 2) + pow((float) (x[2] - y[2]), 2));
}

int array_distance(int x[][3], int y[][3], int sample_size)
{
  int distance = 0;
  for (int i = 0; i < sample_size; i++)
  {
    distance = distance + (int) d3_dist(x[i], y[i]);  
  }
  return distance;
}