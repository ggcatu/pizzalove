(function($) {
  "use strict"; // Start of use strict

	var ctx = document.getElementById("myChart").getContext('2d');
	var LoveChart = new Chart(ctx, {
	    type: 'bar',
	    data: {
	        labels: [],
	        datasets: [{
	            label: '<3 Pizza love',
	            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(255, 206, 86, 0.9)'
            	],
            	borderColor: [
                'rgba(255,99,132,1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255,99,132,1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255,99,132,1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255,99,132,1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255,99,132,1)',
            	],
	            data: [],
	            borderWidth: 1
	        }]
	    },
	    options: {
	        scales: {
	            yAxes: [{
	                ticks: {
	                    beginAtZero:true
	                }
	            }]
	        }
	    }
	   });


	function updateChart(){
	    $.getJSON( DATA_ENDPOINT, function( data ) {
	    	var labels = [];
			var results = [];

		    $.each( data.results, function( indx, val ) {
			    labels.push( val["username"] );
			    results.push( val["pizza_love"] );
			 });

		    LoveChart.data.datasets[0].data = results;
		    LoveChart.data.labels = labels;
    		LoveChart.update();  
		});

	}
	updateChart();
	setInterval(updateChart, 5000);

    
	$("#love").click(function() {
	    $.get( VOTE_LINK , function() {
		    	var labels = LoveChart.data.labels;
				var ix = labels.indexOf(USERNAME);
				if (ix != -1){
					LoveChart.data.datasets[0].data[ix]+=1;
				}
				LoveChart.update();  
			})
    });

})(jQuery); // End of use strict
