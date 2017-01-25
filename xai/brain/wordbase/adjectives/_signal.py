

#calss header
class _SIGNAL():
	def __init__(self,): 
		self.name = "SIGNAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
