$(document).ready(function() {
    //When the modal is shown
    $("#deleteConfirmModal").on("show.bs.modal", function(event){
        const button = $(event.relatedTarget);
        const contactId = button.data("id");
        const deleteUrl = button.data("url");

        //Update modal content
        $("#modal-contact-id").text(contactId);

        //Set the delete URL
        // const deleteUrl = `{% url 'contacts:delete_contact' 0 %}`.replace(
        //     "0",
        //     contactId
        // );
        $("#confirmDeleteBtn").attr("href", deleteUrl);
    });

    //When delete button is clicked
    $("#confirmDeleteBtn").click(function (e) {
        //print("confirm delete");
        console.log("confirm delete");
        //close the modal
        $("#deleteConfirmModal").modal("hide");

        //Optional
        setTimeout(function(){
            window.location.href = $("#confirmDeleteBtn").attr("href");
        },300);
    });
});