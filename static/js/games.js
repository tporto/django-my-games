$(function(){
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-bottom-right",        
    };

    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#modal-game").modal("show");
            },
            success: function(data){
                $("#modal-game .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function(){
        var form = $(this);
        var formData = new FormData(form[0]);
        $.ajax({
            url: form.attr("action"),
            data: formData.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data){                
                if(data.form_is_valid){
                    $("#table-list").html(data.html_game_list);
                    $("#modal-game").modal("hide");                    
                    toastr.success('',data.message);                                  
                }else{
                    $("#modal-game .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    /* Binding */
    // Create
    $(".js-create-game").click(loadForm);
    $("#modal-game").on("submit", ".js-game-create-form", saveForm);

    // Update
    $("#game-table").on("click", ".js-update-game", loadForm);
    $("#modal-game").on("submit", ".js-game-update-form", saveForm);

    // Delete
    $("#game-table").on("click", ".js-delete-game", loadForm);
    $("#modal-game").on("submit", ".js-game-delete-form", saveForm);
});
