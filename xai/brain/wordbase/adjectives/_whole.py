

#calss header
class _WHOLE():
	def __init__(self,): 
		self.name = "WHOLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
