

#calss header
class _PERSONAL():
	def __init__(self,): 
		self.name = "PERSONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
