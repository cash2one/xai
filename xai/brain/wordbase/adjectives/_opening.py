

#calss header
class _OPENING():
	def __init__(self,): 
		self.name = "OPENING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata