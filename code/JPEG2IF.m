function JPEG2IF(input, output, size, factor, gp, bf)
%-start_number : 인코딩 시작 인덱스 설정 (JPEG 파일의 번호)
%-c:v: 코덱 설정
%gp  : GOP size
%-bf : B-frame 수
%-r  : 프레임 레이트
%-an : audion 제거
%y   : 같은 이름의 파일 있을 때 덮어쓰기

command = strcat('ffmpeg',{' '}, '-start_number 0', {' '}, '-s:v',{' '}, size, {' '}, '-i', {' '},input);
command = strcat(command,{' '},'-c:v libx264 -x264opts keyint=',int2str(gp),':min-keyint=',int2str(gp),':scenecut=-1');
command = strcat(command,{' '}, '-r 30', {' '}, '-b:v',{' '}, factor,{' '}, '-bf', {' '}, int2str(bf), {' '}, '-an' ,{' '}, '-y');
command = strcat(command, {' '},output);
% command{1};
system(command{1});
