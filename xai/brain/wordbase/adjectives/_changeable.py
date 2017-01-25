

#calss header
class _CHANGEABLE():
	def __init__(self,): 
		self.name = "CHANGEABLE"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
