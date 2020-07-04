(
x = OSCFunc( { | msg, time, addr, port |
	var prescaler = 0.14;
	var size = round((100 - msg[1]) * prescaler);
	var start = round((50 - msg[2]) * prescaler);

	~degree.source = Pxrand(Array.series(size: size, start: start, step: 1), inf);
}, '/neuro' );
)

(
~degree = PatternProxy(Pn(Pxrand(Array.series(size: 1, start: 0, step: 1), inf), inf));

a = Pbind(
	\scale, Scale.indian,
	\degree, ~degree,
	\dur, 0.17,
	\amp, Pxrand([0, 0, 0.3, 0.2, 0.2, 0.5], inf),
	\legato, Pxrand([0.5, 0.3, 0.4, 1, 0.2], inf)
);
a.play;
)

Scale.directory;
