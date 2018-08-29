# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

__author__ = "Tiago Conceição <Tiago_caza@hotmail.com>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2018 Tiago Conceição - Released under terms of the AGPLv3 License"

class SDS011Plugin(octoprint.plugin.StartupPlugin,
				   octoprint.plugin.SettingsPlugin,
                   octoprint.plugin.AssetPlugin,
                   octoprint.plugin.TemplatePlugin):

	def __init__(self):
		self.port = 81

	def on_after_startup(self):
		self.port = self._settings.get(["port"])

	def on_settings_save(self, data):
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

		self.port = self._settings.get(["port"])

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			port=self.port
		)

	#def get_template_vars(self):
	#	return dict(port=self._settings.get(["port"]))

	def get_template_configs(self):
		return [
			dict(type="tab", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/SDS011.js"],
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			SDS011=dict(
				displayName="SDS011 Sensor",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="sn4k3",
				repo="OctoPrint-SDS011",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/sn4k3/OctoPrint-SDS011/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "SDS011 Sensor"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = SDS011Plugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

