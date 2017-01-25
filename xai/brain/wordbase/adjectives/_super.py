

#calss header
class _SUPER():
	def __init__(self,): 
		self.name = "SUPER"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
