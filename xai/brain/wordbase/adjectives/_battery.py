

#calss header
class _BATTERY():
	def __init__(self,): 
		self.name = "BATTERY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
