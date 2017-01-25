

#calss header
class _NORTHERN():
	def __init__(self,): 
		self.name = "NORTHERN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
