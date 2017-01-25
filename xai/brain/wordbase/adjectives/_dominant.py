

#calss header
class _DOMINANT():
	def __init__(self,): 
		self.name = "DOMINANT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
