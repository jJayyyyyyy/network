'use strict';
var md = window.markdownit();

var app = new Vue({
	el: '#editor',
	data: {
		content: '# hello',
		cmd: ''
	},
	// computed: {

	// },
	methods: {
		compiledMarkdown: function () {
			var self = this;
			return md.render(self.content);
		}
	}
})