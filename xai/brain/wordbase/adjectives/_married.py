

#calss header
class _MARRIED():
	def __init__(self,): 
		self.name = "MARRIED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
