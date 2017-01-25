

#calss header
class _PERIOD():
	def __init__(self,): 
		self.name = "PERIOD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
