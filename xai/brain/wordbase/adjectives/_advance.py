

#calss header
class _ADVANCE():
	def __init__(self,): 
		self.name = "ADVANCE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
