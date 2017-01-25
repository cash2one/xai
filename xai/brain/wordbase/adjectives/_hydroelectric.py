

#calss header
class _HYDROELECTRIC():
	def __init__(self,): 
		self.name = "HYDROELECTRIC"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
