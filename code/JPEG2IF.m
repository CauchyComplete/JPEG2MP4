function JPEG2IF(input, output, size, factor, gp, bf)
%-start_number : ���ڵ� ���� �ε��� ���� (JPEG ������ ��ȣ)
%-c:v: �ڵ� ����
%gp  : GOP size
%-bf : B-frame ��
%-r  : ������ ����Ʈ
%-an : audion ����
%y   : ���� �̸��� ���� ���� �� �����

command = strcat('ffmpeg',{' '}, '-start_number 0', {' '}, '-s:v',{' '}, size, {' '}, '-i', {' '},input);
command = strcat(command,{' '},'-c:v libx264 -x264opts keyint=',int2str(gp),':min-keyint=',int2str(gp),':scenecut=-1');
command = strcat(command,{' '}, '-r 30', {' '}, '-b:v',{' '}, factor,{' '}, '-bf', {' '}, int2str(bf), {' '}, '-an' ,{' '}, '-y');
command = strcat(command, {' '},output);
% command{1};
system(command{1});
