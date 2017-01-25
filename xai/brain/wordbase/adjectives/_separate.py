

#calss header
class _SEPARATE():
	def __init__(self,): 
		self.name = "SEPARATE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
