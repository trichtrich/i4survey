$(document).ready(function() {
    var maxIndex = 0;
    $('#survey-wizard').bootstrapWizard({
        onInit: function(tab, navigation) {
            var $total = navigation.find('li').length;
            var $percent = (1 / $total) * 100;
            $('#survey-wizard').find('.progress-bar').css({ width: $percent + '%' });
        },
        onTabShow: function(tab, navigation, index) {
            var title = tab.find('a').data('group-title');
            $('#survey-wizard').find('.wizard-group-title').html(title);
        },
        onTabClick: function(tab, navigation, currentIndex, clickedIndex) {
            if (clickedIndex > maxIndex) return false;
        },
        onNext: function(tab, navigation, index) {
            if (index > maxIndex) {
                maxIndex++;
                var $total = navigation.find('li').length;
                var $current = index + 1;
                var $percent = ($current / $total) * 100;
                $('#survey-wizard').find('.progress-bar').css({ width: $percent + '%' });
            }
        }
    });

    $('#survey-wizard .finish').click(function() {
        $('#form-survey').submit();
    });

    Highcharts.chart('container-chart', {

        chart: {
            polar: true,
            type: 'line'
        },

        title: {
            text: 'Budget vs spending',
            x: -80
        },

        pane: {
            size: '80%'
        },

        xAxis: {
            categories: $('#gdisplay').val(),
            tickmarkPlacement: 'on',
            lineWidth: 0
        },

        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
        },

        tooltip: {
            shared: true,
            pointFormat: '${point.y:,.0f}'
        },

        legend: {
            align: 'right',
            verticalAlign: 'top',
            y: 70,
            layout: 'vertical'
        },

        series: [{
            name: 'Allocated Budget',
            data: $('#total_mark').val(),
            pointPlacement: 'on'
        }]
    });
});