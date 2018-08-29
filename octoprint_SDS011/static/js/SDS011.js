/*
 * View model for OctoPrint-SDS011
 *
 * Author: Tiago Conceição
 * License: AGPLv3
 */
$(function() {
    function SDS011ViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        self.loginStateViewModel = parameters[0];
        self.settingsViewModel = parameters[1];

        self.onAfterBinding = function() {
            var url = window.location.href;
            url = url.split("/");
            url = url[0] + "//" + url[2] + ":" + self.settingsViewModel.settings.plugins.SDS011.port();
            document.getElementById('SDS011frame').src = url;
		}
    }



    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: SDS011ViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "loginStateViewModel", "settingsViewModel" ],
        // Elements to bind to, e.g. #settings_plugin_SDS011, #tab_plugin_SDS011, ...
        elements: [ document.getElementById("tab_plugin_SDS011") ]
    });
});
