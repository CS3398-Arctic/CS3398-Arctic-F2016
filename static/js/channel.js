/**
 * JavaScript/jQuery code needed for channels
 */

monthAbbrs = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function outputNote(note) {
    if ($("#note-" + note.pk).length === 0) { // Create new note element
        var noteElement = $("<article></article>", {
            id: "note-" + note.pk,
            "class": "note",
            tabindex: "0"
        });

        // Generate the note body
        var noteBody = $("<div></div>", {
            "class": "note-body"
        });

        var noteParagraph = $("<p></p>", {
            html: note.fields.body_text
        });
        noteBody.append(noteParagraph);

        commonmarkParse(noteBody);

        noteElement.append(noteBody);


        // Generate the note meta

        var noteMeta = $("<p></p>", {
            "class": "note-meta clearfix"
        });

        // Generate the note author if sent
        if ("author" in note.fields) {
            if (note.fields.author == user.email) var author = "You"; else var author = note.fields.author;
            var noteAuthor = $("<span></span>", {
                "class": "note-author",
                html: author + ",&nbsp;"
            });
            noteMeta.append(noteAuthor);
        }

        // Generate the note date
        var today = new Date();
        var createdDate = new Date(note.fields.created_date);

        var noteDate = $("<span></span>", {
            "class": "note-date"
        });

        var timeHTML = "";
        if (createdDate.getFullYear() == today.getFullYear()    // Note was created today
            && createdDate.getMonth() == today.getMonth()
            && createdDate.getDay() == today.getDay()) {

            var hoursDiff = today.getHours() - createdDate.getHours();
            var minsDiff = today.getMinutes() - createdDate.getMinutes();
            var secsDiff = today.getSeconds() - createdDate.getSeconds();
            if (minsDiff < 0) {
                minsDiff += 60;
                hoursDiff -= 1;
            }
            if (secsDiff < 0)
                minsDiff -= 1;

            if (hoursDiff > 0) { // Output hour
                timeHTML += hoursDiff + " hour";
                if (hoursDiff != 1) // (s)
                    timeHTML += "s";
                if (minsDiff != 0)
                    timeHTML += ", ";
            }
            if ((hoursDiff > 0 && minsDiff > 0) || hoursDiff == 0) { // Output minute
                timeHTML += minsDiff + " minute";
                if (minsDiff != 1) // (s)
                    timeHTML += "s";
            }
        }
        else {  // Note was not created today
            timeHTML += monthAbbrs[createdDate.getMonth()] + " ";
            if (createdDate.getDay() < 10) // Precede day number with 0 if single digit
                timeHTML += "0";
            timeHTML += createdDate.getDay();
            if (today.getYear() != createdDate.getYear()) // Note was not created this year
                timeHTML += ", " + createdDate.getYear();
        }

        // Generate the time tag
        var noteDateTime = $("<time></time>", {
            datetime: note.fields.created_date,
            html: timeHTML
        });

        noteDate.append(noteDateTime);
        noteMeta.append(noteDate);

        // Generate the note comments
        var noteComments = $("<span></span>", {
            "class": "note-comments",
            html: "0 comments"
        });
        noteMeta.append(noteComments);

        // Generate the note actions

        var noteActions = $("<span></span>", {
            "class": "note-actions"
        });

        if ("author" in note.fields && (note.fields.author == user.email || user.is_superuser)) {
            // This is one of user's notes (or user is a superuser), display appropriate actions
            var noteEdit = $("<a></a>", {
                "class": "note-edit fa fa-pencil",
                href: "#", // FIXME: Does nothing, fix in Sprint 3.
                role: "button",
                "aria-label": "edit"
            });
            noteActions.append(noteEdit);

            var noteDelete = $("<a></a>", {
                "class": "note-delete fa fa-trash",
                href: ajax_url + "?action=delete&note=" + note.pk,
                role: "button",
                "aria-label": "delete"
            });
            noteActions.append(noteDelete);
        }

        noteMeta.append(noteActions);

        noteElement.append(noteMeta);

        $('#results').prepend(noteElement);
    }
    else if (note.fields.body_text !== "") { // Update note
        var the_note = $("#note-" + note.pk + " .note-body p");
        the_note.html(note.body_text);
        commonmarkParse(the_note);
    }
    else { // Delete note
        $("#note-" + note.pk).remove();
    }
}

function ajaxPostForm() {
    $.ajax({
       type: "POST",
       url: ajax_url,
       data: $("#note-form").serialize(),
       success: function() {
           ajaxSingleUpdate();
           $('#id_body_text').val('');
       }
     });
}
$("#note-post").click( function(event){
    event.preventDefault();
    ajaxPostForm();
});

function ajaxLiveUpdate() {
    $.ajax({
        url: ajax_url
            + '?action=load&channel=1&session=all&modified_date='
            + encodeURIComponent(last_update.toISOString()),
        dataType: 'json',
        success: function(notes) {
            notes_changes = notes;

            var empty = $.isEmptyObject(notes_changes);
            $("#update-indicator")[ !empty ? 'show' : 'hide' ]();
            },
        complete: function() {
            // Schedule the next request in 5 seconds
            setTimeout(ajaxLiveUpdate, 5 * 1000);
        }
    });
}
function ajaxSingleUpdate(action) {
    $.ajax({
        url: ajax_url
            + '?action=load&channel=1&session=all&modified_date='
            + encodeURIComponent(last_update.toISOString()),
        dataType: 'json',
        success: function(notes) {
            updateNotes(notes);
        }
    });
}

function updateNotes(notes) {
    $("#update-indicator")['hide']();
    last_update = new Date();
    for (var i in notes) {
        outputNote(notes[i]);
    }
    applyNoteActions();
}
$("#update-indicator a").click( function(event){
    event.preventDefault();
    updateNotes(notes_changes);
});

function noteEdit (id) {
    var the_note = $('#note-' + id);
    the_note.toggleClass('editing');

    $('#note-edit-form').appendTo(the_note);
}

function ajaxDeleteNote(href) {
    $.ajax({
        url: href,
        success: function() {ajaxSingleUpdate();}
    });
}

function applyNoteActions () {
    $(".note-edit").click( function(event){
        event.preventDefault();
        noteEdit($(this).closest('.note').attr('id').split("note-")[1]);
    });
    $(".note-delete").click( function(event){
        event.preventDefault();
        ajaxDeleteNote($(this).prop("href"));
    });
}
function commonmarkParse (element) {
    var reader = new commonmark.Parser();
    var writer = new commonmark.HtmlRenderer({smart: true, safe: true});
    var parsed = reader.parse($(element).text());
    $(element).html(writer.render(parsed));
}
function commonmarkParseAll () {
    $(".note-body").each(function (i, obj) {
        commonmarkParse(this);
    });
}


$("#note-search").on("keyup", function() {
    var g = $(this).val().toLowerCase();
    $(".note .note-body p").each(function() {
        var s = $(this).text().toLowerCase();
        $(this).closest('.note')[ s.indexOf(g) !== -1 ? 'show' : 'hide' ]();
    });
});