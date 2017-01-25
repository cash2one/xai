

#calss header
class _DOMESTIC():
	def __init__(self,): 
		self.name = "DOMESTIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
