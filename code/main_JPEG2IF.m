% codec = 'h.264'; codec type-default
% mode = 'c'; CBR mode-default

input = 'D:\test\JPEG\JPEG%3d.jpg';
output = 'D:\test\H264\output.mp4';
factor = '1000k';
size = '512x384';
bf = 0;
gp = 1;

JPEG2IF(input, output, size, factor, gp, bf);
































% list = dir(inputdir);
% for i = 1:length(list)
%     if(list(i).isdir ~= 1)
%         filename = list(i).name;
%         input = strcat(inputdir,'\',filename);
%         for j = 1:length(factor)
%             raw2single_crop(video_num, crop_num, input, outputdir, size, codec, mode, factor{j}, gp, bf, crop_length, w_start,h_start);
%         end
%         video_num = video_num + 1;
%     end
% end

% list = dir(inputdir);
% for i = 1:length(list)
%     if(list(i).isdir ~= 1)
%         filename = list(i).name;
%         input = strcat(inputdir,'\',filename);
%         for j = 1:length(factor)
%             raw2single_crop(video_num, crop_num, input, outputdir, size, codec, mode, factor{j}, gp, bf, crop_length, w_start,h_start);
%         end
%         video_num = video_num + 1;
%     end
% end
