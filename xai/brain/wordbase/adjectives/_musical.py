

#calss header
class _MUSICAL():
	def __init__(self,): 
		self.name = "MUSICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
