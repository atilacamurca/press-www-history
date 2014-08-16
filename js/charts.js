
$(function() {
	var s1 = [0, 0, 83.4, 0, 0, 8];
	var s2 = [25.23, 1.21, 67.84, 2.41, 2.83, 0];
	var s3 = [23.73, 33.81, 32.04, 7.12, 1.72, 0];
	
	// Can specify a custom tick Array.
    // Ticks should match up one for each y value (category) in the series.
    var ticks = ['Firefox', 'Chrome', 'Intenet Explorer', 'Safari', 'Opera', 'NetScape'];
     
    var plot1 = $.jqplot('chartdiv', [s1, s2, s3], {
        // The "seriesDefaults" option is an options object that will
        // be applied to all series in the chart.
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {fillToZero: true},
            pointLabels: { show:true }
        },
        // Custom labels for the series are specified with the "label"
        // option on the series option.  Here a series option object
        // is specified for each series.
        series:[
				{label: 'Nov/2002'},
			   {label:'Dez/2008'},
            {label:'Jul/2012'}
        ],
        // Show the legend and put it outside the grid, but inside the
        // plot container, shrinking the grid to accomodate the legend.
        // A value of "outside" would not shrink the grid and allow
        // the legend to overflow the container.
        legend: {
            show: true,
            placement: 'outsideGrid'
        },
        axes: {
            // Use a category axis on the x axis and use our custom ticks.
            xaxis: {
                renderer: $.jqplot.CategoryAxisRenderer,
                ticks: ticks
            },
            // Pad the y axis just a little so bars can get close to, but
            // not touch, the grid boundaries.  1.2 is the default padding.
            yaxis: {
                pad: 1.05,
                tickOptions: {formatString: '%d%%'}
            }
        }
    });
});
