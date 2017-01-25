

#calss header
class _TOUCHING():
	def __init__(self,): 
		self.name = "TOUCHING"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
