console.log("hello world");

$.ajax({
    url: '/api/exercise',
    dataType: 'json',
    success: function (data) {
        exercise = data.objects;
        i = 2;
        // initialize the title 
        title = exercise[i].title
        $("#exercise-title").text(title);
        // assign "next title"
        $("#test-button").click(function () {
            i++;
            title = exercise[i].title
            $("#exercise-title").text(title);
            console.log(title);
        });

    }
})