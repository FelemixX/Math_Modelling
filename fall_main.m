clc
global S m g mu
%условно безопасной для приземления является скорость в <5 м\с 
m=120;
g=9.81;
mu=0.0182; %динамическая вязкость среды для воздуха с температурой 20 градусов и давлением 1 атм
v = 0;
h = 6000;

% площадь сечения парашютиста и парашюта
S1=0.7;
S2=82.5;

% S1=input('input square of a man body (0.5...1.0) ');
% S2=input('input square of a parachute (15...83) ');
tspan=[0:2000]; 

% расчет для нераскрывшегося парашюта
% 2-мерная матрица высоты и скорости – начальные условия
y0=[h,v];
S=S1;
[t1,y1]=ode45('fall',tspan,y0);

% расчет для раскрывшегося парашюта
S=S2;
[t2,y2]=ode45('fall',tspan,y0);

% создание 2 окон вывода графиков,
% расположенных одно под другим
subplot(2,1,1)

% график высоты от времени
imax=find(y1(:,1)>0);
indexmax=max(imax);
plot(t1(1:indexmax),y1((1:indexmax),1),'b--','LineWidth',2)

% удержание графика в окне
hold on

% 2-й график зависимости высоты от времени
imax=find(y2(:,1)>0);
indexmax=max(imax);
plot(t2((1:indexmax)),y2((1:indexmax),1),'g-','LineWidth',2)
legend('без парашюта', 'с парашютом')
hold on

% отображение сетки
grid on

% заголовок верхнего окна, подписи осей
title('Зависимость высоты от времени')
ylabel('Высота H,m')
xlabel('Время t,s')

% создание нижнего окна для вывода зависимости
% скорости от времени; вывод графиков и подписи осей
subplot(2,1,2)

imax=find(y1(:,1)>0);
indexmax=max(imax);
plot(y1(1:indexmax,1),y1(1:indexmax,2),'b--','LineWidth',2) 

% реверс оси абсцисс
set(gca,'XDir','reverse')
hold on
imax=find(y2(:,1)>0);
indexmax=max(imax);
plot(y2(1:indexmax,1),y2(1:indexmax,2),'g-','LineWidth',2)
hold on
grid on
title('Зависимость скорости от высоты')
ylabel('Скорость v,m/s')
xlabel('Высота h,m') 
