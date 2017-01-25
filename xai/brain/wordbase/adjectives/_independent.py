

#calss header
class _INDEPENDENT():
	def __init__(self,): 
		self.name = "INDEPENDENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
