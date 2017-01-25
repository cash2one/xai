

#calss header
class _CONGRESSIONAL():
	def __init__(self,): 
		self.name = "CONGRESSIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
