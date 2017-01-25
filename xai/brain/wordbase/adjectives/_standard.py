

#calss header
class _STANDARD():
	def __init__(self,): 
		self.name = "STANDARD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
