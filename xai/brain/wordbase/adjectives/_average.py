

#calss header
class _AVERAGE():
	def __init__(self,): 
		self.name = "AVERAGE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
