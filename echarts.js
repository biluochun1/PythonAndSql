
var date = ['1.24', '2.1', '2.8', '2.15', '2.22', '2.29', '3.7', '3.14', '3.21', '3.28', '4.4', '4.11', '4.18'];
var index = ['The cumulative number of confirmed cases', 'The cumulative number of deaths', 'The cumulative number of cured cases'];

var data = [[0, 0, 1287], [0, 1, 14380], [0, 2, 33738], [0, 3, 57416], [0, 4, 51606], [0, 5, 35329], [0, 6, 20533], [0, 7, 10734], [0, 8, 5549], [0, 9, 2691], [0, 10, 1376], [0, 11, 1138], [0, 12, 1041], [1, 0, 41], [1, 1, 304], [1, 2, 811], [1, 3, 1665], [1, 4, 2442], [1, 5, 2870], [1, 6, 3079], [1, 7, 3199], [1, 8, 3261], [1, 9, 3300], [1, 10, 3329], [1, 11, 3339], [1, 12, 4632], [2, 0, 38], [2, 1, 328], [2, 2, 2659], [2, 3, 9419], [2, 4, 22888], [2, 5, 41625], [2, 6, 57065], [2, 7, 66911], [2, 8, 72244], [2, 9, 75448], [2, 10, 76964], [2, 11, 77575], [2, 12, 77062]];
option = {
    tooltip: {},
    visualMap: {
        max: 80000,
        inRange: {
            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        }
    },
    xAxis3D: {
        type: 'category',
        data: date,
        name:""
    },
    yAxis3D: {
        type: 'category',
        data: index,
        barCategoryGap:'20%',
        name:""
    },
    zAxis3D: {
        type: 'value',
        name:""
    },
    grid3D: {
        boxWidth: 200,
        boxDepth: 80,
        viewControl: {
            // projection: 'orthographic'
        },
        light: {
            main: {
                intensity: 1,
                shadow: true
            },
            ambient: {
                intensity: 0.4
            }
        }
    },
    series: [{
        type: 'bar3D',
        data: data.map(function (item) {
            return {
                value: [item[1], item[0], item[2]],
            }
        }),
        shading: 'lambert',
        label: {
            textStyle: {
                fontSize: 16,
                borderWidth: 1
            }
        },
        emphasis: {
            label: {
                textStyle: {
                    fontSize: 20,
                    color: '#900'
                }
            },
            itemStyle: {
                color: '#900'
            }
        }
    }]
}