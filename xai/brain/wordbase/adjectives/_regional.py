

#calss header
class _REGIONAL():
	def __init__(self,): 
		self.name = "REGIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
