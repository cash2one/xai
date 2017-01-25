

#calss header
class _CLEAR():
	def __init__(self,): 
		self.name = "CLEAR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
