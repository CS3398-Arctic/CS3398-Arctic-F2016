/**
 * JavaScript/jQuery code needed for channels
 */

monthAbbrs = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function outputNote(note) {
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
        url: ajax_url + '?action=load&channel=1&session=all',
        success: function(notes) {
            $('#results').html("");
            for (var i in notes) {
                outputNote(notes[i]);
            }
            applyNoteActions();
            commonmarkParse();
        },
        complete: function() {
            // Schedule the next request in 5 seconds
            setTimeout(ajaxLiveUpdate, 5 * 1000);
        }
    });
}
function ajaxSingleUpdate(action) {
    $.ajax({
        url: ajax_url + '?action=load&channel=1&session=all',
        success: function(notes) {
            $('#results').html("");
            for (var i in notes) {
                outputNote(notes[i]);
            }
            applyNoteActions();
            commonmarkParse();
        }
    });
}

function ajaxDeleteNote(href) {
    $.ajax({
        url: href,
        success: function() {ajaxSingleUpdate();}
    });
}
function applyNoteActions () {
    $(".note-delete").click( function(event){
        event.preventDefault();
        ajaxDeleteNote($(this).prop("href"));
    });
}
function commonmarkParse () {
    $(".note-body").each(function(i, obj) {
        var reader = new commonmark.Parser();
        var writer = new commonmark.HtmlRenderer({smart: true, safe: true});
        var parsed = reader.parse($(this).text());
        $(this).html(writer.render(parsed));
    });
}


$("#note-search").on("keyup", function() {
    var g = $(this).val().toLowerCase();
    $(".note .note-body p").each(function() {
        var s = $(this).text().toLowerCase();
        $(this).closest('.note')[ s.indexOf(g) !== -1 ? 'show' : 'hide' ]();
    });
});