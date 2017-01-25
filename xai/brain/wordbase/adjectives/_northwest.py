

#calss header
class _NORTHWEST():
	def __init__(self,): 
		self.name = "NORTHWEST"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
