$(function () {
    var textEditor = $('.text_editor');
    var selectedFormat = $('#content_format');
    if (textEditor != undefined) {
        if (selectedFormat.val() == 'markdown') {
            load_markdown_editor();
            textEditor.focus()
        } else if (selectedFormat.val() == 'html') {
            load_html_editor();
        }
    }
    selectedFormat.change(function () {
        if (this.value == 'markdown') {
            destroy_html_editor();
            load_markdown_editor();
            textEditor.focus()
        } else if (this.value == 'html') {
            destroy_markdown_editor();
            load_html_editor();
        } else {
            destroy_markdown_editor();
            destroy_html_editor()
            textEditor.focus()
        }
    });
});
