

#calss header
class _READY():
	def __init__(self,): 
		self.name = "READY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
