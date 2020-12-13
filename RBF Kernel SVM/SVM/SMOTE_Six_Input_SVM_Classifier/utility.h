void haar_transform(double x[], double y[], int n)
{
    for (int i = 0; i < ((n/2)-1); i++)
    {
      y[i] = (x[2*i] + x[(2*i)+1]) / 2;
    }
   
    return; 
}
