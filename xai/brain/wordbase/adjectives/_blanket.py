

#calss header
class _BLANKET():
	def __init__(self,): 
		self.name = "BLANKET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
