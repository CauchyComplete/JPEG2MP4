% codec = 'h.264'; codec type-default
% mode = 'c'; CBR mode-default

input = '..\data\AU_S_%3d.bmp'; %'D:\test\JPEG\JPEG%3d.jpg';
output = '..\output\output.mp4'; %'D:\test\H264\output.mp4';
factor = '1000k';
size = '128x128';
bf = 0;
gp = 1;

JPEG2IF(input, output, size, factor, gp, bf);