

#calss header
class _LETTER():
	def __init__(self,): 
		self.name = "LETTER"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata