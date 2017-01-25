

#calss header
class _RETURN():
	def __init__(self,): 
		self.name = "RETURN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
