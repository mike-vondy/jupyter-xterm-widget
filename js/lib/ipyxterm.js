var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
//var xterm = require('//cdnjs.cloudflare.com/ajax/libs/xterm/2.9.2/xterm.min')

// See example.py for the kernel counterpart to this file.


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var IPyXtermModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'IPyXtermModel',
        _view_name : 'IPyXtermView',
        _model_module : 'jupyter-xterm-widget',
        _view_module : 'jupyter-xterm-widget',
        _model_module_version : '0.1.0',
        _view_module_version : '0.1.0',
        status : false,
        pid: 0,
        fd: 0,
        io_file: null,
    })
});


// Custom View. Renders the widget model.
var IPyXtermView = widgets.DOMWidgetView.extend({
    // Defines how the widget gets rendered into the DOM
    render: function() {
        //this.terminal = document.createElement('div')
        //this.terminal.setAttribute('id', 'terminal')
        //var termArea = xterm.Terminal({rows: 25, cols:100})
        //termArea.open(document.getElementById('terminal'))

        //this.terminal = document.createElement('input');
        //this.terminal.status = this.model.get('status');
        //this.terminal.pid = this.model.get('pid');
        //this.terminal.fd = this.model.get('fd');
        //this.terminal.io_file = this.model.get('io_file');
        //this.terminal.value = this.model.get('io_file');
//
        //// Layout Updates 
        //this.el.appendChild(this.terminal);
        //
        //// Python -> JavaScript Update
        //this.model.on('change:status', this.status_changed, this);
        //this.model.on('change:pid', this.pid_changed, this);
        //this.model.on('change:fd', this.fd_changed, this);
        //this.model.on('change:io_file', this.io_file_changed, this);

        // JavaScript -> Python Update
    },

    // Terminal Child Functions
    status_changed: function() {
        this.terminal.status = this.model.get('status');
    },
    pid_changed: function() {
        this.terminal.pid = this.model.get('pid');
    },
    fd_changed: function() {
        this.terminal.fd = this.model.get('fd');
    },
    io_file_changed: function() {
        this.terminal.io_file = this.model.get('io_file');
    }
});


module.exports = {
    IPyXtermModel: IPyXtermModel,
    IPyXtermView: IPyXtermView
};
