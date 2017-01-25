

#calss header
class _CHARACTERISTIC():
	def __init__(self,): 
		self.name = "CHARACTERISTIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
