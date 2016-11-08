/**
 * jQuery/JS code needed for channels
 */

monthAbbrs = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function outputNote(note) {
    var noteElement = $("<article></article>", {
        id: "note-" + note.pk,
        "class": "note",
        tabindex: "0"
    });

    // Generate the note body
    var noteBody = $("<p></p>", {
        html: note.fields.body_text
    });

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
        if (minsDiff > 0) { // Output minute
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

    if (note.fields.author == user.email) { // This is one of user's notes, display appropriate actions
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